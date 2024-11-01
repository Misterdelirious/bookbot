def main():
    letter_dict = {}
    letter_dict_list = []
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
    dictionarymaker(file_contents, letter_dict)


    nicelist(letter_dict, letter_dict_list)   


    

def dictionarymaker(file_contents, dictionary):
    words = file_contents.split()
# For words in file > for letters in those words > check of alphabetical > make lowercase > add to dict and count up.
    for word in words:
        for letter in word:
            if letter.isalpha() == True:
                lowercase = letter.lower()
                if lowercase not in dictionary:
                  dictionary[lowercase] = 0
                dictionary[lowercase] += 1
    return dictionary

def dictionarysplits (dictionary):
    for each in dictionary.items():
        print(each)     #Prints each  combo as a (x, #) tuple
        print(each[0])  #Prints each Key - Tuple
        print(each[1])  #prints each Value - Tuple
        
def sort_on(dict):
    return dict["num"]

def nicelist(dict, list):
    #Make a list of dicts
    for character, num in dict.items():
        char_dict = {"character": character, "num":num}
        list.append(char_dict)

    #sort it using sort_on
    list.sort(reverse=True, key=sort_on)

    #print the nice list
    for each in list:
        print(f"The {each['character']} was found {each['num']} times.")


main()
