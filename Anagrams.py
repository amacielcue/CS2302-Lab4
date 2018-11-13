#CS2302 Lab4-B
#By: Alejandra Maciel
#Last Modified: Nov-12-2018
#Instructor: Diego Aguirre
#TA: Manoj  Pravaka  Saha
#The purpose of this lab was to practice the use of hash tables. Just as the past lab it was assigned to create a
# program that would read a file with all the valid english words, which would be use to find valid anagrams for
# specific words. The program would store the english words in a hash table.
import sys

#HASH TABLE NODE CLASS
class Node:
    def __init__(self, item, next):
        self.item = item
        self.next = next

#HASH TABLE CLASS
class HashTable:
    def __init__(self, table_size):
        self.table = [None] * table_size

    #Method to assign the hash value to a new element
    def hash(self, w):
        ascii_value = 0
        #For in in range of the length of the word add the ascii value of each character
        for i in range (len(w)):
            ascii_value += ord(w.lower()[i])

        return ascii_value % len(self.table)

    #Method to insert new elements to the hash table
    def insert(self, w):
        loc = self.hash(w)
        self.table[loc] = Node(w, self.table[loc])

    #Method to search elements on the hash table
    def search(self, w):
        loc = self.hash(w)
        temp = self.table[loc]
        while temp is not None:
            if w == temp.item:
                return True
            temp = temp.next
        return False
#Method to create the hash table with the english words
def build_hash_table(fileName):
    print("Building...")
    words = HashTable(3000)
    f = open(fileName, 'r')
    line = f.readline()
    #Whikle there are lines on the file keep inserting to the hash table
    while line:
        words.insert(line)
        line = f.readline()

    return words

#Method to get the permutations of any word
def permutations(word):
    perms=[]
    #If the length of the word is 1 then add the word to the list
    if len(word) <= 1:
        perms.append(word)
    #Else for the length of the word add to the list the permutations of a fragment of the original wprd and for all the
    #charcaters or strings in the list add the new combination to the list
    else:
        for pos in range(len(word)):
            list = permutations(word[0:pos] + word[pos+1:len(word)])

            for character in list:
                perms.append(word[pos] + character)
    #Return permutations list
    return perms

# Function that returns the number of valid anagrams from a given word
def count_anagrams(hash_table,word):
    #Get the word's permutations and store in a p variable
    p = permutations(word)
    count = 0
    #For the length of the permutations list, if a permutation is in the hash table add 1 to the counter
    for i in range(len(p)):
        if hash_table.search(p[i]):
            count += 1
    #Return counter
    return count
#Method to get the load factor of the hash table
def load_factor(hash_table):
    if hash_table is None:
        return None
    count = 0
    #For i in range of the length of table assign the current value to a temporal variable
    for i in range (len(hash_table.table)):
        temp = hash_table.table[i]
        #While the temporal value is not empty increase the counter by 1 and set temp value to the next value.
        while temp is not None:
            count += 1
            temp = temp.next
    #Return load factor
    return count / len(hash_table.table)
#Method to get number of necessary comparison to find a word on the table
def comparisons(hash_table):
    if hash_table is None:
        return None
    comp = 0
    #For in imn range of the length of the table assign the current value to a temporal variable
    for i in range(len(hash_table.table)):
        count = 0
        temp = hash_table.table[i]
        #While the temporal value is not empty increase counter by 1 and set temp to the next value
        while temp is not None:
            count += 1
            temp = temp.next
        #Increase comparison's counter by the average comparisons it takes per line to find a word
        comp += (count // 2)
    #Return average number of comparisons
    return comp // len(hash_table.table)

def main():
    #Print first options
    print("-----------------------------------------------------------------------------------------------------------")
    print("Please enter 1 to create Hash Table or 2 to Quit.")
    user = input()

    #If user input is 1 proceed to build a Hash Table
    if user == "1":
        #HASH TABLE
        hash_table = build_hash_table("word")
        print("DONE!")

    #Else if user input is 2 quit program
    elif user == "2":
        sys.exit()
    #Else notify the user their choice is not available and ask to try again
    else:
        print("Your input is not an option. Please try again.")
        main()

    #While the user doesn't quit keep asking for the nexr action
    repeat = True
    while repeat:
        #Ask user for the next action
        print("-----------------------------------------------------------------------------------------------------------")
        print("What would you like to do next?")
        print("1. Get number of anagrams of a word.")
        print("2. Find the load factor of your hash table.")
        print("3. Get the number of comparisons necessary to find a word.")
        print("4. Quit.")
        user_input = input()

        #If user input is 1 then get the number of anagrams a word has.
        if user_input == "1":
            # NUM OF ANAGRAMS
            word = input("Please enter a word: ")
            print(str(count_anagrams(hash_table, word)))
        #Else if the user input is 2 find the load factor of the hash table
        elif user_input == "2":
            # LOAD FACTOR
            print("The load factor of your hash table is: " + str(load_factor(hash_table)))
        #Else if the user input is 3 get the number of comparisons needed to find a word on the table.
        elif user_input == "3":
            print("The number of comparisons needed is : " + str(comparisons(hash_table)))
        #Else if the user input is 4 quit the program
        elif user_input == "4":
            sys.exit()
        #Else notify the user their choice is not an option and ask to try again.
        else:
            print("Your input is not an option. Please try again.")



#Run the program
main()
