def get_num_words(file_contents):
    return len(file_contents.split())

def get_char_number(file_contents):
    new_dict = {}
    file_contents = file_contents.lower()

    for char in file_contents:
        if char not in new_dict:
            new_dict[char] = 1
        else: 
            new_dict[char] += 1
    
    return new_dict



def sort_dict(dictionary):
    def sort_on(dict_item):
        return dict_item["num"]

    dict_list = [] 

    for key in dictionary:
        new_dict = {}
        new_dict["char"]=key
        new_dict["num"]=int(dictionary[key])
        dict_list.append(new_dict)
    
    dict_list.sort(reverse=True, key=sort_on)
    

    return dict_list