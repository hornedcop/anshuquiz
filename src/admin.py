import pickle


def _input_admin():
    # GETS INPUT FOR ADMIN DETAILS
    print("Looks like no admin user exists, create one now.")
    while True:
        admin_name = input("Enter admin username: ")
        if admin_name.isalpha():
            break
        else:
            print("Username can only contain alphabets, let's try again.")

    while True:
        admin_pass = input("Enter password: ")
        if len(admin_pass) > 5:
            break
        else:
            print("Too weak password, let's try again.")

    return [admin_name, admin_pass]


def _create_admin():
    # CREATES A NEW ADMIN USER
    admin_details_file = open("admin.dat", "wb")
    admin_data = _input_admin()
    pickle.dump(admin_data, admin_details_file)
    admin_details_file.close()


def get_admin():
    try:
        admin_details_file = open("admin.dat", "rb")
        admin_data = pickle.load(admin_details_file)
        admin_details_file.close()
        return admin_data
    except FileNotFoundError:
        _create_admin()
        return get_admin()


def authenticate_admin():
    admin_data = get_admin()
    unauthenticated_data = [
        input("Enter admin username: "),
        input("Enter admin pass: ")
    ]
    return admin_data == unauthenticated_data
