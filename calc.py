import os

def inputfloat(message):
	while True:
		try:
			return float(input(message))
		except ValueError:
			clear()
			print("Please only input numbers! Try again.")
			continue


def inputint(message):
	while True:
		try:
			return int(input(message))
		except ValueError:
			clear()
			print("Please only input numbers! Try again.")
			continue


def clear():
    os.system('cls' if os.name == 'nt' else 'clear')


def calculate(first_number, second_number):
	valid_input = False
	while not valid_input:
		print(f'\t{first_number} _?_ {second_number}')
		raw_operation = input("Please type the first letter of your operation: \n\t(A-addition/S-subtraction/M-multiplication/D-division)\n\t>>>")
		clear()
		raw_operation = raw_operation.strip().upper()
		if raw_operation == "A":
			valid_input = True
			return(first_number + second_number)
		elif raw_operation == "S":
			valid_input = True
			return(first_number - second_number)
		elif raw_operation == "M":
			valid_input = True
			return(first_number * second_number)
		elif raw_operation == "D":
			valid_input = True
			return(first_number / second_number)
		else:
			print("Please give the first letter of your operation")
  
def cont():  
	valid_procedure = False
	while not valid_procedure:
		print("Would you like to procede? Yes/No")
		procedure = input("\t>>>").strip().lower()

		if procedure == "yes":
			clear()
			return True
		
		elif procedure == "no":
			clear()
			print("Thank you for using Colby's Calc")
			return False

		else:
			clear()
			print("There was an error in your procedure, please try again.")
   

if __name__=="__main__":
	proceed = True
	while proceed == True:
		first_number = inputfloat("x  _?_  x\nWhat is the first number you would like to calculate?  \n\t>>>")
		print()
		second_number = inputfloat(f"{first_number}  _?_  x\nWhat is the second number you would like to calculate?  \n\t>>>")
		print()
		raw_output = calculate(first_number, second_number)
		round_to = inputint('How many digits after the decimal would you like to round to?\n\t>>>')
		print(round(raw_output, round_to))
		print()
		proceed = cont()
