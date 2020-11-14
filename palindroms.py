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