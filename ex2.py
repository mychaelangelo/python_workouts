def mysum(*args): # using '*' means can take a variable number of arguments
    result = 0
    for i in args:
        result += i
    return result
#print(mysum(1,2,3,4))

def mysum_alt(num_list, optional_num=0):
    result = optional_num
    for i in num_list:
        result += i
    return result

#print(mysum_alt([1,2,3],5))

def ret_avg(num_list):
    return mysum_alt(num_list) / len(num_list)

#print(ret_avg([1,2,4]))

def word_calc(words_list):
    """
    Take list of words (the words are strings).
    Calculate length of: shortest word, longest word, average length
    Return as a tuple.
    """
    min_words, max_words = len(min(words_list)), len(max(words_list))
    avg_words = len(''.join(words_list)) / len(words_list)
    return (min_words, max_words, avg_words)

#print(word_calc(['a','ab','abc']))

def sum_objects(objects_list):
    result = 0
    for object_item in objects_list:
        if isinstance(object_item, int):
            result += object_item
        else:
            try:
                result += int(object_item)
            except:
                pass
    return result



print(sum_objects(["1", 'a']))
    