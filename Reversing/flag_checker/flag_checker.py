#!/usr/bin/python3

def check(flag):
    if len(flag) != 43:
        return False
    if flag[6] + flag[15] - flag[9] - flag[23] != 56:
        return False
    if flag[19] - flag[14] - flag[1] - flag[27] != -269:
        return False
    if flag[15] + flag[32] + flag[12] - flag[21] != 234:
        return False
    if flag[37] + flag[35] - flag[13] - flag[26] != -75:
        return False
    if flag[0] - flag[21] + flag[0] - flag[4] != -72:
        return False
    if flag[22] - flag[22] - flag[33] + flag[11] != 14:
        return False
    if flag[39] + flag[24] - flag[34] + flag[27] != 137:
        return False
    if flag[14] - flag[22] - flag[32] + flag[14] != -2:
        return False
    if flag[29] - flag[22] - flag[29] + flag[15] != 0:
        return False
    if flag[41] - flag[21] + flag[19] + flag[30] != 165:
        return False
    if flag[30] - flag[5] - flag[32] - flag[19] != -174:
        return False
    if flag[16] + flag[15] + flag[22] + flag[13] != 426:
        return False
    if flag[29] - flag[3] + flag[27] - flag[8] != 27:
        return False
    if flag[6] - flag[25] + flag[37] - flag[35] != -19:
        return False
    if flag[3] + flag[35] + flag[13] - flag[12] != 200:
        return False
    if flag[3] - flag[40] - flag[0] + flag[10] != 52:
        return False
    if flag[21] - flag[17] + flag[34] + flag[24] != 217:
        return False
    if flag[27] + flag[25] + flag[13] - flag[17] != 209:
        return False
    if flag[40] + flag[3] - flag[34] - flag[10] != -34:
        return False
    if flag[1] - flag[38] + flag[41] - flag[32] != 43:
        return False
    if flag[0] + flag[2] + flag[29] - flag[32] != 181:
        return False
    if flag[40] + flag[18] - flag[17] + flag[26] != 243:
        return False
    if flag[19] - flag[0] - flag[17] + flag[33] != -13:
        return False
    if flag[15] - flag[36] + flag[41] + flag[33] != 212:
        return False
    if flag[10] - flag[39] - flag[14] - flag[37] != -95:
        return False
    if flag[29] - flag[29] - flag[17] - flag[9] != -165:
        return False
    if flag[15] + flag[29] - flag[11] + flag[19] != 159:
        return False
    if flag[40] + flag[7] - flag[6] - flag[9] != -22:
        return False
    if flag[31] - flag[16] + flag[26] + flag[34] != 235:
        return False
    if flag[24] - flag[14] + flag[30] - flag[5] != -16:
        return False
    if flag[11] - flag[12] + flag[7] + flag[22] != 185:
        return False
    if flag[37] - flag[26] + flag[25] + flag[42] != 162:
        return False
    if flag[33] + flag[27] - flag[5] - flag[26] != -32:
        return False
    if flag[18] - flag[23] - flag[37] - flag[1] != -145:
        return False
    if flag[38] + flag[35] + flag[15] - flag[40] != 151:
        return False
    if flag[36] + flag[33] + flag[0] + flag[30] != 379:
        return False
    if flag[31] + flag[17] - flag[25] - flag[1] != -6:
        return False
    if flag[21] - flag[13] - flag[16] - flag[38] != -163:
        return False
    if flag[16] + flag[20] - flag[31] - flag[27] != -9:
        return False
    if flag[26] - flag[0] + flag[31] - flag[22] != 44:
        return False
    if flag[22] - flag[36] + flag[13] - flag[1] != 9:
        return False
    if flag[17] + flag[34] + flag[8] - flag[28] != 198:
        return False
    return True


if __name__ == '__main__':
    inp_flag = input("Validate your flag: ").encode()
    
    if check(inp_flag):
        print("Correct!")
    else:
        print("Wrong!")