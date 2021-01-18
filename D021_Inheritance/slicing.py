piano_keys = ["a", "b", "c", "d", "e", "f", "g"]

print(piano_keys[2:5])  # ['c', 'd', 'e']
print(piano_keys[2:])  # ['c', 'd', 'e', 'f', 'g']
print(piano_keys[:5])  # ['a', 'b', 'c', 'd', 'e']

print(piano_keys[2:5:2])  # ['c', 'e']
print(piano_keys[1::])  # ['b', 'c', 'd', 'e', 'f', 'g']
print(piano_keys[::2])  # ['a', 'c', 'e', 'g']
print(piano_keys[::-1])  # ['g', 'f', 'e', 'd', 'c', 'b', 'a']

