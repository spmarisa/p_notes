def reverse(text):
    return text[::-1]

def is_palindrome(text):
    return text == reverse(text)

something = input('enter something:')

if is_palindrome(something):
    print('{0} is palindrome'.format(something))
else:
    print('{0} is not palindrome'.format(something))