from cipher.playfair import PlayfairCipher
from cipher.railfence import RailFenceCipher
from flask import Flask, request, jsonify, render_template
from cipher.caesar import CaesarCipher
from cipher.vigenere import VigenereCipher

app = Flask(__name__)

# Initialize cipher objects
caesar_cipher = CaesarCipher()
vigenere_cipher = VigenereCipher()
railfence_cipher = RailFenceCipher()
playfair_cipher = PlayfairCipher()

# Web routes for rendering pages
@app.route("/")
def home():
    return render_template('index.html')

@app.route("/caesar")
def caesar_page():
    return render_template('caesar.html')

# Form handling routes for Caesar cipher
@app.route("/encrypt", methods=['POST'])
def caesar_encrypt_form():
    try:
        text = request.form['inputPlainText']
        key = int(request.form['inputKeyPlain'])
        encrypted_text = caesar_cipher.encrypt_text(text, key)
        return f"text: {text}<br/>key: {key}<br/>encrypted text: {encrypted_text}"
    except ValueError:
        return "Error: Key must be a number", 400
    except Exception as e:
        return f"Error: {str(e)}", 500

@app.route("/decrypt", methods=['POST'])
def caesar_decrypt_form():
    try:
        text = request.form['inputCipherText']
        key = int(request.form['inputKeyCipher'])
        decrypted_text = caesar_cipher.decrypt_text(text, key)
        return f"text: {text}<br/>key: {key}<br/>decrypted text: {decrypted_text}"
    except ValueError:
        return "Error: Key must be a number", 400
    except Exception as e:
        return f"Error: {str(e)}", 500

# API routes for Caesar cipher
@app.route("/api/caesar/encrypt", methods=["POST"])
def caesar_encrypt_api():
    try:
        data = request.json
        if not data:
            return jsonify({'error': 'No input data provided'}), 400
        
        plain_text = data.get('plain_text')
        key = data.get('key')
        
        if not plain_text or key is None:
            return jsonify({'error': 'Missing plain_text or key'}), 400
            
        try:
            key = int(key)
        except ValueError:
            return jsonify({'error': 'Key must be an integer'}), 400
            
        encrypted_text = caesar_cipher.encrypt_text(plain_text, key)
        return jsonify({'encrypted_text': encrypted_text}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route("/api/caesar/decrypt", methods=["POST"])
def caesar_decrypt_api():
    try:
        data = request.json
        if not data:
            return jsonify({'error': 'No input data provided'}), 400
        
        cipher_text = data.get('cipher_text')
        key = data.get('key')
        
        if not cipher_text or key is None:
            return jsonify({'error': 'Missing cipher_text or key'}), 400
            
        try:
            key = int(key)
        except ValueError:
            return jsonify({'error': 'Key must be an integer'}), 400
            
        decrypted_text = caesar_cipher.decrypt_text(cipher_text, key)
        return jsonify({'decrypted_text': decrypted_text}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# API routes for Vigenere cipher
@app.route('/api/vigenere/encrypt', methods=['POST'])
def vigenere_encrypt_api():
    try:
        data = request.json
        if not data:
            return jsonify({'error': 'No input data provided'}), 400
        
        plain_text = data.get('plain_text')
        key = data.get('key')
        
        if not plain_text or not key:
            return jsonify({'error': 'Missing plain_text or key'}), 400
            
        encrypted_text = vigenere_cipher.vigenere_encrypt(plain_text, key)
        return jsonify({'encrypted_text': encrypted_text}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/vigenere/decrypt', methods=['POST'])
def vigenere_decrypt_api():
    try:
        data = request.json
        if not data:
            return jsonify({'error': 'No input data provided'}), 400
        
        cipher_text = data.get('cipher_text')
        key = data.get('key')
        
        if not cipher_text or not key:
            return jsonify({'error': 'Missing cipher_text or key'}), 400
            
        decrypted_text = vigenere_cipher.vigenere_decrypt(cipher_text, key)
        return jsonify({'decrypted_text': decrypted_text}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# API routes for Railfence cipher
@app.route('/api/railfence/encrypt', methods=['POST'])
def railfence_encrypt_api():
    try:
        data = request.json
        if not data:
            return jsonify({'error': 'No input data provided'}), 400
        
        plain_text = data.get('plain_text')
        key = data.get('key')
        
        if not plain_text or key is None:
            return jsonify({'error': 'Missing plain_text or key'}), 400
            
        try:
            key = int(key)
        except ValueError:
            return jsonify({'error': 'Key must be an integer'}), 400
            
        encrypted_text = railfence_cipher.rail_fence_encrypt(plain_text, key)
        return jsonify({'encrypted_text': encrypted_text}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/railfence/decrypt', methods=['POST'])
def railfence_decrypt_api():
    try:
        data = request.json
        if not data:
            return jsonify({'error': 'No input data provided'}), 400
        
        cipher_text = data.get('cipher_text')
        key = data.get('key')
        
        if not cipher_text or key is None:
            return jsonify({'error': 'Missing cipher_text or key'}), 400
            
        try:
            key = int(key)
        except ValueError:
            return jsonify({'error': 'Key must be an integer'}), 400
            
        decrypted_text = railfence_cipher.rail_fence_decrypt(cipher_text, key)
        return jsonify({'decrypted_text': decrypted_text}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# API routes for Playfair cipher
@app.route('/api/playfair/creatematrix', methods=['POST'])
def playfair_creatematrix_api():
    try:
        data = request.json
        if not data:
            return jsonify({'error': 'No input data provided'}), 400
        
        key = data.get('key')
        if not key:
            return jsonify({'error': 'Missing key'}), 400
            
        playfair_matrix = playfair_cipher.create_playfair_matrix(key)
        return jsonify({'playfair_matrix': playfair_matrix}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/playfair/encrypt', methods=['POST'])
def playfair_encrypt_api():
    try:
        data = request.json
        if not data:
            return jsonify({'error': 'No input data provided'}), 400
        
        plain_text = data.get('plain_text')
        key = data.get('key')
        
        if not plain_text or not key:
            return jsonify({'error': 'Missing plain_text or key'}), 400
            
        playfair_matrix = playfair_cipher.create_playfair_matrix(key)
        encrypted_text = playfair_cipher.playfair_encrypt(plain_text, playfair_matrix)
        return jsonify({'encrypted_text': encrypted_text}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/playfair/decrypt', methods=['POST'])
def playfair_decrypt_api():
    try:
        data = request.json
        if not data:
            return jsonify({'error': 'No input data provided'}), 400
        
        cipher_text = data.get('cipher_text')
        key = data.get('key')
        
        if not cipher_text or not key:
            return jsonify({'error': 'Missing cipher_text or key'}), 400
            
        playfair_matrix = playfair_cipher.create_playfair_matrix(key)
        decrypted_text = playfair_cipher.playfair_decrypt(cipher_text, playfair_matrix)
        return jsonify({'decrypted_text': decrypted_text}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5050, debug=True)