import getpass
import telnetlib
import time

HOST = "10.99.99.11"
username = "sntuser"
password = "Ilovenetworks99"
enable = "cisco"

tn = telnetlib.Telnet(HOST)
tn.read_until(b"Username: ")
tn.write(username.encode('ascii')+ b"\n")
tn.read_until(b"Password: ")    
tn.write(password.encode('ascii')+ b"\n")
tn.read_until(b"R1>")
tn.write(b"show clock\n")
clock = tn.read_until(b"R1>")
print ("Current clock : " + clock.decode('ascii'))

tn.write(b"enable\n")
tn.read_until(b"Password: ")
tn.write(enable.encode('ascii')+ b"\n")
clock = tn.read_until(b"R1#")

tn.write(b"terminal length 0\n")
tn.read_until(b"R1#")

tn.write(b"show run\n")
showrun =  tn.read_until(b"R1#")
print(showrun.decode('ascii'))


tn.write(b"exit\n")
print(tn.read_all().decode('ascii'))

