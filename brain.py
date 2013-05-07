#Neocortex:
#100 neurons in a column,L6: 20, L5: 18, L4:20, L3: 18, L:2 14, L1: 10 (Genetic Algo to arrive at structure? How would you evaluate effectiveness?)
#column number
#row number
#Every neuron starts out being connected to every neuron in it's row (within it's column, and the columns to the right and left) and the column above and below it.
#neuron represeneted as a list of inputs and weights (all set randomly between 0 and 1 to start) with a binary output (above >1= fire or <1 = off). 
#one input row. 
#need to decide on input
# weights adjust randomly between .001 and .01 every iteration
#inhibitory neurons?
#fire together, connection improves,  if not, connection decreases. 
#
#
#
#
##
#
import numpy as np
import random
import math
random.seed()

def enum(**enums):
    return type('Enum', (), enums)


#LAYER1_SIZE=10
#LAYER2_SIZE=14
#LAYER3_SIZE=18
#LAYER4_SIZE=20
#LAYER5_SIZE=18
#LAYER6_SIZE=20
LAYER1_SIZE=5
LAYER2_SIZE=9
LAYER3_SIZE=14
LAYER4_SIZE=16
LAYER5_SIZE=18
LAYER6_SIZE=25
ROW_NUMBER=1
COLUMN_NUMBER=1
NUMBER_OF_NEURONS_IN_COLUMN=LAYER1_SIZE+LAYER2_SIZE+LAYER3_SIZE+LAYER4_SIZE+LAYER5_SIZE+LAYER6_SIZE

Layers={0:LAYER6_SIZE, 1:LAYER5_SIZE, 2:LAYER4_SIZE, 3:LAYER3_SIZE, 4:LAYER2_SIZE, 5:LAYER1_SIZE}
Layer_array=[LAYER6_SIZE, LAYER5_SIZE, LAYER4_SIZE, LAYER3_SIZE, LAYER2_SIZE, LAYER1_SIZE]

class Tetris:
    # input is an array of input neuron activations. grid_width*grid_height inputs are used
    # output is an array of target output activations. Assumes 8 outputs.

    LONG_BLOCK = [[1],
                  [1],
                  [1],
                  [1]]

    L_BLOCK = [[1, 0],
               [1, 0],
               [1, 1]]

    REVERSE_L_BLOCK = [[0, 1],
                       [0, 1],
                       [1, 1]]

    SQUARE_BLOCK = [[1, 1],
                    [1, 1]]

    T_BLOCK = [[1, 0],
               [1, 1],
               [1, 0]]

    Z_BLOCK = [[0, 1],
               [1, 1],
               [1, 0]]

    S_BLOCK = [[1, 0],
               [1, 1],
               [0, 1]]

    blockDict = {'long': LONG_BLOCK, 'l': L_BLOCK, 'reverse-l': REVERSE_L_BLOCK, 'square': SQUARE_BLOCK, 't': T_BLOCK, 'z': Z_BLOCK, 's': S_BLOCK}

    def rotateBlockDimensions(self, width, height, rotation):
        if rotation % 2 == 0: return width, height
        return height, width
        
    # rotation is an integer from 0 to 3
    def blockDimensions(self, blockType, rotation):
        if blockType == "long":
            return self.rotateBlockDimensions(1, 4, rotation)
        if blockType == "s" or blockType == "z" or blockType == "t" or blockType == "reverse-l" or blockType == "l":
            return self.rotateBlockDimensions(2, 3, rotation)
        if blockType == "square":
            return 2, 2

    def randomBlockPositionInGrid(self, blockType, gridWidth, gridHeight):
        rotation = random.randrange(4)
        blockWidth, blockHeight = self.blockDimensions(blockType, rotation)
        #blockTopLeftX = random.randrange(gridWidth - blockWidth + 1)
        #blockTopLeftY = random.randrange(gridHeight - blockHeight + 1)
        blockTopLeftY=1
        blockTopLeftX=1
        return blockTopLeftX, blockTopLeftY, rotation

    def generateBlockInGrid(self, blockType, gridWidth, gridHeight):
        x, y, rotation = self.randomBlockPositionInGrid(blockType, gridWidth, gridHeight)
        blockArray = self.blockDict[blockType]
        blockWidth, blockHeight = self.blockDimensions(blockType, rotation)
        grid = []
        for k in range(gridHeight):
            for i in range(gridWidth):
                if i >= x and i < x + blockWidth and k >= y and k < y + blockHeight:
                    bx, by = i-x, k-y
                    if rotation == 0:
                        grid.append(blockArray[by][bx])
                    if rotation == 1:
                        grid.append(blockArray[bx][-1-by])
                    if rotation == 2:
                        grid.append(blockArray[-1-by][-1-bx])
                    if rotation == 3:
                        grid.append(blockArray[-1-bx][by])
                else:
                    grid.append(0)
        return grid

    def generateTetrisInputAndOutput(self, gridWidth, gridHeight):
        blockTypes = ["long", "s", "z", "t", "reverse-l", "l", "square"]
        blockType = random.choice(blockTypes)
        inputs = self.generateBlockInGrid(blockType, gridWidth, gridHeight)
        outputs = []
        for type in blockTypes:
            if type == blockType: outputs.append(1)
            if type != blockType: outputs.append(0)
        return inputs, outputs

