import random


def hand_cricket():
    print("Welcome to Hand Cricket!")
    print("Rules: Choose numbers between 1 to 6. If your number matches the computer's, you're OUT!")

    while True:  # Main loop for replaying the game
        # Toss
        print("\n--- Toss Time ---")
        SumValue = "junk"
        print("Welcome to Hand Cricket, a new era of cricket for kids")
        randnum = random.randint(1, 10)
        # TOSS
        toss = input(
            "Welcome to the toss, please choose either odd(o) or even(e):\n").lower()
        tossNum = int(input("Please choose a number between 1 to 10:\n"))
        if (tossNum > 10 or tossNum < 1):
            print("Invalid Input, ERROR 402 :(")
        else:
            print(f"You chose {tossNum} and the computer chose {randnum}")
            sumToss = tossNum + randnum
            if (sumToss % 2) == 0:
                SumValue = "e"
                print("It's even")
            else:
                SumValue = "o"
                print("It's odd")
        if SumValue == toss:
            print("You win the toss!")
        batbowl = input("Would you like to bat or bowl? ").lower()

        while batbowl not in ["bat", "bowl"]:  # Validate bat or bowl choice
            batbowl = input(
                "Invalid choice. Would you like to bat or bowl? ").lower()

        # Choose number of wickets
        while True:
            try:
                total_wickets = int(
                    input("Enter the number of wickets you want to play with (1-10): "))
                if 1 <= total_wickets <= 10:
                    break
                else:
                    print("Please choose a number between 1 and 10.")
            except ValueError:
                print("Please enter a valid number.")

        def player_turn(target=None, wickets=total_wickets):
            print("\nYour Batting Turn!")
            player_score, player_wickets = 0, 0
            while player_wickets < wickets:
                try:
                    player_input = int(input("Enter your number (1-6): "))
                    if player_input < 1 or player_input > 6:
                        print("Invalid input! Choose a number between 1 and 6.")
                        continue
                except ValueError:
                    print("Please enter a valid number.")
                    continue
                computer_input = random.randint(1, 6)
                print(f"Computer chose: {computer_input}")
                if player_input == computer_input:
                    player_wickets += 1
                    print(
                        f"You're OUT! Remaining wickets: {wickets - player_wickets}")
                else:
                    player_score += player_input
                    print(f"Your score: {player_score}")
                if target and player_score > target:
                    print("You chased the target successfully!")
                    break
            return player_score, player_wickets

        def computer_turn(target=None, wickets=total_wickets):
            print("\nComputer's Batting Turn!")
            computer_score, computer_wickets = 0, 0
            while computer_wickets < wickets:
                try:
                    player_input = int(input("Enter your number (1-6): "))
                    if player_input < 1 or player_input > 6:
                        print("Invalid input! Choose a number between 1 and 6.")
                        continue
                except ValueError:
                    print("Please enter a valid number.")
                    continue
                computer_input = random.randint(1, 6)
                print(f"Computer chose: {computer_input}")
                if player_input == computer_input:
                    computer_wickets += 1
                    print(f"Computer is OUT! Remaining wickets: {wickets - computer_wickets}")
                else:
                    computer_score += computer_input
                    print(f"Computer's score: {computer_score}")
                if target and computer_score > target:
                    print("Computer chased the target successfully!")
                    break
            return computer_score, computer_wickets

        # Game logic based on toss outcome
        if batbowl == "bat":
            player_score, _ = player_turn()
            print(f"\nYour total score: {player_score}")
            print("Now, it's the computer's turn to bat.")
            computer_score, _ = computer_turn(target=player_score)
            print(f"Computer's total score: {computer_score}")
            if computer_score < player_score:
                print("Congratulations! You win!")
            elif computer_score > player_score:
                print("Computer wins!")
            else:
                print("It's a tie!")
        else:
            computer_score, _ = computer_turn()
            print(f"\nComputer's total score: {computer_score}")
            print("Now, it's your turn to bat.")
            player_score, _ = player_turn(target=computer_score)
            print(f"Your total score: {player_score}")
            if player_score < computer_score:
                print("Computer wins!")
            elif player_score > computer_score:
                print("Congratulations! You win!")
            else:
                print("It's a tie!")

        # Play again prompt
        replay = input(
            "\nDo you want to play again? (yes/no): ").strip().lower()
        if replay != "yes":
            print("Thanks for playing Hand Cricket! Goodbye!")
            break


# Run the game
hand_cricket()
