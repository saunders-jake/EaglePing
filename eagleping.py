from pythonping import ping
import time, logging, sys
print("##########################")
print("........EAGLE PING........")
print("##########################")
print("  Made by: Jake Saunders  ")


packettotal = 3 #Determines the amount of packets to be sent per address, per ping "round"

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
    ipct = int(input("Enter amount of addresses: ")) #Takes user input for the desired amount of addresses to be pinged.
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

while True:
  try:
    for i in range(len(iplst)):
      print(ping(iplst[i],verbose=True,count=packettotal)) #Iterates though the iplst list, pinging each address x amount of times (determined by the packtettoal), and displays output to terminal
    time.sleep(pingint - .5) #Pauses the program for x amount of seconds (determined by the user input from pingint) between rounds of pings.
  except KeyboardInterrupt:
    break #Makes the program quit once the user hits the proper break key
print("Quitting program...")
sys.exit()
