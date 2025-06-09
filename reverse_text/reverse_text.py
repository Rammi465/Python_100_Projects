#read thetext from file
with open('reverse_text/example.txt') as file:
    text = file.read()
    
#spilt the text into worda
words = text.split()
reversed_words = []

#append the reversed words
for word in words:
    word = word[::-1]
    reversed_words.append(word)

#join the revrsed word to text    
reversed_text = "".join(reversed_words)
    
#write reversed text into new file
with open('reverse_text/example_reversed.txt', 'w') as file:
    file.write(reversed_text)
    