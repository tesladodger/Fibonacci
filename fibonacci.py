#Fibonacci
#Calculates the sequence to the nth iteration or up to a certain number
#Future versions will save the solution to a file (and read existing files, maybe)
#André Martins, 2018


def ntimes(n) :
	try:
		n = int(n);
	except ValueError:
		print('\n\nYou must introduce an integer\n\n')
		return;
	if (n <= 0):
		print('\n\nYou must introduce a positive integer\n\n')
		return;
	num = 1;
	next_num = 1;
	for x in range(0,n):
		print(num)
		temp = next_num;
		next_num = next_num + num;
		num = temp;
	print('S    - Save to a file')
	print('else - Go to the main menu')
	ntimeschoice = str(input('==> '));
	if (ntimeschoice=='s'):
		print('\n\nFeature in development\n\n')
		return;
	else:
		print('')
		return;


def upton(maxnum) :
	try:
		maxnum = int(maxnum);
	except ValueError:
		print('\n\nYou must introduce an integer\n\n')
		return;
	if (maxnum < 1):
		print('\n\nYou must insert a value greater or equal to 1\n\n')
	num = 1;
	next_num = 1;
	itera = 0;
	while (num<=maxnum) :
		print(num)
		temp = next_num;
		next_num = next_num + num;
		num = temp;
		itera += 1;
	print('S    - Show more information')
	print('else - Go to the main menu')
	ntimeschoice = str(input('==> '));
	if (ntimeschoice=='s'):
		print("\n\nNumber of iterations:       ", itera)
		print("Your number:                ", maxnum)
		print("Next number in the sequence:", num)
		print("Diference to that number:   ", (num - maxnum))
		print("\n\n")
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
		ntimes(n);
	elif (choice=='2'):
		maxnum = str(input('Calculate to the number: '))
		upton(maxnum);
	elif (choice=='T'):
		print('\nGoodbye\n')
		repeat = 0;