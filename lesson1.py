def cookies(a):
    if a <= 9:
        print("The number of cookies is: " + str(a))
    else:
        print("Too many cookies")


def stringcut(a):
    return(a[2:][:-2])

def stringexgange(a, b):
    return (b[0]+b[1]+a[2:] + " " + a[0]+a[1]+b[2:])

def stringcount(a):
    count = 0
    for str in a:
        if (len(str) >= 2) and (str[0] == str[-1]):
            count+=1
    return(count)

def stringsort(a):
    b = []
    for str in a:
        if str[0] == 'x':
            b.append(str)
    return(sorted(b))

def numberscompress(a):
    b = []
    tmp = None
    for num in a:
        if num != tmp:
            b.append(num)
            tmp = num
    return(b)

def filetodic():
    d = {}
    filename = "files/lista.txt"
    file = open(filename, "r")
    for line in file:
        d[line.split()[0]] = line.split()[1]
        # print (line.split()[0])
    print(d)

from collections import Counter
def filesort():
    filename = "files/text.txt"
    file = open(filename, "r")
    wordcount = Counter(file.read().split())
    for item in wordcount.items():
        print (item)

def filesortwithdic():
    d = {}
    filename = "files/text.txt"
    file = open(filename, "r")
    for str in file.read().split():
        if not(str in d):
            d[str] = 1
        else:
            num = d[str] + 1
            d.update({str: num})
    print(d)

#8
filesortwithdic()
#7
# filetodic()
#6
# print(numberscompress([1,2,2,3]))
#5
# print(stringsort(["xba", "aaa", "xab"]))
#4
# print(stringcount(["aaf", "aa", "gg"]))
#3
# cookies(10)
#2
# print(stringcut("1234567"))
#1
# print(stringexgange("123456", "asdfgh"))
