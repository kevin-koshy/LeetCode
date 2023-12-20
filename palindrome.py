def is_palindrome(num):
    temp = num
    rev = 0
    while num > 0:
        dig = num % 10
        num = num // 10
        rev = rev * 10 + dig
    return temp == rev


num = 101
print(is_palindrome(num))