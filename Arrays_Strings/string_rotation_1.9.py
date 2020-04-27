import unittest


def isSubstring(str1,str2):

    index = str1.find(str2)

    if index == -1:
        return False
    return True


def string_rotation(str1,str2):

    if str1 == str2:
        return True

    i = len(str1)
    j = len(str2)

    if i != j:
        return False

    cnt_eql = 0
    cnt_not_eql = 0

    while i > 0 and j > 0:
        if str1[i-1] != str2[j-1]:
            j = j - 1
            cnt_not_eql += 1
        else:
            i = i - 1
            j = j -1
            cnt_eql +=1

    if cnt_not_eql == len(str1):
        return False

    if i!= cnt_not_eql:
        return False

    if isSubstring(str1,str2[-cnt_not_eql:]):
        return True
    return False

class Test(unittest.TestCase):
    '''Test Cases'''
    data = [
        ('waterbottle', 'erbottlewat', True),
        ('foo', 'bar', False),
        ('foo', 'foofoo', False)
    ]

    def test_string_rotation(self):
        for [s1, s2, expected] in self.data:
            actual = string_rotation(s1, s2)
            self.assertEqual(actual, expected)

if __name__ == "__main__":
    unittest.main()





