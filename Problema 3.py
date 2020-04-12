def candy(A):
    n=len(A)
    c=0
    for i in range (n):
        c+=1    # Un caramelo por cada niño
    for i in range (1,n-1):  # Se toma en cuenta todos menos el útimo y el primero
        if A[i+1]<A[i] or A[i-1]<A[i]:  # La posición actual es mayor que una de las continuas
            c+=1    # Se agrega un caramelo
            if A[i+1]<A[i] and A[i-1]<A[i]: # La posición actual es mayor que ambas continuas
                c+=1
    return c    # Retorna el múmero de caramelos

print (candy([1,2]))
print (candy([1,5,2,1]))
