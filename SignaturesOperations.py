from Crypto.Signature import pkcs1_15
from Crypto.PublicKey import RSA

from HashOperations import generate_hash
from KeysOperations import get_public_key
from base64 import b64encode, b64decode

def generate_signature(private_key, hash_object):
  return pkcs1_15.new(private_key).sign(hash_object)

def verify_signature(public_key, signature, hash_object):
  try: 
    key = RSA.import_key(public_key)
    pkcs1_15.new(key).verify(hash_object, signature)
    
    return True
  except (ValueError, TypeError):
    return False

def assign(plain_text, private_key, hash_algorithm_name):
  hash_object = generate_hash(plain_text, hash_algorithm_name)

  if hash_object is None:
    raise ValueError("Hash algorithm not supported")

  hash_hexadecimal = hash_object.hexdigest().encode('utf-8')
  hash_of_hash_hexadecimal = generate_hash(hash_hexadecimal, hash_algorithm_name)

  public_key = get_public_key(private_key)
  base64_public_key = b64encode(public_key)

  signature = generate_signature(private_key, hash_of_hash_hexadecimal)
  base64_signature = b64encode(signature)
  
  return base64_public_key, base64_signature

def verify(plain_text, base64_public_key, base64_signature, hash_algorithm_name):
  public_key = b64decode(base64_public_key)
  signature = b64decode(base64_signature)

  read_hash_object = generate_hash(plain_text, hash_algorithm_name)
  hash_hexadecimal = read_hash_object.hexdigest().encode('utf-8')
  hash_of_hash_hexadecimal = generate_hash(hash_hexadecimal, hash_algorithm_name)

  return verify_signature(public_key, signature, hash_of_hash_hexadecimal)
