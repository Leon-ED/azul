from upemtk import *

########################################
lines, columns = 3, 5
size = 100
height = size * lines
width = size * columns

########################################
def init(data):
    for i in range(lines):
        data.append([0]*columns)


########################################
def cell():
    x, y, _ = attente_clic()
    return   (y // size), (x // size) # line, column

def select_cell(data):
    i, j = cell()
    data[i][j] = 1-data[i][j]
    return i,j

def end(i, j, data):
    return (i,j) == (0,0)


########################################
def print_grid():
    for i in range(1, columns):
        ligne(i*size, 0, i*size, height)
    for i in range(1, lines):
        ligne(0, i*size, width, i*size)

def print_data(data):
    for i in range(lines):
        for j in range(columns):
            if data[i][j] != 0:
                rectangle(j*size, i*size, (j+1)*size, (i+1)*size,"blue","blue")

def whole_display(data):
    efface_tout()
    print_grid()
    print_data(data)

########################################

if __name__ == '__main__':
    cree_fenetre(width, height)
    
    data=[]
    init(data)

    whole_display(data)
    
    while(True):
        i,j = select_cell(data)
        whole_display(data)
        
        if end(i, j, data):
            break

print("this is the end...")    
attente_clic()
ferme_fenetre()











