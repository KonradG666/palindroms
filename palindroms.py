def palindrome():
    """
          Print result if word is palindrome or not
          Set conditional to compare string/rev string
          Add bool True/False
          Add input
          Use another condition to check true or false
    """
    rev_string = string[::-1]
    if string != rev_string:
        return False
    return True

if __name__ == "__main__":
    string = input("enter the text: ")
    check = palindrome()
    if check:
        print("The string is a palindrome.")
    else:
        print("The string is not a palindrome.")