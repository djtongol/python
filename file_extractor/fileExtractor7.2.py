# Reads, extract, and compute data from a file

def confidenceAverage():                                        #gets user input
    fname = input("Enter file name: ")
    try:fh = open(fname)
    except:fh = open('mbox-short.txt')
    count=0
    digits=[]

    for line in fh:                                              #iterates overall the lines in the file
        if not line.startswith("X-DSPAM-Confidence:") : continue #filters target lines
        count=count+1                                            #counts all the targeted lines
        zeros=line.find("0")                                     #finds the index of the digits
        catch= float(line[zeros:zeros+6])                        #catches the number
        digits.append(catch)                                     #appends the number to a list
        

    return sum(digits)/count

print('The aggreagated average of the confidence is ', confidenceAverage())