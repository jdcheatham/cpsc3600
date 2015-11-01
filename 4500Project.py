"""J. Cheatham
CPSC4500 First project
Encryption program"""


def enigma(text, enc):
    """enigma encryption tool"""

    """setting up rotors"""
    firstRotor = " gnuahovbipwcjqxdkryelszfmt"
    secondRotor = " ejotychmrwafkpuzdinsxbglqv"
    thirdRotor = " bdfhjlnprtvxzacegikmoqsuwy"

    """setting up counters"""
    firstCounter = 0
    secondCounter = 0
    thirdCounter = 0

    cipher = []
    """create encrypted/decrypted output"""
    if enc.lower() == "e":  #encrypt
        for each in text:
            crypt = ""
            for letter in each.lower():
                if letter in firstRotor:
                    x = firstRotor.find(letter)
                    y = thirdRotor[(x+firstCounter)%27]
                    z = secondRotor.find(y)
                    if firstCounter > 26:
                        secondCounter += 1
                        firstCounter = 0
                    crypt = crypt + thirdRotor[(z+secondCounter)%27]
                else:
                    crypt=crypt + letter
                firstCounter+=1
            cipher.append(crypt)
        return cipher

    else:#decrypt
        for each in text:
            crypt = ""
            for letter in each.lower():
                if letter in firstRotor:
                    x = thirdRotor.find(letter)
                    y = secondRotor[(x-secondCounter)%27]
                    z = thirdRotor.find(y)
                    crypt = crypt + firstRotor[(z - firstCounter)%27]
                    if firstCounter > 26:
                        secondCounter += 1
                        firstCounter = 0
                else:
                    crypt=crypt+letter
                firstCounter+=1
            print (crypt)
            cipher.append(crypt)
        return cipher


def Ceasar(text, enc, shift):
    """the Ceasar shift function. """

    alphabet="abcdefghijklmnopqrstuvwxyz "#setting things up
    cipher=[]

    """create encrypted/decrypted output"""
    if enc =="e":#encode
        for each in text:
            crypt=""
            for letter in each:
                if letter in alphabet:
                    x=alphabet.find(letter)
                    crypt=crypt + alphabet[(x+int(shift))%len(alphabet)]
                else:
                    crypt = crypt + letter
            print(crypt)
            cipher.append(crypt)
        return cipher

    else:
        for each in text:
            crypt=""
            for letter in each:
                if letter in alphabet:
                    x=alphabet.find(letter)
                    crypt=crypt+alphabet[(x-int(shift))%len(alphabet)]
                else:
                    crypt=crypt+letter
            cipher.append(crypt)
        return cipher

def Substitution(text,enc):
    """ The substitution function.  Creates a substitution dictionary based on a key alphabet"""
    """set up variables for the function"""
    keydictionary={}
    dekeydictionary={}
    ciphertext=[]
    alphabet="abcdefghijklmnopqrstuvwxyz "
    key="ebcdifghojklmnupqrstavwxyz "#the key can be changed for others.

    #create dictionarys for substitution
    for x in range (len(alphabet)):
        keydictionary[alphabet[x]]=key[x]
    for x in range (len(key)):
        dekeydictionary[key[x]]=alphabet[x]

    if enc=="e":
        #create encrypted output
        for each in text:
            crypt = ""
            for letter in each.lower():
                if letter in keydictionary:
                    crypt = crypt+keydictionary[letter]
                else:
                    crypt = crypt + letter
            ciphertext.append(crypt+"\n")
        return ciphertext
    else:
        #create decrypted output
        for each in text:
            decrypt = ""
            for letter in each.lower():
                if letter in dekeydictionary:
                    decrypt = decrypt + dekeydictionary[letter]
                else:
                    decrypt = decrypt + letter
            ciphertext.append(decrypt+"\n")
        return ciphertext

def main():
    while True:
        txt=[]
        text=""
        text = input("File to encrypt/decrypt, exit to quit")#input the filename
        if text =="exit":
            break

        """get the file to encrypt"""

            enctype = input("Cypher type?  Ceasar (c),Substitution (s) or Enigma (e)")
            enc = input("encrypt or decrypt?")

            """this is where we will decide what type of encryption to use"""
            if enctype[0] == "s":
                cipherText= Substitution(txt,enc)
            elif enctype[0] == "c":
                shift=input("shift number")
                cipherText = Ceasar(txt,enc, shift)
            elif enctype[0] == "e":
                cipherText = enigma(txt, enc)

            #write the new file
            if enctype[0] == "s":
                outName = "substitution"
            elif enctype[0] == "c":
                outName = "caesar"
            else:
                outName = "enigma"
            if enc[0]=="e":
                outName = outName +"-encrypted"
            else:
                outName = outName + "-decrypted"

            with open(outName,'w') as fout:
                for each in cipherText:
                    fout.write(each+"\n")
                fout.close()
        except:
            print("Could not find file.")

    print("exiting the program")

if __name__ == "__main__":
    main()
