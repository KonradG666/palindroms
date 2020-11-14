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

import sys
import logging
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s %(message)s')
logging.debug("debug")

def palindrome():
    """
          Print result if word is palindrome or not
          Set conditional to compare string/rev string
          Add bool True/False
          Use another condition to check true or false
    """
    rev_string = string[::-1]
    if string != rev_string:
        return False
    return True

if __name__ == "__main__":
    logging.debug("The program was called with this parameters %s" % sys.argv[1])
    string = sys.argv[1]
    check = palindrome()
    if check:
        logging.debug("The string is a palindrome.")
    else:
        logging.debug("The string is not a palindrome.")