import socket

try:
    f = open(input('Type in your file path: '), "r")
except:
        print("Reading File ERROR!");

domain_list_raw = f.read()
domain_list = domain_list_raw.split('\n')

for domain  in domain_list:
    try:
        # print(domain)
        output = socket.gethostbyname(domain)
        print(output)
    except:
        print("ERROR!");
f.close()
