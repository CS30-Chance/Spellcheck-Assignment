# Spell Check Starter
# This start code creates two lists
# 1: dictionary: a list containing all the words from "dictionary.txt"
# 2: aliceWords: a list containing all the words from "AliceInWonderland.txt"

import re  # Needed for splitting text with a regular expression
import math
import time


def linearSearch(anyArray, item):
    st = time.time()
    for i in range(len(anyArray)):
        if anyArray[i] == item:
            ft = time.time() - st
            return i, ft
    else:
        ft = time.time() - st
        return -1, ft


def binarySearch(anyArray, item):
    st = time.time()
    li = 0
    ui = len(anyArray) - 1
    while ui >= li:
        mi = math.floor((li + ui) / 2)
        if item == anyArray[mi]:
            ft = time.time() - st
            return mi, ft
        elif anyArray[mi] > item:
            ui = mi - 1
        elif anyArray[mi] < item:
            li = mi + 1
    ft = time.time() - st
    return -1, ft


def main():
    # Load data files into lists
    dictionary = loadWordsFromFile("data-files/dictionary.txt")
    aliceWords = loadWordsFromFile("data-files/AliceInWonderLand.txt")

    while True:
        print('Main Menu\n'
              '1: Spell Check a Word (Linear Search)\n'
              '2: Spell Check a Word (Binary Search)\n'
              '3: Spell Check Alice In Wonderland (Linear Search)\n'
              '4: Spell Check Alice In Wonderland (Binary Search)\n'
              '5: Exit'
              )

        selection = int(input('Enter menu selection (1-5): '))
        if selection == 1:
            word = input('Please enter a word: ')
            print('Linear Search starting')
            res = linearSearch(dictionary, word.lower())
            if res[0] == -1:
                print(f'{word} is not in the dictionary. ({res[1]})Seconds')
            else:
                print(f'{word} is in the dictionary at position {res[0]}. ({res[1]})Seconds')

        elif selection == 2:
            word = input('Please enter a word: ')
            print('Binary Search starting')
            res = binarySearch(dictionary, word.lower())
            if res[0] == -1:
                print(f'{word} is not in the dictionary. ({res[1]})Seconds')
            else:
                print(f'{word} is in the dictionary at position {res[0]}. ({res[1]})Seconds')

        elif selection == 3:
            print('Linear Search starting')
            st = time.time()
            counter = 0
            for i in aliceWords:
                if linearSearch(dictionary, i)[0] == -1:
                    counter += 1
                else:
                    pass
            ft = time.time() - st
            print(f'Number of words not found in dictionary: {counter} ({ft} seconds)')

        elif selection == 4:
            print('Binary Search starting')
            st = time.time()
            counter = 0
            already_searched = []
            for i in aliceWords:
                # if i not in already_searched:
                #     already_searched.append(i)
                if binarySearch(dictionary, i)[0] == -1:
                    counter += 1
            ft = time.time() - st
            print(f'Number of words not found in dictionary: {counter} ({ft} seconds)')
        else:
            break
# end main()


def loadWordsFromFile(fileName):
    # Read file as a string
    fileref = open(fileName, "r")
    textData = fileref.read()
    fileref.close()

    # Split text by one or more whitespace characters
    return re.split('\s+', textData)


# end loadWordsFromFile()


# Call main() to begin program
main()
