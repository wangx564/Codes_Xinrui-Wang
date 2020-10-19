"""Starter for CSC108 Assignment 2"""

from typing import List, TextIO

ENCRYPT = 'e'
DECRYPT = 'd'

# Write your functions here:
def clean_message(s: str) -> str:
    """Return a copy of the message that includes only its alphabetic \
    characters, where each of those characters has been converted to uppercase.
    
    >>>clean_message('abcdE f@g')
    'ABCDEFG'
    >>>clean_message('122AAb')
    'AAB'
    """
    clean_s = ''
    for i in s:
        if i.isalpha():
            clean_s = clean_s + i
    return clean_s.upper()

def encrypt_letter(e_letter: str, key_value: int) -> str:
    """Return the result of applying the key_value to the e_letter to encrypt\
    e_letter.
    
    Precondition: key_value <= 26
    
    >>>encrypt_letter('J', 5)
    'O'
    >>>encrypt_letter('H', 25)
    'G'
    """
    # Translate to a number in the range 0-25.  
    # 'A' translates to 0, 'B' to 1, and so on.
    ord_diff = ord(e_letter) - ord('A')

    # Apply the right shift; we use % to handle the end of the alphabet.
    # The result is still in the range 0-25.
    new_char_ord = (ord_diff + key_value) % 26

    # Convert back to a letter.
    return chr(new_char_ord + ord('A'))

def decrypt_letter(d_letter: str, key_value: int) -> str:
    """Return the result of applying the key_value to the d_letter to decrypt\
    the d_letter.
    
    Precondition: key_value <= 26
    
    >>>decrypt_letter('K', 8)
    'C'
    >>>decrypt_letter('E', 4)
    'A'
    """
    # Translate to a number.
    ord_diff = ord(d_letter) - ord('A')
    
    # Apply the left shift.
    new_char_ord = (ord_diff - key_value) % 26
    
    # Convert back to a letter.
    return chr(new_char_ord + ord('A'))
    
def swap_cards(card_deck: List[int], card_index: int) -> None:
    """Swap the card at the card_index with the card that follows it.\
    Treat the card_deck as circular: if the card at the card_index is on the \
    bottom of the card_deck, swap that card with the top card.
    
    Precondition: No repeated values in card_deck, values <= 28 and \
    card_index < len(card_deck)
    
    >>>card_deck = [5, 2, 1, 4, 3]
    >>>swap_cards(card_deck, 2)
    >>>card_deck
    [5, 2, 4, 1, 3]
    
    >>>card_deck = [9, 1, 7, 6, 8, 3, 4, 5, 2]
    >>>swap_cards(card_deck, 8)
    >>>card_deck
    [2, 1, 7, 6, 8, 3, 4, 5, 9]
    """
    if card_index < len(card_deck) - 1:
        card_at_i = card_deck[card_index] 
        card_deck[card_index] = card_deck[card_index + 1]
        card_deck[card_index + 1] = card_at_i
    
    elif card_index == len(card_deck) - 1:
        card_at_i = card_deck[0]
        card_deck[0] = card_deck[-1]
        card_deck[-1] = card_at_i

#Find the Big Joker first.       

def get_big_joker_value(card_deck: List[int]) -> int:
    """Return the value of the big joker (value of the highest card) for the \
    given card_deck.
    
    Precondition: len(card_deck) >= 3
    
    >>>get_big_joker_value([3, 1, 2, 4])
    4
    >>>get_big_joker_value([2, 4, 1, 3, 5, 6, 7])
    7
    """
    big_j = 0
    for value in card_deck:
        if value > big_j:
            big_j = value
    return big_j

#Use Big Joker to find Small Joker.

def get_small_joker_value(card_deck: List[int]) -> int:
    """Return the value of the small joker (value of the second highest card) \
    for the given card_deck.
    
    Precondition: len(card_deck) >= 3
    
    >>>get_small_joker_value([])
    9
    >>>get_small_joker_value([15, 1, 10, 3, 5, 14, 12, 2, 4, 8, 6, 11, 9, 7, 13])
    14
    """
    small_j = 0
    for number in card_deck:
        if number > small_j and number != get_big_joker_value(card_deck):
            small_j = number
    return small_j        

def move_small_joker(card_deck: List[int]) -> None:
    """Swap the small joker with the card that follows it in the card_deck.\
    Treat the card_deck as circular. This is Step 1 of the algorithm.
    
    >>>card_deck = [3, 1, 2, 4, 5]
    >>>move_small_joker(card_deck)
    >>>card_deck
    [3, 1, 2, 5, 4]
    
    >>>card_deck = [3, 4, 5, 2, 9, 1, 6, 7, 8]
    >>>move_small_joker(card_deck)
    >>>card_deck
    [8, 4, 5, 2, 9, 1, 6, 7, 3]
    """
    swap_cards(card_deck, card_deck.index(get_small_joker_value(card_deck)))
    
