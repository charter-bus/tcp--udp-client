import socket

target_host = "127.0.0.1"
target_port = 9997

# create a socket object
client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

print("Sending data...\n")
client.sendto(b"AAABBBCCC", (target_host, target_port))

print("Receiving data...\n")
data, addr = client.recvfrom(4096)

print(data.decode())
client.close()

