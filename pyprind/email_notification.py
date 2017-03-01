import base64
import os
try:
    import configparser
except ImportError:
    import ConfigParser as configparser

try:
    from Crypto.Cipher import AES
    from Crypto import Random
    crypto_import = True
except ImportError:
    crypto_import = False


class AESCipher(object):

    def __init__(self):
        self.dir_path = os.path.dirname(os.path.abspath(__file__))
        self.key = self.generate_key()
        self.file = None
        self.get_current_path()
        if not crypto_import:
                raise ValueError('crypto package is required when using'
                                 ' email notifications.')

    @staticmethod
    def pad(s):
        return s + (16 - len(s) % 16) * chr(16 - len(s) % 16)

    @staticmethod
    def unpad(s):
        return s[:-ord(s[len(s) - 1:])]

    def get_current_path(self):
        self.file = os.path.join(self.dir_path, 'email_settings.ini.enc')

    def generate_key(self):
        key_path = os.path.join(self.dir_path, 'pyprind.key')
        if not os.path.exists(key_path):
            with open(key_path, 'wb') as key_file:
                key_file.write(os.urandom(16))
        with open(key_path, 'rb') as f:
            key = f.read()
        return key

    def encrypt(self, text):
        text = self.pad(text)
        iv = Random.new().read(AES.block_size)
        cipher = AES.new(self.key, AES.MODE_CBC, iv)
        encrypted_mes = base64.b64encode(iv + cipher.encrypt(text))
        with open(self.file, 'wb') as f:
            f.write(encrypted_mes)

    def decrypt(self):
        with open(self.file, 'rb') as f:
            enc = base64.b64decode(f.read())
        iv = enc[:16]
        cipher = AES.new(self.key, AES.MODE_CBC, iv)
        return self.unpad(cipher.decrypt(enc[16:]))


def setup_email(smtp_server, smtp_port, username, password):
    dir_path = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(dir_path, 'email_settings.ini.enc')
    cipher = AESCipher()
    config = configparser.ConfigParser()
    config.add_section('Email')
    config.set('Email', 'smtp_server', smtp_server)
    config.set('Email', 'smtp_port', str(smtp_port))
    config.set('Email', 'username', username)
    config.set('Email', 'password', password)
    with open(file_path, 'wb') as f:
        config.write(f)
    with open(file_path, 'rb') as af:
        cipher.encrypt(af.read())
