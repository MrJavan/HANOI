# Tower of Hanoi with Recursive Function in Python

This project demonstrates a solution to the **Tower of Hanoi** problem using Python. The code uses **recursive functions** to move discs between three pegs (represented as lists: `A`, `B`, and `C`) while following the rules of the Tower of Hanoi.

---

## How It Works

- **`A`**: Source peg (initially holds all discs).
- **`B`**: Auxiliary peg (used as a temporary holding place).
- **`C`**: Target peg (discs will be moved here in the correct order).

### Recursive Logic

The function `move(n, x, y, z)` follows this logic:
1. Move `n-1` discs from the source peg (`x`) to the auxiliary peg (`z`).
2. Move the last disc directly from the source peg (`x`) to the target peg (`y`).
3. Move the `n-1` discs from the auxiliary peg (`z`) to the target peg (`y`).

### Code Structure

```python
A = [3, 2, 1]  # Source peg
B = []         # Auxiliary peg
C = []         # Target peg

def move(n, x, y, z):
    if n == 1:
        y.append(x.pop())
        print_state()
        return
    move(n - 1, x, z, y)
    y.append(x.pop())
    print_state()
    move(n - 1, z, y, x)

def print_state():
    print("A:", A)
    print("B:", B)
    print("C:", C)
    print("------------")

print_state()
move(len(A), A, C, B)
```
### Output Example

For 3 discs (`A = [3, 2, 1]`), the output will be:
```
A: [3, 2, 1]
B: []
C: []
------------
A: [3, 2]
B: []
C: [1]
------------
A: [3]
B: [2]
C: [1]
------------
A: [3]
B: [2, 1]
C: []
------------
A: []
B: [2, 1]
C: [3]
------------
A: []
B: []
C: [3, 2, 1]
------------
```
### How to Run

1. Save the code in a file (e.g., ``tower_of_hanoi.py``).
2. Run the script using Python:

```
python tower_of_hanoi.py
```