# Functions

def average(nums):
    return sum(nums) / len(nums)

def word_count(sentence):
    return len(sentence.split())

marks = [80, 85, 90]
print("Average:", average(marks))

sentence = "ai is the future"
print("Words:", word_count(sentence))
