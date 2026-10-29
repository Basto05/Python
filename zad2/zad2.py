# ZADANIE 2.10
line = """Python jest super.
Python jest prosty i przyjemny."""

result = len(line.split())
print(result)


# ZADANIE 2.11
word = "Python"

result = "_".join(word)
print(result)


# ZADANIE 2.12
line = "Kocham python, programowanie w pythonie jest najlepsze na swiecie bardzo go kocham jest najlepszy"
words = line.split()

first_chars = "".join(word[0] for word in words)
last_chars = "".join(word[-1] for word in words)

print(first_chars)
print(last_chars)


# ZADANIE 2.13
line = "Kocham python, programowanie w pythonie jest najlepsze na swiecie bardzo go kocham jest najlepszy"

result = sum(len(word) for word in line.split())
print(result)


# ZADANIE 2.14
line = "Kocham python, programowanie w pythonie jest najlepsze na swiecie bardzo go kocham jest najlepszy"

words = line.split()
longest_word = max(words, key=len)
longest_length = len(longest_word)

print(longest_word)
print(longest_length)


# ZADANIE 2.15
L = [12, 345, 6, 78]

result = "".join(str(number) for number in L)
print(result)


# ZADANIE 2.16
line = "Kocham py, programowanie w py jest najlepsze na swiecie bardzo go kocham jest najlepszy."

result = line.replace("py", "python")
print(result)


# ZADANIE 2.17
line = "Python jest prostym i popularnym jezykiem"

words = line.split()

alphabetically = sorted(words)
by_length = sorted(words, key=len)

print(alphabetically)
print(by_length)


# ZADANIE 2.18
number = 123456000789000

result = str(number).count("0")
print(result)


# ZADANIE 2.19
L = [7, 24, 123, 5, 89, 456]

result = "".join(str(number).zfill(3) for number in L)
print(result)