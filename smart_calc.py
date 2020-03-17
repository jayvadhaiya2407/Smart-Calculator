
#Creating Function For Feaching Numbers From The String
def fetch_num(string):
	numbers = []
	for num in string.split(' '):
		try:
			numbers.append(float(num))
		except:
			pass
	return numbers

#End Function
def end():
	print("Good Bye!,See You Later")
	input("Press Enter For Exit :\n")
	exit()
	
#Add Function
def add(l):
	sum = 0
	for n in l:
		sum = sum + n
	return sum
	
#Sub Function
def sub(l):
	ans = l[0] - l[1]
	return ans
	
#Mul Function
def mul(l):
	ans = 1
	for n in l:
		ans = ans * n
	return ans
	
#Div Function
def div(l):
	ans = l[0] / l[1]
	return ans
	
#Mod Function
def mod(l):
	ans = l[0] % l[1]
	return ans
	
#Hcf Function
def hcf(l):
	a = l[0]
	b = l[1]
	H = a if a<b else b 
	while H>=1: 
		if a%H==0 and b%H==0:
			return H
		H-=1
	
#Lcm Function
def lcm(l):
	a = l[0]
	b = l[1]
	L=a if a>b else b 
	while L<=a*b:
		if L%a==0 and L%b==0:
			return L
		L+=1
	
#Operations List
operations = {"ADD":add,"ADDITION":add,"PLUS":add,"SARVADO":add,"+":add,"SUM":add,"SUMMETION":add,"MINUS":sub,"SUBTRACT":sub,"-":sub,"BAD":sub,"BADBAKI":sub,"SUB":sub,"SUBTRACTION":sub,"MUL":mul,"MULTIPLICATION":mul,"GUNAKAR":mul,"*":mul,"PRODUCT":mul,"INTO":mul,"DIV":div,"DIVISION":div,"BHAGAKAR":div,"DIVIDETION":div,"/":div,"%":mod,"MODULO":mod,"REMAINDER":mod,"HCF":hcf,"LCM":lcm}

#Starting Function
def start():
	print("Hello Sir, My Name Is JARVI")
	print("Hope!, You Will Enjoy With Me")
	print("My Functionalities Are \n\n\t1. Addition \n\t2. Multiplication \n\t3. Subtraction \n\t4. Division \n\t5. HCF \n\t6. LCM \n\t7. Modulo")
	
#Creating Commands
commands = {"END":end,"CLOSE":end,"STOP":end,"EXIT":end,"BANDH":end}

#Starting Of The Programme
start()

while True:
#Tacking Sting From User
	print()
	string = input("Enter Your Queries :\n")

	for word in string.split(' '):
		if word.upper() in operations.keys():
			try:
				l = fetch_num(string)
				ans = operations[word.upper()] (l)
				print("Your Ans Is :",ans)
			except:
				print("Something Went Wrong!! Try Again")
		else:
			if word.upper() in commands.keys():
				commands[word.upper()]()			