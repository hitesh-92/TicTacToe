# Picks
P = [' ',' ',' ',' ',' ',' ',' ',' ',' ']
# Picks Reset
# Preset = [' ',' ',' ',' ',' ',' ',' ',' ',' ']

def gridReset():
	for i in range(len(P)):
		P[i] = ' '

# Turn counter (max turns = 9. if 9 tiebreak)
count = [0]

# Turn counter
def add():
	count[0] += 1

# Current Grid showing picks
def display_board():
    print('{n7}|{n8}|{n9}\n------\n{n4}|{n5}|{n6}\n------\n{n1}|{n2}|{n3}'.format(n1=P[0],n2=P[1],n3=P[2],n4=P[3],n5=P[4],n6=P[5],n7=P[6],n8=P[7],n9=P[8]))
    #print(show)


def runTicTacToe():
	restart = True

	while restart == True:
		begin = start()

		if begin == False:
			restart = False
			break

		# P = Preset
		gridReset()
		count[0] = 0


#Start the game!
def start():
    p1=''
    p2=''


    print('\n Playing TicTacToe!\nPlease use the num pad grid system as guide\n')
    display_board()

    playersPicked = False

    while playersPicked == False:
    	initial = input('\nPick character: X or O:  ')

    	p1 = initial.upper()

    	if p1 == 'X':
    		p2 = 'O'
    		playersPicked = True
    	if p1 == 'O':
    		p2 = 'X'
    		playersPicked = True

    print(f'\nplayer 1 is {p1}   |  player 2 is {p2}\n')

    result = player_turns(p1,p2)

    if result == True:
    	gameTie()
    else:
    	showWinner(result)

    if_replay = play_again()

    if if_replay == True:
    	return True
    else:
    	return False



#alternate between players to pick X or O until tie or win
#returns [1] or [2] or True. True = tie
def player_turns(p1,p2):
	play = True
	switch_turn = True
	winner = []
	tie = False

	while play == True:

		while switch_turn == True:
			player_turn = pick(p1)
			res = pick_complete(player_turn)
			#print(f"\nplayerturn: {player_turn} \nres: {res}")

			if res != True:
				print('ERROR! pick_complete FALSE player 1')# chnage this to error restart

			match = check_for_match()
			if match == True:
				ifwinner = haswon(1)
				winner.append(1)
				play = False
				break
			switch_turn = False

		ifTie = tiebreak()
		if ifTie == True:
			play = False
			tie = True
			display_board()
			break

		while switch_turn == False:
			player_turn = pick(p2)
			res = pick_complete(player_turn)

			if res != True:
				print('ERROR! pick_complete FALSE player 2')

			if match == True:
				haswon(2)
				winner.append(2)
				play = False
				break
			switch_turn = True

	#returns winner number
	if play == False:
		print('\nTHE GAME HAS BEEN PLAYED!\n')
		return winner

	#if tie break
	if tie == True:
		return True


#player picks position on grid. if successful return true
def pick(p):
	completed = False

	while completed == False:
		picked = input(p + ' | pick number 1-9:  ')
		pick = int(picked)
		print(f"\n\nPICK: {pick}\n\n")

		if pick > 10:
			print('Pick number between 1-9:  ')
			break

		t = pick - 1

		if P[t] == ' ':
			P[t] = p
			completed = True

	if completed == True:
		return True


#add to count, display_board() and switch if pick made
def pick_complete(player_turn):
	if player_turn == True:
		add()
		display_board()
		return True
	return False


def check_for_match():
## MAKE SURE THIS WORKS - just copied and pasted in
#THEN CHECK FOR TIE
#THEN sort out if there was a winner
    win_combo = [ [6,3,0], [7,4,1], [8,5,3], [8,4,0], [6,7,8], [3,4,5], [0,1,2], [6,4,2] ]

    Xwin = ['X', 'X', 'X']
    Owin = ['O','O','O']

    winner = False

    for i in range(len(win_combo)):

        check = []

        for y in win_combo[i]:
            if P[y] == 'X' or P[y] == 'O':
                check.append(P[y])
                if check == Xwin or check == Owin:
                    winner = True

    return winner == True


#if a player has 3 in a row
def haswon(num):
	print(f"***  Player {num} has WON!  ***")
	return True


# check all moves amde
def tiebreak():
	if count[0] == 9:
		return True


#print Game has finished in tie
def gameTie():
	print("\n***\nTIS A TIE!\n***\n")


#print winning statement
def showWinner(res):
	player = ''
	if res[0] == 1:
		player = 1
	else:
		player = 2
	print(f"\n*****\nPLayer {player} has WON!!!\n***\n")


# ask if user wants to restart game. return true or false
def play_again():
	toPlayy = input("\nThanks for playing. Would you like to play agin? (Y/N)")
	should_play = toPlayy.upper()

	if should_play == 'Y':
		return True
	else:
		return False



runTicTacToe()
