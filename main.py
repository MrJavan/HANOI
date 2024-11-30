A = [3,2,1]
B = []
C = []

def move(n , x , y , z):
    if n == 1:
        y.append(x.pop())
        print("A:", A)
        print("B:", B)
        print("C:", C)
        print("------------")
        return
    move(n - 1 , x , z , y )
    y.append(x.pop())
    print("A:", A)
    print("B:", B)
    print("C:", C)
    print("------------")
    move(n - 1 , z , y , x )

print("A:", A)
print("B:", B)
print("C:", C)
print("------------")

move(len(A) , A , C , B)
