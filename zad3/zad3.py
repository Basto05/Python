# ZADANIE 3.1

print("Zadanie 3.1")

# kod 1: Niepoprawny składniowo w tej postaci, ponieważ instrukcja if nie może
# być umieszczona po średniku jako część prostego wiersza złożonego.
# poprawnie:
x, y = 2, 3
if x > y:
    result = x
else:
    result = y
print(result)

# kod 2: Niepoprawny składniowo w tej postaci, ponieważ po nagłówku for
# musi być dwukropek, a instrukcja w pętli musi być poprawnie zapisana.
# poprawnie:
result = ""
for i in "axby":
    if ord(i) < 100:
        result += i
print(result)

# kod 3: Poprawny składniowo.
result = "".join(str(ord(i)) if ord(i) < 100 else i for i in "axby")
print(result)


# ZADANIE 3.2

print("\nZadanie 3.2")

# 1. sort() sortuje listę w miejscu i zwraca None.
# poprawnie:
L = [3, 5, 4]
L.sort()
result = L
print(result)

# 2. Za dużo wartości do rozpakowania do dwóch zmiennych.
# poprawnie:
x, y, z = 1, 2, 3
print(x, y, z)

# 3. Krotka jest niemodyfikowalna.
# poprawnie:
X = (1, 2, 3)
result = X
print(result)

# 4. Indeks 3 nie istnieje w liście o długości 3.
# poprawnie:
X = [1, 2, 3]
X.append(4)
result = X
print(result)

# 5. Napisy nie mają metody append().
# poprawnie:
X = "abc"
X = X + "d"
print(X)

# 6. pow() wymaga dwóch argumentów, a range(8) przekazuje tylko jeden.
# poprawnie:
L = list(map(lambda x: pow(x, 2), range(8)))
print(L)


# ZADANIE 3.3

print("\nZadanie 3.3")

# for
result = []
for i in range(31):
    if i % 3 != 0:
        result.append(i)
print(result)

# while
result = []
i = 0
while i <= 30:
    if i % 3 != 0:
        result.append(i)
    i += 1
print(result)


# ZADANIE 3.4

print("\nZadanie 3.4")
print("Wpisz liczbę rzeczywistą albo 'stop', aby zakończyć.")

while True:
    user_input = input("Podaj x: ")
    if user_input.lower() == "stop":
        break
    try:
        x = float(user_input)
        result = x ** 3
        print("x =", x)
        print("x^3 =", result)
    except ValueError:
        print("Błąd: podaj liczbę albo wpisz 'stop'.")


# ZADANIE 3.5

print("\nZadanie 3.5")

x = 12

result = ""
for i in range(x + 1):
    result += "|"
    if i < x:
        result += "...."
print(result)

result = "0"
for i in range(1, x + 1):
    result += str(i).rjust(5)
print(result)


# ZADANIE 3.6

print("\nZadanie 3.6")

x = 4
y = 2

border = "+" + "---+" * x
result = border

for i in range(y):
    result += "\n" + "|" + "   |" * x
    result += "\n" + border

print(result)


# ZADANIE 3.8

print("\nZadanie 3.8")

sequence1 = [1, 2, 3, 2, 4, 5]
sequence2 = [3, 4, 4, 5, 6, 1]

result = []
for element in sequence1:
    if element in sequence2 and element not in result:
        result.append(element)
print(result)

result = []
for element in sequence1 + sequence2:
    if element not in result:
        result.append(element)
print(result)


# ZADANIE 3.9

print("\nZadanie 3.9")

sequences = [[], [4], (1, 2), [3, 4], (5, 6, 7)]

result = [sum(sequence) for sequence in sequences]
print(result)


# ZADANIE 3.10

print("\nZadanie 3.10")

# sposób 1:
roman_values = {
    "I": 1,
    "V": 5,
    "X": 10,
    "L": 50,
    "C": 100,
    "D": 500,
    "M": 1000
}
print(roman_values)

# sposób 2:
roman_symbols = ["I", "V", "X", "L", "C", "D", "M"]
arabic_values = [1, 5, 10, 50, 100, 500, 1000]
roman_values_2 = dict(zip(roman_symbols, arabic_values))
print(roman_values_2)


def roman2int(roman):
    roman = roman.upper()
    result = 0

    for i in range(len(roman)):
        value = roman_values[roman[i]]

        if i + 1 < len(roman) and value < roman_values[roman[i + 1]]:
            result -= value
        else:
            result += value

    return result


# Przykładowe tłumaczenia
for roman in ["III", "IV", "IX", "XIV", "XL", "LVIII", "LXVII", "MCMXCIV", "MMXXVI"]:
    result = roman2int(roman)
    print(roman, "=", result)
