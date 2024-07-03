import math
from collections import Counter

def calculate_entropy(line):
    """Calculate the Shannon entropy of a given string."""
    if not line:
        return 0
    
    # Calculate the frequency of each character
    freqs = Counter(line)
    # Calculate the probability of each character
    probs = [float(freqs[char]) / len(line) for char in freqs]
    # Calculate the entropy
    entropy = - sum(p * math.log(p, 2) for p in probs)
    
    return entropy

def calculate_entropy_for_file(input_file, output_file):
    index=0
    """Calculate entropy for each line in the input file and write to output file."""
    with open(input_file, 'r') as infile, open(output_file, 'w') as outfile:
        for line in infile:
            print(index)
            index+=1

            line = line.strip()  # Remove newline characters
            if line:
                entropy = calculate_entropy(line)
                outfile.write(f"{entropy}\n")
    
    print(f"Entropies calculated and saved to '{output_file}'.")


input_filename = 'hashes.txt'      # Change this to your input file name
output_filename = 'entropies.txt' # Change this to your output file name
calculate_entropy_for_file(input_filename, output_filename)
