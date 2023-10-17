import time
import pyotp
import qrcode

#print(pyotp.random_base32())

chave_mestre =  "VBGNKEMGRLXN65VTHMF3TTLC66DN3Z4W"

codigo = pyotp.TOTP(chave_mestre)
print(codigo.now())

codigo_usuario = input("Codigo: ")
print(codigo.verify(codigo_usuario))


link = pyotp.TOTP(chave_mestre).provisioning_uri(name="matheus", issuer_name="CodigoPython")

meu_qrcode = qrcode.make(link)
meu_qrcode.save("qrcode.png")
