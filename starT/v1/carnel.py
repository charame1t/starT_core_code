import userset as ju
import json
def terminal ( token ) :
	if (input("User login? {y/n} >>> ") == "y"):
		ju.signIn(None)
	else:
		if(input("User create? {y/n} >>> ") == "y"):
			ju.signUp(None)
	while (True):
		cmd = input(">>> ")
		if (cmd == "end"):
			print()
#=======================#
#=========carnel========#
#=======================#
terminal(None)
#=======================#