import sys
import re

def main():
    with open(sys.argv[1], encoding='utf8') as file:
        lines = file.readlines()
        
        # remove lines with no lowercase letters
        lines = [l for l in lines if any(c.islower() for c in l)]
        
        # join lines
        data = ' '.join(lines)
        
        # remove text between square brackets
        data = re.sub(r'\[.+\]', '', data)
        
        # find and strip all sentences
        sentences = re.findall(r'[^\.]+\w+\.', data)
        sentences = list(s.strip() for s in sentences)
        
        data = re.sub(r'[^A-Za-z\.,!;\:\?\- ]', '', data)
            
        # find all words
        words = re.findall(r'\w+', data)
        unique_words = set(w.strip().lower() for w in words)
        
        sentence_lengths = list(s.count(' ')+1 for s in sentences)
        sentence_punctuation = list((s.count(',')+s.count(';')+s.count(':')) for s in sentences)
        unique_word_lengths = list(len(w) for w in unique_words)
        complexity = round(average(sentence_lengths) + average(unique_word_lengths) + 2*average(sentence_punctuation), 1)
        
        print(f's: {round(average(sentence_lengths), 1)}, w: {round(average(unique_word_lengths), 1)}, p: {round(average(sentence_punctuation), 1)}, c: {complexity}')

def average(list):
    return sum(list) / len(list)

if __name__ == '__main__':
    main()

