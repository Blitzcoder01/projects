#developer:-RIYA MATHUR
#language chosen:- Python 3.x

import random
print("******stone ,paper, scissor******")
print("to play press 1")
print("for exit press 0")
p=int(input(" your choice"))
while True:	
	while (p==1):
		print("\n")
		print("enter1 for stone:")
		print("enter 2 for paper:")
		print("enter 3 for scissor")
		a=int(input("enter your choice here  "))
		print("your choice is ",a)

		d=random.randint(1,3)
		print("computer choice is ",d)

		if a >3:
				print("not required")
				break
		if a==d:
				print("tie , try again")
		elif ( a==1 and d==2) or (a==2 and d==3) 			or 	(a==3 and d==1):
				print("you loose, computer has won the match")
		else:
				print("you won")
	else:
		print("you have successfully left the game")
