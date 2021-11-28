
import serial.tools.list_ports
import gspread

from typing import Text
import speech_recognition as sr

#--------------------------------------#
# tommy = "C2"
# smokie = "C3"
# Dhruv = "C4"
# Utkarsh = "C5"
# patrik = "C6"
#--------------------------------------#
#---------serial monitor on python-----#
ports = serial.tools.list_ports.comports()
serialInst = serial.Serial()


portList = []

for onePort in ports:
    portList.append(str(onePort))
    print(str(onePort))

print("COM3")

for x in range(0,len(portList)):             
    if portList[x].startswith("COM" + str("3")):
        portVar = "COM" + str("3")
        print(portVar[x])

serialInst.baudrate = 9600
serialInst.port = portVar
serialInst.open()
#----------end1-------------------------#
        
        
        




    
#-------------voice_rec-----------------#
while True:
    


    r = sr.Recognizer()

    

    with sr.Microphone() as  source:    
        print('Speak Anything : ')
        audio = r.listen(source)
       

        try:
            Text = r.recognize_google(audio)
            usaid= (format(Text))
            usaid = usaid.replace(" ","").lower()
            print(usaid.replace(" ","").lower())
        except:
            print('Sorry could not recognize Your voice')
            
#--------------end2--------------------------------------#        

#--------------------gspread-----------------------------#
    gc = gspread.service_account(filename=r'C:\Users\dhruv\Desktop\Project Tommy\crested-pursuit-319310-3094db7fdf6e.json')

        # #open the sheet
    sh = gc.open('Smart Thermometer').sheet1

        # sh.update(f'{usaid}',f'{temp}')

#----------------if_else_statements----------------------#

    if usaid in "s": 

        packet = serialInst.readline()
        temp1= packet.decode('utf') 
        if float(temp1) > 92 :
            print(temp1)
            sh.update('C2',f'{temp1}')
    

    elif usaid in "92":  

        packet = serialInst.readline()
        temp2=packet.decode('utf') 
        if float(temp2) > 92 :
            print(temp2)
            sh.update('C3',f'{temp2}')

    elif usaid in 'c': 

        packet = serialInst.readline()
        temp3= packet.decode('utf')
        if float(temp3) > 92 :
            print(temp3)
            sh.update('C4',f'{temp3}')

    elif usaid in 'd':

        packet = serialInst.readline()
        temp4= packet.decode('utf') 
        if float(temp4) > 92 :
            print(temp4)
            sh.update('C5',f'{temp4}')

    elif usaid in 'x':

        packet = serialInst.readline ()
        temp5= packet.decode('utf')
        if float(temp5) > 92 :
            print(temp5)
            sh.update('C6',f'{temp5}')