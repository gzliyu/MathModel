import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation 
import seaborn as sns
import random
import math

width = 300; height = 300
Fire = 3; Tree = 2; Empty = 1


def setFire(map):
    fireMap = np.zeros((width,height))
    for i in range(100):
        x = int(random.random() * width)
        y = int(random.random() * height)
        fireMap[x, y] = Fire

    # for p in firePos:
    #     fireMap[int(p[0]), int(p[1])] = 1

    for i in range(int(width * height / 40)):
        x = int(random.random() * width)
        y = int(random.random() * height)
        fireMap[x, y] = Tree

    return fireMap

def nxtState(fireMp):
    nxtMp = np.zeros((width, height))+fireMp
    pos = [(1, 1), (1, 0), (-1, -1),
           (0, 1), (0, -1), (-1, 0),
           (-1, 1),(-1, -1)]
    for w in range(width):
        for h in range(height):
            # 火元胞下一刻烧尽为0
            # 遵循这样过程即是一个马尔可夫过程，
            # 可以得到最后会趋于三种状态都存在的稳态，
            # 然而这样的结论不符合实际，遂放弃 
            if fireMp[w, h] == Fire: nxtMp[w, h] = Empty
            # 空元胞下一刻以一定概率变成树
            if fireMp[w, h] == Empty: nxtMp[w, h] = tree()
            # 树的元胞若周围有火，下一刻燃烧
            else:
                for p in pos:
                    x = w + p[0]; y = h + p[1]
                    if ifinMp(x, y) and fireMp[x, y] == Fire:
                        nxtMp[w, h] = fire(x - w, y - h)
    return nxtMp

def ifinMp(w, h):
    if (w >= 0 and w < width) and (h >= 0 and h < height): return True
    else: return False

# fire:3,tree:2,empty:1
def fire(x, y):
    t = random.random()
    dirc = np.array([x, y])
    wind = np.array([1,0])
    prob = 0.5*(dirc.dot(wind)/(math.sqrt(x ** 2+y ** 2)**2))
    if t <= prob: return Fire
    else: return Tree
    
def tree():
    prob = 0.2
    t = random.random()
    if t <= prob:return Tree
    else: return Empty

def run(iterTimes):
    map = np.zeros((width, height))
    fMp = setFire(map)
    for i in range(iterTimes):
        nxtMp = nxtState(fMp)
        fMp = nxtMp
        
    # animation=animation.FuncAnimation(fig=fig)
    sns.heatmap(fMp)
    # cmap = sns.cubehelix_palette(start=0, rot=3, gamma=0.8, as_cmap=True,reverse=True)
    plt.show()
    print(fMp)
run(50)
