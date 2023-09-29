# 5) Read about the Tower of Hanoi algorithm. Write a program to implement it.

# Program:-

def tower_of_hanoi(n, source, auxiliary, target):
    if n == 1:
        print(f"Move disk 1 from {source} to {target}")
        return
    tower_of_hanoi(n-1, source, target, auxiliary)
    print(f"Move disk {n} from {source} to {target}")
    tower_of_hanoi(n-1, auxiliary, source, target)


num_disks = int(input("Enter the number of disks: "))


tower_of_hanoi(num_disks, 'A', 'B', 'C')
     