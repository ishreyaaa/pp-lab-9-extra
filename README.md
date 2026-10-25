pp lab 9

🎯 Aim
To write a Python program to perform lambda functions and list comprehension.  
📚 Overview & Theory
 Lambda Functions: Small anonymous functions defined using the ⁠lambda⁠ keyword. They can take any number of arguments but contain only a single expression, which is evaluated and returned automatically. They are frequently used with built-in functions like ⁠map()⁠ and ⁠filter()⁠.  
 List Comprehension: A concise and elegant way to create lists in a single line of code. It provides a shorter, more readable syntax compared to traditional ⁠for⁠ loops and ensures efficient list construction.

 
💻 Source Code

# Lambda Functions
numbers = [1, 2, 3, 4, 5][span_5](start_span)[span_5](end_span)

# Using lambda with map() to find squares
squares = list(map(lambda x: x**2, numbers))[span_6](start_span)[span_6](end_span)

# Using lambda with filter() to find even numbers
evens = list(filter(lambda x: x % 2 == 0, numbers))[span_7](start_span)[span_7](end_span)

print("Original list:", numbers)[span_8](start_span)[span_8](end_span)
print("Squares using lambda:", squares)[span_9](start_span)[span_9](end_span)
print("Even numbers using lambda:", evens)[span_10](start_span)[span_10](end_span)

# List Comprehension
squares_lc = [x**2 for x in numbers][span_11](start_span)[span_11](end_span)
evens_lc = [x for x in numbers if x % 2 == 0][span_12](start_span)[span_12](end_span)

print("Squares using list comprehension:", squares_lc)[span_13](start_span)[span_13](end_span)
print("Evens using list comprehension:", evens_lc)[span_14](start_span)[span_14](end_span)

Output

Original list: [1, 2, 3, 4, 5]
Squares using lambda: [1, 4, 9, 16, 25]
Even numbers using lambda: [2, 4]
Squares using list comprehension: [1, 4, 9, 16, 25]
Evens using list comprehension: [2, 4]

How to Run the Code
1. Ensure you have Python installed on your system.
2. Download or clone this repository.
3. Open your terminal or command prompt in the project directory and run:

BASH
python script.py

📝 Conclusion
This program demonstrates how lambda functions and list comprehensions simplify Python code by offering compact and efficient ways to handle short anonymous operations and list creation, ultimately boosting code readability.
