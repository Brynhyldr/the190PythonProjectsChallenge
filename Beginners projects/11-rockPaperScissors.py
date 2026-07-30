import random as rd


while True:
    try:
        ai = rd.choice(["Rock", "Paper", "Scissors"])
        choice = input("Let's play Rock Paper Scissors! Choose a move: ")
        if choice == "Rock":
            match ai:
                case "Rock":
                    print("I played Rock, it's a draw, let's play again!")
                case "Paper":
                    print("I played Paper, you lost, try again!")
                case "Scissors":
                    print("I played Scissors, you won, well played!")
                    break
        elif choice == "Paper":
            match ai:
                case "Paper":
                    print("I played Paper, it's a draw, let's play again!")
                case "Scissors":
                    print("I played Scissors, you lost, try again!")
                case "Rock":
                    print("I played Rock, you won, well played!")
        elif choice == "Scissors":
                match ai:
                    case "Scissors":
                        print("I played Scissors, it's a draw, let's play again!")
                    case "Rock":
                        print("I played Rock, you lost, try again!")
                    case "Paper":
                        print("I played Paper, you won, well played!")
        else:
            print("Sorry, your move is incorrect, try again")
    except:
        print("Sorry, your move is incorrect, try again")