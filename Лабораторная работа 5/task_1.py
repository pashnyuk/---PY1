from pprint import pprint

dictionary = [{"bin": bin(i), "dec": i, "hex": hex(i), "oct": oct(i)} for i in range(16)]

pprint(dictionary)
