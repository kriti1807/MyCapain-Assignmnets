x= input("Enter string= ")
def most_frequent(string):
    d = dict()
    for n in string:
        if n not in d:
            d[n] = 1
        else:
            d[n] += 1
    return d

print (most_frequent(x))
