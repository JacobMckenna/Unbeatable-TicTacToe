
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

PLAYER = 1 # x
AI = 2     # o
TURN = 3
FULL = 4

NUM_BITS = 32

MASK_ = {
    AI:     0b00000000000000000000000111111111,
    PLAYER: 0b10000000000000111111111000000000,
    TURN:   0b10000000000000000000000000000000, # 1 == player to place, 0 = AI to place
    FULL:   0b111111111
}

EMPTY_BOARD = 0b10000000000000000000000000000000

OUTCOME_STR_ = {
    0: "No one",
    PLAYER: "Player",
    AI: "Ai"
}

ENDING_OUTCOME = {
   PLAYER: -1,
   0:0,
   AI:1
}
MOVE_IDX_ = {
}
for i in range(0):
    MOVE_IDX_.update({0b1<<i:i})

STARTING_TURN = AI


MOVES = [
    # ordered from most likely to be good to least likely to be good
    # for optimal efficient move
    0b100000000,    # best first move if no other moves   - should be first since move 1 has longest run time
    0b000010000,    # best 2nd move if other already played
    0b001000000,
    0b000000100,
    0b000000001,
    0b010000000,
    0b000100000,
    0b000001000,
    0b000000010
]


# WINNING_VECTORS = preCalculateWinningVectors()
WINNING_BITBOARDS = [
    0b000000111,
    0b000111000,
    0b111000000,
    0b100100100,
    0b010010010,
    0b001001001,
    0b100010001,
    0b001010100
]
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




