def find_lowest_entropies_with_lines(entropies_file, data_file):
    entropies = []
    with open(entropies_file, 'r') as file:
        for line_number, line in enumerate(file, start=1):
            try:
                entropy_value = float(line.strip().split(': ')[-1])  # Extract entropy value from the line
                entropies.append((entropy_value, line_number))
            except ValueError:
                print(f"Skipping line {line_number} in {entropies_file}. Invalid format.")
    
    # Sort entropies in ascending order to find the lowest values
    sorted_entropies = sorted(entropies, key=lambda x: x[0])
    
    # Fetch corresponding lines from data_file for the lowest entropies
    lowest_entropies_with_lines = []
    with open(data_file, 'r') as data_file:
        for entropy_value, line_number in sorted_entropies[:10]:  # Get the first 10 lowest entropies
            line = None
            for current_line_number, current_line in enumerate(data_file, start=1):
                if current_line_number == line_number:
                    line = current_line.strip()
                    break
            if line:
                lowest_entropies_with_lines.append((line_number, entropy_value, line))
            data_file.seek(0)  # Reset file pointer to beginning for next search
    
    return lowest_entropies_with_lines

entropies_filename = 'entropies.txt'  # Change this to your entropies file name
data_filename = 'hashes.txt'      # Change this to your data lines file name

lowest_entropies_with_lines = find_lowest_entropies_with_lines(entropies_filename, data_filename)

print("Lines with lowest entropies:")
for line_number, entropy_value, line_content in lowest_entropies_with_lines:
    print(f"Line {line_number} - Entropy: {entropy_value} - Content: {line_content}")
