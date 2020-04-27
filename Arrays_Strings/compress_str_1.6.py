import unittest
import tracemalloc

# tracemalloc.start()


def string_compression(str1):
    comp_str = ""
    count = 0

    for i in range(len(str1)):
        if i != 0 and str1[i] != str1[i-1]:
            comp_str += str1[i-1] + str(count)
            count = 0
        count = count + 1
    comp_str += str1[-1] + str(count)
    print("com",comp_str)
    if len(comp_str) >= len(str1):
        return str1
    return comp_str

#print(string_compression("abccccccccccccc"))

# snapshot = tracemalloc.take_snapshot()
# top_stats = snapshot.statistics('lineno')
#
# print("[ Top 10 ]")
# for stat in top_stats[:10]:
#     print(stat)

class Test(unittest.TestCase):
    '''Test Cases'''
    data = [
        ('aabcccccaaa', 'a2b1c5a3'),
        ('abcdef', 'abcdef')
    ]

    def test_string_compression(self):
        for [test_string, expected] in self.data:
            actual = string_compression(test_string)
            self.assertEqual(actual, expected)

if __name__ == "__main__":
    unittest.main()