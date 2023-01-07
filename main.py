from base64 import b64encode, b64decode

from KeysOperations import generate_private_key, get_public_key
from SignaturesOperations import generate_signature, verify_signature
from HashOperations import generate_hash

def assign(plain_text, private_key, hash_algorithm):
  hash_object = generate_hash(plain_text)

  # hash_hexadecimal = hash_object.hexdigest()

  signature = generate_signature(private_key, hash_object)

  public_key = get_public_key(private_key)
  base64_public_key = b64encode(public_key)
  f = open('mypublickey.base64','wb')
  f.write(base64_public_key)
  f.close()

  signature = generate_signature(private_key, hash_object)
  base64_signature = b64encode(signature)
  f = open('signature.base64','wb')
  f.write(base64_signature)
  f.close()
  
  return base64_public_key, base64_signature

def verify(plain_text, base64_public_key, base64_signature, hash_algorithm):
  public_key = b64decode(base64_public_key)
  signature = b64decode(base64_signature)

  read_hash_object = generate_hash(plain_text)

  return verify_signature(public_key, signature, read_hash_object)

textToTest = "first"
f = open('text.txt','wb')
f.write(textToTest.encode('utf-8'))
f.close()

private_key = generate_private_key()
public_key, signature = assign(textToTest, private_key, "SHA256")

f = open('mypublickey.base64','r')
base64_public_key = f.read()
f.close()

# Ler assinatura de arquivo
f = open('signature.base64','r')
base64_signature = f.read()
f.close()

# Ler texto a ser verificado
f = open('text.txt','r')
text = f.read()
f.close()

print(verify(text, base64_public_key, base64_signature, "SHA256"))