# Your code here

# read in the txt file
with open('applications/histo/robin.txt','r') as f:
    output = f.read()

# use the word count function to get the count of each word. 
def word_count(s):
    ignored = '" : ; , . - + = / \ | [ ] { } ( ) * ^ &'
    
    s = s.lower()

    for i in ignored:
        s = s.replace(i, " ")

    cache = {}
    for i in s.split():
        cache[i] = s.split().count(i)
    
    return cache

# save the results to a variable
results = word_count(output)

# sort the results by count then word
sorted_results = sorted(results.items(), key=lambda x: (-x[1], x), reverse=False)

# print the results with a # for each number of times word appears
for i in sorted_results:
    pound_sign = i[1] * "#"
    print('{:20s}{:}'.format(i[0], pound_sign))
