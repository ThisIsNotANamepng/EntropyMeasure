f = open("table.txt", "r")
list = f.readlines()
f.close()

import hashlib

def compute_hash(word):
    hash_object = hashlib.sha256(word.encode())
    return hash_object.hexdigest()

def hash_words(input_file, output_file):
    index=0
    length=len(list)
    print(length)

    with open(input_file, 'r') as infile, open(output_file, 'w') as outfile:
        for line in infile:
            index+=1
            print(index, "/", length)

            word = line.strip()  # Remove newline characters
            if word:
                hashed_word = compute_hash(word)
                outfile.write(hashed_word + '\n')

input_filename = 'table.txt'      # Change this to your input file name
output_filename = 'hashes.txt'    # Change this to your output file name
hash_words(input_filename, output_filename)
print(f'Hashes saved to {output_filename}')
