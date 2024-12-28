import os
import time


print("Run the Code in the folder where you want your hugo site")
print()

def process():
	selector = input("""What do you want to do?
1) Push existing hugo repo to github
2) create a new Hugo Site

>> """)
	if selector == "2":
		print()
		location = input(f"Enter path to the Main Dir(Desktop, Documents, etc.): ")
		site = input("Enter the name of your hugo site: ")
		gitlink = input("Enter your github repo link: ")
		print()
		os.chdir(f"{location}")
		os.system(f"hugo new site {site}")
		os.chdir(f"{site}")
		os.system("git init")
		os.system("hugo")
		os.system(f"git remote add origin {gitlink}")
		os.system("git status")
		os.system("git add --all")
		commit_message = input("Enter a commit message: ")
		os.system(f"git commit -m '{commit_message}'")
		os.system("git push -u origin master")
	elif selector == "1":
		print()
		location = input(f"Enter path to the Main Dir(Desktop, Documents, etc.): ")
		site = input("Enter the name of your hugo site: ")
		gitlink = input("Enter your github repo link: ")
		print()
		os.chdir(f"{location}")
		os.chdir(f"{site}")
		os.system("git init")
		os.system("hugo")
		os.system(f"git remote add origin {gitlink}")
		os.system("git status")
		os.system("git add --all")
		commit_message = input("Enter a commit message: ")
		os.system(f"git commit -m '{commit_message}'")
		os.system("git push -u origin master")
	else:
		print("Invalid Command")
		

process()



