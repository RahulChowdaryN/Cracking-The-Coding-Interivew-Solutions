def IsUnique(str1):
    for i in range(len(str1)):
        if str1[i] in str1[i+1:]:
            return False
    return True

def IsUnique1(str1):

    while str1:
        if str1[0] in str1[1:]:
            return False
        str1 = "".join(str1.split(str1[0]))
    return True

def IsUnique2(str1):
    temp_str = set()
    for i in range(len(str1)):
        if str1[i] in temp_str:
            return False
        temp_str.add(str1[i])
    return True


print(IsUnique("a"))
print(IsUnique1("a"))
print(IsUnique2("a"))

