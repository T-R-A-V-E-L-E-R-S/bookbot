def get_num_words(fs):
    with open(fs) as f:
        file_digest = len(f.read().split())
    return file_digest

def get_word_count(fs):
    count_char = {}
    
    with open(fs) as f:
        text =  f.read()
    
    for word in text:
        lower_w = word.lower()
        if lower_w in count_char:
            count_char[lower_w] += 1
        else:
            count_char[lower_w] = 1
    return count_char

def sort_on(dict):
    return dict["num"]

def get_sorted_list(char_dict):
    sorted_list = []
    for char, count in char_dict.items():
        if char.isalpha():
            sorted_list.append({"char": char, "num": count})
    
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list