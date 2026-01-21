import threading

class Character():
  def __init__(self, name, level, health):
    self._name=name
    self._level=float(level)
    self._health=float(health)

class PlayerCharacter(Character):
  def __init__(self,name, level, health, inventory):
    super().__init__(name, level, health)
    self._inventory=inventory

  def __str__(self):
    return f"NAME: {self._name}, LEVEL: {self._level}, HEALTH: {self._health}, INVENTORY: {self._inventory}"
  
  def save(self,filename):
    try:
      with open (filename, "w") as f:
        f.write(f"""{self._name}
{self._level}
{self._health}
{self._inventory}\n""")
    except Exception as e:
      print("error")
  
  def save_in_background(self,filename):
    t=threading.Thread(target=self.save, args=(filename,))
    t.start()
    
  
def main():
  # Character1=Character("Stone Giant", 1, 780)
  playerCharacter1=PlayerCharacter("Stone Giant", 1, 780,55)
  playerCharacter1.save_in_background("player.txt")
  print(playerCharacter1)



main()