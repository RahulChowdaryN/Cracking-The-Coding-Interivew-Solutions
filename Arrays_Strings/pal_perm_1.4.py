def pal(str1):

    count = 0
    temp_str = {}
    for i in str1:
        if not i.isspace():
            temp_str[i.lower()] = temp_str.get(i.lower(),0) + 1
            count = count + 1
    print(count,temp_str)
    temp = 0
    if count %2 == 0:
        for i,j in temp_str.items():
            if j%2 != 0 :
                return False

        return True
    temp = 0
    for i,j in temp_str.items():

        if j%2 != 0:
            temp = temp + 1
        if temp > 1:
            return False
    return True

def pal2(phrase):

    char_map = set()

    for i in phrase:
        if not i.isspace():
            if not i in char_map:
                char_map.add(i)
            else:
                char_map.remove(i)
    return len(char_map) <=1

print(pal2("care rac"))

