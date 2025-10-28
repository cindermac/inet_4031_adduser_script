INET4031 Add Users Script and User List
Program Description
The program used in this repository is called create-users.py It was created to help automate adding users and their info into a Linux system. This is usually done one by one using commands such as adduser,
passwd, group, or a combination of these commands together. This python file does these same commands but makes things more easy and automated by using the os.system() function.
This can be used to help people who need to add a ton of different people to a system, and all that is needed is an input file. It can also help with commands that need sudo before every statement.

Program User Operation
This program was built to read and add user information from an input file and automatically add and set the user information
to the provided groups. User input can be provided by using the < symbol to run the program, and it can either
be run normally or tested by doing a dry run. Doing a dry run is important to make sure no errors are in the 
code so that nothing is put through the os.command incorrectly. 

Input File Format
Every new line in the given input file represents a new user account and it must have five sections separated
by colons. They must be in this exact order:
username:password:lastname:firstname:group, group

Username is the username for said user.
Password is the password being assigned to the user.
Lastname is the user's last name.
Firstname is the user's first name.
Group is whichever group the user is being assigned to. Users can be assigned to multiple groups, so long as it
is separated by commas.

Users must be added in this specific way otherwise it will not work. There are some things that can be added
that can change the way a user is or is not added.
If the line begins with a #, it is treated like a comment and ignored by the code.
If the line doesn't have exactly five fields, aka anything is missing, it will also be ignored by the code.
If the group field has a -, the user will not be assigned to any groups but can still be added.

Command Excuction
The script can be run by doing this in the terminal: ./create-users.py < createusers.input.
However, you need to make sure it is executable as you might receive a permission error doing this.
You can do this by doing chmod a+x create-users.py.
You can then run the script by doing sudo ./create-users.py < create-users.input.

"Dry Run"
A dry run can be done to test the script and make sure nothing is changed in the system
if you want to make sure there are no errors with the input data.
If you want to do a "dry run" of this script, all you need to do is comment out all of the lines that say
os.system(cmd). There should be three of them in create-users.py. The script can then be run by doing
./create-users.py < create-users.input, and it should print out everything needed to ensure things
are working right. Once everything looks good, you can uncomment the previous lines and run it normally.
