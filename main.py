from base64 import b64encode, b64decode

from KeysOperations import generate_private_key, get_public_key
from SignaturesOperations import generate_signature, verify_signature
from HashOperations import generate_hash
from FilesOperations import saveFileInBase64, readBase64File, readPlainTextFile, savePlainTextFile

def assign(plain_text, private_key, hash_algorithm_name):
  hash_object = generate_hash(plain_text, hash_algorithm_name)

  if hash_object is None:
    raise ValueError("Hash algorithm not supported")

  # If it is really necessary to encrypt the hash, uncomment the following lines
  hash_hexadecimal = hash_object.hexdigest().encode('utf-8')
  hash_of_hash_hexadecimal = generate_hash(hash_hexadecimal, hash_algorithm_name)

  public_key = get_public_key(private_key)
  base64_public_key = b64encode(public_key)

  saveFileInBase64('my_publickey', base64_public_key)

  signature = generate_signature(private_key, hash_of_hash_hexadecimal)
  base64_signature = b64encode(signature)

  saveFileInBase64('signature', base64_signature)
  
  return base64_public_key, base64_signature

def verify(plain_text, base64_public_key, base64_signature, hash_algorithm_name):
  public_key = b64decode(base64_public_key)
  signature = b64decode(base64_signature)

  read_hash_object = generate_hash(plain_text, hash_algorithm_name)
  hash_hexadecimal = read_hash_object.hexdigest().encode('utf-8')
  hash_of_hash_hexadecimal = generate_hash(hash_hexadecimal, hash_algorithm_name)

  return verify_signature(public_key, signature, hash_of_hash_hexadecimal)

textToTest = "first"

savePlainTextFile('text', textToTest)

private_key = generate_private_key()

public_key, signature = assign(textToTest, private_key, "SHA224")

base64_public_key = readBase64File('my_publickey')
base64_signature = readBase64File('signature')
text = readPlainTextFile('text')

print(verify(text, base64_public_key, base64_signature, "SHA224"))