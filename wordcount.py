# put your code here.
#Psuedocode
#1. Process the file you want to get: splitting each word in the file
#2. Iterate over that list and populating the dictionary, count the frequency
#3. Displaying whatever's in the dictionary

#1
def process_file(file):
    filename = open(file)
    words = []
    for line in filename:
        line = line.rstrip()
        word = line.split(' ')
        words.extend(word)
    return words   


#2
def make_dict(file):
    words_list = process_file(file)

    word_dict = {}

    for word in words_list:
        word_dict[word] = word_dict.get(word, 0) + 1
        #if it finds the key word then it will + 1, otherwise it returns the default we have set as 0

    for word, frequency in word_dict.items():
        print('{} {}'.format(word,frequency))

make_dict("test.txt")