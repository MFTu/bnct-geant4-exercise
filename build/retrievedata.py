
#read raw file and retrieve and print data to another file  


fraw = open("proton500MeVBeamOn1e4_0517_2020.out", "r")
fdata = open("proton500MeVBeamOn1e4data_0517_2020.txt", "a")

while True:  
  oneline = fraw.readline()
#  if not oneline:
#      break
  print(oneline)
#  brokenline = []
  brokenline = oneline.split()
#  checkword0, checkword1, checkword2, checkword3, checkword4, checkword5, checkword6, checkword7, checkword8, checkword9 = oneline.split() 
  print(brokenline)
  print(range(len(brokenline)))

  print(brokenline[0:1])
  checkword0 = brokenline[0:1]
  print(checkword0)

  print(brokenline[1:2])
  particle = brokenline[1:2]
  print(particle)

  print(brokenline[2:3])
  energy = brokenline[2:3]
  print(energy)

  for x in range(len(brokenline)): 
    print(x, brokenline[x])
#    checkword = brokenline[0]
  if ((checkword0 == ['From_steppingaction']) and (particle == ['neutron'])):
      fdata.write(oneline)
  if not oneline:
      break
  


#for x in f:
#  print(x) 

fraw.close()
fdata.close()
