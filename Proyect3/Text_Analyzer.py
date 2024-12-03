text = input("Enter a text of your choice: ")
letters = []

text = text.lower()

letters.append(input("Enter the first letter: ".lower()))
letters.append(input("Enter the second letter: ".lower()))
letters.append(input("Enter the third letter: ".lower()))

print("\n")
print("NUMBER OF LETTERS")
letter_count1 = text.count(letters[0])
letter_count2 = text.count(letters[1])
letter_count3 = text.count(letters[2])

print(f"We found the letter '{letters[0]}' repeated {letter_count1} times")
print(f"We found the letter '{letters[1]}' repeated {letter_count2} times")
print(f"We found the letter '{letters[2]}' repeated {letter_count3} times")

print("\n")
print("NUMBER OF WORDS")
words = text.split()
print(f"We found {len(words)} words in your text")

print("\n")
print("FIRST AND LAST LETTERS")
first_letter = text[0]
last_letter = text[-1]
print(f"The first letter is '{first_letter}' and the last letter is '{last_letter}'")

print("\n")
print("REVERSED TEXT")
words.reverse()
reversed_text = ' '.join(words)
print(f"If we reverse your text, it will say: '{reversed_text}'")

print("\n")
print("LOOKING FOR THE WORD PYTHON")
search_python = 'python' in text
response_dict = {True: "yes", False: "no"}
print(f"The word 'Python' {response_dict[search_python]} is found in the text")
