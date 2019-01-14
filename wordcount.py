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

file_process('test.txt')

#2
def  make_dict(file):
    processed_File = process_file(file)