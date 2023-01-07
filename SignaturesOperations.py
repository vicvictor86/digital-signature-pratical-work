from Crypto.Signature import pkcs1_15
from Crypto.PublicKey import RSA

def generate_signature(private_key, hash_object):
  return pkcs1_15.new(private_key).sign(hash_object)

def verify_signature(public_key, signature, hash_object):
  try: 
    key = RSA.import_key(public_key)
    pkcs1_15.new(key).verify(hash_object, signature)
    return True
  except (ValueError, TypeError):
    return False