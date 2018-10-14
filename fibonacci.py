#Fibonacci
#Calculates the sequence to the nth iteration or up to a certain number
#You can save the results to a '.txt' file with the name you want
#André Martins, 2018

import os

def ntimes(n) :
	save_file = 0;
	try:
		n = int(n);
	except ValueError:
		print('\n\nYou must introduce an integer\n\n')
		return save_file;
	if (n <= 0):
		print('\n\nYou must introduce a positive integer\n\n')
		return save_file; #=False
	os.system('cls')
	num = 1;
	next_num = 1;
	print(num)
	for x in range(0,n-1):         
		print(next_num)            #By doing this we do one less calculation
		temp = next_num;           #Is there a better way to do this without temp?
		next_num = next_num + num;
		num = temp;
	print('\nS    - Save to a file')
	print('else - Go to the main menu')
	ntimeschoice = str(input('==> '));
	if (ntimeschoice=='s'):
		save_file = 1;
		return save_file; #=True
	else:
		os.system('cls')
		return save_file; #=False


def upton(maxnum) :
	try:
		maxnum = int(maxnum);
	except ValueError:
		print('\n\nYou must introduce an integer\n\n')
		return;
	if (maxnum < 1):
		print('\n\nYou must insert a value greater or equal to 1\n\n')
	os.system('cls')
	num = 1;
	next_num = 1;
	itera = 0;
	print(num)
	while (next_num<=maxnum) :
		print(next_num)
		temp = next_num;
		next_num = next_num + num;
		num = temp;
		itera += 1;
	print('\nS    - Show more information')
	print('else - Go to the main menu')
	ntimeschoice = str(input('==> '));
	if (ntimeschoice=='s'):
		os.system('cls')
		if (num==maxnum):
			print("The number", maxnum, "is in the Fibonacci sequence")
		print("Number of iterations:       ", itera)
		print("Your number:                ", maxnum)
		print("Next number in the sequence:", next_num)
		print("Diference to that number:   ", (next_num - maxnum))
		print("\n\n")
		return;
	else:
		print('')
		return;


def file_saver(n) :
	name = str(input('Name of the file: '));
	name = name.replace(" ","") #Remove whitespaces to avoid issues
	name = name + '.txt';
	file = open(name,"w");
	conc = "Number of iterations: " + n + '\n';
	file.write(conc)
	num = 1;
	next_num = 1;
	n = int(n); #No need to check, we already know it's an int
	for x in range(0,n):
		str_num = str(num) + '\n';
		file.write(str_num)
		temp = next_num;
		next_num = next_num + num;
		num = temp;
	file.close()
	return name;



os.system('cls')
print(' __________________________')
print('|                          |')
print('|** Fibonacci calculator **|')
print('|__________________________|\n\n')
repeat = 1;
while (repeat==True) :
	print('1 - Calculate n number of times')
	print('2 - Calculate up to a certain number')
	print('T - Terminate')
	choice = str(input('==> '));
	choice = choice.upper();
	if (choice=='1') :
		n = str(input('Number of times: '));
		save_file = ntimes(n);
		if (save_file==True):
			name = file_saver(n);
			os.system('cls')
			print('\nFile saved as:', name, '\n\n')
	elif (choice=='2'):
		maxnum = str(input('Calculate to the number: '))
		upton(maxnum);
	elif (choice=='T'):
		print('\nGoodbye\n')
		repeat = 0;
	else:
		print('\nInvalid option\n')