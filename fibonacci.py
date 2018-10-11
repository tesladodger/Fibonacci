#Fibonacci
#Calculates the sequence to the nth number or up to a certain number
#Future versions will save the solution to a file (and read existing files, maybe)
#André Martins, 2018


def ntimes(n) :
	try:
		n = int(n);
	except ValueError:
		print('\n\nYou must introduce an integer\n\n')
		return;
	num = 1;
	next_num = 1;
	for x in range(0,n):
		print(num)
		temp = next_num;
		next_num = next_num + num;
		num = temp;
	print('s    - Save to a file')
	print('else - Go to the main menu')
	ntimeschoice = str(input('==> '));
	if (ntimeschoice=='s'):
		print('\n\nFeature in development\n\n')
		return;
	else:
		print('')
		return;





print('\n\n** Fibonacci calculator **\n\n')

repeat = 1;
while (repeat==True) :
	print('1 - Calculate n number of times')
	print('2 - Calculate up to a certain number')
	print('T - Terminate')
	choice = str(input('==> '));
	choice = choice.upper();
	if (choice=='1') :
		n = str(input('Number of times: '));
		loop = ntimes(n);
	elif (choice=='T'):
		print('\nGoodbye\n')
		repeat = 0;