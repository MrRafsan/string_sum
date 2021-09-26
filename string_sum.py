#taking input and checking if its a number
num1 = input("Enter number and hit enter: ")

def check_is_digit(input_str):
	if input_str.strip().isdigit():
# listing the numbers into digit
		n = [int(d) for d in str(num1)]
#sum of the list
		Sum = sum(n)
#		print(n)

		print("Output: ", Sum)
		print("made by Mr.Rafsan")
		#list korbo
	else:
		print("User input is not a number")

check_is_digit(num1)
