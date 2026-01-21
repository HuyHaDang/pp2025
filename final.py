import threading
import math
tanksList=[]
NAME_FILE="listTank.txt"
def creatInput():
  try:
    with open (NAME_FILE, "w") as f:
      
      f.write("""4
5 5 5 20
3 8 9 15
10 20 9 45
20 10 30 30 """)
  except Exception as e:
         print(f"decompression failed: {e}")

def input_hanle():
  try:
    with open(NAME_FILE, "r") as f:
      numberofTanks=f.readline()
      while True:
        line=f.readline()
        if not line:
          break
        attributes=line.strip().split(" ")
        tanksList.append(Tank(attributes[0].strip(),attributes[1].strip(),attributes[2].strip(),attributes[3].strip()))
  except Exception as e:
    print("error")
      

class Tank():
  def __init__(self, HP, Damage, Armor, Price):
    self.__HP=HP
    self.__Damage=Damage
    self.__Armor=Armor
    self.__Price=Price

  def getHP(self):
    return self.__HP
  
  def getDamage(self):
    return self.__Damage
  
  def getArmor(self):
    return self.__Armor
  
  def getPrice(self):
    return self.__Price
  
  def setPrice(self, Price):
    self.__Price=Price

  def setHP(self, HP):
    self.__HP=HP

  def setArmor(self, Armor):
    self.__Armor=Armor
    
  def setDamage(self, Damage):
    self.__Damage=Damage 

  def display(self):
    print(f"HP: {self.__HP}, Armor: {self.__Armor}, Damage: {self.__Damage}, Price: {self.__Price}, Strength: {self.compute_strength()}")

  def compute_strength(self):
    val=pow(int(self.__HP),2)+pow(int(self.__Damage),2)+pow(int(self.__Armor),2)
    return round(math.sqrt(val),2)


def solve_task1():
  list=[]
  budget=75

  tankListTask1=[]
  # tankListTask1.extend(tanksList)
  # tankListTask1.sort(key=lambda x: x.getPrice(), reverse=False)
  tankListTask1 = sorted(enumerate(tanksList, start=1), key=lambda x:x[1].getPrice(), reverse=False)
  # for tank in tankListTask1:
  #   tank.display()

  
  for index, tank in (tankListTask1):
    # tank.display()
    price = int(tank.getPrice())
    # budget=budget-int(tank.getPrice())
    if budget >= price:
            budget = budget - price
            list.append(index)
    if budget < 0:
      break
  print(list)

  try:
     with open("output.txt", "a") as f:
        f.write(f"{list} \n")
  except Exception as error:
     print("error")

def solve_task2():
  list=[]
  budget=75

  tankListTask2=[]
  # tankListTask1.extend(tanksList)
  # tankListTask1.sort(key=lambda x: x.getPrice(), reverse=False)
  tankListTask2 = sorted(enumerate(tanksList, start=1), key=lambda x:x[1].compute_strength(), reverse=True)
  # for tank in tankListTask1:
  #   tank.display()

  list.append(tankListTask2[0][0])
  # for index, tank in (tankListTask2):
  #   # tank.display()
  #   price = int(tank.getPrice())
  #   # budget=budget-int(tank.getPrice())
  #   if budget >= price:
  #           budget = budget - price
  #           list.append(index+1)
  #   if budget < 0:
  #     break
  print(list)
  
  try:
     with open("output.txt", "a") as f:
        f.write(f"{list} \n")
  except Exception as error:
     print("error")

def threadingg():
    t=threading.Thread(target=solve_task1)
    t.start()
    t.join()
    l=threading.Thread(target=solve_task2)
    l.start()
    l.join()

def main():
  creatInput()
  # tank1=Tank(100,80, 100, 999)
  # tank1.display()
  # print(tank1.compute_strength())
  input_hanle()
  for tank in tanksList:
    tank.display()
  print("\n")
  # solve_task1()
  # solve_task2()
  threadingg()

main()