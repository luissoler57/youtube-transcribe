from utils.validators import validate_link_youtube


def main():
    print("Hello, World!")
    # Get input from the user
    user_input = input("Please enter the link to the youtube: ")
    while not validate_link_youtube(user_input):
        print("Please enter a valid youtube link!")
        user_input = input("Please enter the link to the youtube: ")


if __name__ == "__main__":
    main()
