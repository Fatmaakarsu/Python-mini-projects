print("Wellcome!")
i = 1

while i==1:
	
	num1 = int(input("Enter first number : "))
	num2 = int(input("Enter second number : "))
	operation = input("Chose +  -  *  /  : ")
 
	def add(num1,num2):
   
		print(f"{num1} + {num2} = {num1+num2} ")

	def subtraction(num1,num2):
		print(f"{num1} - {num2} = {num1-num2}")

	def multiply(num1,num2):
		print(f"{num1} * {num2} = {num1*num2}")

	def divide(num1,num2):
		print(f"{num1} / {num2} = {num1/num2}")


	if operation == "+":
		add(num1,num2)

	elif operation == "-":
		subtraction(num1,num2)

	elif operation == "*":
		multiply(num1,num2)

	elif operation == "/":
		divide(num1,num2)

	else:
		print("Wrong entrance")

