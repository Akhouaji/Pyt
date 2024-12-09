def count_char(s, char):
    s = s.lower()
    char = char.lower()
    return s.count(char)

print(count_char("Hello World", "O"))