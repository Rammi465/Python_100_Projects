# #open the text file for reading
# with open('snowwhite.txt', 'r') as file:
#     text = file.read()
    
# #split the text into sentences and sae the sentence in a list
# sentences = text.split(". ")
# corrected_sentences = []

# #Ietrate over the lsit of sentences and capatilize the first word
# for sentence in sentences:
#     sentence = sentence.capitalize()
#     corrected_sentences.append(sentence)
    
# #Join the sentences of the list into one single string
# corrected_text = ". ".join(corrected_sentences)

# #write the corrected text into file

# with open('corrected_snowwhite.txt', 'w') as file:
#     file.write(corrected_text)

# Read the text from the file
#with open('sentence_reverse_capitalize/snowwhite.txt') as file:
with open('snowwhite.txt', 'r') as file:
    text = file.read()

# Split the text into sentences and save the sentences in a list
sentences = text.split(". ")
#sentences = text.replace("\n", " ").split(". ")

corrected_sentences = []

# Iterate over the list of sentences
# and add each capitalized sentence in a list
for sentence in sentences:
    sentence = sentence.capitalize()
    corrected_sentences.append(sentence)

# Join the sentences of the list into one single string
corrected_text = ". ".join(corrected_sentences)

# Write the corrected text to a file
#with open('sentence_reverse_capitalize/snowwhite_corrected.txt', 'w') as file:
with open('snowwhite_corrected.txt', 'w') as file:
    #for text_line in corrected_text:
        file.write(corrected_text)
    
print("snowwhite_corrected.txt created successfully")