# This file contains code for a simple file compression example
#
# Author: Josh McIntyre
#
#
import argparse

SUB_PLACEHOLDER = "***\n"

# The compression algorithm
def compress(filename, verbose=False):

    with open(filename) as f:
        uncompressed_data = f.read()
    
    # Read the data and build a substitution list
    # This naive algorithm will look for repeat words
    # Any word that appears twice or more will go in the substitution list
    # Each substitution will then be done by index in the list
    # Ex: "belt" index 0 of substitutions will be replaced with "0" in the compressed file
    wordlist = []
    substitutions = []
    split_data = uncompressed_data.split()
    for word in split_data:
        if word in wordlist:
            if word not in substitutions:
                substitutions.append(word)
        else:
            wordlist.append(word)
    
    if verbose:
        print("Substitution list:")
        print(substitutions)
    
    # Write the new compressed file and substitution dictionary
    compressed_filename = filename.replace(".txt", ".wbp")
    compressed_data = uncompressed_data
    for i in range(len(substitutions)):
        compressed_data = compressed_data.replace(substitutions[i], str(i))
    
    with open(compressed_filename, "w") as f:
        f.write(compressed_data)
        f.write(SUB_PLACEHOLDER)
        for substitution in substitutions:
            f.write(f"{substitution}\n")

# The decompression algorithm
def decompress(filename, verbose=False):

    with open(filename, "r") as f:
        all_lines = f.read()
        compressed_data = all_lines.split(SUB_PLACEHOLDER)[0]
        substitutions = all_lines.split(SUB_PLACEHOLDER)[1].split()
        
        if verbose:
            print("Substitutions:")
            print(substitutions)
    
    # Uncompress the data
    # Here, we move backwards through the substitution list
    # The simple reason is to prevent mis-substitutions 
    # For example: 10 -> Jonathan but 1 -> white 0 -> belt
    # If we substitute 10 for Jonathan first, we won't accidentally sub in whitebelt
    uncompressed_filename = filename.replace(".wbp", ".txt")
    uncompressed_data = compressed_data
    for i in range(len(substitutions) - 1, -1, -1):
        uncompressed_data = uncompressed_data.replace(str(i), substitutions[i])
        
    with open(uncompressed_filename, "w") as f:
        f.write(uncompressed_data)

# The main entry point for the program
def main():

    parser = argparse.ArgumentParser(description="A simple, naive demo of a file compression algorithm")
    parser.add_argument("filename", type=str, help="The file path to compress")
    parser.add_argument("--verbose", action="store_true")
    args = parser.parse_args()
    
    if args.filename.endswith(".txt"):
        compress(args.filename)
    if args.filename.endswith(".wbp"):
        decompress(args.filename)

if __name__ == "__main__":
    main()