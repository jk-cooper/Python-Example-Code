# Program finds phone numbers and emails on clipboard

import pyperclip
import re

# create phone regex

phoneRegex = re.compile(r'''(
    (\d{3}|\(\d{3}\))? # find an area code if there is one
    (\s|-|\.)? # find a dash or dot or space after the area code if there is one
    (\d{3}) # match prefix
    (\s|-|\.)
    (\d{4}) # match suffix
    (\s*(ext|x|ext.)\s*(\d{2,5}))? # find an extension if there is one
    )''', re.VERBOSE)

# create email regex

emailRegex = re.compile(r'''([a-zA-Z0-9._%+-]+ # username
                        @[a-zA-Z0-9.-]+ # at domain
                        (\.[a-zA-Z]{2,4}) # dot something 
                        )''', re.VERBOSE)

text = str(pyperclip.paste())

matches = []

for groups in phoneRegex.findall(text):
    phoneNum = '-'.join([groups[1], groups[3], groups[5]])
    if groups[8] != '':
        phoneNum += ' x' + groups[8]
    matches.append(phoneNum)
for groups in emailRegex.findall(text):
    matches.append(groups[0])

if len(matches) > 0:
    pyperclip.copy('\n'.join(matches))
    print("Copied to clipboard:")
    print('\n'.join(matches))
else:
    print("No phone number or email addresses found.")
