letter = '''Dear <|NAME|>,
Greetings from ABC coding house. I am happy to tell you about ypur selection in ABC coding house. We are happy to have you on board.
you are selected!
Have a great day ahead.
Thank and Regards,
Bill
Date: <|DATE|>'''

name = input("Enter your name: \n")
date = input("Enter Date: \n")

letter = letter.replace("<|NAME|>", name)
letter = letter.replace("<|DATE|>", date)
print(letter)