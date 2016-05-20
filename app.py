import socket,sys

# FLAMES PART
def getFlamesCount(name1, name2):
  return len(set(name1) ^ set(name2))

def getFlames(name1, name2):
  flamesList = ['f','l','a','m','e','s']
  count = getFlamesCount(name1, name2)
  print count
  counter = 1
  pointer = 0
  while(len(flamesList) != 1):
    if(counter%count == 0 ):
      flamesList.pop(pointer%len(flamesList))
      pointer = pointer%(len(flamesList)+1)
      counter=1
    else:
      counter+=1
      pointer+=1
  return ''.join(flamesList)

# TRUE LOVE PART
def getTrueLove(name1, name2): #HAHA ULOL GAGO 
  true = ['t','r','u','e']
  love =['l','o','v','e']
  trueSum = getRepetitions(true, name1.lower(),name2.lower())
  loveSum = getRepetitions(love, name1.lower(),name2.lower())
  strTrueSum = str(trueSum)
  strLoveSum = str(loveSum)
  strTrueLove = strTrueSum+strLoveSum
  trueLove = int(strTrueLove)
  return trueLove

def getRepetitions(arr,name1, name2):
  sum = 0
  for i in range(len(arr)):
    sum += name1.count(arr[i])
    sum += name2.count(arr[i])
  return sum


# Ma-socket na po, tama na

print "enter 1 - flames , 2 - true love"
status = input()

funcToBeUsed = None

if status == 1:
  funcToBeUsed = getFlames
elif status == 2:
  funcToBeUsed = getTrueLove

host = ''
port = 5000

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((host,port))
s.listen(5)

while True:
  client, address = s.accept()
  data = client.recv(1028)
  if data:
    data = data.split(',')
    name1 = data[0]
    name2 = data[1]
    info = funcToBeUsed(name1, name2)
    client.send(info)