def move_big_joker(card_deck: List[int]) -> None:
    """Move the big joker two cards down the card_deck. Treat the card_deckdeck\
    as circular.This is Step 2 of the algorithm.
    
    >>>card_deck = [6, 3, 1, 2, 4, 5]
    >>>move_big_joker(card_deck)
    >>>card_deck
    [3, 1, 6, 2, 4, 5]
    
    >>>card_deck = [4, 1, 2, 5, 3, 6, 7]
    >>>move_big_joker(card_deck)
    >>>card_deck
    [1, 7, 2, 5, 3, 6, 4]
    """
    swap_cards(card_deck, card_deck.index(get_big_joker_value(card_deck)))
    swap_cards(card_deck, card_deck.index(get_big_joker_value(card_deck)))
    
def triple_cut(card_deck: List[int]) -> None:
    """Swap the stack of cards above the first joker with the stack of cards\
    below the second joker where the joker closest to the top of the card_deck\
    is the first joker, and the one closest to the bottom is the second joker.\
    This is Step 3 of the algorithm.
    
    >>>card_deck = [2, 6, 3, 5, 1, 7, 4]
    >>>triple_cut(card_deck)
    >>>card_deck
    [4, 6, 3, 5, 1, 7, 2]
      
    >>>card_deck = [2, 6, 5, 3, 4, 1]
    >>>triple_cut(card_deck)
    >>>card_deck
    [3, 4, 1, 6, 5, 2]
    
    >>>card_deck = [2, 3, 4, 1, 5]
    >>>triple_cut(card_deck)
    >>>card_deck
    [4,1,5,2,3]
   
    >>>card_deck = [3, 1, 2]
    >>>triple_cut(card_deck)
    >>>card_deck
    [3, 1, 2]
    """
    big_index = card_deck.index(get_big_joker_value(card_deck))
    small_index = card_deck.index(get_small_joker_value(card_deck))
    
    if  big_index > small_index:
        first_stack = card_deck[:small_index]
        card_deck[:small_index] = card_deck[big_index + 1:]
        card_deck[card_deck.index(get_big_joker_value(card_deck)) + 1:] = \
            first_stack
    else: 
        # big_index < small_index
        first_stack_2 = card_deck[:big_index]
        card_deck[:big_index] = card_deck[small_index + 1:]
        card_deck[card_deck.index(get_small_joker_value(card_deck)) + 1:] = \
            first_stack_2
        
def insert_top_to_bottom(card_deck: List[int]) -> None:
    """Examine the value of the bottom card of the card_deck; move that many \
    cards from the top of the card_deck to the bottom, inserting them just \
    above the bottom card. If the bottom card is the big joker, use the \
    value of the small joker as the number of cards.This is Step 4 of the \
    algorithm.
    
    >>>card_deck = [3, 1, 2, 5, 7, 6, 4]
    >>>insert_top_to_bottom(card_deck)
    >>>card_deck
    [7, 6, 3, 1, 2, 5, 4]
    
    >>>card_deck = [1, 5, 2, 3, 4, 6]
    >>>insert_top_to_bottom(card_deck)
    >>>card_deck
    [1, 5, 2, 3, 4, 6]
    """
    bottom_value = card_deck[-1]
    
    if bottom_value != get_big_joker_value(card_deck):
        insert_string = card_deck[:bottom_value]
        length_of_second_s = len(card_deck) - len(insert_string) - 1
        card_deck[:bottom_value] = card_deck[bottom_value:-1]
        card_deck[length_of_second_s:-1] = insert_string
        
def get_card_at_top_index(card_deck: List[int]) -> int:
    """Return the card in the card_deck at the index of using the value of the \
    top card. If the top card is the big joker, use the value of the small \
    joker as the index.This is Step 5 of the algorithm.
    
    >>>get_card_at_top_index([4, 2, 6, 1, 5, 3])
    5
    >>>get_card_at_top_index([4, 1, 3, 2])
    2
    """
    
    if card_deck[0] != get_big_joker_value(card_deck):
        return card_deck[card_deck[0]]
    else:
        return card_deck[get_small_joker_value(card_deck)]

#New function to help me with the following.
def get_new_card_deck(card_deck: List[int]) -> List[int]:
    """Return a new deck of card after the swaps and cuts are applied to the \
    old card_deck.
    
    >>>get_new_card_deck([1, 4, 7, 10, 13, 16, 19, 22, 25, 28, 3, 6, 9,\
    12, 15, 18, 21, 24, 27, 2, 5, 8, 11, 14, 17, 20, 23, 26])
    [23, 26, 28, 9, 12, 15, 18, 21, 24, 2, 27, 1, \
    4, 7, 10, 13, 16, 19, 22, 25, 3, 5, 8, 11, 14, 17, 20, 6]
    """
    move_small_joker(card_deck)
    move_big_joker(card_deck)

    triple_cut(card_deck)
    insert_top_to_bottom(card_deck)
    
    new_card_deck = card_deck
    return new_card_deck

