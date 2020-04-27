from collections import Counter
def check_perm(str1,str2):
    char_dict = Counter()

    if len(str1) != len(str2):
        return False

    for i in str1:
        char_dict[i] = char_dict.get(i,0) + 1

    for i in str2:
        ##if you use {} instead of counter, must add one more if condition
        #if i in char_dict
        if char_dict[i] > 0:
            char_dict[i] -= 1
        else:
            return False
    return True

print(check_perm("AD","CB"))

