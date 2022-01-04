import random 

def ranact():
	act = random.choice(action)
	return act
	
def inp():
	guss = input('Enter Your choice : (sang , kaghaz, gheichi) ("s" for score "0" for end)')
	return guss
	
action=['sang','kaghaz','gheichi']
cscore=0
score=0
x=1
while x==1:
	computer = ranact()
	player = inp()
	if player==computer:
		print('equal,computer choice was',computer)
	elif player not in action:
			if player=='0':
				if int(score)>int(cscore) :
					print('you win\n scores:\n    your score : {}\n    computer score : {}'.format(score,cscore))
					break
				elif int(score)<int(cscore) : 
					print('computer win\n scores:\n    your score : {}\n    computer score : {}'.format(score,cscore))
					break
			elif player=='s':
				print('your score is : ',score)
			else:
				print('thats not corect , try another')
	elif player=='sang' and computer=='gheichi'or player=='kaghaz'and computer=='sang' or player == 'gheichi' and computer == 'kaghaz':
		print('you won,computer choice was',computer)
		score+=1
	else:
		print('you lose,computer choice was :',computer)
		cscore+=1
	