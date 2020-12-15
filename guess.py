import random 

def generate_hint(number_generated, number_guessed):
	options = ['multiples', 'differences']
	hint_type = random.choice(options)
	if hint_type == 'multiples':
		multiple_list = [(number_generated * i) for i in range(2, 10)]
		print(str(random.choice(multiple_list)) + " is a multiple!")

	else:
		diff = abs(number_generated - number_guessed)
		print("You are " + str(diff) + " numbers away from the right number")

def guess_number(number_generated, count):
	score = 0
	msg = "Guess number " + str(count) + ":"
	number_guessed = int(raw_input(msg))

	if number_guessed == number_generated:
		print("BINGO! YOU GOT IT ON YOUR FIRST TRY")
		print("+10")
		score += 10

	while number_guessed != number_generated:
		generate_hint(number_generated, number_guessed)
		score -= 2
		print("OOPS, -2")
		number_guessed = int(raw_input("Try again:"))
		if number_guessed==number_generated:
			print("RIGHT!")

	return score

def start_play(min_range, max_range):
	c = 1
	avoid = []
	overall_score = 0
	while c<=5:
		number = random.randrange(min_range, max_range)
		while number in avoid:
			number = random.randrange(min_range, max_range)
		avoid.append(number)
		overall_score += guess_number(number, c)
		c +=1

	print("YOUR OVERALL SCORE: " + str(overall_score))
	dec = (raw_input("If you want to stop playing, press N. Else, press any key to play again."))
	if dec == 'Y' or dec == 'y':
		return True
	return False

def main():
	play_again = True
	min_range = 1
	max_range = 10
	print("WELCOME TO THE GAME OF NUMBER GUESSING")
	print("If you guess the number correct on your first try, you get +10")
	print("Everytime you guess wrong, 2 points will be deducted from overall score.")
	print("But do not worry, we will give you a HINT!")
	while play_again:
		print("By default, range of the number is 1 to 10")
		dec = (raw_input("If you want to change the range, press Y. Else, press any key to continue."))
		if dec == 'Y' or dec == 'y':
			min_range = input("Minimum:")
			max_range = input("Maximum:")
			print("Let's start!")
		else:
			print("Let's start!")

		play_again = start_play(min_range, max_range)
	print("BYE SEE YOU AGAIN")

if __name__ == '__main__':
	main()