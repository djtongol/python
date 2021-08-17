#Extracts email from a file given, the email garnered are saved to a list
#the list is counted and presented when the code is being ram


def email():
    fname = input("Enter file name: ")
    if len(fname) < 1 : fname = "mbox-short.txt"

    fh = open(fname)
    mail = list()

    for line in fh:
        if line.startswith('From:'):
            words=line.rstrip().split()
            mail.append(words[1])
    
    return mail

print(f'There are {len(email())} emails receive, these are from \n',email() )
#print("There were", count, "lines in the file with From as the first word")


