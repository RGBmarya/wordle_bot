

from re import L
from weakref import WeakValueDictionary


all_words = open("valid_words.txt", "r")
word_list = all_words.read().split("\n")
all_words.close()
print("Initial word list length: " + str(len(word_list)))

agg_not_in_word_list = []
agg_in_word_incorrect_position_list = []
agg_in_word_correct_position_list = []


def remove_words_incorrect_letters(list):
    i = 0
    removed = False
    while i < len(word_list):
        removed = False
        word = word_list[i]
        for pair in list:
            char = pair[0]
            index = int(pair[1]) - 1
            # remove word that has char at specified index (char should not be in word)
            if word[index] == char:
                word_list.remove(word)
                removed = True
                break
        if not removed:
            i += 1


def remove_words_correct_letter_incorrect_position(list):
    i = 0
    removed = False
    while i < len(word_list):
        removed = False
        word = word_list[i]
        for pair in list:
            char = pair[0]
            index = int(pair[1]) - 1
            if char not in word or word[index] == char:
                word_list.remove(word)
                removed = True
                break
        if not removed:
            i += 1


def remove_words_correct_letter_correct_position(list):
    i = 0
    removed = False
    while i < len(word_list):
        removed = False
        word = word_list[i]
        for pair in list:
            char = pair[0]
            index = int(pair[1]) - 1
            if char not in word or word[index] != char:
                word_list.remove(word)
                removed = True
                break
        if not removed:
            i += 1


while len(agg_in_word_correct_position_list) < 5:
    not_in_word = input(
        "\nCharacters not in word (char,position) (separated by space): ").split(" ")
    if not_in_word and not_in_word[0] != '':
        for pair in not_in_word:
            # convert String (char, pos) to iterable list [char, pos]
            char_index = [x for x in pair if x.isdigit() or x.isalpha()]
            if char_index not in agg_not_in_word_list:
                agg_not_in_word_list.append(char_index)

    in_word_incorrect_position = input(
        "Characters in word but at incorrect position (char,position) (separated by space): ").split(" ")
    if in_word_incorrect_position and in_word_incorrect_position[0] != '':
        for pair in in_word_incorrect_position:
            char_index = [x for x in pair if x.isdigit() or x.isalpha()]
            if char_index not in agg_in_word_incorrect_position_list:
                agg_in_word_incorrect_position_list.append(char_index)

    in_word_correct_position = input(
        "Characters in word and at correct position (char,position) (separated by space): ").split(" ")
    if in_word_correct_position and in_word_correct_position[0] != '':
        for pair in in_word_correct_position:
            char_index = [x for x in pair if x.isdigit() or x.isalpha()]
            if char_index not in agg_in_word_correct_position_list:
                agg_in_word_correct_position_list.append(char_index)

    if(agg_not_in_word_list):
        remove_words_incorrect_letters(agg_not_in_word_list)
        # print("Just removed words: " + str(len(word_list)))

    if(agg_in_word_incorrect_position_list):
        remove_words_correct_letter_incorrect_position(
            agg_in_word_incorrect_position_list)
        # print("Just removed words: " + str(len(word_list)))

    if(agg_in_word_correct_position_list):
        remove_words_correct_letter_correct_position(
            agg_in_word_correct_position_list)
        # print("Just removed words: " + str(len(word_list)))

    if len(word_list) == 1:
        print("Success! The correct word is " + word_list[0])
        break
    else:
        print("\nJust removed words!")

    # Recommend next letter
    letter_counts = {}
    for word in word_list:
        for letter in word:
            # LIST OF KNOWN LETTERS + POSITION:
            if letter in letter_counts.keys():
                letter_counts[letter] += 1
            else:
                letter_counts[letter] = 1

    # print("agg_not_in_word_list" + str(agg_not_in_word_list))
    not_in_word_set = []
    for pair in agg_not_in_word_list:
        not_in_word_set.append(pair[0])

    # print("agg_in_word_incorrect_position_list: " + str(agg_in_word_incorrect_position_list))
    in_word_incorrect_position_set = []
    for pair in agg_in_word_incorrect_position_list:
        in_word_incorrect_position_set.append(pair[0])

    # print("agg_in_word_correct_position_list: " + str(agg_in_word_correct_position_list))
    in_word_correct_position_set = []
    for pair in agg_in_word_correct_position_list:
        in_word_correct_position_set.append(pair[0])

    unused_letter_counts = {}
    for k, v in letter_counts.items():
        if k not in not_in_word_set and k not in in_word_incorrect_position_set and k not in in_word_correct_position_set:
            unused_letter_counts[k] = v
        # else:
        #     print("Excluded: " + k)

    commonLetter = max(unused_letter_counts, key=unused_letter_counts.get)
    print("Remaining Words: " + str(len(word_list)))
    if(len(word_list) <= 15):
        print(word_list)
    print("Common letter: " + commonLetter)
