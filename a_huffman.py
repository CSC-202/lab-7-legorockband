# huffman.py
## author - nick s.
### get huffman to work first here, then make it into a function for the analysis

# the input, what we want to encode
message: str = 'Hello there'

# the output, should be all 0's and 1s
result: str = str()

# for counting the letter frequencies
freq: dict = dict() # key  -> a letter
                    # item -> num of occurences

# for holding the nodes of the huffman tree
nodes: list = list() 

# for storing the code for each letter
coding: dict = dict()   # key  -> a letter
                        # item -> a binary encoding


# STEP 0 - TODO
## defining our data structures
class Node: # NOT given to students
    letter: str
    weight : int
    left: any
    right: any
    
    def __init__(self, letter, weight, left: any = None, right: any = None):
        self.letter = letter
        self.weight = weight
        self.left = left
        self.right = right

## defining operations
### recursively traverses the huffman tree to record the codes
def retrieve_codes(v: Node, path: str=''):
    global coding
    if v.letter != None: # if 'TODO': # TODO
        coding[v.letter] = path # TODO
    else:
        retrieve_codes(v.left, path + '0') 
        retrieve_codes(v.right, path + '1') 

# STEP 1
## counting the frequencies - TODO
for letter, count in freq.items():
    single_node: Node = Node(letter, count)
    nodes.append(single_node)
    print(f'{letter} = {count}')

# STEP 2
## initialize the nodes - TODO
nodes = list()
nodes.append(Node('H', 1))
nodes.append(Node('e', 3))
nodes.append(Node('l', 2))
nodes.append(Node('o', 1))
nodes.append(Node(' ', 1))
nodes.append(Node('t', 1))
nodes.append(Node('h', 1))
nodes.append(Node('r', 1))

# STEP 3 - TODO
## combine each nodes until there's only one item in the nodes list
while len(nodes) > 1:
    ## sort based on weight
    nodes.sort(key=lambda x: x.weight, reverse=True)

    ## get the first min
    min_a: Node = nodes.pop()

    ## get the second min
    min_b: Node = nodes.pop()

    ## combine the two
    combined: Node = Node(letter = None, weight = min_a.weight + min_b.weight, left = min_a, right = min_b)
    ## put the combined nodes back in the list of nodes
    nodes.append(combined)

# STEP 4
## reconstruct the codes
huff_root = nodes[0]
retrieve_codes(huff_root)
result_list: list = []
for letter in coding:
    result: str = str(coding[letter]) # TODO (hint coding[letter] -> code)
    result_list.append(result)
    result_list = [''.join(result_list)]

final_result = result_list[0]
# STEP 5
## analyize compression performance
n_original_bits: int = len(message) * 8
n_encoded_bits: int = len(final_result)
compression_ratio: float = (1 - n_encoded_bits / n_original_bits) * 100

print(f'original: {n_original_bits:^4d} bits')
print(f'encoded : {n_encoded_bits:^4d} bits')
print(f'savings : {int(compression_ratio):^4d} % compression')