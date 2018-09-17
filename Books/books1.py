# @author Dawson D'almeida and Conor Gormally


import csv, sys, re


def books1():
    fileName = sys.argv[1]
    try:
        dataToDisplay = sys.argv[2]
    except IndexError:
        catchUserError()
    try:
        sortDirection = sys.argv[3]
    except IndexError:
        sortDirection = None
    titleData = []
    authorData = []
    with open(fileName, newline='') as f:
        fileReader = csv.reader(f)
        print('test')
        for row in fileReader:
            parseBookData(row, titleData, authorData)
        authorData = sortData(authorData)
        titleData = sortData(titleData)
    checkUserInput(dataToDisplay, sortDirection, titleData, authorData)

def checkUserInput(dataToDisplay, sortDirection, titleData, authorData):
    if(sortDirection == 'reverse'):
        titleData.reverse()
        authorData.reverse()
    if(dataToDisplay == 'books'):
        print(titleData)
    elif(dataToDisplay == 'authors'):
        print(authorData)
    else:
        catchUserError()

def catchUserError():
    print('Usage: \'books\' or \'authors\', sort direction is \'forward\' or \'reverse\' and is optional, file = sys.stderr')
    exit(0)

def parseBookData(titleYearAuthor, titleData, authorData):
    titleData.append(titleYearAuthor[0])
    getCorrectAuthorSyntax(titleYearAuthor, authorData)


def getCorrectAuthorSyntax(titleYearAuthor, authorData):
    justAuthorNames = re.sub(r'\([^()]*\)', '', titleYearAuthor[2])
    for authors in justAuthorNames.split('and'):
        authors = authors.strip()
        authorFirstLastName = authors.split(' ')
        lastName = authorFirstLastName[-1] + ', '
        authorFirstLastName = authorFirstLastName[0:-1]
        properNameDisplay = lastName + " ".join(str(x) for x in authorFirstLastName)
        if properNameDisplay not in authorData:
            authorData.append(properNameDisplay)

def sortData(authorOrTitle):
    return mergesortData(authorOrTitle)

def mergesortData(x):
    if len(x) == 0 or len(x) == 1:
        return x
    else:
        center = len(x)//2
        a = mergesortData(x[0:center])
        b = mergesortData(x[center:])
        return merge(a, b)

def merge(a, b):
    c = []
    while len(a) != 0 and len(b) != 0:
        if a[0] <= b[0]:
            c.append(a[0])
            a.remove(a[0])
        else:
            c.append(b[0])
            b.remove(b[0])
    if len(a) == 0:
        c += b
    elif len(b) == 0:
        c += a
    return c

books1()
