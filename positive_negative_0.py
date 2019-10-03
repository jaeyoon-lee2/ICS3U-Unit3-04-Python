#!/user/bin/env python3

# Created by: Jaeyoon
# Created on: Oct 2019
# This program determines the sign of the number


def main():
    # this function determines the sign of the number

    # input
    user_number = int(input("Enter the number (integer number): "))
    print("")

    # process
    if user_number > 0:
        # output
        print("The number is positive(+)!")
    elif user_number < 0:
        print("The number is negative(-)!")
    else:
        print("THe number is 0!")


if __name__ == "__main__":
    main()
