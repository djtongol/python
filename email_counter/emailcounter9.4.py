#extracts all email to a file, extract all emails receive and put it in a dictionary
#the out put of the program shows a sorted dictionary based on the frequency of emails received.

def Dictionary():
    fname = input("Enter file name: ")
    if len(fname) < 1 : fname = "mbox-short.txt"

    fh = open(fname)
    list= []
    dict= {}
    sortedDict={}

    for line in fh:
        if line.startswith('From:'):
            words=line.rstrip().split()
            list.append(words[1])

    for count in list:
        dict[count]=dict.get(count,0)+1
        

    sortedDict={k:v for k,v in sorted(dict.items(), key=lambda item: item[1], reverse= True)}
    return sortedDict


print('The frequency of emails receive based on where it came from \n', Dictionary())

