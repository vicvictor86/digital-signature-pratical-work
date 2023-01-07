def saveFileInBase64(filename, base64_file):
  file = open(f'{filename}.base64','wb')
  file.write(base64_file)
  file.close()

def readBase64File(filename):
  file = open(f'{filename}.base64','r')
  file_content = file.read()
  file.close()

  return file_content

def readPlainTextFile(filename):
  file = open(f'{filename}.txt','r')
  text = file.read()
  file.close()

  return text

def savePlainTextFile(filename, text_to_save):
  file = open(f'{filename}.txt','w')
  file.write(text_to_save)
  file.close()
