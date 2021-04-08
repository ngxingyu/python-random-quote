import random
def primary():
  with open('quotes.txt','a') as f:
    f.write('Blah')
    f.write('This is not a line')

  f = open("quotes.txt")
  quotes = f.readlines()
  f.close()

  last = 13
  rnd = lambda x:random.randint(x, last)
  a= rnd(0)
  print('\n'.join(quotes[a:rnd(a)]))

if __name__== "__main__":
  primary()
