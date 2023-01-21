from KeysOperations import generate_private_key
from FilesOperations import readBase64File, readPlainTextFile, savePlainTextFile
from SignaturesOperations import assign, verify
from FilesOperations import saveFileInBase64

textToTest = "first"

savePlainTextFile('text', textToTest)

private_key = generate_private_key()

public_key, signature = assign(textToTest, private_key, "SHA224")

saveFileInBase64('my_publickey', public_key)
saveFileInBase64('signature', signature)

base64_public_key = readBase64File('my_publickey')
base64_signature = readBase64File('signature')
text = readPlainTextFile('text')

print(verify(text, base64_public_key, base64_signature, "SHA224"))
