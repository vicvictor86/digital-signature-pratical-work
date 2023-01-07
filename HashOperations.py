from Crypto.Hash import SHA256

def generate_hash(text):
  return SHA256.new(data=text.encode('utf-8'))