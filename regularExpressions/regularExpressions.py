import re

text = "I am HARINDER SINGH DHANI, my phone number is 647-203-0037, earlier my phone number was: 647-203-2237"

#pattern = re.compile(r'(\d{3})-(\d{3})-(\d{4})')
pattern = r'(\d{3})-(\d{3})-(\d{4})'
# it will only return the first occurrence
match  = re.search(pattern, text)
print(match.group())
print(match.group(1))
print(match.groups())
print(match.span())
print(match.start())
print(match.end())

# it get all the occurrence use below method
matches = re.finditer(pattern, text)
count = 0
for match in matches:
    count += 1
    print(f'my match number {count} is:')
    print(match.group())
    print(match.group(1))
    print(match.groups())
    print(match.span())
    print(match.start())
    print(match.end())

#another way of doing this
count = 0
for match in re.finditer(pattern, text):
    count += 1
    print(f'my match number {count} is:')
    print(match.group())
    print(match.group(1))
    print(match.groups())
    print(match.span())
    print(match.start())
    print(match.end())