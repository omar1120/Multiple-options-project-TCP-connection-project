#client
import socket

c = socket.socket(family=socket.AF_INET,type=socket.SOCK_STREAM)
c.connect(("127.0.0.1",20))

while True:
	print("1- gernearate a random srecure password")
	print("2- resolve a records of a given domain")
	print("3- crack md5 hash")
	print("4- exit client\n")
	choice = int(input("Enter choice: "))

	while choice <= 0 and choice >=5:
		print("Invalid choice -- try again!!\n")
		print("1- gernearate a random srecure password")
		print("2- resolve a records of a given domain")
		print("3- crack md5 hash")
		print("4- exit client\n")
		choice = int(input("Enter choice: "))

	if choice == 1:
		data = str(choice)
		c.send(data.encode())
		response = c.recv(1024)
		print("password is:",response.decode())

	elif choice == 2:
		data = str(choice)
		c.send(data.encode())
		Sdata = input("Enter domain: ")
		c.send(Sdata.encode())
		response = c.recv(1024)
		print("host ips for domain:",response.decode())

	elif choice == 3:
		data = str(choice)
		c.send(data.encode())
		Sdata = input("Enter md5 hash to crack: ")
		c.send(Sdata.encode())
		response = c.recv(1024)
		print("cracked hash is:",response.decode())

	elif choice == 4:
		break

c.close()
