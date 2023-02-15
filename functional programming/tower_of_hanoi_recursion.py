# Tower of Hanoi

# The objective is to move n number of disks from one tower to another following a set of rules. 
# These rules are as follows: 
# - Only one disk can be moved at a time 
# - Only the upper disk of any of the towers can be moved 
# - Larger disks cannot be placed over smaller disks

# In the optimal scenario of solving the puzzle, 
# the total moves will be 2^n – 1 where n is the number of disks that need to be moved.

def tower_of_hanoi(disks, source, helper, destination):
    if (disks == 1 ):
        print(f'Disk {disks} moves from tower {source} to tower {destination}.')
        return

    tower_of_hanoi(disks - 1, source, destination, helper)
    print(f'Disk {disks} moves from tower {source} to tower {destination}.')
    tower_of_hanoi(disks - 1, helper, source, destination)

disks = int(input("Number of disks to be displaced: "))

tower_of_hanoi(disks, "A", "B", "C")
