from Crypto.Cipher import Salsa20

def encrypt(text, key):
  cipher = Salsa20.new(key=key)
  cypher_text = cipher.encrypt(text.encode('utf-8'))
  return cipher.nonce + cypher_text

def decrypt(cypher_text, key):
  nonce = cypher_text[:8]
  cypher_text = cypher_text[8:]

  cipher = Salsa20.new(key=key, nonce=nonce)
  return cipher.decrypt(cypher_text)