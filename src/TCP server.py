#server
import socket
import hashlib
import random
import dns.resolver

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('127.0.0.1', 23232))
s.listen(8)
client, address = s.accept()
print("Server is running...")
while True:

    req = client.recv(1024)
    response = req.decode()

    if response == "1":
        letters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
        pass1 = random.choice(letters) + random.choice(letters) + random.choice(letters)
        pass2 = str(random.randint(0,9)) + str(random.randint(0,9)) + str(random.randint(0,9)) + str(random.randint(0,9)) + str(random.randint(0,9)) + str(random.randint(0,9))
        password = pass1 + str(pass2)
        client.send(password.encode())

    elif response == "2":
        Cr = client.recv(1024)
        Cresponse = Cr.decode()
        A_record = []
        R = dns.resolver.resolve(Cresponse, "A",raise_on_no_answer=False)
        for value in R:
            record.append(str(value.to_text()))
        string_record = str(A_record)
        client.send(string_record.encode())

    elif response == "3":
        r = client.recv(1024)
        Response = r.decode()
        hash_target = Response
        result = "No password found in dictionary"

        with open("dictionary.txt", "r") as file:
            for line in file.readlines():
                cleaned_line = line.strip()
                hashed_line = hashlib.md5(cleaned_line.encode()).hexdigest()

                if hashed_line == hash_target:
                    result = cleaned_line
                    break 

        client.send(result.encode())           

    elif response == "4":
        break

client.close()