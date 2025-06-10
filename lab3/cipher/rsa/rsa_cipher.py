from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives import hashes, serialization
import os

class RSACipher:
    def __init__(self):
        self.private_key = None
        self.public_key = None
        self.keys_dir = os.path.join(os.path.dirname(__file__), 'keys')
        if not os.path.exists(self.keys_dir):
            os.makedirs(self.keys_dir)
            
    def generate_keys(self):
        """Generate a new RSA key pair"""
        self.private_key = rsa.generate_private_key(
            public_exponent=65537,
            key_size=2048
        )
        self.public_key = self.private_key.public_key()
        
        # Save private key
        with open(os.path.join(self.keys_dir, 'private.pem'), 'wb') as f:
            f.write(self.private_key.private_bytes(
                encoding=serialization.Encoding.PEM,
                format=serialization.PrivateFormat.PKCS8,
                encryption_algorithm=serialization.NoEncryption()
            ))
            
        # Save public key
        with open(os.path.join(self.keys_dir, 'public.pem'), 'wb') as f:
            f.write(self.public_key.public_bytes(
                encoding=serialization.Encoding.PEM,
                format=serialization.PublicFormat.SubjectPublicKeyInfo
            ))
            
    def load_keys(self):
        """Load RSA keys from files"""
        try:
            # Load private key
            with open(os.path.join(self.keys_dir, 'private.pem'), 'rb') as f:
                self.private_key = serialization.load_pem_private_key(
                    f.read(),
                    password=None
                )
                
            # Load public key
            with open(os.path.join(self.keys_dir, 'public.pem'), 'rb') as f:
                self.public_key = serialization.load_pem_public_key(f.read())
                
        except FileNotFoundError:
            self.generate_keys()
            
        return self.private_key, self.public_key
        
    def encrypt(self, message: str, key) -> bytes:
        """Encrypt a message using RSA"""
        encrypted = key.encrypt(
            message.encode(),
            padding.OAEP(
                mgf=padding.MGF1(algorithm=hashes.SHA256()),
                algorithm=hashes.SHA256(),
                label=None
            )
        )
        return encrypted
        
    def decrypt(self, ciphertext: bytes, key) -> str:
        """Decrypt a message using RSA"""
        decrypted = key.decrypt(
            ciphertext,
            padding.OAEP(
                mgf=padding.MGF1(algorithm=hashes.SHA256()),
                algorithm=hashes.SHA256(),
                label=None
            )
        )
        return decrypted.decode()
        
    def sign(self, message: str, private_key) -> bytes:
        """Sign a message using RSA"""
        signature = private_key.sign(
            message.encode(),
            padding.PSS(
                mgf=padding.MGF1(hashes.SHA256()),
                salt_length=padding.PSS.MAX_LENGTH
            ),
            hashes.SHA256()
        )
        return signature
        
    def verify(self, message: str, signature: bytes, public_key) -> bool:
        """Verify a signature using RSA"""
        try:
            public_key.verify(
                signature,
                message.encode(),
                padding.PSS(
                    mgf=padding.MGF1(hashes.SHA256()),
                    salt_length=padding.PSS.MAX_LENGTH
                ),
                hashes.SHA256()
            )
            return True
        except:
            return False 