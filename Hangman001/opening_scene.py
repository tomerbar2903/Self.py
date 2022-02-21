"""
Opening Screen - Title + Number Of Guesses Allowed
"""


HANGMAN_ASCII_ART = """  _    _                                         
 | |  | |                                        
 | |__| | __ _ _ __   __ _ _ __ ___   __ _ _ __  
 |  __  |/ _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
 | |  | | (_| | | | | (_| | | | | | | (_| | | | |
 |_|  |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                      __/ |                      
                     |___/"""
MAX_TRIES = 6
GUESS_LINE = '_'
WHITESPACE = ' '


def print_title(number_of_guesses: int):
    """
    :param number_of_guesses: number of guesses allowed for user
    :return: prints the title + number_of_guesses
    """
    print(f"{HANGMAN_ASCII_ART}\n\nNumber Of Guesses: {number_of_guesses}")


def is_valid_input(input_from_user: str):
    """
    :param input_from_user: a string that the user inputs
    :return: true if only single alpha letter
    """
    return len(input_from_user) == 1 and input_from_user.isalpha()


def get_response(input_from_user: str):
    """
    :param input_from_user: string that user inputs
    :return:
    -- if len > 1 and all_alphas -> 'E1'
    -- if len == 1 and not alpha -> 'E2'
    -- if len > 1 and not_all_alphas -> 'E3'
    -- otherwise: the input, transformed as lower case
    """
    length_of_message = len(input_from_user)
    if is_valid_input(input_from_user):
        return_val = input_from_user.lower()
    elif length_of_message == 1 and not input_from_user.isalpha():
        return_val = "E2"
    elif length_of_message > 1 and input_from_user.isalpha():
        return_val = "E1"
    else:  # all other ifs cover all the rest of the cases
        return_val = "E3"
    return return_val


def main():
    print_title(MAX_TRIES)
    guess_of_user = input("Enter Your Guess: ")
    print(get_response(guess_of_user))
    word = input("Please Enter A Word: ")
    guess_lines = (GUESS_LINE + WHITESPACE) * (len(word) - 1) + GUESS_LINE  # so that the last underscore won't have a whitespace following it
    print(guess_lines)


if __name__ == '__main__':
    main()
