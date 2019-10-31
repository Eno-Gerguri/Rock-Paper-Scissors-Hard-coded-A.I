from random import randint

options = ["rock", "paper", "scissors"]  # Contains all options
user_wins = 0  # Counts the number of times the user wins
program_wins = 0  # Counts the number of times the AI wins
number_of_ties = 0
user_last_choice = ""  # Stores what the user last played for the AI
program_last_choice = ""  # Stores what the AI last played for the user
was_tie = False  # Stores if the previous game was a tie
is_first_turn = True
user_won_last = None


def make_program_choice(users_last_choice, programs_last_choice):
    """
    Makes the AI's choice and is the AI.
    :param users_last_choice: STRING
    :param programs_last_choice: STRING
    :return: STRING
    """

    if is_first_turn:
        return "paper"
        # People are likely to pick, "Rock" first due to it being: the shortest to type, portrayed as strong,
        # it is the first in the game's name

    elif was_tie:
        random_option = randint(0, 1)  # Makes the program more random and less predictable
        # If it less predictable it is more likely to win

        if random_option == 0:
            return options[randint(0, 2)]  # Returns a random option

        else:
            return programs_last_choice

    if user_won_last:
        try:
            return options[options.index(users_last_choice) + 1]
            # Returns the option that would have beat their last move
            # people who win are more likely to pick the same option

        except IndexError:
            return "rock"  # Returns the what would beat scissors (the last index in, "options")

    else:  # If AI wins
        return users_last_choice


def find_game_result(users_choice, programs_choice):
    if users_choice == programs_choice:
        return "Tie"

    try:
        if options[options.index(users_choice) + 1] == programs_choice:
            # If the program chose the option that beats the user's option
            return "AI"

        else:  # If the program chose the losing option
            return "User"

    except IndexError:  # If the user picked scissors
        if programs_choice == "rock":  # If the program beat scissors
            return "AI"

        else:
            return "User"


while 1:
    # Main loop and plays the game

    while 1:  # Inner infinite while loop to get the correct input or end the main loop and display the results
        user_choice = input("Rock, Paper, Scissors? ('end' or 'quit' to display your results)\n\n").lower().strip()\
            .replace(" ", "")  # Gets the users option and properly formats it to be used in functions

        if user_choice == "end" or user_choice == "quit":
            print("\n\nYou won " + str(user_wins) + " times!\n" +
                  "I won " + str(program_wins) + " times!\n" +
                  "We tied " + str(number_of_ties) + " times!\n")

            quit()

        elif user_choice not in options:
            print("\n\nNot Valid. Please check your spelling.\n\n")

        else:  # If they put in a proper option continue the game
            break

    print("\n")

    program_choice = make_program_choice(user_last_choice, program_last_choice)  # Gets the programs choice
    winner = find_game_result(user_choice, program_choice)  # Determines who won that game

    if winner == "User":
        print("You Win!", end=" ")

        if user_choice == "rock":
            print("Rock smashes Scissors")

        elif user_choice == "paper":
            print("Paper covers Rock")

        else:
            print("Scissors cut Paper")

        print("\n")
        user_wins += 1
        user_won_last = True
        was_tie = False

    elif winner == "AI":
        print("I Win!", end=" ")

        if program_choice == "rock":
            print("Rock smashes Scissors")

        elif program_choice == "paper":
            print("Paper covers Rock")

        else:
            print("Scissors cut Paper")

        print("\n")
        program_wins += 1
        user_won_last = False
        was_tie = False

    else:
        print("It was a tie!\n")
        number_of_ties += 1
        was_tie = True

    user_last_choice = user_choice
    program_last_choice = program_choice
    is_first_turn = False
