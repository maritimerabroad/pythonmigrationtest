from os import system, name
from time import sleep
import classesfile

def run(): #simulate running the migration.
	sleep(60)

def clear(): #clear the terminal window
    # for windows 
    if name == 'nt': 
        _ = system('cls') 
    # for mac and linux(here, os.name is 'posix') 
    else: 
        _ = system('clear') 
        
def mainchoices(): #User interaction logic here
	while True:
		choice=input("\n(L)ist mountpoints \n(C)redentials \n(A)dd devices  \n(M)igrate devices \n(Q)uit\n").lower()
		
		if choice == "l":
			for info in classesfile.Mountpoint.mountinfo:
				size = info.get('size')
				point = info.get('mountpoint')
				print("Mountpoint: ", point,"Size: ", size, "bytes")
		elif choice == "m":
			source = input("What is the source volume?")
			target = input("What is the target volume?")
			print("You\'ve chosen ",source,"as your source volume and ", target, "as your target volume\n")
			yesno = input("Is this correct? Y/N\n").lower()
			if yesno == "y":
				print("Migrating data......\n")
				run()
				print("Verifying data integrity.......\n")
				run()
				print("Data successfully migrated!\n")
				sleep(0.5)
			else:
				pass
		elif choice == "c":
			credchoice = input("\n(V)iew your credentials \n(D)elete saved credentials \n(E)nter new credentials?\n").lower()
			if credchoice == "v":
				print("Your Username is:", classesfile.MigrationTarget.cloudusername, "\nYour password is:", classesfile.MigrationTarget.cloudpassword, "\nAnd your domain is:", classesfile.MigrationTarget.clouddomain,"\n")
			elif credchoice == "d":
				classesfile.MigrationTarget.clouddomain = ''
				classesfile.MigrationTarget.cloudpassword = ''
				classesfile.MigrationTarget.cloudusername = ''
				print("All credentials have been deleted\n")
			elif credchoice == "e":
				newusername = input("Enter your username: \n")
				classesfile.MigrationTarget.cloudusername = newusername
				newpassword = input("Enter your password: \n")
				classesfile.MigrationTarget.cloudpassword = newpassword
				newdomain = input("Enter the domain name: \n")
				classesfile.MigrationTarget.clouddomain = newdomain
			else:
				pass
		elif choice == "a":
			addchoice = input("\n(L)ocal device \n(C)loud device\n").lower()
			if addchoice == "l":
				mp = input("\nEnter mountpoint: \n")
				lc = input("Location or address of device\n")
				mpsize = input("Size of device being added in bytes\n")
				classesfile.Mountpoint.mountinfo.append({'mountpoint': mp, 'size': mpsize})
			elif addchoice == "c":
				mp = input("\nEnter mountpoint: \n")
				lc = input("Location or address of device\n")
				mpsize = input("Size of device being addedin bytes\n")
				classesfile.Mountpoint.mountinfo.append({'mountpoint': mp, 'size': mpsize})
		elif choice == "q":
			print("\nThank you for using Booth Migration Software... Have a nice day!\n")
			return
		else:
			pass
