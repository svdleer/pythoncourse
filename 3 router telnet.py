import getpass
import telnetlib


HOST = "10.99.99.11"
username = "sntuser"
password = "Ilovenetworks99"
enable = "cisco"

routerlist = ["10.99.99.11", "10.99.99.12", "10.99.99.13"]
    
for ip in routerlist:   
    print("Connecting to: " + ip)
    f = open(ip, "w")
    tn = telnetlib.Telnet(ip, timeout=2)
    tn.read_until(b"Username: ")
    tn.write(username.encode('ascii')+ b"\n")
    tn.read_until(b"Password: ")    
    tn.write(password.encode('ascii')+ b"\n")
    index, m, output = tn.expect([b">", b"#"])
    if index == 0:
        tn.write(b"enable\n")
        tn.read_until(b"Password")
        tn.write(enable.encode('ascii')+ b"\n")
        tn.read_until(b"#", timeout=5)

    tn.write(b"terminal length 0\n")
    tn.expect([b">", b"#"])   
    tn.read_very_lazy()
    tn.write(b"show run\n")
    showrun = tn.read_until(b'#')
    cmdIndex = showrun.find(b"bytes")
    output = showrun[cmdIndex + len("bytes\n"):]

    print (output)
    tn.write(b"exit\n") 
    f.write(output.decode('ascii'))
    f.close

