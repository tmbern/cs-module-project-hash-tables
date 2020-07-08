# Use frequency analysis to find the key to ciphertext.txt, and then
# decode it.

# read in the txt file
with open('applications/crack_caesar/ciphertext.txt','r') as f:
    output = f.read()

# print the output for comparrison
print(output)
print(" ")
print("_________" * 15)
# these are the most frequent letters that are used...or at least we are saying they are.
most_frequent_letters = ['E', 'T', 'A', 'O', 'H', 'N', 'R', 'I', 'S', 'D', 'L', 'W', 'U',
'G', 'F', 'B', 'M', 'Y', 'C', 'P', 'K', 'V', 'Q', 'J', 'X', 'Z']


# create a dictionary to get the most frequently used characters from the read in text file
h = {}
for i in most_frequent_letters:
  h[i] = output.count(i)

# get the list of characters from the dictionary sorted by the most frequent
sorted_h = [i for i, j in sorted(h.items(), key=lambda x: x[1], reverse=True)]

# create the mapping for the cipher. The keys are the most frequent from the read in file
# the values are the most frequent that occur in plain text.
cipher_map = dict(zip(sorted_h, most_frequent_letters))

# decode the txt file
decode = ""
for i in output:
  if i in cipher_map.values():
    decode += cipher_map[i]
  else:
    decode += i

print(decode)