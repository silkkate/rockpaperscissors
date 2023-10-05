
def main():

    def draw():
        if computer_choice == choice:
                print("It's a draw! Try again.")
                return True
        else:
            return False
    
    def win():
        if computer_choice == "rock" and choice == "paper":
            print("Paper covers rock. You win!")
            return True
        elif computer_choice == "paper" and  choice == "scissors":
            print("Scissors cut paper. You win!")
            return True
        elif computer_choice == "scissors" and choice == "rock":
            print("Rock crushes scissors. You win!")
            return True
        else:
            return False

    def lose():
        if computer_choice == "rock" and choice == "scissors":
            print("Rock crushes scissors. Computer wins!")
            return True
        elif computer_choice == "paper" and choice == "rock":
            print("Paper covers rock. Computer wins!")
            return True
        elif computer_choice == "scissors" and choice == "paper":
            print("Scissors cut paper. Computer wins!")
            return True
        else:
            return False
        
    def end_game():
        while True:
            try:
                answer = input("Continue game? (Yes/No): ").casefold()
                if answer == "yes":
                    return False
                elif answer == "no":
                    return True
                else:
                    continue
            except NameError or ValueError:
                continue
            
    import random
    import sys

    score = 0

    while True:
        try:
            options = ["rock", "paper", "scissors"]
            choice = input("Rock, paper, scissors, shoot! ").casefold()
            if choice not in options:
                continue
            else:
                computer_choice = random.choice(options)
                if draw():
                    continue
                elif win():
                    score += 1
                    if end_game():
                        print(f"Thanks for playing! Final score: {score}")
                        sys.exit()
                elif lose():
                    if end_game():
                        print(f"Thanks for playing! Final score: {score}")
                        sys.exit()
        except NameError or ValueError:
            continue
main()


