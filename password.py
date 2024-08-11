import string
import random


# Getting password length
length = int(input("Enter the length of the password you want to generate: "))

print("Select the character set for your password") 
print("1.Digits \n2.Lower_Letters \n3.Upper_Letters \n4.Special characters \n5.Exit")

temp = ""

while True:
    ch = int(input("Choose the above options you would like to include in your passport \n(NOTE:Enter 5 to exit after selecting the options)"))

    if ch==1:
        temp+=string.digits
    elif ch==2:
        temp+=string.ascii_lowercase
    elif ch==3:
        temp+=string.ascii_uppercase
    elif ch==4:
        temp+=string.punctuation
    elif ch==5:
        break
    else:
        print("select a valid option")

password = []

for i in range(length):
	rndm_password = random.choice(temp)
	password.append(rndm_password)
print("The password is " + "".join(password))