def constructNeocortex():
    random.seed()
    neocortex=[[[[[] for i in range(LAYER6_SIZE)],[[] for i in range(LAYER5_SIZE)],[[] for i in range(LAYER4_SIZE)],[[] for i in range(LAYER3_SIZE)],[[] for i in range(LAYER2_SIZE)], [[] for i in range(LAYER1_SIZE)]] for i in range(COLUMN_NUMBER)] for i in range(ROW_NUMBER)]
    i=0
    for row in range(len(neocortex)):
        for column in range(len(neocortex[row])):
            for level in range(len(neocortex[row][column])):
                for neuron in range(len(neocortex[row][column][level])):
                    for i in range(-1, 2):
                        if row+i>=0 and row+i<ROW_NUMBER:
                            for j in range(-1,2):
                                if column+j>=0 and column+j<COLUMN_NUMBER:
                                    for k in range(0,2):
                                        if level+k<6:
                                            for n in range(Layers[level+k]):
                                              neocortex[row][column][level][neuron].append((row+i,column+j,level+k,n))
    
    return neocortex

def timestep(matrix, prev_activations):
    curr_activations = (matrix * prev_activations)#.transpose()
    for (x,y), activation_potential in np.ndenumerate(curr_activations):
        curr_activations[x,y] = activation_ease(activation_potential)
    matrix=learn(matrix, curr_activations)
    return curr_activations, matrix

def timestepNoLearning(matrix, prev_activations):
    curr_activations = (matrix * prev_activations)#.transpose()
    for (x,y), activation_potential in np.ndenumerate(curr_activations):
        curr_activations[x,y] = activation_ease(activation_potential)
    return curr_activations, matrix

def learn(matrix, activations):
    for (i,k), activation_potential in np.ndenumerate(activations):
        if activation_potential != 0:
            if i!=k:
                if activations[i, 0] == 1 and activations[ k, 0] == 1:
                    matrix[i,k] = matrix[i,k] + random.uniform(0.1, 0.15)
                if activations[i, 0]!= activations[k, 0]:
                    matrix[i,k] = matrix[i,k] - random.uniform(0.1, 0.15)
    return matrix

def activation_ease(n):
    if n < 1:
        return 0
    return 1

def buildMatrix(neocortex):
    size=ROW_NUMBER*COLUMN_NUMBER*NUMBER_OF_NEURONS_IN_COLUMN
    neuron_matrix=[[0 for col in range(size)] for row in range(size)]
    for row in range(len(neocortex)):
        for column in range(len(neocortex[row])):
            for level in range(len(neocortex[row][column])):
                neurons_from_lower_layer=0
                for layer in range(level):
                    neurons_from_lower_layer+=Layer_array[layer]
                for neuron in range(len(neocortex[row][column][level])):
                    Y_index=row*COLUMN_NUMBER*NUMBER_OF_NEURONS_IN_COLUMN + column*NUMBER_OF_NEURONS_IN_COLUMN + neurons_from_lower_layer +neuron
                    for connection in neocortex[row][column][level][neuron]:
                        neurons_from_lower_layer_inputs=0
                        for layer_index in range(connection[2]):
                            neurons_from_lower_layer_inputs+=Layer_array[layer_index]
                        neurons_from_lower_layer=0
                        X_index=connection[0]*COLUMN_NUMBER*NUMBER_OF_NEURONS_IN_COLUMN + connection[1]*NUMBER_OF_NEURONS_IN_COLUMN + neurons_from_lower_layer_inputs+connection[3]
                        if X_index==Y_index:
                            neuron_matrix[X_index][Y_index]=.1
                        else:
                            neuron_matrix[X_index][Y_index]=random.uniform(0.3, .4)
    return np.matrix(neuron_matrix)

