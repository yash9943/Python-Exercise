import re

emailRegex = re.compile(r'^[a-zA-Z-_.]+@[a-zA-Z0-9]+\.[a-zA-Z]{2,3}$')

emails = ["abc@gmail.com", "123$tt*@xyz.com", "good@bad@uk.in", 
"nasa@usa12.space", "no-reply@domain.in", "ramhanuman@saketa.lok", 
"ruhi.mohan@exter123.123", "fake@fake123.fakercom"]

valid_emails = []
invalid_emails = []

for email in emails:
    if emailRegex.match(email):
        valid_emails.append(email)
    else:
        invalid_emails.append(email)

print("Valid Emails: ", valid_emails)