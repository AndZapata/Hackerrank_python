if __name__ == '__main__':
    x = 2
    y = 2
    z = 2
    n = 2
    cubito=[]
    
    for i in range(x+1):
        for j in range(y+1):
            for k in range(z+1):
                cuadrito=[]
                if (i+j+k) != n:
                    cuadrito.append(i)
                    cuadrito.append(j)
                    cuadrito.append(k)
                    cubito.append(cuadrito)
    print(cubito)