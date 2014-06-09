
import random

def gen_cube(upperBound):
    cube = set()
    while len(cube) < 6:
        cube.add(int(random.random()*upperBound))
    return cube
    
def gen_cubes(numCubes, upperBound):
    cubes = []
    cube = gen_cube(upperBound)
    
    while len(cubes) < numCubes:
        cube = gen_cube(upperBound)
        flag = True
        for i in cubes:
            if len(cube.intersection(i)) != 1:
                flag = False
                break
        if flag:
            cubes.append(cube)
            
    return cubes        

numCubes   = 15
upperBound = 31


for i in gen_cubes(numCubes, upperBound):
    string = ''
    for j in i:
        string += str(j)
        string += '\t'
    print string

