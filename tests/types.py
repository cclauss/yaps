import sys
import os
sys.path.append(os.path.abspath(os.path.join('..', 'yaps')))

from yaps.lib import *
import yaps as yaps


N = type_var("N")

@yaps.model
def test(A: matrix(lower=0)[5, 6][6],
    B:matrix[5, 6][6],
    C:matrix[5, 6][6,7],
    D:matrix(lower=0)[5, 6],
    E:simplex[5],
    F:simplex(lower=0)[5][5, 6],
    G:simplex[5],
    H:simplex(lower=0)[5],
    I:int(upper=5)[3],
    J:int(upper=5),
    K:int,
    L:int[6]
    ):

    pass

print(test)
