def main():
	dict = {"1": '1', "2" : '2', "3" : '3',
	"4" : '4', "5" : '5', "6" : '6',
	"7" : '7', "8" : '8', "9" : '9'}

	while True:
		player_turn(dict, 'X') #this makes the player 'X' which is defined at line 19
		player_turn(dict, 'O')#this makes the player 'O' which is defined at line 19
	return

def board_print(dict):
	print(dict["1"] +' | ' + dict["2"] +' | ' + dict["3"]) #has the brackets and the value of one in the dictionary which is '1|2|3'
	print("-" * 10)# prints - ten times
	print(dict["4"] +' | ' + dict["5"] +' | ' + dict["6"]) #has the brackets and the value of one in the dictionary which is '4|5|6'
	print("-" * 10)
	print(dict["7"] +' | ' + dict["8"] +' | ' + dict["9"]) #has the brackets and the value of one in the dictionary which is '7|8|9'
	print() #prints an empty space
	return

def player_turn(dict, player):
	board_print(dict) #calling out the board print function
	var = input("What position would you like to place it at?")
	while True:
		try:
			if int(var) in range(1, 10) and len(var) == 1 and var != 0: #making the input of var is in the range of 1-9 and is just one number
				if dict[var] == 'X' or dict[var] == 'O': #if a spot already = X or O it will ask you for another place
					var = input('position taken please try again :( ')
				else:
					dict[var] = player #replaces the number with x
					break #breaks the while loop
		except:
			var = input('bad charcter in this one')#this will prompt you if its any other input



	return

main()
