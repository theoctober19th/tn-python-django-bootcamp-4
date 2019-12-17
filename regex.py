import re

pattern = r'\w+@\w+\.\w+'

sequence = 'gsdfsdfdsfsadfs aashish@gmail.com asdgkjadslkgjagrlkjfkljsdkjd kritika@gmail.com'

print(re.findall(pattern, sequence))