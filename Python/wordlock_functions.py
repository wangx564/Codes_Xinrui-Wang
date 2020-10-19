"""Starter code for CSC108 Assignment 1 Winter 2018"""

# Game setting constants
SECTION_LENGTH = 3
ANSWER = 'CATDOGFOXEMU'

# Move constants
SWAP = 'S'
ROTATE = 'R'
CHECK = 'C'

# Add any additional constants here

def get_section_start(section_num: int) -> int: 
    """ Return the starting index of the section corresponding to section_num.
    
    
    Precondition : section_num <= len(ANSWER) / SECTION_LENGTH
    
    >>> get_section_start(1)
    0
    >>> get_section_start(3)
    6
    """
    starting_index = (section_num - 1) * SECTION_LENGTH
    return starting_index

def is_valid_move(move: str) -> bool: 
    """ Return whether move is valid.
    
    >>> is_valid_move('R')
    True
    >>> is_valid_move('d')
    False
    """
    move1 = 'R'
    move2 = 'S'
    move3 = 'C'
    return(move == move1) or (move == move2) or (move == move3)

def is_valid_section(section_num: int) -> bool:
    """Return whether section_num is a valid section number.
    
    >>>is_valid_section(6)
    False
    >>>is_valid_section(1)
    True
    """
    
    return section_num <= len(ANSWER) / SECTION_LENGTH

def check_section(game_state: str, section_num: int) -> bool: 
    """Return whether the game_state of the section corresponding to \
    section_num has been correctly unscrambled.
    
    Precondition : is_valid_section(section_num) == True
    
    >>>check_section('CATDOGFOXEMU', 1)
    True
    >>>check_section('CATGDOFOXEMU', 2)
    False
    """
    return game_state[get_section_start(section_num): get_section_start\
                      (section_num + 1)] == ANSWER[get_section_start\
                            (section_num): get_section_start(section_num + 1)]

def change_state(game_state: str, section_num: int, move: str) -> str: 
    """Return new game_state of the section corresponding to section_num after \
    the move is applied to game_state.
    
    Precondition : move == 'S' or move == 'R'
    
    >>>change_state('CATDOGFOXUME', 4, 'S')
    'CATDOGFOXEMU'
    >>>change_state('ATCDOGFOXUME', 1, 'R')
    'CATDOGFOXUME'
    """
    
    if move == 'S':
        new_game_state1 = game_state[: get_section_start(section_num)] +\
            game_state[get_section_start(section_num + 1) - 1] + \
            game_state[get_section_start(section_num) + 1: get_section_start\
            (section_num + 1) - 1] + game_state[get_section_start\
            (section_num)] + game_state[get_section_start(section_num + 1): ]
        return new_game_state1
       
    else:
        new_game_state2 = game_state[: get_section_start(section_num)] + \
            game_state[get_section_start(section_num + 1) - 1] + \
            game_state[get_section_start(section_num)] + game_state\
            [get_section_start(section_num) + 1: get_section_start\
            (section_num + 1) - 1] + game_state[get_section_start\
            (section_num + 1): ]        
        return new_game_state2
           
def get_move_hint(game_state: str, section_num: int) -> str: 
    """Return the string move which will unscramble the section of game_state\
    corresponding to section_num.
    
    Precondition : iff LENGTH == 3 and check_section(game_state, section_num) is False
    
    >>>get_move_hint('CATGODFOXEMU', 2)
    'S'
    >>>get_move_hint('CATDOGOXFEMU', 3)
    'R'
    """
    game_state_section = game_state[get_section_start(section_num) :\
                                    get_section_start(section_num + 1)]
    
    answer_section = ANSWER[get_section_start(section_num) : get_section_start\
                            (section_num + 1)]
    
    if game_state_section == answer_section[2] + answer_section[1] + \
       answer_section[0] or game_state_section == answer_section[0] + \
       answer_section[2] + answer_section[1]:
        return 'S'
    
    else:
        return 'R'