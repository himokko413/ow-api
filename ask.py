from upl import getUpl

def askId():
	plt = None
	usr = None
	dsc = None

	while not usr:
		usr = None
		usr = input('What is your username?\n-> ')
		if not usr:
			print("Please enter a username.")

	while not plt in range(0,2):
		try:
			plt = None
			plt = input('1 - PC\n2 - XBL\n3 - PSN\nWhich platform are you using?\n-> ')
			if not plt:
				print("Please enter a value.")
			elif not int(plt) in range(1,3):
				print("Invalid value, please try again.")
			else:
				plt = int(plt) - 1
		except ValueError:
			print("Invalid value, please try again.")

	while plt == 0 and not dsc:
		dsc = None
		dsc = input('Enter the discriminator. This is the number after your username.\nExample: himokko413#\033[1;37m1907\033[0m\n-> ')
		if not dsc:
			print("Please enter a discriminator or search another platform.")

	return(getUpl(plt,usr,dsc))
