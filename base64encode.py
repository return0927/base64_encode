def base64encode(plain):
    bn = ""
    for text in plain:
        bn += (("0" * (8-len(bin(ord(text)).split("b")[1])%8)) + bin(ord(text)).split("b")[1])

    bn = [bn[i:i+6] for i in range(0, len(bn), 6)]
    if len(bn[len(bn)-1]) < 6:
        bn[len(bn)-1] = bn[len(bn)-1]+ ("0" * (6-len(bn[len(bn)-1])))

    dic = [chr(n) for n in range(ord("A"), ord("Z")+1)] + [chr(n) for n in range(ord("a"), ord("z")+1)] + [str(n) for n in range(0, 10)] + ["+", "/"]


    for n in range(len(bn)):
        bn[n] = dic[int(bn[n], 2)]

    out = "".join(bn)
    out += "=" * ((4 - len(out) %4)%4)
    return out

    
data = input("input plain text : ")

print("%20s : %s " % ( 'Plain Phrase', data ))
print("%20s : %s " % ( 'Moduler Cipher', (__import__("base64").b64encode(data.encode("UTF-8"))).decode("UTF-8") ))
print("%20s : %s " % ( 'Manual Cipher', base64encode(data) ))
