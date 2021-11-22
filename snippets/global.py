print()

name = 'abc'.upper()

def get_name():
    name = 'def'.upper()
    print(f"inside: {name}")

get_name()
print(f"Outside: {name}")

print()

def get_name():
    global name
    name = 'def'.upper()
    print(f"inside: {name}")


get_name()
print(f"Outside: {name}")

def get_name():
    global name
    #but
    #name: str = 'gHi'.upper()
    # SyntaxError: annotated name 'name' can't be global

    #and
    #global name = 'gHi'.upper()
    #            ^
    #SyntaxError: invalid syntax

    print(f"inside: {name}")

get_name()
print(f"Outside: {name}")
