from tarfile import LENGTH_NAME


print('Bai1:')
def sx1():
    a = [3,27,5,123,9,1]
    print(sorted(a))
    return
def sx2():
    a = ['3','27','5','123','9','1']
    print(sorted(a))
    return
sx1()
sx2()
print('2.')
def era():
    a=[12,24,36,70,88,120,155]
    pos = [0,1,2,5]
    for i in sorted(pos, reverse= True):
        a.pop(i)
    print(a)
era()
print('3.')
A = [1,2,3,1,2,5,6,7,8]
B= []
for a in A:
    if a not in B:
        B.append(a)
print(B)
print("Khong Rang Buoc")
B= list(set(A))
print(B)