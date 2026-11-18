
# SCCM4910  lab project - a four-operation calculator


def add (a, b):
	return a + b

def sub (a, b):
	return a - b

def multiply (a, b):
	return a + b

def divide (a, b):
	return a / b


def main():
	while True:
		a = float(input("first number: "))
		op = input("operator (+,-,*,/)")
		b = float(input("second number: "))
		if op == "-":
			print("result: ",sub(a, b))
		elif op == "+":
			print("result: ",add(a, b))
		elif op == "*":
			print("result: ",multiply(a, b))
		elif op == "/":
			print("result: ",divide(a, b))
		else:
			print("unknown operator: ",op)

def CircleArea(r):
	if r >= 0:
		return 3.14 * r * r
	else:
		return "NaN"
	

if __name__ == "__main__":
	main()
