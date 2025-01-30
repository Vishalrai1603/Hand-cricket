import random

def hand_cricket():
    print("Welcome to Hand Cricket!")
    print("Rules: Choose numbers between 1 to 6. If your number matches the computer's, you're OUT!")

    while True:  # Main loop for replaying the game
        # Toss
        print("\n--- Toss Time ---")
        print("Welcome to Hand Cricket, a new era of cricket for kids")
        randnum = random.randint(1, 10)
        
        while True:
            toss = input("Welcome to the toss, please choose either odd(o) or even(e):\n").lower()
            if toss not in ['odd', 'even']:
                print("Invalid input! Please choose either 'odd' or 'even'.")
            else:
                break

        while True:
            try:
                tossNum = int(input("Please choose a number between 1 to 10:\n"))
                if 1 <= tossNum <= 10:
                    break
                else:
                    print("Invalid Input, ERROR 402 :(")
            except ValueError:
                print("Invalid Input, Please Enter a valid Input")

        print(f"You chose {tossNum} and the computer chose {randnum}")
        sumToss = tossNum + randnum
        SumValue = "even" if sumToss % 2 == 0 else "odd"
        print(f"It's {SumValue}")

        if SumValue == toss:
            print("You win the toss!")
            batbowl = input("Would you like to bat or bowl? ").lower()
            while batbowl not in ["bat", "bowl"]:
                batbowl = input("Invalid choice. Would you like to bat or bowl? ").lower()
            player_batting = batbowl == "bat"
        else:
            print("Computer wins the toss!")
            batbowl = random.choice(["bat", "bowl"])
            print(f"Computer chooses to {batbowl} first.")
            player_batting = batbowl == "bowl"

        while True:
            try:
                total_wickets = int(input("Enter the number of wickets you want to play with (1-10): "))
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
                    print(f"You're OUT! Remaining wickets: {wickets - player_wickets}")
                else:
                    player_score += player_input
                    print(f"Your score: {player_score}")
                if target is not None and player_score > target:
                    print("You chased the target successfully!")
                    break
            return player_score

        def computer_turn(target=None, wickets=total_wickets):
            print("\nComputer's Batting Turn!")
            computer_score, computer_wickets = 0, 0
            while computer_wickets < wickets:
                computer_input = random.randint(1, 6)
                
                try:
                    player_input = int(input("Enter your number (1-6): "))
                    if player_input < 1 or player_input > 6:
                        print("Invalid input! Choose a number between 1 and 6.")
                        continue
                except ValueError:
                    print("Please enter a valid number.")
                    continue
                print(f"Computer chose: {computer_input}")
                if player_input == computer_input:
                    computer_wickets += 1
                    print(f"Computer is OUT! Remaining wickets: {wickets - computer_wickets}")
                else:
                    computer_score += computer_input
                    print(f"Computer's score: {computer_score}")
                if target is not None and computer_score > target:
                    print("Computer chased the target successfully!")
                    break
            return computer_score

        if player_batting:
            player_score = player_turn()
            print(f"\nYour total score: {player_score}")
            print("Now, it's the computer's turn to bat.")
            computer_score = computer_turn(target=player_score)
        else:
            computer_score = computer_turn()
            print(f"\nComputer's total score: {computer_score}")
            print("Now, it's your turn to bat.")
            player_score = player_turn(target=computer_score)

        print(f"Final Scores -> You: {player_score} | Computer: {computer_score}")
        if player_score > computer_score:
            print("Congratulations! You win!")
        elif player_score < computer_score:
            print("Computer wins!")
        else:
            print("It's a tie!")

        replay = input("\nDo you want to play again? (yes/no): ").strip().lower()
        if replay != "yes":
            print("Thanks for playing Hand Cricket! Goodbye!")
            break

hand_cricket()
