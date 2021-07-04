import os, sys, platform

# requires: pip3 install requests

# ----------------Init Phase----------------#

# creates directories for storing files
try:
    os.mkdir('.bank')
except:
    pass
try:
    os.mkdir('.temp')
except:
    pass
try:
    os.mkdir('.desktop')
except:
    pass

version = '1.1.0'


# ----------------Defining Phase----------------#

# just clears the terminal, compatible with every os (hopefully)
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

# banking
# saves a string to a bank
def sbank(string, id):
    try:
        open('.bank/' + str(int(id)), "x")
    except:
        pass
    pbsbank = open('.bank/' + str(int(id)), "w")
    pbsbank.write(string)
    pbsbank.close()

# appends to a bank
def abank(string, id):
    try:
        open('.bank/' + str(id), "x")
    except:
        pass
    pbabank = open('.bank/' + str(int(id)), "a")
    pbabank.write(string)
    pbabank.close()

# deletes a bank
def dbank(id):
    os.remove('.bank/' + str(int(id)))

# reads from a bank and returns it
def rbank(id):
    pbrbank = open('.bank/' + str(int(id)), "r")
    retnum = pbrbank.read()
    return retnum

# reads up to a certain character in the bank
def rcbank(character, id):
    pbrbank = open('.bank/' + str(int(id)), "r")
    retnum = pbrbank.readline(int(character))
    return retnum

# reads up to a certain line in the bank
def rlbank(line, id):
    pbrbank = open('.bank/' + str(int(id)), "r")
    retnum = pbrbank.readlines(int(line))
    return retnum

# formats a string using a file and returns it
def format(string):
    format = open('.temp/format', 'w')
    format.write(string)
    format.close()
    format = open('.temp/format', 'r')
    formatstring = format.read()
    format.close()
    return formatstring

# returns the version of pybitz
def getversion():
    return version

# runs the file specified
def runfile(file):
    exec(open(file).read())