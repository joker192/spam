import os
black='\033[30m'
red='\033[31m'
green='\033[32m'
orange='\033[33m'
blue='\033[34m'
purple='\033[35m'
cyan='\033[36m'
lightgrey='\033[37m'
darkgrey='\033[90m'
lightred='\033[91m'
lightgreen='\033[92m'
yellow='\033[93m'
lightblue='\033[94m'
pink='\033[95m'
lightcyan='\033[96m'
reset='\033[0m'
a = "|"
while True:
    print(f"{yellow}================================")
    print(f"{yellow}        made by bad_boy        ")
    print(f"{yellow}  my telegram id : @Bad_boy_468")
    print(f"{yellow}================================")
    print("[1]spam")
    print(f"{orange}[2]exit")
    joker = int(input(f"{pink}[~]bad_boy==>"))
    if joker == 1:
        king = input(f"{green}Enter Your Text : ")
        kinge= int(input("Enter Your Number : "))
        print(king * kinge)
    elif joker == 2:
        os.system("clear")
        print("exiting!!")
        break
else:
    print("what? :| ")
