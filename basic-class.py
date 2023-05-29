import random
import csv

def writetocsv(data,filename='data'): 
  #data = [25.66,50.66] # data need to be list /..
  with open('{}.csv'.format(filename),'a',newline='',encoding='utf-8') as file: # 'a' --> append  '' --> countinue the line
    fw = csv.writer(file) # fw = file writer
    fw.writerow(data)

class Sensor:
  """ Sensor Class for IoT """
  def __init__(self,name='CF-101'):
    self.name = name
    self.type = 'DHT22'

  def get_temp_humid(self):
    t = random.uniform(25,55)
    t = round(t,2)
    h = random.uniform(30,55)
    h = round(h,2)
    return(t,h)

  def show_result(self, writecsv=False):
    temp, humid = self.get_temp_humid()
    print('Tempearature: {:.2f} ° C \n Humidity: {:.2f}% '.format(temp,humid)) #n คือ newline enter บรรทัดใหม่
      
    if writecsv == True:
      data = [temp,humid]
      writetocsv(data, self.name)


sensor1 = Sensor('A-101')
sensor1.show_result(writecsv=True)

sensor2 = Sensor('B-101')
sensor2.show_result(writecsv=True)

sensor3 = Sensor('C-101')
sensor3.show_result(writecsv=True)
