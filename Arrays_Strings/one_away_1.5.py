import unittest
def one_away(str1,str2):
    if len(str1) > len(str2) + 1:
        return False
    if len(str1) < len(str2) - 1:
        return False
    temp_char = {}
    for i in str1:
        temp_char[i] = temp_char.get(i,0) + 1
    temp_count = 0
    for i in str2:
        if i in temp_char:
            temp_char[i] -=1
        else:
            temp_count +=1
            if temp_count > 1:
                return False
    count = 0

    for i,j in temp_char.items():
        count +=j
        if count > 1 :
            return False
    return True

class Test(unittest.TestCase):
    '''Test Cases'''
    data = [
        ('pale', 'ple', True),
        ('pales', 'pale', True),
        ('pale', 'bale', True),
        ('paleabc', 'pleabc', True),
        ('pale', 'ble', False),
        ('a', 'b', True),
        ('', 'd', True),
        ('d', 'de', True),
        ('pale', 'pale', True),
        ('pale', 'ple', True),
        ('ple', 'pale', True),
        ('pale', 'bale', True),
        ('pale', 'bake', False),
        ('pale', 'pse', False),
        ('ples', 'pales', True),
        ('pale', 'pas', False),
        ('pas', 'pale', False),
        ('pale', 'pkle', True),
        ('pkle', 'pable', False),
        ('pal', 'palks', False),
        ('palks', 'pal', False)
    ]

    def test_one_away(self):
        for test_s1, test_s2, expected in self.data:
            actual = one_away(test_s1, test_s2)
            self.assertEqual(actual, expected)

if __name__ == "__main__":
    unittest.main()