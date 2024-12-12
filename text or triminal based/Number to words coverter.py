age = input("Enter your age to get it in words: ")

num = {
    "0": "zero",
    "1": "one",
    "2": "two",
    "3": "three",
    "4": "four",
    "5": "five",
    "6": "six",
    "7": "seven",
    "8": "eight",
    "9": "nine"
    
}
output = ""
for age_in_words in age:
    output += num.get(age_in_words, "!") + " "
print(output)
    