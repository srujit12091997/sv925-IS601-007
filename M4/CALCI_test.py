import unittest

class MyCalc(unittest.TestCase):

    def test_number_add_number(self):
        calc = MyCalc()
        self.assertEqual(calc.addition(4, 6), 10)
        self.assertEqual(calc.addition(8, 9), 17)
        self.assertEqual(calc.addition(6, 6), 12)

# UCID:sv925
# Date and time: 10/16/23 11:09
# two values are passed; the assert keyword tests for addition is true, if not, the program will raise an Error.

    def test_ans_add_number(self):
        calc = MyCalc()
        data = [
            {"a": "5", "b": "5", "r": "10"},
            {"a": "ans", "b": "4", "r": "14"},
            {"a": "ans", "b": "1", "r": "15"},
        ]
        for d in data:
            self.assertEqual(calc.addition(d["a"], d["b"]), float(d["r"]))

# UCID:sv925
# Date: 10/16/23 11:06
# This method contains 3 test cases. 1 We pass values and result of first test case is passed as input to other series. 2 second number we are passing and comparing with r passing value
# 3.for loop checks all the three test cases by calling method addition and returns pass or failure cases

    def test_number_sub_number(self):
        calc = MyCalc()
        self.assertEqual(calc.subtract(10, 5), 5)
        self.assertEqual(calc.subtract(100, 5), 95)
        self.assertEqual(calc.subtract(100, 15), 85)

# UCID:sv925
# Date: 10/16/23 11:11
# This method contains three test case , MyCalc is assigned to calc
# we are passing two values to subtraction method and comparing to the given number and The assert keyword test if a condition in your code returns True, or else AssertionError.

    def test_ans_sub_number(self):
        calc = MyCalc()
        data = [
            {"a": "10", "b": "2", "r": "8"},
            {"a": "ans", "b": "4", "r": "4"},
            {"a": "ans", "b": "1", "r": "3"},
        ]
        for d in data:
            self.assertEqual(calc.subtract(d["a"], d["b"]), float(d["r"]))


# UCID:sv925
# Date: 10/16/23 11:13
# This method contains three test cases
# series of data is passing ,in first test we pass values and result of first test case is passed as input to other series and second number we are passing and comparing with r passing value for loop checks all the three test cases by calling method subtraction and returns pass or failure cases


    def test_number_mult_number(self):
        calc = MyCalc()
        self.assertEqual(calc.multiply(5, 2), 10)
        self.assertEqual(calc.multiply(10, 2), 20)
        self.assertEqual(calc.multiply(15, 2), 30)

# UCID:sv925
# Date: 10/16/23 11:15
# This method contains three test cases
# series of data is passing two numbers for multiplication and compare the numbers method multiplication and returns pass or failure cases

    def test_ans_mult_number(self):
        calc = MyCalc()
        data = [
            {"a": "20", "b": "2", "r": "40"},
            {"a": "ans", "b": "4", "r": "160"},
            {"a": "ans", "b": "2", "r": "320"},
        ]
        for d in data:
            self.assertEqual(calc.multiply(d["a"], d["b"]), float(d["r"]))

#UCID:sv925
# Date: 10/16/23 11:16
#  There are three test cases for this approach. In the first test, we pass the values, and the output from the first test case is supplied as input to the next series. In the second series, we pass the values and compare them to the previous series' passing value.
# The for loop calls the method multiplication to verify all three test scenarios and returns a pass or fail result.

    def test_number_div_number(self):
        calc = MyCalc()
        self.assertEqual(calc.divide(20, 2), 10)
        self.assertEqual(calc.divide(15, 2), 7.5)
        self.assertEqual(calc.divide(100, 4), 25)

#UCID:sv925 
# Date: 10/16/23 11:18
# The assert keyword allows you to verify whether a condition in your code returns True; if it does not, the program will produce an AssertionError. This method comprises three test cases. MyCalc is assigned to calc.

    def test_ans_div_number(self):
        calc = MyCalc()
        data = [
            {"a": "20", "b": "2", "r": "10"},
            {"a": "ans", "b": "2", "r": "5"},
            {"a": "ans", "b": "3", "r": "1.6666666666666667"},
        ]
        for d in data:
            self.assertAlmostEqual(calc.divide(d["a"], d["b"]), float(d["r"]), places=6)

# UCID:sv925 
#Date: 10/16/23 11:18.
#In the first test, we pass the values, and the output from the first test case is supplied as input to the next series. In the second series, we pass the values and compare them to the previous series' passing value.
#for loop calls method division to verify all three test scenarios, returning pass or failure results.


if __name__ == '__main__':
    unittest.main()
