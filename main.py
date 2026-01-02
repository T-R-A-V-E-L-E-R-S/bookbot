import sys
from stats import get_num_words, get_sorted_list, get_word_count
def main():
    if len( sys.argv[1]) > 0:
        filepath = sys.argv[1]
    else:
        filepath = "./books/frankenstein.txt"

    word_count = get_num_words(filepath)
    char_dict = get_word_count(filepath)
    sorted_chars = get_sorted_list(char_dict)
    
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {filepath}...")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    
    for item in sorted_chars:
        print(f"{item['char']}: {item['num']}")
        
    print("============= END ===============")
    
def get_book_text(fs):
    with open(fs) as f:
        file_contents = f.read()
    return file_contents

print("Usage: python3 main.py <path_to_book>")
main()