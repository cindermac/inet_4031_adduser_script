#!/usr/bin/python3

# INET4031
# Makayla Schneider
# 10/27/25
# 10/27/25

#Import OS gives python the ability to use OS commands. Import re is used for regular expressions.
#Import sys is used to read input from standard input or stdin.
import os
import re
import sys


def main():
    for line in sys.stdin:

        #The regular expression is checking if the line starts with a '#'. Then it decides to ignore the line if it does.
        #This is so comments can be used in the inputs.
        match = re.match("^#",line)

        #This code separates the input using the ':' as a parameter. Essentially splitting the users into readable parts of info.
        fields = line.strip().split(':')

        #This IF statement ignores lines that start with '#' or are not exactly 5 length. Otherwise, the code after will run.
        #If uses the two previous lines of code to help determine if the user input is valid or not. It is important that these are before and not after.
        if match or len(fields) != 5:
            continue

        #These lines assign the inputs and their info into what aligns with said info.
        #This is formatted similarly to how it is stored in the passwd file.
        username = fields[0]
        password = fields[1]
        gecos = "%s %s,,," % (fields[3],fields[2])

        #Splits the last field input, groups, by commas. This is for users that are in multiple groups.
        groups = fields[4].split(',')

        #Prints a statement to ensure a new user is being created with the current username.
        print("==> Creating account for %s..." % (username))
        #This line helps actually create the user account with linux commands. cmd is used for the full shell command.
        cmd = "/usr/sbin/adduser --disabled-password --gecos '%s' %s" % (gecos,username)

        print(cmd)
        os.system(cmd)

        #Prints a statement to ensure a new user's password is being created with the current username.
        print("==> Setting the password for %s..." % (username))
        #This line helps set the user's password also with linux commands. It specifically uses the password command to help.
        #The cmd variable will contain something like this: /bin/echo -ne 'mypassword\nmypassword' | /usr/bin/sudo /usr/bin/passwd username
        cmd = "/bin/echo -ne '%s\n%s' | /usr/bin/sudo /usr/bin/passwd %s" % (password,password,username)

        print(cmd)
        os.system(cmd)

        for group in groups:
            #The IF statement is looking for if any of the fields in create-user.input are blank, which is told by a "-".
            #If group !='-', then the code below is going to execute and print and assign user and group.
            if group != '-':
                print("==> Assigning %s to the %s group..." % (username,group))
                cmd = "/usr/sbin/adduser %s %s" % (username,group)
                print(cmd)
                os.system(cmd)

if __name__ == '__main__':
    main()
