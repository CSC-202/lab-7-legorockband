# huffman-analysis.py
## author - nick s.
### get huffman.py working first, then work on this file

import matplotlib.pyplot as plt

# DATA - lyrics
GOUT = "Shadow Wizard Money Gang We love casting spells Ah! This song is sponsored by the Shadow Government Nuke I- Nuke Radio I- I... Yeah, Yeah Warning! Nuking is now legal, worldwide I walk into Balenci, make em' wipe me down Oil filter on the Glock, you wont hear a sound I walk into Balenci, make em' wipe me down Oil filter on the Glock, you won't hear a sound I walk into Balenci, make em wipe me down Oil filter on the Glock, you won't hear a sound You think you heavyweight? We can go pound for pound I'm in Harrods out in London, spend pound aftеr pound If I need a drink, then my man C gone ask around Thesе are Margiela sneakers, I'm not wearing Shein You sought a player cuz the Devil's tryna bring me down Italian leather sneakers, I could have just bought a cow Holy Shit! You're wondering how? Balenciaga Defenders look like I got the gout I'm sipping cup after cup 'til my stomachs poking out I need my pockets, Im retarded, you can keep the clout Ahhhhhhh! If I spend my whole bankroll, Ill affect the DOW I'm in the cut with many drugs, tryna duck this out Ill repent for every sin before my luck runs out I got one of every pill inside a little pouch Hm! I- I... I- Yeah DJ Smokey... Nukes are now legal One- One... One One"
THROUGH_THE_FIRE = "I look in your eyes and I can see We've loved so dangerously You're not trusting your heart to anyone You tell me you're gonna play it smart We're through before we start But I believe that we've only just begun When it's this good, there's no saying no I want you so, I'm ready to go Through the fire, to the limit, to the wall For a chance to be with you I'd gladly risk it all Through the fire Through whatever, come what may For a chance at loving you I'd take it all the way Right down to the wire Even through the fire I know you're afraid of what you feel You still need time to heal And I can help if you'll only let me try You touched me and something in me knew What I could have with you Now I'm not ready to kiss that dream goodbye When it's this sweet, there's no saying no I need you so, I'm ready to go Through the fire, to the limit, to the wall For a chance to be with you I'd gladly risk it all Through the fire Through whatever, come what may For a chance at loving you I'd take it all the way Right down to the wire Even through the fire Through the test of time Through the fire, to the limit, to the wall For the chance to be with you I'd gladly risk it all Through the fire Through whatever, come what may For a chance at loving you I'd take it all the way Right down to the wire Even through the fire To the wire, to the limit through the fire Through the fire, through whatever Through the fire, to the limit Through the fire, through whatever Through the fire, to the limit Through the fire, through whatever Through the fire, to the limit Through the fire, through whatever Through the fire, to the limit Through the fire, through whatever Through the fire, to the limit Through the fire, through whatever"
EVERLONG = "Hello I've waited here for you Everlong Tonight, I throw myself into And out of the red Out of her head, she sang Come down and waste away with me Down with me Slow, how you wanted it to be I'm over my head Out of her head, she sang And I wonder When I sing along with you If everything could ever be this real forever If anything could ever be this good again The only thing I'll ever ask of you You've got to promise not to stop when I say when She sang Breathe out So I can breathe you in Hold you in And now I know you've always been Out of your head Out of my head, I sang And I wonder When I sing along with you If everything could ever feel this real forever If anything could ever be this good again The only thing I'll ever ask of you You've got to promise not to stop when I say when She sang And I wonder If everything could ever feel this real forever If anything could ever be this good again The only thing I'll ever ask of you You've got to promise not to stop when I say when"
# DATA - mantras
HALF_LIFE = 'The right man in the wrong place can make all the difference in the world. So wake up, Mr. Freeman. Wake up and smell the ashes.'
LIFE_OF_PI = 'I suppose in the end the whole of life becomes an act of letting go. But what always hurts the most is not taking a moment to say goodbye. I was never able to thank my father for all I learned from him, to tell him that without his lessons I would never have survived.'
UNDERTALE = "Knowing the mouse might one day leave its hole and get the cheese. You're filled with determination"

# the input, what we want to encode
def huffman(message:str) -> float:
    message = message.upper()

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


    # STEP 0
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
        if v.letter != None: # if 'TODO': # TODO
            coding[v.letter] = path # TODO
        else:
            retrieve_codes(v.left, path + '0') 
            retrieve_codes(v.right, path + '1') 
    
    # STEP 1
    ## initialize the nodes
    nodes = list()
    def letter_count(str: str):
        for i in str:
            freq[i] = freq.get(i,0)+1
        return freq

    letter_count(message)

    # STEP 2
    ## counting the frequencies
    for letter, count in freq.items():
        single_node: Node = Node(letter, count)
        nodes.append(single_node)
        # print(f'{letter} = {count}')

    # STEP 3
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
        result: str = str(coding[letter])
        if freq[letter] > 1:
            for i in range(freq[letter]):
                result_list.append(result)
        else:
            result_list.append(result)
        result_list = [''.join(result_list)]

    final_result = result_list[0]

    # STEP 5
    ## analyize compression performance
    n_original_bits: int = len(message) * 8
    n_encoded_bits: int = len(final_result)
    compression_ratio: float = 1 - (n_encoded_bits / n_original_bits)

    return final_result, coding, compression_ratio

# LYRICS
plt.subplot(2, 1, 1)
plt.suptitle('Lab 7 - Renner Analyzing Huffman')

MAX_N: int = int(128 * 3 / 2)

# PLOT 1
## GOUT
ratios: list = list()
for i in range(1, MAX_N):
    sub_message = GOUT[0:i]
    a, _, ratio = huffman(sub_message)
    ratios.append(ratio)

plt.plot(ratios, '-.', color = 'red', label = 'Gout (n=33)')


## THROUGH THE FIRE
ratios: list = list()
for i in range(1, MAX_N):
    sub_message = THROUGH_THE_FIRE[0:i]
    _, _, ratio = huffman(sub_message)
    ratios.append(ratio)

plt.plot(ratios, '-.', color = 'green', label = 'Through the Fire (n=26)')


## EVERLONG
ratios: list = list()
for i in range(1, MAX_N):
    sub_message = EVERLONG[0:i]
    _, _, ratio = huffman(sub_message)
    ratios.append(ratio)

plt.plot(ratios, '-.', color = 'blue', label = 'Everlong (n=25)')
plt.legend()

# PLOT 2
plt.subplot(2, 1, 2)

## HALF LIFE
ratios: list = list()
for i in range(1, MAX_N):
    sub_message = HALF_LIFE[0:i]
    _, _, ratio = huffman(sub_message)
    ratios.append(ratio)

plt.plot(ratios,'-.', color = 'red', label = 'Half Life (n=22)')

## LIFE OF PI
ratios: list = list()
for i in range(1, MAX_N):
    sub_message = LIFE_OF_PI[0:i]
    _, _, ratio = huffman(sub_message)
    ratios.append(ratio)

plt.plot(ratios, '-.', color = 'green', label = 'Life of PI (n=25)')

## JEDI CODE
ratios: list = list()
for i in range(1, MAX_N):
    sub_message = UNDERTALE[0:i]
    _, _, ratio = huffman(sub_message)
    ratios.append(ratio)

plt.plot(ratios, '-.', color = 'blue', label = 'Undertale (n=23)')
plt.gcf().supylabel('compresson %')
plt.gcf().supxlabel('length of message')
plt.legend()

plt.savefig('./figs/lab7_renner.png')
plt.show()
