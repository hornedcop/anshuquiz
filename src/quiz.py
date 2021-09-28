import pickle


def db_exists():
    try:
        open("quiz.data").close()
        return True
    except FileNotFoundError:
        return False


def create_db():
    data, db = {}, open("quiz.data", "wb")
    pickle.dump(data, db)
    db.close()


def load_db():
    if db_exists():
        db = open("quiz.data", "rb")
        data = pickle.load(db)
        db.close()
        return data
    else:
        create_db()
        return {}


def update_db(data):
    if db_exists():
        db = open("quiz.data", "wb")
        pickle.dump(data, db)
        db.close()
    else:
        create_db()
        update_db(data)


def input_quiz_title(db):
    while True:
        title = input("Enter a unique title for this quiz: ")
        if title not in db.keys():
            db[title] = {}
            return title
        print("This title already exists! Try again...")


def input_question():
    question = input("Enter a unique question: ")
    answer_dict = {"options": [
        input("Enter answer option 1: "),
        input("Enter answer option 2: "),
        input("Enter answer option 3: "),
        input("Enter answer option 4: ")
    ]}
    while True:
        correct_option = input("Enter correct answer (1-4): ")
        is_valid_input = correct_option.isdigit() and int(correct_option) in [1, 2, 3, 4]
        if is_valid_input:
            answer_dict["correct_option"] = int(correct_option)
            break
        else:
            print("Invalid input! Try entering a number between 1 to 4...")

    return question, answer_dict


def add_quiz():
    db = load_db()
    q_title = input_quiz_title(db)
    while input("\nEnter questions (y/n): ").lower() == "y":
        question, answer_dict = input_question()
        db[q_title][question] = answer_dict

    update_db(db)
    print("New Quiz Added Successfully!")


def modify_quiz():
    db = load_db()

    if not db:
        print("No Quiz to modify, add a quiz first.")
        return

    titles = list(db.keys())
    for i in range(len(titles)):
        print(f"{i}: {titles[i]}")
    while True:
        choice = input("Which quiz do you want to modify?: ")
        if choice.isdigit() and int(choice) in range(len(titles)):
            title = titles[int(choice)]
            print("You chose to modify: '", title, "'")
            break
        else:
            print("Please enter a valid choice, let's try again...")

    questions = list(db[title].keys())
    for i in range(len(questions)):
        print(f"{i}: {questions[i]}")
    while True:
        choice = input("Which question do you want to modify?: ")
        if choice.isdigit() and int(choice) in range(len(questions)):
            question = questions[int(choice)]
            print("You chose to modify: '", question, "'")
            break
        else:
            print("Please enter a valid choice, let's try again...")

    del db[title][question]
    new_question, new_answer_dict = input_question()
    db[title][new_question] = new_answer_dict

    update_db(db)
    print("Modified Successfully!")


def delete_quiz():
    db = load_db()

    if not db:
        print("No Quiz to delete, add a quiz first.")
        return

    titles = list(db.keys())
    for i in range(len(titles)):
        print(f"{i}: {titles[i]}")
    while True:
        choice = input("Which quiz do you want to delete?: ")
        if choice.isdigit() and int(choice) in range(len(titles)):
            title = titles[int(choice)]
            print("You chose to delete: '", title, "'")
            break
        else:
            print("Please enter a valid choice, let's try again...")
    del db[title]
    update_db(db)
    print("Deleted Successfully!")


def play_quiz():
    db = load_db()

    if not db:
        print("No Quiz to play, add quiz first!")
        return

    score, max_score = 0, 0
    titles = list(db.keys())
    for i in range(len(titles)):
        print(f"{i}: {titles[i]}")
    while True:
        choice = input("Which quiz do you want to play?: ")
        if choice.isdigit() and int(choice) in range(len(titles)):
            title = titles[int(choice)]
            print("You chose to play: '", title, "'")
            break
        else:
            print("Please enter a valid choice, let's try again...")

    questions = db[title]
    for question in questions.keys():
        max_score += 1

        print(question)
        answer_dict = db[title][question]
        for i in range(len(answer_dict["options"])):
            print(f"{i}: {answer_dict['options'][i]}")

        while True:
            answer = input("\nEnter correct answer (1-4): ")
            is_valid_answer = answer.isdigit() and int(answer) in [1, 2, 3, 4]
            if is_valid_answer:
                answer_is_correct = answer_dict["correct_option"] == int(answer)
                if answer_is_correct:
                    score += 1
                    print("Answer is correct :)")
                else:
                    print("Answer is wrong :(")
                break
            else:
                print("Invalid input! Try entering a number between 1 to 4...")

    print(f"Quiz over you scored {score} out of {max_score}!\nThanks for playing, we'll see you again!")
