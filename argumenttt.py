#points2d=[(1,2),(12,3),(4,-4),(23,4)]
#prints2d_sorted=sorted(points2d, key=lambda x:x[0] + x[1])

#print(points2d)
#print(prints2d_sorted)

a=[1,2,3,4,5,6]
b=filter(lambda x: x%2==0, a)
print(list(b))

c=[x*2 for x in a if x%2==0]
print(c)

