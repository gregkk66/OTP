aDict = dict(zip('abcdefghijklmnopqrstuvwxyz.!?()-ABCDEFGHIJKLMNOPQRSTUVWXYZ', 
                              ['00000','00001','00010','00011','00100',
                              '00101','00110','00111','01000',
                              '01001','01010','01011','01100','01101','01110','01111',
                              '10000','10001','10010','10011',
                              '10100','10101','10110','10111',
                              '11000','11001',
                              '11010','11011','11100','11101','11110','11111',
                              '00000','00001','00010','00011','00100',
                              '00101','00110','00111','01000',
                              '01001','01010','01011','01100','01101','01110','01111',
                              '10000','10001','10010','10011',
                              '10100','10101','10110','10111',
                              '11000','11001']))
def stringxor(str1,str2): ### stringxor
    xor=""
    for i in range(len(str1)):
        xor+=str(int(str1[i])^int(str2[i]))
    return xor

def stringtobin(str1):      ###### string to binary string
    cipherstring=""
    for i in str1:
        cipherstring+=aDict[i]
    return cipherstring

def bintostring(str1):     ######## binary string to string
    inv_map = {v: k for k, v in aDict.items()}
    result=""
    for i in range(0,len(str1),5):
        result+=inv_map[str1[i:i+5]]
    return result

def otp_encrypt(str1): ######### Otp encrypt
    import random
    global key1
    plaintext=stringtobin(str1)
    key1=""
    for i in range(len(plaintext)):    ###### create key, len key = len plaintext
        key1+=str(random.randint(0,1))
    encrypted=stringxor(key1,plaintext)  
    encrypted=(bintostring(encrypted))
    return encrypted


def otp_decrypt(str1):     ######### otp decrypt
    ciphertext=otp_encrypt(str1) 
    plaintext=stringtobin(ciphertext)
    plaintext=stringxor(plaintext,key1)
    plaintext=bintostring(plaintext)
    return plaintext

message="WHATISHIDDENINPLAINSIGHTISTHEMOSTDIFFICULTTOFIND"
print("           Message = " + message )
print()
print("###################################################################################")
print("########  Ciphertext = " +otp_encrypt(message) + "  ##########")
print("########  Plaintext = " +otp_decrypt(message)+ "   ##########")
print("###################################################################################")    
        
       




    
    
    


