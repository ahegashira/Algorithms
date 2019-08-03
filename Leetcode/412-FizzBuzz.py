# 412. Fizz Buzz
# Easy

# Write a program that outputs the string representation of numbers from 1 to n.

# But for multiples of three it should output “Fizz” instead of the number and for the multiples of five output “Buzz”. For numbers which are multiples of both three and five output “FizzBuzz”.

class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        answer=[]
        for n in range(1, n+1):    
            if n % 5 == 0 and n % 3 == 0:
                answer.append("FizzBuzz")
            elif n % 5 == 0:
                answer.append("Buzz")
            elif n % 3 == 0:
                answer.append("Fizz")
            else: 
                answer.append(str(n))       
        return answer


# Example:

# n = 15,

# Return:
# [
#     "1",
#     "2",
#     "Fizz",
#     "4",
#     "Buzz",
#     "Fizz",
#     "7",
#     "8",
#     "Fizz",
#     "Buzz",
#     "11",
#     "Fizz",
#     "13",
#     "14",
#     "FizzBuzz"
# ]