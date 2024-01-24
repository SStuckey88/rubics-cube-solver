#whoever.py
import random

def num_of_cubes(h, w, l):
    num_cubes = w*l*2
    num_cubes += (h-2)*(w)*2
    num_cubes += 2*(h-2)*(w-2)
    return num_cubes

def face_rotate(face_number):
    inbetween_list = []
    for i in range(0, cube_length):
        inbetween_list.append(rubic_list[face_number][i][-1])
    
    for i in range(0, cube_length):
        rubic_list[face_number][i][-1] = rubic_list[face_number][0][(-i-1)]

    for i in range(0, cube_length):
        rubic_list[face_number][0][(-i-1)] = rubic_list[face_number][i][0]

    for i in range(0, cube_length):
        rubic_list[face_number][i][0] = rubic_list[face_number][-1][i]
    
    for i in range(0, cube_length):
        rubic_list[face_number][-1][(-i-1)] = inbetween_list[i]

def create_rubiks_list(l, w, h):
    rubics_list = []
    for i in range(0, 6):
        if i >= 0 or i <= 3:
            rubic_face = []
            for m in range(0, l):
                rubic_face.append([])
                if i >= 0 or i <= 1:
                    for d in range(0, h):
                        rubic_face[m].append(0)
                elif i >= 2 or i <= 3:
                    rubic_face = [m].append(0)

            rubics_list.append(rubic_face)
                
        elif i >= 4 or i <= 5:
            rubic_face = []
            for m in range(0, w):
                rubic_face.append([])
                for d in range(0, h):
                    rubic_face[m].append(0)
            rubics_list.append(rubic_face)
    return rubics_list

if "checks" == "checks":
    def check_for_white_cross():
        white_location = []
        for i in range(0, len(rubic_list)):
            for m in range(0, len(rubic_list[i])):
                for d in range(0, len(rubic_list[i][m])):
                    if rubic_list[i][m][d] == 2:
                        if ((m == 0 or m == (2)) and  (d == 1)) or (m == 1 and (d == 0 or d == (2))):
                            white_location.append([i, m, d])
                        elif m == 1 and d == 1:
                            yellow_center = i
        return yellow_center, white_location
    
if "action" == "action":
    def make_white_cross(white_location, yellow_center):
        cross_locations = [[yellow_center, 0, 1], [yellow_center, 1, 0], [yellow_center, 1, 2], [yellow_center, 2, 1]]
        for i in white_location:
            if i[0] == yellow_center:
                cross_locations

 
if "test" == "test":
    def test1():
        count =0
        for i in range(0, len(rubic_list)):
            for m in range(0, len(rubic_list[i])):
                for d in range(0, len(rubic_list[i][m])):
                    rubic_list[i][m][d] = count
                    count +=1
        
        print(rubic_list)
        right_turn_up()
        print()
        print(rubic_list)

    def test():
        print(rubic_list)
        count = 0
        for i in range(0, len(rubic_list)):
            for m in range(0, len(rubic_list[i])):
                for d in range(0, len(rubic_list[i][m])):
                    rubic_list[i][m][d] = count

        for i in range(0, 5):
            print(
            
            )
        print(rubic_list)
        check_for_white()
        for i in range(0, 5):
            print(
            
            )
        front_face_left()
        print(rubic_list)

        face_rotate(0)
        print()
        print()
        print(rubic_list)

    def test3():
        for i in range(0, len(rubic_list)):
            for m in range(0, len(rubic_list[i])):
                for d in range(0, len(rubic_list[i][m])):
                    rubic_list[i][m][d] = random.randint(0, 6)
        print(rubic_list)
        check_for_white()




if "algorithms" == "algorithms":
    def right_turn_up():
        global curr_face
        inbetween_list = []
        inbetween_list = rubic_list[5][-1]
        rubic_list[5][-1] = rubic_list[1][-1]
        rubic_list[1][-1] = rubic_list[4][-1]
        rubic_list[4][-1] = rubic_list[0][-1]
        rubic_list[0][-1] = inbetween_list
        new_face = 2
        if curr_face <=2 :
            if curr_face == 0:
                new_face = 2
            elif curr_face == 1:
                new_face = 3
            else: 
                new_face = 1
        else:
            if curr_face == 3:
                new_face = 0
            elif curr_face == 4:
                new_face == 2
            else:
                new_face ==2
        face_rotate(new_face)

    def left_turn_up():
        global curr_face
        inbetween_list = []
        inbetween_list = rubic_list[5][0]
        rubic_list[5][0] = rubic_list[1][0]
        rubic_list[1][0] = rubic_list[4][0]
        rubic_list[4][0] = rubic_list[0][0]
        rubic_list[0][0] = inbetween_list
        new_face = 2
        if curr_face <=2 :
            if curr_face == 0:
                new_face = 3
            elif curr_face == 1:
                new_face = 2
            else: 
                new_face = 0
        else:
            if curr_face == 3:
                new_face = 1
            elif curr_face == 4:
                new_face == 3
            else:
                new_face ==3
        face_rotate(new_face)


    def front_face_left():
        inbetween_list = []
        for i in range(0, cube_length):
            inbetween_list.append(rubic_list[5][i][-1])

        for i in range(0, cube_length):
            rubic_list[5][i].pop()
            rubic_list[5][i].append(rubic_list[3][i][-1])
        
        for i in range(0, cube_length):
            rubic_list[3][i].pop()
            rubic_list[3][i].append(rubic_list[4][i][-1])

        for i in range(0, cube_length):
            rubic_list[3][i].pop()
            rubic_list[3][i].append(rubic_list[4][i][-1])

        for i in range(0, cube_length):
            rubic_list[4][i].pop()
            rubic_list[4][i].append(rubic_list[2][i][-1])

        for i in range(0, cube_length):
            rubic_list[2][i].pop()
            rubic_list[2][i].append(inbetween_list[i])
        face_rotate(curr_face)


    def right_algorithm():
        right_turn_up()
        front_face_left()
        for i in range(0, 3):
            right_turn_up()
        for i in range(0, 3):
            front_face_left()

    def left_algorithm():
        left_turn_up()
        for i in range(0, 3):
            front_face_left()
        for i in range(0, 3):
            left_turn_up()
        front_face_left()

def solve3x3():
    pass


rubics_cube = []
rubics_colors = ["blue", "yellow", "white", "red", "green", "orange"]

global cube_up
global cube_length
global cube_width
cube_up = int(input("imput the height of your cube: "))
cube_length = int(input("imput the length of your cube: "))
cube_width = int(input("imput the width of your cube: "))

faces = {1: "front_face", 2: "backface", 3:"rightface", 4:"Leftface", 5: "top", 6: "bottom"}

num_cubes = num_of_cubes(cube_up, cube_length, cube_width)
rubic_list = create_rubiks_list(cube_up, cube_length, cube_width)
global curr_face
curr_face = 0

test1()

if cube_up ==3 and cube_length == 3 and cube_width == 3:
    solve3x3()

else:
    print("die rebel scum and be reborn as a 3x3 cube")



