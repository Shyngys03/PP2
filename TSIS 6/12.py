def Palindrome(s):
    for i in range(len(s)):
        if s[i] != s[len(s) - i - 1]:
            return False
    return True
print(Palindrome(input()))