#Another new function for to help me with the following.
def go_through_five_steps(card_deck: List[int]) -> int:
    """Return the valid keystream value after going through all five steps of \
    the algorithm.
    
    >>>go_through_five_steps([1, 4, 7, 10, 13, 16, 19, 22, 25, 28, 3, 6, 9,\
    12, 15, 18, 21, 24, 27, 2, 5, 8, 11, 14, 17, 20, 23, 26])
    11
    
    >>>go_through_five_steps([23, 26, 28, 9, 12, 15, 18, 21, 24, 2, 27, 1, \
    4, 7, 10, 13, 16, 19, 22, 25, 3, 5, 8, 11, 14, 17, 20, 6])
    9
    """
    move_small_joker(card_deck)
    move_big_joker(card_deck)

    triple_cut(card_deck)
    insert_top_to_bottom(card_deck)    
    keys_value = get_card_at_top_index(card_deck)
    
    return keys_value
#New function for helping me with the following.
def get_next_keystream_value(card_deck: List[int]) -> int:
    """Return the valid keystream value after repeating all five steps of the \
    algorithm.If the value of joker is recived, then repeat the 5 steps again.
    
    >>>get_next_keystream_value([1, 2, 3, 4])
    2
    """
    next_keys_value = go_through_five_steps(card_deck)
    new_card_deck = get_new_card_deck(card_deck)
    
    while next_keys_value == get_big_joker_value(card_deck) or \
        next_keys_value == get_small_joker_value(card_deck):
        
        next_keys_value = go_through_five_steps(new_card_deck)
        new_card_deck = get_new_card_deck(new_card_deck)
    
    return next_keys_value
        
def process_messages(card_deck: List[int], msg: List[str], d_or_e: str) -> \
    List[str]:
    """Return a list of encrypted msg if d_or_e is ENCRYPT or decrypted \
    msg if d_or_e is DECRYPT by using the card_deck.The messages are returned \
    in the same order as they are given.
    
    Precondition: d_or_e == ENCRYPT or DECRYPT
    
    >>>process_messages([2, 1, 6, 4, 5, 3], ['This assignmnet is difficult.'], \
    ENCRYPT)
    ['XIMWDVUJHRNRIUJTHJJJLFWMU']
    
    >>>process_messages([3, 7, 1, 4, 2, 6, 5], ['QJWWBRWBMSU'], DECRYPT)
    ['MISSYOUALOT']
    """ 
    # clean_m is str & clean_message() returns str
    clean_m = clean_message(msg[0])
    ciphertext = ''
    plaintext = ''
    if d_or_e == ENCRYPT:
        for i in range(len(clean_m)):
            
            key = get_next_keystream_value(card_deck) # key is int
            encrypted_l = encrypt_letter(clean_m[i], key)
            ciphertext = ciphertext + encrypted_l
        return [ciphertext]
    else:
        for i_2 in range(len(clean_m)):
            
            key_2 = get_next_keystream_value(card_deck)
            decrypted_l = decrypt_letter(clean_m[i_2], key_2)
            plaintext = plaintext + decrypted_l
        return [plaintext]
    
def read_messages(file: TextIO) -> List[str]:
    """Return the contents of the file with no newline as a list of messages, \
    in the order in which they appear in the file. 
    """
    lines = file.readlines()
    i = 0
    new_file = []
    for line in lines:
        if i < len(lines):
            line = lines[i]       
            clean_line = line.strip('\n')
            new_file.append(clean_line)
        i = i + 1
    return new_file

def is_valid_deck(card_deck: List[int]) -> bool:
    """Return whether the card_deck is valid.It is valid when it contains \
    every integer from 1 up to the number of cards in the deck. 
    
    Precondition: get_small_joker_value(card_deck) == 1
    
    >>>is_valid_deck([1,2,3,4,5])
    True
    
    >>>is_valid_deck([2, 3, 6, 5, 1, 4])
    True
    
    >>>is_valid_deck([22, 19, 3, 16, 20])
    False
    """
    card_deck.sort()
    answer = True
    for i in range(len(card_deck)):
        if i < len(card_deck) - 1 and card_deck[i + 1] != card_deck[i] + 1:
            answer = False
    return answer

def read_deck(file: TextIO) -> List[int]:
    """Return the numbers that are in the file, in the order in which they \
    appear in the file.
    """
    lines = file.readlines()
    num_list = []
    i = 0
    for index in range(len(lines)):
        clean_line = lines[index].strip('\n')
        
        while i < len(clean_line) - 1:
            white_space_i = clean_line.find(' ', i)
            
            if white_space_i >= 0:
                num_list.append(int(clean_line[i:white_space_i]))
                i = white_space_i + 1
        
    return num_list




if __name__ == '__main__':
    
    """Optional: uncomment the lines import doctest and doctest.testmod() to 
    have your docstring examples run when you run cipher_functions.py
    NOTE: your docstrings MUST be properly formatted for this to work!
    """
    
    #import doctest
    #doctest.testmod()     