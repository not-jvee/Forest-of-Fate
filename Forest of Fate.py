def intro():
    print("🌲 Welcome to the Forest of Fate 🌲")
    print("You awaken in a dark forest with only a faint path ahead.")
    print("Two paths lie before you: one to the LEFT, one to the RIGHT.")
    choice = input("Which way do you go? (left/right): ").lower()

    if choice == "left":
        wolf_path()
    elif choice == "right":
        river_path()
    else:
        print("You stand still, lost in indecision... until night falls.")
        game_over()

def wolf_path():
    print("\nYou head left and hear a low growl...")
    print("A wolf appears, blocking your way!")
    choice = input("Do you FIGHT or RUN? ").lower()

    if choice == "fight":
        print("You bravely fight the wolf with a stick!")
        print("After a fierce struggle, you defeat it and find a golden key.")
        print("You continue onward and find a mysterious cabin...")
        cabin()
    elif choice == "run":
        print("You run back to where you started.")
        intro()
    else:
        print("You freeze in fear... and the wolf pounces.")
        game_over()

def river_path():
    print("\nYou follow the path to a rushing river.")
    choice = input("Do you try to SWIM across or BUILD a raft? ").lower()

    if choice == "swim":
        print("The current is too strong! You’re swept away...")
        game_over()
    elif choice == "build":
        print("You craft a crude raft and cross safely.")
        print("On the other side, you find a mysterious cabin...")
        cabin()
    else:
        print("You hesitate too long, and it starts to rain. You slip into the river.")
        game_over()

def cabin():
    print("\nThe cabin door is locked.")
    choice = input("Do you try to PICK the lock or USE the golden key? ").lower()

    if choice == "pick":
        print("The lock is too strong... You break your tool and give up.")
        game_over()
    elif choice == "use":
        print("The key fits! Inside you find a treasure chest.")
        print("Congratulations, adventurer — you’ve found the hidden fortune! 🏆")
        print("🎉 YOU WIN! 🎉")
    else:
        print("You walk away from the cabin, never knowing what was inside...")
        game_over()

def game_over():
    print("\n💀 GAME OVER 💀")
    retry = input("Would you like to play again? (yes/no): ").lower()
    if retry == "yes":
        intro()
    else:
        print("Thanks for playing!")

# Start the game
intro()
