name = input("Enter your name: ")
age = input("Enter your age: ")
language = input("What's your favorite programming language? ")

print(f"{name}, you're {age} years young and already loving {language}. keep coding and stay curious!")

#check number whether it is positive, negative or zero
num = float(input("Enter a number: "))
if num > 0:
    print("The number is positive.")
elif num < 0:
    print("The number is negative.")
else:
    print("The number is zero.")
    
# Check if number is even or odd 
if num.is_integer():
    if int(num) % 2 == 0:
        print("The number is even.")
    else:
        print("The number is odd.")
else:
    print("The number is not an integer, so even/odd check doesn't apply.")

# Loop through numbers from 1 to 100
for num in range(1, 101):
    if num % 3 == 0 and num % 5 != 0:
        print(num)

# String Manipulation
def reverse_string(s):
    reversed_str = ""
    for char in s:
        reversed_str = char + reversed_str  # prepend each char
    return reversed_str

def to_uppercase(s):
    return s.upper()

def count_vowels(s):
    vowels = "aeiouAEIOU"
    count = 0
    for char in s:
        if char in vowels:
            count += 1
    return count

user_input = input("Enter a string: ")

reversed_str = reverse_string(user_input)
uppercase_str = to_uppercase(user_input)
vowel_count = count_vowels(user_input)

print("Reversed string:", reversed_str)
print("Uppercase string:", uppercase_str)
print("Number of vowels:", vowel_count)
