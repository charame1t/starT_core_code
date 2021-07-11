def signUp (token):
	import random
	import json
	file_path = "userdata.json"
	#.get
	usname = input("please your name >>> ")
	userid = random.randint(100000,999999)
	if ('id',userid in json_data == True):
		userid = random.randint(100000,999999)
	userid = str(userid)
	uspass = random.randint(1000,9999)
	if ('pass',userid in json_data == True):
		userid = random.randint(100000,999999)
	uspass = str(uspass)
	with open(file_path, "r") as json_file :
	    data = json.load(json_file)
	data['user'].append({
	    "name": usname,
	    "id": userid,
	    "pass": uspass
	})
	with open(file_path, 'w') as outfile:
	    json.dump(data, outfile,indent=4)
	print("data to \n\'name\' => " + usname + "\n\'id\' => " + userid)
	print("and you are account password is " + uspass)

def signIn (token):
	import json
	global file_path
	file_path = "userdata.json"
	with open(file_path, "r") as json_file :
	    json_data = json.load(json_file)
	inp = input("prease user id (6 charset int) >>> ")
	if ('id',inp in json_data == True):
		logname = inp
		print("succses")
		inp = input("prease user password (4 charset int) >>> ")
		if ('pass',inp in json_data == True):
			print("login succses")
			print("data to \n\'name\' => " + logname + "\n\'id\' => " + inp)
		else:
			print("err")
	else:
		print("err")