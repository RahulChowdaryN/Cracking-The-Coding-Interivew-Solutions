def urlify(str1,length):

   # if length == 0 or len(str1) != length:
    #    return False
    str1 = str1.strip()

    str2 = str1.replace(" ","%20")

    return str2

def urlify1(str1,length):

    s = ""
    for i in range(length):
        if str1[i].isspace():
            s = s+"%20"
        else:
            s = s + str1[i]

    return s


print("hello")

print(urlify("    much ado about nothing   ",26))