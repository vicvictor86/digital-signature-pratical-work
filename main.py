import os
from KeysOperations import generate_private_key
from FilesOperations import readBase64File, readPlainTextFile, savePlainTextFile
from SignaturesOperations import assign, verify
from FilesOperations import saveFileInBase64

option = 0
sha = {224: "SHA224", 256: "SHA256", 384: "SHA384", 512: "SHA512"}
while(True):
    print("1. Assinar um arquivo de texto")
    print("2. Verificar assinatura de um arquivo de texto")
    print("0. Sair")
    option = int(input("Digite a opção desejada: "))

    sha_version = 0

    if(option == 1):
        os.system('cls' if os.name == 'nt' else 'clear')

        textToTest = str(input("Digite o texto a ser assinado: "))

        savePlainTextFile(str(input("Digite o nome do arquivo txt a ser salvo: ")), textToTest)

        private_key = generate_private_key()
        
        while(True):
            print("Versões disponíveis: \nSHA-224\nSHA-256\nSHA-384\nSHA-512")
            sha_version = int(input("Digite o numero correspondente a versão desejada do SHA: "))
            if sha_version in sha.keys():
                public_key, signature = assign(textToTest, private_key, sha[sha_version])
                break
            else:
                print("Opção inválida! Digite novamente!")

        saveFileInBase64(str(input("Digite o nome do arquivo que vai conter a chave pública: ")), public_key)
        saveFileInBase64(str(input("Digite o nome do arquivo que vai conter a mensagem assinada: ")), signature)

        print("Assinatura realizada!")
    elif(option == 2):
        os.system('cls' if os.name == 'nt' else 'clear')

        base64_public_key, base64_signature, text = "", "", ""
        openFiles = False

        try : 
            base64_public_key = readBase64File(str(input("Digite o nome do arquivo que contém a chave: ")))
            base64_signature = readBase64File(str(input("Digite o nome do arquivo que contém a mensagem assinada: ")))
            text = readPlainTextFile(str(input("Digite o nome do arquivo txt de entrada: ")))
            openFiles = True
        except:
            print("Nome de arquivo inválido!")

        if openFiles:
            while(True):
                print("Versões disponíveis: \nSHA-224\nSHA-256\nSHA-384\nSHA-512")
                sha_version = int(input("Digite o numero correspondente a versão desejada do SHA: "))
                if sha_version in sha.keys():
                    break
                else:
                    print("Opção inválida! Digite novamente!")

            if verify(text, base64_public_key, base64_signature, sha[sha_version]):                                          
                print("Assinatura válida!")
            else:
                print("Assinatura inválida!")
        
        else:
            
            os.system('cls' if os.name == 'nt' else 'clear')
            print("Erro ao abrir arquivos!")
            
            
    elif(option == 0):
        print("Finalizando...")
        break

