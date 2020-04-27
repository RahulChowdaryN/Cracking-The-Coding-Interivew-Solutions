import unittest
def sub_string(str1,str2):
    i = 0
    j = 0
    if len(str2) > len(str1):
        return False

    if str1 == str2:
        return True

    if not str1 or not str2:
        return False

    while i < len(str1):
        if str1[i] != str2[j]:
            i = i+1
            j = 0
        else:
            i +=1
            j +=1

        if j == len(str2):
            return True
    return False

class Test(unittest.TestCase):

    data = [
        ('hello','llo',True),
        ('rahul','hul',True),
        ('sa','sasd',False),
        ("simple","imp",True),
        ("Sample","aopl",False)
    ]

    def test_sub_string(self):
        for s1,s2,expected in self.data:

            actual = sub_string(s1,s2)
            self.assertEqual(actual,expected)

if __name__ == "__main__":
    unittest.main()