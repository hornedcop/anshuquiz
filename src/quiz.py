import pickle


def create_question_file():
    question_file = open("questions.dat", "wb")
    question_data = {}
    pickle.dump(question_data, question_file)
    question_file.close()


def get_question_data():
    try:
        question_file = open("questions.dat", "rb")
        question_data = pickle.load(question_file)
        question_file.close()
        return question_data
    except FileNotFoundError:
        create_question_file()
        return get_question_data()


def input_question():
    pass


def add_quiz():
    question_data = get_question_data()

    while True:
        quiz_name = input("Enter new quiz name: ")
        existing_quiz_names = question_data.keys()
        if quiz_name not in existing_quiz_names:
            break
        else:
            print("This quiz already exists!")
