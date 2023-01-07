from Crypto.Hash import SHA224, SHA256, SHA384, SHA512

hash_algorithms = {
  "SHA224": SHA224,
  "SHA256": SHA256,
  "SHA384": SHA384,
  "SHA512": SHA512
}

def generate_hash(text, hash_algorithm_name):
  hash_algorithm = get_hash_algorithm(hash_algorithm_name)

  if hash_algorithm is None:
    return None

  return hash_algorithm.new(data=text.encode('utf-8'))

def get_hash_algorithm(hash_algorithm_name):
  try:
    return hash_algorithms[hash_algorithm_name]
  except KeyError:
    return None