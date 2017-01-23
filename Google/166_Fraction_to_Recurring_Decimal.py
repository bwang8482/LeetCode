"""
Given two integers representing the numerator and denominator of a fraction, return the fraction in string format.

If the fractional part is repeating, enclose the repeating part in parentheses.

For example,

Given numerator = 1, denominator = 2, return "0.5".
Given numerator = 2, denominator = 1, return "2".
Given numerator = 2, denominator = 3, return "0.(6)".
Hint:

No scary math, just apply elementary math knowledge. Still remember how to perform a long division?
Try a long division on 4/9, the repeating part is obvious. Now try 4/333. Do you see a pattern?
Be wary of edge cases! List out as many test cases as you can think of and test your code thoroughly.
"""


"""Solution:
    1. using dictionary to remember the appearance location of each digit and reminder
    2. if same digit have same reminder, there is a loop
"""

class Solution(object):
    def fractionToDecimal(self, numerator, denominator):
        """
        :type numerator: int
        :type denominator: int
        :rtype: str
        """
        # check zero
        if denominator == 0: return 'NaN'
        if numerator == 0: return '0'
        
        # check sign
        self.sign = str(numerator/abs(numerator) * (denominator/abs(denominator)))[:-1]
        numerator, denominator = abs(numerator), abs(denominator)
        self.integer = str(numerator/denominator)
        self.reminder = numerator%denominator
        
        # return if interger
        if self.reminder == 0:
            return self.sign + self.integer

        self.decimal = ''
        self.appear = collections.defaultdict(list)
        self.index = 0
        # calculate decimal
        while True:
            digit = self.reminder*10 / denominator
            self.reminder = self.reminder*10 % denominator
            # if exact division
            if self.reminder == 0:
                return self.sign + self.integer + '.' + self.decimal + str(digit)
            # otherwise, check for loop
            for location, value in self.appear[digit]:
                if value == self.reminder:
                    return self.sign + self.integer + '.' + self.decimal[:location] + '(' + self.decimal[location:] + ')'
            # update
            self.decimal += (str(digit))
            self.appear[digit].append((self.index, self.reminder))
            self.index += 1

"""Summary:
    there is no need to check the loop by substring. Check the reminder instead.
"""
