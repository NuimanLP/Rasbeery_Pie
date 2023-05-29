import random
def random_temperature():
  t = random.uniform(25,55)
  t = round(t,2)
  return t
def random_humidity():
  h = random.uniform(30,55)
  h = round(h,2)
  return h

def random_mix():
  t = random.uniform(25,55)
  t = round(t,2)
  h = random.uniform(30,55)
  h = round(h,2)
  return(t,h)

def random_mix_dict():
  t = random.uniform(22,50)
  t = round(t,2)
  h = random.uniform(30,55)
  h = round(h,2)
  return{'tempearature':t,'humidity':h}

def check_temperature():
  #temp,humid = random_mix()
  #data = random_mix_dict()
  #temp  = data['tempearature']
  data = random_mix_dict()
  temp  = data['temperature']
  humid = data['humidity']
  print('Temperature: {}'.format(temp))
  print('Humidity: {}%'.format(humid))

check_temperature()