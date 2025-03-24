def get_num_words(text):
    word_list = text.split()

    return len(word_list)

def character_count(text):
    text = text.lower()
    
    character_count ={}

    for i in text:
        if i in character_count:
            character_count[i] += 1
        else:
            character_count[i] = 1

    return (character_count)

def sort_by(char_dict):
    chars_list = []
    for char, count in char_dict.items():
        chars_list.append({"char": char, "count": count})
    
    def sort_on(dict):
        return dict["count"]
    
    # Sort the list by count in descending order
    chars_list.sort(reverse=True, key=sort_on)
    return chars_list
