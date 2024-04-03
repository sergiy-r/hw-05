# Module 4 Homework: Exercise 4
# This is program for a Command Line Interface bot that allows to interact with a contact list
# It allows a user to add, change, and retrieve a contact's phone number, as well as print all contacts
# Names and commands are case-insensitive.


# decorator function for error handling
def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except KeyError:
            return "KeyError"
        except ValueError:
            if func.__name__ == 'parse_input':
                print("You did not enter a command. Please enter a command.")
                return parse_input('try_again')
            if func.__name__ == 'add_contact':
                return ("This contact already exists. To view the contact number, please enter 'phone [Name]', e.g., "
                        "phone Alex")
            if func.__name__ == 'phone':
                return ("There is no such contact. To view all contacts, please enter 'all'. \nTo add a contact, "
                        "please enter 'add [Name] [Number]', e.g., add Alex 07770000001")
            if func.__name__ == 'show_all':
                return ("There are no stored contacts. To add a contact, please enter 'add [Name] [Number]', e.g., "
                        "add Alex 07770000001")
            if func.__name__ == 'change_contact':
                return "There is no such contact. To view all contacts enter 'all'."
            return "ValueError"
        except IndexError:
            if func.__name__ in ['add_contact', 'change_contact', 'phone']:
                return "Please enter the argument(s) for the command."
            return "IndexError"
        except Warning:
            if func.__name__ == 'parse_input':
                return ("Incorrect command. To view all contacts, please enter 'all'. \nTo add a contact, "
                        "please enter 'add [Name] [Number]', e.g., add Alex 07770000001")

    return inner


# parses user input
@input_error
def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    if cmd == 'other':
        raise Warning
    else:
        return cmd, *args


@input_error
# adds name and phone to a dictionary 'contacts'
def add_contact(args, contacts, debug):
    name = args[0].title()
    phone = args[1]
    if name not in contacts.keys():
        contacts[name] = phone
        debug and print(f"{name}: {phone}")  # if debug = True then print else not
        return "Contact added."
    else:
        raise ValueError


# changes a phone number for a name in contacts dictionary
@input_error
def change_contact(args, contacts, debug):
    name = args[0].title()
    debug and print(f"Old details: {name}: {contacts.get(name)}")
    phone = args[1]
    if name in contacts.keys():
        contacts.update({name: phone})
        debug and print(f"New details: {name}: {contacts.get(name)}")
        return "Contact updated."
    else:
        raise ValueError


# returns the phone number for a name from contacts dictionary
@input_error
def phone(args, contacts):
    name = args[0].title()
    if name in contacts.keys():
        return contacts[name]
    else:
        raise ValueError


# returns all names and numbers from contacts dictionary
@input_error
def show_all(contacts):
    if contacts:
        sorted_keys = sorted(contacts.keys())
        contacts_str = ''
        for key in sorted_keys: # create a string with all contacts sorted by name
            contacts_str += f"{key}: {contacts[key]}\n"
        #contacts_str = "\n".join(f"{name}: {phone}" for name, phone in contacts.items())
        return "Contacts:\n" + contacts_str
    else:
        raise ValueError


# main function for processing user input, output and logic of the CLI bot
def main():
    contacts = {}
    debug = False
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)

        if command in ["close", "exit", "bye"]:
            print("Good bye!")
            break
        elif command in ["hello", "hi"]:
            print("How can I help you?")
        elif command == "add":
            print(add_contact(args, contacts, debug))
        elif command in ["change", "update"]:
            print(change_contact(args, contacts, debug))
        elif command == "phone":
            print(phone(args, contacts))
        elif command == "all":
            print(show_all(contacts))
        elif command == "debug=true":
            debug = True
        elif command == "debug=false":
            debug = False
        elif command == 'try_again':  # go to input prompt if user didn't enter a command
            pass
        else:
            print(parse_input('other'))  # if command is not in the list, 'other' triggers a Warning in parse_input
                                         # which is in turn handled by input_error decorator.


if __name__ == "__main__":
    main()
