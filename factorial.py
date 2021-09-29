#!/usr/bin/env python3

# Created by: Mikayla Barthelette
# Created on: Sept 2021
# This program will show the factorial of a positive integer


def main():
    # this function calculates the factorial
    loop_counter = 1
    the_product = 1

    # input
    user_input = input("Enter a positive integer: ")

    # process & output
    try:
        positive_integer = int(user_input)
        while loop_counter <= positive_integer:
            the_product = the_product * loop_counter
            loop_counter = loop_counter + 1
        print("{0}! = {1}.".format(positive_integer, the_product))
    except Exception:
        print("{0} is not a positive number.".format(user_input))
    finally:
        print("\nDone.")


if __name__ == "__main__":
    main()
