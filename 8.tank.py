import math
import threading

# --- Helper: Create input.txt for testing ---
def create_dummy_input():
    content = """4
5 5 5 20
3 8 9 15
10 20 9 45
20 10 30 30"""
    with open("input.txt", "w") as f:
        f.write(content)
    print("Created 'input.txt' for testing.\n")

# ==========================================
# 1. The Tank Class
# ==========================================
class Tank:
    def __init__(self, index, hp, damage, armor, price):
        self.__index = index  # To track the original line number
        self.__hp = hp
        self.__damage = damage
        self.__armor = armor
        self.__price = price

    # --- Getters ---
    def get_index(self): return self.__index
    def get_hp(self): return self.__hp
    def get_damage(self): return self.__damage
    def get_armor(self): return self.__armor
    def get_price(self): return self.__price

    # --- Setters ---
    def set_hp(self, hp): self.__hp = hp
    def set_damage(self, damage): self.__damage = damage
    def set_armor(self, armor): self.__armor = armor
    def set_price(self, price): self.__price = price

    # --- Methods ---
    def display(self):
        print(f"Tank {self.__index}: HP={self.__hp}, Dmg={self.__damage}, Arm={self.__armor}, Price={self.__price}")

    def compute_strength(self):
        # strength = sqrt(HP^2 + Damage^2 + Armor^2)
        val = self.__hp**2 + self.__damage**2 + self.__armor**2
        return math.sqrt(val)

# ==========================================
# 2. Input Handling
# ==========================================
def input_handle():
    tanks_list = []
    try:
        with open("input.txt", "r") as f:
            # Read number of tanks
            line = f.readline()
            if not line: return []
            n = int(line.strip())

            # Read each tank
            for i in range(n):
                line = f.readline()
                parts = list(map(int, line.split()))
                # parts = [HP, Damage, Armor, Price]
                # We pass 'i+1' as the index (1-based)
                t = Tank(i+1, parts[0], parts[1], parts[2], parts[3])
                tanks_list.append(t)
    except FileNotFoundError:
        print("Error: input.txt not found.")
    return tanks_list

# ==========================================
# 3. Task Logic (The Worker Functions)
# ==========================================

def solve_task1(tanks):
    """
    Task 1: Sort by Price (Ascending) to buy the MOST tanks with 75 coins.
    """
    # Create a copy so we don't mess up the list for the other thread
    local_tanks = list(tanks)
    
    # Sort by Price (Cheapest first)
    local_tanks.sort(key=lambda x: x.get_price())

    budget = 75
    bought_indices = []

    for t in local_tanks:
        
        if budget >= t.get_price():
            budget -= t.get_price()
            bought_indices.append(t.get_index())
    
    return bought_indices

def solve_task2(tanks):
    """
    Task 2: Sort by Strength (Descending) to buy the STRONGEST tanks with 75 coins.
    """
    local_tanks = list(tanks)

    # Sort by Strength (Strongest first)
    local_tanks.sort(key=lambda x: x.compute_strength(), reverse=True)

    budget = 75
    bought_indices = []

    for t in local_tanks:
        if budget >= t.get_price():
            budget -= t.get_price()
            bought_indices.append(t.get_index())

    return bought_indices

# Wrapper to store thread results
def thread_target(func, tanks, result_list, index):
    result_list[index] = func(tanks)

# ==========================================
# 4. Output Handling
# ==========================================
def output_handle(result1, result2):
    with open("output.txt", "w") as f:
        f.write(str(result1) + "\n")
        f.write(str(result2))
    print("Results written to 'output.txt'.")
    print(f"Task 1 Result: {result1}")
    print(f"Task 2 Result: {result2}")

# ==========================================
# 5. Main Execution
# ==========================================
def main():
    # 0. Generate file for testing
    create_dummy_input()

    # 1. Read Input
    all_tanks = input_handle()

    # Shared list to store results from threads: [Task1_Result, Task2_Result]
    results = [None, None]

    # 2. Setup Threading
    # Thread for Task 1
    t1 = threading.Thread(target=thread_target, args=(solve_task1, all_tanks, results, 0))
    # Thread for Task 2
    t2 = threading.Thread(target=thread_target, args=(solve_task2, all_tanks, results, 1))

    # 3. Start Threads
    t1.start()
    t2.start()

    # 4. Wait for Threads to finish
    t1.join()
    t2.join()

    # 5. Write Output
    output_handle(results[0], results[1])

if __name__ == "__main__":
    main()