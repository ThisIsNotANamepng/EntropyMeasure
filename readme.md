# Entropy Measure

This repo is to satify two curiousity/research projects

1. Measuring the entropy of regular files you find on a computer, the entropy of encrypted or partially encrypted files, and the entropy of malware files which are partially or fully encrypted
2. Running througha  rainbow table and using entropy to find the least random hash

## Hash Entropy

Process:
- Get the wordlist table from https://crackstation.net/crackstation-wordlist-password-cracking-dictionary.htm
- Unzip it and translate it to utf-8 with `iconv -f ISO-8859-1 -t UTF-8//TRANSLIT input.txt -o table.txt`
- Use `createhash.py` to create a file with all of the hashes
- Use `entropy.py` to find the entropy for each hash and put them in entropies.txt
- Use `lowestentropy.py` to find the lowest 10 entropies in entropies.txt, the line numbers correspond in the three hash/entropy/password files

