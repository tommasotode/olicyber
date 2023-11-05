import socket

def client_program():
	host = "2048.challs.olicyber.it"
	port = 10007

	client_socket = socket.socket()
	client_socket.connect((host, port))

	for i in range(2048):
		data = client_socket.recv(1024).decode()
		
		dat = data.split("\n")[-1]
		d = dat.split(" ")
		op = d[0]
		n1 = int(d[1])
		n2 = int(d[2])
		r = 0

		if op == "POTENZA":
			r = pow(n1, n2)
		elif op == "SOMMA":
			r = n1 + n2
		elif op == "DIFFERENZA":
			r = n1 - n2
		else:
			r = n1 // n2

		client_socket.send(str(r).encode())



	client_socket.close()

if __name__ == '__main__':
	client_program()