#!/usr/bin/python3

from z3 import *

s = Solver()

flag = [BitVec(f'flag[{i}]', 8) for i in range(100)]

for i in range(len(flag)):
    s.add(flag[i] >= 32)

s.add(flag[6] + flag[15] - flag[9] - flag[23] == 56)
s.add(flag[19] - flag[14] - flag[1] - flag[27] == -269)
s.add(flag[15] + flag[32] + flag[12] - flag[21] == 234)
s.add(flag[37] + flag[35] - flag[13] - flag[26] == -75)
s.add(flag[0] - flag[21] + flag[0] - flag[4] == -72)
s.add(flag[22] - flag[22] - flag[33] + flag[11] == 14)
s.add(flag[39] + flag[24] - flag[34] + flag[27] == 137)
s.add(flag[14] - flag[22] - flag[32] + flag[14] == -2)
s.add(flag[29] - flag[22] - flag[29] + flag[15] == 0)
s.add(flag[41] - flag[21] + flag[19] + flag[30] == 165)
s.add(flag[30] - flag[5] - flag[32] - flag[19] == -174)
s.add(flag[16] + flag[15] + flag[22] + flag[13] == 426)
s.add(flag[29] - flag[3] + flag[27] - flag[8] == 27)
s.add(flag[6] - flag[25] + flag[37] - flag[35] == -19)
s.add(flag[3] + flag[35] + flag[13] - flag[12] == 200)
s.add(flag[3] - flag[40] - flag[0] + flag[10] == 52)
s.add(flag[21] - flag[17] + flag[34] + flag[24] == 217)
s.add(flag[27] + flag[25] + flag[13] - flag[17] == 209)
s.add(flag[40] + flag[3] - flag[34] - flag[10] == -34)
s.add(flag[1] - flag[38] + flag[41] - flag[32] == 43)
s.add(flag[0] + flag[2] + flag[29] - flag[32] == 181)
s.add(flag[40] + flag[18] - flag[17] + flag[26] == 243)
s.add(flag[19] - flag[0] - flag[17] + flag[33] == -13)
s.add(flag[15] - flag[36] + flag[41] + flag[33] == 212)
s.add(flag[10] - flag[39] - flag[14] - flag[37] == -95)
s.add(flag[29] - flag[29] - flag[17] - flag[9] == -165)
s.add(flag[15] + flag[29] - flag[11] + flag[19] == 159)
s.add(flag[40] + flag[7] - flag[6] - flag[9] == -22)
s.add(flag[31] - flag[16] + flag[26] + flag[34] == 235)
s.add(flag[24] - flag[14] + flag[30] - flag[5] == -16)
s.add(flag[11] - flag[12] + flag[7] + flag[22] == 185)
s.add(flag[37] - flag[26] + flag[25] + flag[42] == 162)
s.add(flag[33] + flag[27] - flag[5] - flag[26] == -32)
s.add(flag[18] - flag[23] - flag[37] - flag[1] == -145)
s.add(flag[38] + flag[35] + flag[15] - flag[40] == 151)
s.add(flag[36] + flag[33] + flag[0] + flag[30] == 379)
s.add(flag[31] + flag[17] - flag[25] - flag[1] == -6)
s.add(flag[21] - flag[13] - flag[16] - flag[38] == -163)
s.add(flag[16] + flag[20] - flag[31] - flag[27] == -9)
s.add(flag[26] - flag[0] + flag[31] - flag[22] == 44)
s.add(flag[22] - flag[36] + flag[13] - flag[1] == 9)
s.add(flag[17] + flag[34] + flag[8] - flag[28] == 198)


s.check()

print(''.join([chr(s.model()[flag[i]].as_long()) for i in range(100)]))