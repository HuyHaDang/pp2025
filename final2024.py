class Reservation():
  def __init__(self, guest, paid, room):
    self._guest=guest
    self._paid=paid
    self._room=room

  def greet(self):
    print(f"gud morning {self._guest}, your room is {self._room}")


class LongReservation(Reservation):
  def __init__(self, guest, paid, room, months):
    super().__init__(guest, paid , room)
    self._months=months

  def greet(self):
      print(f"gud morning {self._guest}, your room is {self._room} in {self._months} months")


  def save(self,filename):
    try: 
      with open(filename, "w") as f:
        f.write(f"""{self._guest}
{self._paid}
{self._room}
{self._months}""")
    except Exception as e:
      print("error")

def main():
  guest1=Reservation("Emmanuel Macrion", True, "R408")


main()
