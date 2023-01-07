from Crypto.PublicKey import RSA

def generate_private_key():
  return RSA.generate(2048)

def get_public_key(private_key):
  return private_key.publickey().export_key('PEM')