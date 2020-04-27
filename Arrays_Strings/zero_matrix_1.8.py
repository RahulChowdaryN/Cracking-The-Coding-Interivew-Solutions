import unittest


# O(MN)
def zero_matrix(arr):
    ls_column = []
    ls_row = []
    for i in range(len(arr)):
        for j in range(len(arr[i])):
            if arr[i][j] == 0:
                ls_column.append(j)
                ls_row.append(i)
    print(ls_row,ls_column)
    for i in ls_row:
        arr[i] = [0] * len(arr[i])
    for i in arr:
        for j in ls_column:
            i[j] = 0
    print(arr)
    return arr

# print(zero_matrix([
#             [1, 2, 3, 4, 0],
#             [6, 0, 8, 9, 10],
#             [11, 12, 13, 14, 15],
#             [16, 0, 18, 19, 20],
#             [21, 22, 23, 24, 25]
#         ]))


class Test(unittest.TestCase):
    '''Test Cases'''
    data = [
        ([
            [1, 2, 3, 4, 0],
            [6, 0, 8, 9, 10],
            [11, 12, 13, 14, 15],
            [16, 0, 18, 19, 20],
            [21, 22, 23, 24, 25]
        ], [
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [11, 0, 13, 14, 0],
            [0, 0, 0, 0, 0],
            [21, 0, 23, 24, 0]
        ])
    ]

    def test_zero_matrix(self):
        for [test_matrix, expected] in self.data:
            actual = zero_matrix(test_matrix)
            self.assertEqual(actual, expected)

if __name__ == "__main__":
    unittest.main()