maze = {}

def gen(x, c):
    if c == 0:
        x[0] = 0
        x[1] = 0
        x[2] = 0
        return
    
    x[0] = {}
    gen(x[0], c-1)
    x[1] = {}
    gen(x[1], c-1)
    x[2] = {}
    gen(x[2], c-1)
    
x = {
    0: {
        "deez": "nuts"
    }
}

