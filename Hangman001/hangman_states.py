STATE1 = "    x-------x"
STATE2 = """    x-------x
    |
    |
    |
    |
    |"""
STATE3 = """    x-------x
    |       |
    |       0
    |
    |
    |"""
STATE4 = """    x-------x
    |       |
    |       0
    |       |
    |
    |"""
STATE5 = """    x-------x
    |       |
    |       0
    |      /|\\
    |
    |"""
STATE6 = """    x-------x
    |       |
    |       0
    |      /|\\
    |      /
    |"""
STATE7 = """    x-------x
    |       |
    |       0
    |      /|\\
    |      / \\
    |"""

HANGMAN_STATES = [STATE1, STATE2, STATE3, STATE4, STATE5, STATE6, STATE7]


def print_hangman_states():
    for state in HANGMAN_STATES:
        print(state)


def print_hangman_state(state: int):
    print(HANGMAN_STATES[state - 1])


eggs = 4
print(bool(eggs))

