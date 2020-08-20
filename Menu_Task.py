import pyttsx3
import os
import datetime

pyttsx3.speak('Hello I am Sai, the chitti robo')
pyttsx3.speak('Please let me know your good name')

val = input("Enter your Name: ") 
pyttsx3.speak(f'Hello "{val}" ') 

x= datetime.datetime.now()
hour = int(x.strftime("%H"))
if(hour<12):
	greeting = "Good Morning"
elif(hour<16):
	greeting = "Good afternoon"
else:
	greeting = "Good Evening"
pyttsx3.speak(greeting + "Nice to meet you")
print()

while True:
	pyttsx3.speak("Enter your choice")
	print("Enter your choice:", end ='')
	i = 0
	x = input()
	p = x.lower()
	
	if ("not " in p) or ("don't" in p) or ("dont" in p) or ("do not" in p) or ("close" in p):
		print("Invalid selection")
		
	elif (("open" in p) or ("launch" in p) or ("start" in p) or ("initiate" in p) or ("execute" in p)):
		
		if ("chrome" in p) or ("google" in p) or ("search engine" in p): 
			print("Are you looking for any particular search:", end="")
			site = input()
			if "no" == site:
				os.system("chrome")
				pyttsx3.speak("Welcome to chrome")
			else:
				os.system(f'chrome "{site}.com"')
				print(f'chrome "{site}.com"')
				
							
		elif (("vlc" in p) or ("video lan client" in p) or ("videon lanclient" in p)):
			os.system("vlc")
			pyttsx3.speak("Welcome to VLC player")
					
		elif ("notepad" in p) or ("text editor" in p) or ("texteditor" in p):
			os.system("notepad")
			pyttsx3.speak("Welcome to Notepad")
				
		elif ("adobe" in p) or ("pdf" in p): 
			os.system("AcroRd32")
			pyttsx3.speak("Welcome to Adobe PDF")
				
		elif ("msword" in p) or ("word" in p) or ("document" in p): 
			os.system("WINWORD")
			pyttsx3.speak("Welcome to MS Word")
				
		elif ("git" in p) or ("git gui" in p) or ("git-gui" in p) or ("gitgui" in p): 
			os.system("git-gui")
			pyttsx3.speak("Welcome to GIT")
				
		elif ("power point" in p) or ("powerpoint" in p) or ("presentation" in p) or ("ppt" in p):
			os.system("POWERPNT")
			pyttsx3.speak("Welcome to Powerpoint")
				
		elif ("outlook" in p) or ("mail" in p): 
			os.system("OUTLOOK")
			pyttsx3.speak("Welcome to Outlook")
				
		elif ("onenote" in p) or ("one note" in p): 
			os.system("ONENOTE")
			pyttsx3.speak("Welcome to Onenote")
					
		elif ("excel" in p) or ("msexcel" in p): 
			os.system("EXCEL")
			pyttsx3.speak("Welcome to MS EXCEL")
					
		elif ("putty" in p) or ("multiputty" in p) or ("multi putty" in p):
			os.system("mtputty")
			pyttsx3.speak("Welcome to Multiputty")
					
		elif ("paint" in p) or ("picture" in p) or ("drawing" in p):
			os.system("mspaint")
			pyttsx3.speak("Welcome to Paint")
					
		elif ("calc" in p) or ("calculator" in p):
			os.system("calc")
			pyttsx3.speak("Welcome to Calculator")
				
		else:
			print("Enter a valid Software to open")
				
	elif ("exit" in p) or ("leave" in p) or ("close" in p):
		pyttsx3.speak("Thank you, hope i had served the purpose")
		print("Thank you!")
		break
	else:
		print("Enter a valid Software to open")

