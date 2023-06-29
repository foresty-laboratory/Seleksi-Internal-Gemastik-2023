#!/usr/bin/python3

import random

flag = b"ForestyCTF{simple_z3_algebra_solver_a525fd}"

selected_index = set()
after = 0

while len(selected_index) != len(flag) and after <= 10:
    ans = None
    tmp = []
    for _ in range(4):
        idx = random.randint(0, len(flag) - 1)
        if ans == None:
            ans = flag[idx]
            tmp.append(f'flag[{idx}]')
        else:
            op = random.randint(0, 1)
            if op == 0:
                ans += flag[idx]
            else:
                ans -= flag[idx]
            tmp.append('+' if op == 0 else '-')
            tmp.append(f'flag[{idx}]')
        
        
        selected_index.add(idx)
    
    tmp = tmp + ['==', f'{ans}']
    print(' '.join(tmp))
    

        
    
    