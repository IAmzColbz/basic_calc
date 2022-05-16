import os

os.system('cls' if os.name == 'nt' else 'clear')

full_name = input("What is your name?\n\t>>>")

os.system('cls' if os.name == 'nt' else 'clear')

full_name = full_name.lower().strip()
message = f"Hello {full_name.title()}"
print(message)

valid_procedure = False
while not valid_procedure:
	print("Would you like to procede? Yes/No")
	procedure = input("\t>>>").strip().lower()

	if procedure == "yes":
		os.system('cls' if os.name == 'nt' else 'clear')
		print("Thank you for using Colby's Calc")
		valid_procedure = True
	
	elif procedure == "no":
		os.system('cls' if os.name == 'nt' else 'clear')
		quit()

	else:
		os.system('cls' if os.name == 'nt' else 'clear')
		print("There was an error in your procedure, please try again.")

def inputfloat(message):
	while True:
		try:
			userInput = float(input(message))
		except ValueError:
			os.system('cls' if os.name == 'nt' else 'clear')
			print("Please only input numbers! Try again.")
			continue
		else:
			os.system('cls' if os.name == 'nt' else 'clear')
			return userInput
			break

def inputint(message):
	while True:
		try:
			userInput = int(input(message))
		except ValueError:
			os.system('cls' if os.name == 'nt' else 'clear')
			print("Please only input numbers! Try again.")
			continue
		else:
			os.system('cls' if os.name == 'nt' else 'clear')
			return userInput
			break

first_number = inputfloat("x  _?_  x\nWhat is the first number you would like to calculate?  \n\t>>>")

print()
second_number = inputfloat(f"{first_number}  _?_  x\nWhat is the second number you would like to calculate?  \n\t>>>")

valid_input = False
while not valid_input:
	print(f'\t{first_number} _?_ {second_number}')
	raw_operation = input("Please type the first letter of your operation: \n\t(A-addition/S-subtraction/M-multiplication/D-division)\n\t>>>")
	os.system('cls' if os.name == 'nt' else 'clear')
	raw_operation = raw_operation.strip().upper()
	if raw_operation == "A":
		raw_output(first_number + second_number)
		operation = '+'
		valid_input = True
	elif raw_operation == "S":
		raw_output = (first_number - second_number)
		operation = '-'
		valid_input = True
	elif raw_operation == "M":
		raw_output = (first_number * second_number)
		operation = 'x'
		valid_input = True
	elif raw_operation == "D":
		raw_output = (first_number / second_number)
		operation = '/'
		valid_input = True
	else:
		print("Please give the first letter of your operation")

roundto = inputint('How many digits after the decimal would you like to round to?\n\t>>>')
complete = round(raw_output, roundto)

print(complete)