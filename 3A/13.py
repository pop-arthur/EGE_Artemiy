from ipaddress import ip_network

count = 0
net = ip_network("164.90.160.0/255.255.224.0")
for ip in net:
    if bin(int(ip))[2:].count("1") % 4 == 0:
        count += 1

print(count)
