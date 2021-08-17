#Looks for all unique words in a file and saves it to a list.

def uniqueWords():
    fname = input("Enter file name: ")
    try: fh=open(fname)
    except: fh=open('romeo.txt')
    lst = list()
    for line in fh:
        words=line.rstrip().split()
    
        for i in words:
            if i in lst:
                continue
            else:
                lst.append(i)

    lst.sort()
    return lst          
    
print(uniqueWords())