#activates all level 1 neurons for testing!
def testActivation(neocortex):
    size=ROW_NUMBER*COLUMN_NUMBER*NUMBER_OF_NEURONS_IN_COLUMN
    activation_array=[0 for act in range(size)]
    for row in range(len(neocortex)):
        for column in range(len(neocortex[row])):
            for level in range(len(neocortex[row][column])):
                for neuron in range(len(neocortex[row][column][level])):
                    index=row*COLUMN_NUMBER*NUMBER_OF_NEURONS_IN_COLUMN + column*NUMBER_OF_NEURONS_IN_COLUMN +neuron
                    activation_array[index]=1
    return np.matrix(activation_array).transpose()
                    
                    

def getOutputs(neocortex, curr_activations):
    for row in range(len(neocortex)):
        for column in range(len(neocortex[row])):
            level=6
            neurons_from_lower_layer=0
            for layer in range(level):
                neurons_from_lower_layer+=Layer_array[layer]
            for neuron in range(len(neocortex[row][column][level-1])):
                Y_index=row*COLUMN_NUMBER*NUMBER_OF_NEURONS_IN_COLUMN + column*NUMBER_OF_NEURONS_IN_COLUMN + neurons_from_lower_layer +neuron
                print "current activation"+ str(curr_activations[Y_index, :])
    
    
neocortex=constructNeocortex()
neuron_matrix=buildMatrix(neocortex)
#curr_activations=testActivation(neocortex)
print neuron_matrix

#    for row in range(len(neocortex)):
#        for column in range(len(neocortex[row])):
#            level=1
#            neurons_from_lower_layer=0
#            for layer in range(level):
#                neurons_from_lower_layer+=Layer_array[layer]
#            for neuron in range(len(neocortex[row][column][level])):
#                Y_index=row*COLUMN_NUMBER*NUMBER_OF_NEURONS_IN_COLUMN + column*NUMBER_OF_NEURONS_IN_COLUMN + neurons_from_lower_layer +neuron
#                print "weights array"+ str( neuron_matrix[Y_index, :])
#                print "previous activation" + str(prev_activations[Y_index, :])
#                print "current activation"+ str(curr_activations[Y_index, :])
                
#    print curr_activations
print neuron_matrix

x=Tetris()
blank=[0 for i in range(25)]
blank=np.matrix(blank).transpose()
for i in range(120):
    ins, outs = x.generateTetrisInputAndOutput(5,5)
    ins=np.matrix(ins).transpose()
    curr_activations=[0 for i in range(LAYER6_SIZE+LAYER5_SIZE+LAYER4_SIZE+ LAYER3_SIZE+LAYER2_SIZE+LAYER1_SIZE)]
    curr_activations=np.matrix(curr_activations).transpose()
    for i in range(60):
        prev_activations=curr_activations
        curr_activations[0:25]=ins
        curr_activations, neuron_matrix=timestep(neuron_matrix, curr_activations)
    for i in range(20):
        curr_activations[0:25]=blank
        prev_activations=curr_activations
        curr_activations, neuron_matrix=timestep(neuron_matrix, curr_activations)
print neuron_matrix

for i in range(10):
    ins, outs = x.generateTetrisInputAndOutput(5,5)
    ins=np.matrix(ins).transpose()
    for i in range(4):
        curr_activations=[0 for i in range(LAYER6_SIZE+LAYER5_SIZE+LAYER4_SIZE+ LAYER3_SIZE+LAYER2_SIZE+LAYER1_SIZE)]
        curr_activations=np.matrix(curr_activations).transpose()
        for i in range(7):
            prev_activations=curr_activations
            curr_activations[0:25]=ins
            curr_activations, neuron_matrix=timestepNoLearning(neuron_matrix, curr_activations)
            #getOutputs(neocortex, np.matrix(curr_activations).transpose())
        print np.matrix(curr_activations[-5:]).transpose()
        for k in range(len(outs)):
            if outs[k]:
                print ["long", "s", "z", "t", "reverse-l", "l", "square"][k]
        for i in range(200):
            curr_activations[0:25]=blank
            prev_activations=curr_activations
            curr_activations, neuron_matrix=timestepNoLearning(neuron_matrix, curr_activations)   
    #print ins[0:5]
    #print ins[5:10]
    #print ins[10:15]
    #print ins[15:20]
    #print ins[20:25]
    #for k in range(len(outs)):
    #    if outs[k]:
    #        print ["long", "s", "z", "t", "reverse-l", "l", "square"][k]
