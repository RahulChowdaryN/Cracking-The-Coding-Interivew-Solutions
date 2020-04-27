import unittest


class Solution:

    month_map = {"january": 1, "february": 2, "march": 3, "april": 4, "may": 5, "june": 6, "july": 7, "august": 8,
                 "september": 9, "october": 10, "november": 11, "december": 12}
    # Using hash-map as access time and search time is O(1)
    # key represents number on each face of cube and value represent index of each face
    cube_one = {1: 0, 2: 1, 3: 2, 4: 3, 5: 4, 6: 5}
    cube_two = {7: 0, 8:1, 9: 2, 10: 3, 11: 4, 12: 5}
    cube_three = {1: 0, 2: 1, 3: 2, 4: 3, 5: 4, 6: 5}
    cube_four = {1: 0, 2: 1, 0: 2,7 : 3, 8: 4, 9: 5}

    def display_dates(self,date: str):
        """ function to represent month and date from four six-faced cubes
            i/p: date: string ex: December 12
            o/p: LIST  ex: [-1,5,0,1]
        """
        if not date:
            return [-1,-1,-1,-1]
        month,date = date.split(" ")
        if not month or not date:
            return [-1, -1,-1,-1]

        result = [-1,-1,-1,-1]
        date = int(date)
        month = self.month_map[month.lower()]
        # search the month in the first two cubes. if not present returns -1
        result[0] = self.cube_one.get(month,-1)
        result[1] = self.cube_two.get(month, -1)
        # if the date is single digit, it’s straightforward
        if date <= 9:
            result[2] = self.cube_three.get(date,-1)
            if result[2] == - 1:
                result[3] = self.cube_four.get(date,-1)
            return result
        # if the digit has two numbers
        digit_one, digit_two = divmod(date, 10)
        # if first digit in 3rd cube and second digit in 4th cube return indices here
        if digit_one in self.cube_three and digit_two in self.cube_four:
            result[2] = self.cube_three.get(digit_one,-1)
            result[3] = self.cube_four.get(digit_two, -1)
            return result
        # if not return second digit from 3rd cube and first digit from 4th cube
        result[2] = self.cube_three.get(digit_two,-1)
        result[3] = self.cube_four.get(digit_one,-1)
        return result


class Test(unittest.TestCase):

    # unit-test cases

    def test_displayDates(self):
        dates = Solution()
        self.assertEqual(dates.display_dates("January 01"), [0,-1,0,-1])
        self.assertEqual(dates.display_dates("February 13"), [1,-1,2,0])
        self.assertEqual(dates.display_dates("March 23"), [2,-1,2,1])
        self.assertEqual(dates.display_dates("April 30"), [3,-1,2,2])
        self.assertEqual(dates.display_dates("June 7"), [5,-1,-1,3])
        self.assertEqual(dates.display_dates("July 23"), [-1,0,2,1])
        self.assertEqual(dates.display_dates("August 30"), [-1,1,2,2])
        self.assertEqual(dates.display_dates("September 7"), [-1,2,-1,3])
        self.assertEqual(dates.display_dates("October 10"), [-1, 3, 0, 2])
        self.assertEqual(dates.display_dates("November 19"), [-1, 4, 0, 5])
        self.assertEqual(dates.display_dates("December 4"), [-1, 5, 3, -1])


if __name__ == "__main__":

    unittest.main()


