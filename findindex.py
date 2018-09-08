def findindex(findme, inthelist):
    '''returns the index of the first argument in the second argument list'''
    return [y for y, x in enumerate(inthelist) if x == findme]

# example
# findindex("name",["name","home","house"])
#findindex("1","1010101010")
