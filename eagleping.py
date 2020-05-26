from pythonping import ping
from time import sleep, localtime, strftime
import time
import sys
print("##########################")
print("........EAGLE PING........")
print("##########################")
print("  Made by: Jake Saunders  ")
print("##########################\n")

logpath = "output.txt" #Path to your desired output file. 
packettotal = 2 #Determines the amount of packets to be sent per address, per ping "round" (I recommend 2)

while True:
  try:
    pingint = int(input("Enter ping interval(seconds): ")) #Takes user input for the amount of time between rounds of pings
    if pingint <= 0: 
      print("Please enter a positive integer.") #Verifies that user input is not a negative number.
    else:
      break #Breaks the loop, input has been completely verifed and saved to the pingint variable. 
  except(ValueError): 
    print("Please enter a positive integer.") #Verifies that user input doesn't include any non-numeric characters

while True:
  try:
    ipct = int(input("\nEnter amount of addresses: ")) #Takes user input for the desired amount of addresses to be pinged.
    if ipct <= 0:
      print("Please enter a positive integer.") #Verifies that user input is not a negative number.
    else:
      break #Breaks the loop, input has been completely verifed and saved to the ipct variable.
  except(ValueError): 
    print("Please enter a positive integer.") #Verifies that user input doesn't include any non-numeric characters

iplst = []
for i in range(0,ipct):
  z = input("Address {}: ".format(str(i+1))) #Takes user input for the ip/domain to be pinged.
  iplst.append(z) #Appends above ip/domain to iplst

log = open(logpath, 'a+') #Opens/Creates temp.txt in append mode.
roundcounter = 0
print("")
while True:
  try:
    for q in range(len(iplst)):
      response = ping(iplst[q],verbose=False,count=packettotal) #Iterates though the iplst list, pinging each address x amount of times (determined by packtettotal), and displays output to terminal.
      if "Reply from" not in str(response._responses):
        for i in range(packettotal):
          timestamp = strftime("%d %b %Y %H:%M:%S", localtime()) #Creates the timestamp used in the log
          log.write("{}   {}   {}\n".format(timestamp, iplst[q], response._responses[q]))
    time.sleep(pingint-.5) #Pauses the program for x amount of seconds (determined by the user input from pingint) between rounds of pings.
    roundcounter += 1
    print("Round {} complete".format(roundcounter))
  except KeyboardInterrupt:
    break #Makes the program quit once the user hits the proper break key
print("\nCompleted {} rounds".format(roundcounter))
print("Quitting program...\n")
sys.exit()

#infinate While Loops
#Commenting
#Logging technique
