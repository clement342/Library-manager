import json
import base64

FILE_NAME = "passwords.json"


# LOAD DATA


def load_data():
    try:
        with open(FILE_NAME, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []


# SAVE DATA
def save_data(data):
    with open(FILE_NAME, "w") as file:
        json.dump(data, file, indent=4)


# ADD PASSWORD
def add_password():
    website = input("Website: ")
    username = input("Username: ")
    password = input("Password: ")

    # simple encoding (not real encryption)
    encoded_password = base64.b64encode(password.encode()).decode()

    data = load_data()

    new_entry = {"website": website, "username": username, "password": encoded_password}

    data.append(new_entry)
    save_data(data)

    print("✅ Password saved successfully!")


# VIEW PASSWORDS
def view_passwords():
    data = load_data()

    if len(data) == 0:
        print("No passwords saved yet.")
        return

    for item in data:
        decoded_password = base64.b64decode(item["password"]).decode()

        print("\n----------------------")
        print("Website :", item["website"])
        print("Username:", item["username"])
        print("Password:", decoded_password)


# SEARCH PASSWORD
def search_password():
    website = input("Enter website to search: ")
    data = load_data()

    for item in data:
        if item["website"].lower() == website.lower():
            decoded_password = base64.b64decode(item["password"]).decode()

            print("\n🔍 FOUND")
            print("Website :", item["website"])
            print("Username:", item["username"])
            print("Password:", decoded_password)
            return

    print("❌ No password found.")


# DELETE PASSWORD
def delete_password():
    website = input("Enter website to delete: ")
    data = load_data()

    new_data = []
    found = False

    for item in data:
        if item["website"].lower() != website.lower():
            new_data.append(item)
        else:
            found = True

    if found:
        save_data(new_data)
        print("🗑 Password deleted successfully.")
    else:
        print("❌ Website not found.")


# UPDATE PASSWORD
def update_password():
    website = input("Enter website to update: ")
    data = load_data()

    for item in data:
        if item["website"].lower() == website.lower():
            print("Leave blank if you don't want to change")

            new_username = input("New Username: ")
            new_password = input("New Password: ")

            if new_username:
                item["username"] = new_username

            if new_password:
                item["password"] = base64.b64encode(new_password.encode()).decode()

            save_data(data)
            print("✏ Password updated successfully.")
            return

    print("❌ Website not found.")


# MAIN MENU
def main():
    while True:
        print("\n===== PASSWORD MANAGER =====")
        print("1. Add Password")
        print("2. View Passwords")
        print("3. Search Password")
        print("4. Delete Password")
        print("5. Update Password")
        print("6. Exit")

        choice = input("Choose option: ")

        if choice == "1":
            add_password()

        elif choice == "2":
            view_passwords()

        elif choice == "3":
            search_password()

        elif choice == "4":
            delete_password()

        elif choice == "5":
            update_password()

        elif choice == "6":
            print("Goodbye 👋")
            break

        else:
            print("Invalid choice")


# RUN PROGRAM
main()
