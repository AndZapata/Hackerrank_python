if __name__ == '__main__':
    estudiantes=[]
    for _ in range(int(input())):
        name = input()
        score = float(input())
        
        estudiante=[]
        estudiante.append(name)
        estudiante.append(score)
        estudiantes.append(estudiante)
    
    estudiantes.sort(key = lambda x: x[1])
    for i in range(len(estudiantes)):
        if estudiantes[i][i] == estudiantes[i][i]:
            print(estudiantes[i][0])

# Recordatorio: La clase de mañana comienza desde aqui!!!
# 5
# Harry
# 37.21
# Berry
# 37.21
# Tina
# 37.2
# Akriti
# 41
# Harsh
# 39