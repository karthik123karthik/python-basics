import random
import string

message = input("Enter the message you want to send: ")
characters = list(string.printable)

def encrypt(msg):
    n = len(msg)
    if n<3:
         return msg[::-1]
    else:
        front = ""
        back = ""
        for _ in range(3):
            front+=random.choice(characters)
            back+=random.choice(characters)
        newmsg = msg[1:]+msg[0]
        #print(newmsg)
        newmsg = front + newmsg + back
        return newmsg


def decrypt(msg):
    n = len(msg)
    if n<3:
        return msg[::-1]
    else:
        actualmsg = msg[3:n-4]
        #print(actualmsg)
        actualmsg = msg[n-4]+ actualmsg
        return actualmsg



if __name__ == '__main__':
    encryptedmsg = encrypt(message)
    #print(encryptedmsg)
    print("THE DECRYPTED MESSAGE IS :",decrypt(encryptedmsg))
