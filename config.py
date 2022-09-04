
import image
import color



def preCalculateWinningVectors():
    vectors = []
    v = []
    vi = []
    # horizontal vectors
    for x in range(3):
        for y in range(3):
            v.append((x,y))
        vectors.append(v)
        v=[]
    
    # vertical vectors
    for y in range(3):
        for x in range(3):
            v.append((x,y))
        vectors.append(v)
        v=[]
    
    # diagonal vectors
    for i in range(3):
        v.append((i,i))
        vi.append((i,2-i))
    vectors.append(v)
    vectors.append(vi)

    return vectors


def preCalculateWinningVectorsAt(x,y):
    # horizontal and vertical winning vectors
    vectors = []
    vh = []     # horizontal vector
    vv = []     # vertical vector

    for i in range(3):
        vh.append((x,i))
        vv.append((i,y))
    
    vectors.append(vh)
    vectors.append(vv)

    if x % 2 == y % 2:
        # diagonal top left to bottom right
        if x == y:
            vectors.append([(0,0),(1,1),(2,2)])
        # diagonal top right to bottom left
        if x + y == 2:
            vectors.append([(0,2),(1,1),(2,0)])
    

    return vectors





#main

WINDOW_SIZE = image.IMAGE_SIZE*5
WINDOW_NAME = "Tic Tac Toe"

PLAYER = 1
AI = 2

ENDING_OUTCOME = {
   PLAYER: -1,
   0:0,
   AI:1
}

STARTING_TURN = PLAYER

WINNING_VECTORS = preCalculateWinningVectors()
WINNING_VECTORS_MATRIX = [      # contains 3x3 matrix of list of winning vectors for each square
    [],
    [],
    []
]
for x in range(3):
    for y in range(3):
        WINNING_VECTORS_MATRIX[x].append(preCalculateWinningVectorsAt(x,y))

# SQUARE_VALUE_MATRIX = [
#     [0.5,0.3,0.5],
#     [0.3,1.0,0.3],
#     [0.5,0.3,0.5]
# ]




