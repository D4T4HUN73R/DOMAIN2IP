import socket

f = open(input('Type in your file path: '), "r")
domain_list = f.readlines()

for domains in domain_list:
    print(domains) # Debugging
    try:
        output = socket.gethostbyname(domains)
        print(output)
    except:
        print("ERROR!");
f.close()