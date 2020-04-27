class Solution:
    def __init__(self):
        self.monthMap = {"january":1,"february":2,"march":3,"april":4,"may":5,"june":6,"july":7,"august":8,"september":9,"october":10,"november":11,"december":12}
        self.cubeOne = {1:0,2:1,3:2,4:3,5:4,6:5}
        self.cubeTwo = {7:0,8:1,9:2,10:3,11:4,12:5}
        self.cubeThree = {1:0,2:1,3:2,4:3,5:4,6:5}
        self.cubeFour = {1:0,2:1,0:2,7:3,8:4,9:5}


    def displayDates(self,date: str):
        if not date:
            return [-1,-1,-1,-1]
        month,date = date.split(" ")
        if not month or not date:
            return [-1, -1,-1,-1]
        result = [-1,-1,-1,-1]
        date = int(date)
      #  date_digit_one, date_digit_two = -1, -1
        month = self.monthMap[month.lower()]

        result[0] = self.cubeOne.get(month,-1)
        result[1] = self.cubeTwo.get(month, -1)

        if date <= 9:
            result[2] = self.cubeThree.get(date,-1)
           # date_digit_one = self.cubeThree.get(month,-1)
           # result.append(date_digit_one)
            # if date in self.cubeThree:
            #     result.append(self.cubeThree[int(date)])
            # else:
            #     result.append(-1)
            if result[2] == - 1:
                result[3] = self.cubeFour.get(date,-1)
                #date_digit_two = self.cubeFour[date] if date in self.cubeFour else -1
            else:
                result[3] = -1
            #result.append(date_digit_two)
            return result

        digit_one, digit_two = divmod(date, 10)
        if digit_one in self.cubeThree and digit_two in self.cubeFour:
            result[2] = self.cubeThree[digit_one]
            result[3] = self.cubeFour[digit_two]
            #result.append(self.cubeThree[digit_one])
            #result.append(self.cubeFour[digit_two])
        else:
            result[2] = self.cubeThree[digit_two]
            result[3] = self.cubeFour[digit_one]
            # result.append(self.cubeThree[digit_two])
            # result.append(self.cubeFour[digit_one])

        # date_digit_one = self.cubeThree[digit_one] if digit_one in self.cubeThree and digit_two in self.cubeFour else self.cubeFour[digit_one]
        # date_digit_two = self.cubeFour[digit_two] if digit_one in self.cubeThree and digit_two in self.cubeFour else self.cubeThree[digit_two]


        # result.append(date_digit_one)
        # result.append(date_digit_two)
        # if int(date[0]) in self.cubeThree:
        #     flag_one = True
        # if int(date[1]) in self.cubeFour:
        #     flag_two = True
        # if flag_one and flag_two:
        #     result.append(self.cubeThree[int(date[0])])
        #     result.append(self.cubeFour[int(date[1])])
        # else:
        #     result.append(self.cubeThree[int(date[1])])
        #     result.append(self.cubeFour[int(date[0])])
        return result


import unittest


class Test(unittest.TestCase):
    def test_displayDates(self):
        dates = Solution()

        self.assertEqual(dates.displayDates("January 01"), [0,-1,0,-1])
        self.assertEqual(dates.displayDates("February 13"), [1,-1,2,0])
        self.assertEqual(dates.displayDates("March 23"), [2,-1,2,1])
        self.assertEqual(dates.displayDates("April 30"), [3,-1,2,2])
        self.assertEqual(dates.displayDates("June 7"), [5,-1,-1,3])
        self.assertEqual(dates.displayDates("July 23"), [-1,0,2,1])
        self.assertEqual(dates.displayDates("August 30"), [-1,1,2,2])
        self.assertEqual(dates.displayDates("September 7"), [-1,2,-1,3])



if __name__ == "__main__":
    unittest.main()
