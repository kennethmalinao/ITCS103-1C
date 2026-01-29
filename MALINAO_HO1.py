word = input("Enter a word: ")
word_len = len(word)

numbers = []

for i in range(word_len):
    num = int(input(f"Enter a number {i + 1}: "))
    numbers.append(num)

def the_average(nums):
    return sum(nums) / len(nums)

def compare(word_len, the_average):
    if word_len > the_average:
        print(f"The length of the word '{word}' is greater than the average.")
    elif word_len < the_average:
        print(f"The length of the word '{word}' is less than the average.")
    else:
        print(f"The length of the word '{word}' is equal to the average.")

average = the_average(numbers)

print(numbers)
print("The length of the word is", word_len)
print("The average of the numbers is", average)

compare(word_len, average)
