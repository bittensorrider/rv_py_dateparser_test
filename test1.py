import dateparser

dd = dateparser.parse('Fri, 12 Dec 2014 10:55:50')
print(type(dd))
print(dd)

# dd = dateparser.parse('in the past 24 hours')
# dd = dateparser.parse('past 24 hours')
# dd = dateparser.parse('today')
# dd = dateparser.parse('3 days ago')
# dd = dateparser.parse('last week')
dd = dateparser.parse('5 PM yesterday')
print(dd)

