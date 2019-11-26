import sys
if len(sys.argv) < 3:
    sys.exit()
nodos = [1,2,3,4,5]
ids = [7,3,2,1,8]
for nodo, idx in zip(nodos, ids):
    print(nodo, idx)
    
