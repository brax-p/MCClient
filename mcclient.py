import socket
target_host = "192.168.1.77"
target_port = 5094

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client.connect((target_host, target_port))

client.send(bytes("start", 'utf-8'))

response = client.recv(4096)

print(bytes.decode(response))