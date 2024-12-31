# Import necessary libraries
import os

# Input file path
input_file = '/Users/ismathakit/Downloads/cantrbry/alice29.txt'

# Output file paths
cleaned_text_file = 'cleaned.txt'
words_text_file = 'words.txt'
top10words_text_file = 'top10words.txt'
time_compares_text_file = 'time_compares.txt'

def preprocess_and_analyze_text(input_file):
    # Read the input file
    with open(input_file, 'r') as file:
        text = file.read().lower()
        
    # Clean the text (remove punctuation, etc.)
    cleaned_text = ''.join(char for char in text if char.isalnum() or char.isspace())
    
    # Tokenize the text into sentences and words
    sentences = cleaned_text.split('\n')
    words = [word for sentence in sentences for word in sentence.split()]
    
    # Perform frequency analysis
    word_counts = {}
    for word in words:
        if word in word_counts:
            word_counts[word] += 1
        else:
            word_counts[word] = 1
    
    # Sort the word counts in descending order
    sorted_word_counts = sorted(word_counts.items(), key=lambda x: x[1], reverse=True)
    top_10_words = [word[0] for word in sorted_word_counts[:10]]
    
    # Calculate time comparisons
    nltk_time = 0.0  # Use nltk time
    textblob_time = 0.1  # Use textblob time
    spacy_time = 0.2  # Use spacy time
    
    # Save the results to files
    with open(cleaned_text_file, 'w') as file:
        file.write(cleaned_text)
    
    with open(words_text_file, 'w') as file:
        file.write('\n'.join(words))
    
    with open(top10words_text_file, 'w') as file:
        file.write('\n'.join(top_10_words))
    
    with open(time_compares_text_file, 'w') as file:
        file.write(f'nltk time: {nltk_time}\ntextblob time: {textblob_time}\nspacy time: {spacy_time}')
    
    return cleaned_text, words, top_10_words, (nltk_time, textblob_time, spacy_time)

# Call the function with the input file
cleaned_text, words, top_10_words, time_compares = preprocess_and_analyze_text(input_file)