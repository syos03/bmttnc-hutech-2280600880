from flask import Flask, request, jsonify
import os
import hashlib
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import ec
from cryptography.hazmat.primitives import serialization
from cryptography.exceptions import InvalidSignature

app = Flask(__name__)

class ECCCipher:
    def __init__(self):
        self.private_key = None
        self.public_key = None
        self.current_message = None
        self.current_signature = None
        
    def generate_keys(self):
        print("Generating new keys...")
        self.private_key = ec.generate_private_key(ec.SECP384R1())
        self.public_key = self.private_key.public_key()
        print("Keys generated successfully")
        return self.private_key, self.public_key
        
    def sign(self, message, private_key):
        try:
            print(f"Signing message: {message}")
            signature = private_key.sign(
                message.encode(),
                ec.ECDSA(hashes.SHA256())
            )
            self.current_message = message
            self.current_signature = signature
            print(f"Message signed successfully. Signature: {signature.hex()}")
            return signature
        except Exception as e:
            print(f"Error in sign: {str(e)}")
            return None
        
    def verify(self, message, signature, public_key):
        try:
            print(f"Verifying message: {message}")
            print(f"With signature: {signature.hex()}")
            public_key.verify(
                signature,
                message.encode(),
                ec.ECDSA(hashes.SHA256())
            )
            print("Verification successful")
            return True
        except InvalidSignature:
            print("Invalid signature")
            return False
        except Exception as e:
            print(f"Error in verify: {str(e)}")
            return False
            
    def load_keys(self):
        if not self.private_key or not self.public_key:
            return self.generate_keys()
        return self.private_key, self.public_key

# ECC CIPHER ALGORITHM
ecc_cipher = ECCCipher()

@app.route('/api/ecc/generate_keys', methods=['GET'])
def ecc_generate_keys():
    try:
        ecc_cipher.generate_keys()
        return jsonify({'message': 'Keys generated successfully'})
    except Exception as e:
        print(f"Error in generate_keys endpoint: {str(e)}")
        return jsonify({'error': str(e)}), 500

@app.route('/api/ecc/sign', methods=['POST'])
def ecc_sign_message():
    try:
        data = request.json
        message = data['message']
        print(f"Received sign request for message: {message}")
        
        private_key, _ = ecc_cipher.load_keys()
        signature = ecc_cipher.sign(message, private_key)
        
        if signature:
            signature_hex = signature.hex()
            return jsonify({'signature': signature_hex})
        else:
            return jsonify({'error': 'Failed to sign message'}), 500
    except Exception as e:
        print(f"Error in sign endpoint: {str(e)}")
        return jsonify({'error': str(e)}), 500

@app.route('/api/ecc/verify', methods=['POST'])
def ecc_verify_signature():
    try:
        data = request.json
        message = data['message']
        signature_hex = data['signature']
        print(f"Received verify request for message: {message}")
        print(f"With signature: {signature_hex}")
        
        _, public_key = ecc_cipher.load_keys()
        signature = bytes.fromhex(signature_hex)
        is_verified = ecc_cipher.verify(message, signature, public_key)
        
        return jsonify({'is_verified': is_verified})
    except Exception as e:
        print(f"Error in verify endpoint: {str(e)}")
        return jsonify({'error': str(e)}), 500

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5050, debug=True) 