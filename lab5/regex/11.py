import re
def program(string):
    return re.sub("[a]", "b", string)
print(program("madina"))