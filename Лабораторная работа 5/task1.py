# TODO решить с помощью list comprehension и распечатать
import pprint
def over_list(i):
    return [{"bin": bin(i),"dec" :i , "hex":hex(i),"oct":oct(i)} for i in range(0, i+1)]
pprint.pprint(over_list(15))
