import math
import sys
import time
import csv

def timestamp():
   now = time.time()
   localtime = time.localtime(now)
   milliseconds = '%03d' % int((now - int(now)) * 1000)
   return time.strftime('%Y%m%d%H%M%S', localtime) + milliseconds

def Get_Mag_Data() :
   #Create lists of zeros for the data.
   Bx = [0]
   By = [0]
   Bz = [0]
   seconds  = [0]

   #Now fill the lists with zeros.  I want to overwrite the zeros with actual data since there is no guarantee
   #that I will start the program at the first second of the hour but I want to have my files be 3600 lines long.
   for i in range(1,3600) :
      Bx.append(0)
      By.append(0)
      Bz.append(0)
      seconds.append(0)

   #Get the time and date.
   date_time = timestamp()
   year = date_time[0:4]
   month = date_time[4:6]
   day = date_time[6:8]
   hour = date_time[8:10]
   minutes = date_time[10:12]
   sec = int(date_time[12:14])
   msec = float(date_time[14:])

   #Create a dictionary.
   data = {'year' : year, 'month' : month, 'day' : day, 'hour' : hour, 'minutes' : minutes,
           'seconds' : seconds, 'B_x' : Bx, 'B_y' : By, 'B_z' : Bz}

   #Open the serial port.
   #ser = serial.Serial(baudrate=38400,port=com1)
   #ser.open()

   #initialize some counters.
   t = 60*int(minutes) + sec
   counter = 0
   t10 = t + 10

   #Loop until the end of the hour.
#   while (t < 3600) :
   while (t < t10) :
       #Write to the serial port
#       ser.write('d' + '\r\n')

       #Read from the serial port
#       data = ser.readline(size=None,eol='\r\n')

       #For now create fake data.
       B_x = 1
       B_y = 2
       B_z = 3
               
       #Delay for 1 second
       time.sleep(1)

       #Increment the while loop counter.
       if (counter != 0) :
          #Put the data into the array.
          Bx[t] = B_x
          By[t] = B_y
          Bz[t] = B_z
          seconds[t] = t
          print(sec,t,Bx[t],By[t],Bz[t],seconds[t])
          t += 1
       else :
          counter = 1


   #Close the serial port.
#   ser.close()
   #Return the dictionary
   return data


#Create an infinite loop so as to continually get data.
j = 1
while (j < 10) :
   Mag_data = Get_Mag_Data()
   #Write out the data

   #Create a file name.
   filename = 'Mag' + Mag_data['year'] + Mag_data['month'] + Mag_data['day'] + Mag_data['hour'] + '.txt'
      
   #Open the file in write mode.
   f = open(filename, 'w')

   #Write to the file.
   try :
      writer = csv.writer(f)
      writer.writerow(('Time', 'B_x','B_y','B_z'))
      for i in range(3600) :
         date_time = int(Mag_data['year'] + Mag_data['month'] + Mag_data['day'] + Mag_data['hour'] + Mag_data['minutes']
                         + str(Mag_data['seconds'][i]))
         writer.writerow((date_time,Mag_data['B_x'][i],Mag_data['B_y'][i],Mag_data['B_z'][i]))
   finally:
      f.close()


    


    

    
