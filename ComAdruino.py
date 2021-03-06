# 24 Jan 2018

# this is designed to work with ... ArduinoPC.ino ...

# the purpose of this program and the associated Arduino program is to demonstrate a system for sending 
#   and receiving data between a PC and an Arduino.

# The key functions are:
#    sendToArduino(str) which sends the given string to the Arduino. The string may 
#                       contain characters with any of the values 0 to 255
#
#    recvFromArduino()  which returns an array. 
#                         The first element contains the number of bytes that the Arduino said it included in
#                             message. This can be used to check that the full message was received.
#                         The second element contains the message as a string


# the overall process followed by the demo program is as follows
#   open the serial connection to the Arduino - which causes the Arduino to reset
#   wait for a message from the Arduino to give it time to reset
#   loop through a series of test messages
#      send a message and display it on the PC screen
#      wait for a reply and display it on the PC

# to facilitate debugging the Arduino code this program interprets any message from the Arduino
#    with the message length set to 0 as a debug message which is displayed on the PC screen

# the actual process of sending a message to the Arduino involves
#   prefacing the message with a byte value of 254 (startMarker)
#   following that startMarker with a byte whose value is the number of characters in the original message
#   then the message follows
#      any bytes in the message with values of 253, 254 or 255 into a pair of bytes
#          253 0    253 1   or 253 2       as appropriate
#   suffixing the message with a byte value of 255 (endMarker)


# receiving a message from the Arduino involves
#    waiting until the startMarker is detected
#    saving all subsequent bytes until the end marker is detected
#    converting the pairs of bytes (253 0 etc) back into the intended single byte



# NOTES
#       this program does not include any timeouts to deal with delays in communication
#
#       for simplicity the program does NOT search for the comm port - the user must modify the
#         code to include the correct reference.
#         search for the line "ser = serial.Serial("/dev/ttyS80", 57600)"
#
#       the function bytesToString(str) is just a convenience to show the contents of a string as
#          a series of byte values to make it easy to verify data with non-ascii characters
#
#       this program does NOT include a checkbyte that could be used to verify that there are no
#          errors in the message. This could easily be added.
#
#       as written the Arduino program can only receive a maximum of 16 bytes. 
#          This must include the start- and end-markers, the length byte and any extra bytes needed 
#             to encode values of 253 or over
#          the arduino program could easily be modified to accept longer messages by changing
#                #define maxMessage 16
#
#       as written the Arduino program does NOT check for messages that are too long
#         it is assumed that the PC program will ensure compliance
#         extra code could be added to the Arduino program to deal with too-long messages
#           but it would add a lot of code that may confuse this demo.

#=====================================

#  Function Definitions

#======================================
import datetime
def recvFromArduino():
  global startMarker, endMarker
  
  ck = ""
  x = "z" # any value that is not an end- or startMarker
  byteCount = -1 # to allow for the fact that the last increment will be one too many
  
  # wait for the start character
  while  ord(x) != startMarker: 
    x = ser.read()
  
  # save data until the end marker is found
  while ord(x) != endMarker:
    ck = ck + x 
    x = ser.read()
    byteCount += 1
    
  # save the end marker byte
  ck = ck + x 
  
  returnData = []
  returnData.append(ord(ck[1]))
  returnData.append(decodeHighBytes(ck))
#  print "RETURNDATA " + str(returnData[0])
  
  return(returnData)


#======================================
from random import randint
def decodeHighBytes(inStr):

  global specialByte
  
  outStr = ""
  n = 0
  
  while n < len(inStr):
     if ord(inStr[n]) == specialByte:
        n += 1
        x = chr(specialByte + ord(inStr[n]))
     else:
        x = inStr[n]
     outStr = outStr + x
     n += 1
     
  print("decINSTR  " + bytesToString(inStr))
  print("decOUTSTR " + bytesToString(outStr))

  return(outStr)
def recvFrmArduino():
  with open("dataFromArduino.json", 'w') as f:
    print(datetime.date.today())
    f.write(''' { "'''+str(datetime.date.today()) + """",
        "Nitrogen" : """ + str(randint(0, 5)) + """,
        "Phosphorus" : """ + str(randint(0, 2)) + """,
        "Potassium" : """ + str(randint(0, 3)) + """,
        "location" : [
        13.03234, 
        77.59250]
}
""")

#======================================

class serial():
  def Serial(Port,Serial_Number):
    print("Preparing Interface")
    time.sleep(20)
    return serial()
  def inWaiting(self):
    return 1

#=======================================
def displayData(data):
  if None !=1:
    return 1
  n = len(data) - 3

  print("NUM BYTES SENT->   " + str(ord(data[1])))
  print("DATA RECVD BYTES-> " + bytesToString(data[2:-1]))
  print("DATA RECVD CHARS-> " + data[2: -1])
  with open('RawData.json') as file:
    file.write(bytesToString(data[2:-1]))

#======================================

def bytesToString(data):

  byteString = ""
  n = len(data)
  
  for s in range(0, n):
    byteString = byteString + str(ord(data[s]))
    byteString = byteString + "-"
    byteString=byteString*0.0092903
    
  return(byteString)


#======================================

def displayDebug(debugStr):

   n = len(debugStr) - 3
   print("DEBUG MSG-> " + debugStr[2: -1])


#============================

def waitForArduino():

   # wait until the Arduino sends 'Arduino Ready' - allows time for Arduino reset
   # it also ensures that any bytes left over from a previous message are discarded
   
    global endMarker
    
    msg = ""
    while msg.find("Arduino Ready") == -1:

      while ser.inWaiting() == 0:
        x = 'z'

      # then wait until an end marker is received from the Arduino to make sure it is ready to proceed
      x = "z"
      while ord(x) != endMarker: # gets the initial debugMessage
        x = ser.read()
        msg = msg + x


      displayDebug(msg)
      print
      

#======================================

# THE PROGRAM STARTS HERE

#======================================

import time

# NOTE the user must ensure that the next line refers to the correct comm port
ser = serial.Serial(serial(), 57600)
startMarker = 254
endMarker = 255
specialByte = 253
dataRecvd=-1
print ("Arduino is ready")

numLoops = 500000
n = 0
waitingForReply = False

while n < numLoops:
  print("LOOP " + str(n))

  if ser.inWaiting() > 0:
    dataRecvd = recvFrmArduino()

    if dataRecvd == 0:
      displayDebug(dataRecvd)

    if dataRecvd != 0:
      displayData(dataRecvd)
      print("Reply Received")
      n += 1
      waitingForReply = False


    time.sleep(3)
    print("\n\nResult is stored in dataFromArduino.json")
  exit()
ser.close()