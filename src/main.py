from quiz import (
    add_quiz,
    modify_quiz,
    delete_quiz,
    play_quiz
)


def menu():
    while True:
        print(
            "\n",
            "+--------------------+",
            "|   Welcome to KBC?  |",
            "|   1. Add quiz      |",
            "|   2. Modify quiz   |",
            "|   3. Delete quiz   |",
            "|   4. Play Quiz     |",
            "+--------------------+",
            sep="\n"
        )
        choice = input("Enter your choice: ")

        if choice == "1":
            add_quiz()
        elif choice == "2":
            modify_quiz()
        elif choice == "3":
            delete_quiz()
        elif choice == "4":
            play_quiz()
        elif choice == "5":
            print("Thanks for playing KBC! GoodBye!")
            break
        else:
            print("Invalid choice, try again.")


menu()
