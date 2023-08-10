def encrypt(val,key):
    smallalpha = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    bigalpha = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
    retval = ''
    for chr in val:
        if chr.isupper(): 
            chr_index = bigalpha.index(chr)
            enc_index = (chr_index + key) % 26
            retval = retval+bigalpha[enc_index]
        else: 
            chr_index = smallalpha.index(chr)
            enc_index = (chr_index + key) % 26
            retval = retval+smallalpha[enc_index]
    return retval;         

def decrypt(val,key):
    smallalpha = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    bigalpha = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
    retval = ''
    for chr in val:
        if chr.isupper(): 
            chr_index = bigalpha.index(chr)
            enc_index = (chr_index - key) % 26
            retval = retval+bigalpha[enc_index]
        else: 
            chr_index = smallalpha.index(chr)
            enc_index = (chr_index - key) % 26
            retval = retval+smallalpha[enc_index] 
    return retval;    
encval = encrypt("Exlaso",100);   
print(encval)
decval = decrypt(encval,100)
print(decval)
