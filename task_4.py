def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError:
            return "Give me name and phone please."
        except KeyError:
            return "Enter the argument for the command"
        except IndexError:
            return "Enter the argument for the command"

    return inner


def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args


@input_error
def add_contact(args, contacts):
    if len(args) != 2:
        raise ValueError("Please provide name and phone number.")
    name, phone = args
    contacts[name] = phone
    return "Contact added."


@input_error
def change_contact(args, contacts):
    if len(args) != 2:
        raise ValueError("Please provide name and phone number.")
    name, phone = args
    if name not in contacts:
        raise ValueError("Contact not found.")
    contacts[name] = phone
    return 'Contact updated successfully'


@input_error
def show_contact(args, contacts):
    if len(args) != 1:
        raise ValueError("Please provide the name of the contact.")
    name = args[0]
    return contacts.get(name, "Contact not found")


@input_error
def show_all(contacts):
    if not contacts:
        return "The contact list is empty."
    return "\n".join(f"{name}: {phone}" for name, phone in contacts.items())


def main():
    contacts = {}
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("Good bye!")
            break

        elif command == "hello":
            print("How can I help you?")

        elif command == "add":
            print(add_contact(args, contacts))

        elif command == "change":
            print(change_contact(args, contacts))

        elif command == "show":
            print(show_contact(args, contacts))

        elif command == "all":
            print(show_all(contacts))

        else:
            print("Unknown command.")


if __name__ == "__main__":
    main()
