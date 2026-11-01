# Write a recursive function reverse_string(s) that returns the reversed string.

def reverse_string(s):
    if s == "":
        return ""

    return reverse_string(s[1:]) + s[0]

result = reverse_string("hello")
print(result)