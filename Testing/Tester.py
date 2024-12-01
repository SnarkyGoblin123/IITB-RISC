import re

def decimalToBinary(n):
    if n ==0:
        return "000"
    if n ==1:
        return "001"
    if n ==2:
        return "010"
    if n ==3:
        return "011"
    if n ==4:
        return "100"
    if n ==5:
        return "101"
    if n ==6:
        return "110"
    if n ==7:
        return "111" 
def imm6_conv(imm6):
    imm6_ = bin(imm6).replace("0b", "")
    l = len(imm6_)
    for k in range(6-l):
        imm6_ = '0'+imm6_
    return(imm6_)

def imm9_conv(imm9):
    imm9_ = bin(imm9).replace("0b", "")
    l = len(imm9_)
    for k in range(9-l):
        imm9_ = '0'+imm9_
    return(imm9_)

f = open('Instructions.txt', 'r')
f1 = open('decoded.txt', 'w')
ADD = ["ada","adc","adz","awc","aca","acc","acz",]
i = 0
for line in f.readlines():
    line = line.strip()
    ins_split = line.split()
    
    if ins_split[0] == "ada":
        opcode = "0001"
        comp = "0"
        CZ = "00"
        for j in range(8):
            reg = "r"
            if ins_split[1] == reg + str(j):
                rc = j
            if ins_split[2] == reg + str(j):
                ra = j
            if ins_split[3] == reg + str(j):
                rb = j
        rc = decimalToBinary(rc)
        ra = decimalToBinary(ra)
        rb = decimalToBinary(rb)
        ins = opcode+ra+rb+rc+comp+CZ
        # print(ins)
        f1.write(str(i)+' => ')
        f1.write('"'+ins+'",')
        f1.write('\n')
    if ins_split[0] == "adc":
        opcode = "0001"
        comp = "0"
        CZ = "10"
        for j in range(8):
            reg = "r"
            if ins_split[1] == reg + str(j):
                rc = j
            if ins_split[2] == reg + str(j):
                ra = j
            if ins_split[3] == reg + str(j):
                rb = j
        rc = decimalToBinary(rc)
        ra = decimalToBinary(ra)
        rb = decimalToBinary(rb)
        ins = opcode+ra+rb+rc+comp+CZ
        # print(ins)
        f1.write(str(i)+' => ')
        f1.write('"'+ins+'",')
        f1.write('\n')
    if ins_split[0] == "adz":
        opcode = "0001"
        comp = "0"
        CZ = "01"
        for j in range(8):
            reg = "r"
            if ins_split[1] == reg + str(j):
                rc = j
            if ins_split[2] == reg + str(j):
                ra = j
            if ins_split[3] == reg + str(j):
                rb = j
        rc = decimalToBinary(rc)
        ra = decimalToBinary(ra)
        rb = decimalToBinary(rb)
        ins = opcode+ra+rb+rc+comp+CZ
        # print(ins)
        f1.write(str(i)+' => ')
        f1.write('"'+ins+'",')
        f1.write('\n')
    if ins_split[0] == "awc":
        opcode = "0001"
        comp = "0"
        CZ = "11"
        for j in range(8):
            reg = "r"
            if ins_split[1] == reg + str(j):
                rc = j
            if ins_split[2] == reg + str(j):
                ra = j
            if ins_split[3] == reg + str(j):
                rb = j
        rc = decimalToBinary(rc)
        ra = decimalToBinary(ra)
        rb = decimalToBinary(rb)
        ins = opcode+ra+rb+rc+comp+CZ
        # print(ins)
        f1.write(str(i)+' => ')
        f1.write('"'+ins+'",')
        f1.write('\n')
    if ins_split[0] == "aca":
        opcode = "0001"
        comp = "1"
        CZ = "00"
        for j in range(8):
            reg = "r"
            if ins_split[1] == reg + str(j):
                rc = j
            if ins_split[2] == reg + str(j):
                ra = j
            if ins_split[3] == reg + str(j):
                rb = j
        rc = decimalToBinary(rc)
        ra = decimalToBinary(ra)
        rb = decimalToBinary(rb)
        ins = opcode+ra+rb+rc+comp+CZ
        # print(ins)
        f1.write(str(i)+' => ')
        f1.write('"'+ins+'",')
        f1.write('\n')
    if ins_split[0] == "acc":
        opcode = "0001"
        comp = "1"
        CZ = "10"
        for j in range(8):
            reg = "r"
            if ins_split[1] == reg + str(j):
                rc = j
            if ins_split[2] == reg + str(j):
                ra = j
            if ins_split[3] == reg + str(j):
                rb = j
        rc = decimalToBinary(rc)
        ra = decimalToBinary(ra)
        rb = decimalToBinary(rb)
        ins = opcode+ra+rb+rc+comp+CZ
        # print(ins)
        f1.write(str(i)+' => ')
        f1.write('"'+ins+'",')
        f1.write('\n')
    if ins_split[0] == "acz":
        opcode = "0001"
        comp = "1"
        CZ = "01"
        for j in range(8):
            reg = "r"
            if ins_split[1] == reg + str(j):
                rc = j
            if ins_split[2] == reg + str(j):
                ra = j
            if ins_split[3] == reg + str(j):
                rb = j
        rc = decimalToBinary(rc)
        ra = decimalToBinary(ra)
        rb = decimalToBinary(rb)
        ins = opcode+ra+rb+rc+comp+CZ
        # print(ins)
        f1.write(str(i)+' => ')
        f1.write('"'+ins+'",')
        f1.write('\n')
    if ins_split[0] == "acw":
        opcode = "0001"
        comp = "1"
        CZ = "11"
        for j in range(8):
            reg = "r"
            if ins_split[1] == reg + str(j):
                rc = j
            if ins_split[2] == reg + str(j):
                ra = j
            if ins_split[3] == reg + str(j):
                rb = j
        rc = decimalToBinary(rc)
        ra = decimalToBinary(ra)
        rb = decimalToBinary(rb)
        ins = opcode+ra+rb+rc+comp+CZ
        # print(ins)
        f1.write(str(i)+' => ')
        f1.write('"'+ins+'",')
        f1.write('\n')
    if ins_split[0] == "adi":
        opcode = "0000"
        for j in range(8):
            reg = "r"
            if ins_split[1] == reg + str(j):
                rb = j
            if ins_split[2] == reg + str(j):
                ra = j
        ra = decimalToBinary(ra)
        rb = decimalToBinary(rb)
        ins = opcode+ra+rb+imm6_conv(int(ins_split[3]))
        # print(ins)
        f1.write(str(i)+' => ')
        f1.write('"'+ins+'",')
        f1.write('\n')  
    if ins_split[0] == "ndu":
        opcode = "0010"
        comp = "0"
        CZ = "00"
        for j in range(8):
            reg = "r"
            if ins_split[1] == reg + str(j):
                rc = j
            if ins_split[2] == reg + str(j):
                ra = j
            if ins_split[3] == reg + str(j):
                rb = j
        rc = decimalToBinary(rc)
        ra = decimalToBinary(ra)
        rb = decimalToBinary(rb)
        ins = opcode+ra+rb+rc+comp+CZ
        # print(ins)
        f1.write(str(i)+' => ')
        f1.write('"'+ins+'",')
        f1.write('\n')
    if ins_split[0] == "ndc":
        opcode = "0010"
        comp = "0"
        CZ = "10"
        for j in range(8):
            reg = "r"
            if ins_split[1] == reg + str(j):
                rc = j
            if ins_split[2] == reg + str(j):
                ra = j
            if ins_split[3] == reg + str(j):
                rb = j
        rc = decimalToBinary(rc)
        ra = decimalToBinary(ra)
        rb = decimalToBinary(rb)
        ins = opcode+ra+rb+rc+comp+CZ
        # print(ins)
        f1.write(str(i)+' => ')
        f1.write('"'+ins+'",')
        f1.write('\n')  
    if ins_split[0] == "ndz":
        opcode = "0010"
        comp = "0"
        CZ = "01"
        for j in range(8):
            reg = "r"
            if ins_split[1] == reg + str(j):
                rc = j
            if ins_split[2] == reg + str(j):
                ra = j
            if ins_split[3] == reg + str(j):
                rb = j
        rc = decimalToBinary(rc)
        ra = decimalToBinary(ra)
        rb = decimalToBinary(rb)
        ins = opcode+ra+rb+rc+comp+CZ
        # print(ins)
        f1.write(str(i)+' => ')
        f1.write('"'+ins+'",')
        f1.write('\n')
    if ins_split[0] == "ncu":
        opcode = "0010"
        comp = "1"
        CZ = "00"
        for j in range(8):
            reg = "r"
            if ins_split[1] == reg + str(j):
                rc = j
            if ins_split[2] == reg + str(j):
                ra = j
            if ins_split[3] == reg + str(j):
                rb = j
        rc = decimalToBinary(rc)
        ra = decimalToBinary(ra)
        rb = decimalToBinary(rb)
        ins = opcode+ra+rb+rc+comp+CZ
        # print(ins)
        f1.write(str(i)+' => ')
        f1.write('"'+ins+'",')
        f1.write('\n')
    if ins_split[0] == "ncc":
        opcode = "0010"
        comp = "1"
        CZ = "10"
        for j in range(8):
            reg = "r"
            if ins_split[1] == reg + str(j):
                rc = j
            if ins_split[2] == reg + str(j):
                ra = j
            if ins_split[3] == reg + str(j):
                rb = j
        rc = decimalToBinary(rc)
        ra = decimalToBinary(ra)
        rb = decimalToBinary(rb)
        ins = opcode+ra+rb+rc+comp+CZ
        # print(ins)
        f1.write(str(i)+' => ')
        f1.write('"'+ins+'",')
        f1.write('\n')
    if ins_split[0] == "ncz":
        opcode = "0010"
        comp = "1"
        CZ = "01"
        for j in range(8):
            reg = "r"
            if ins_split[1] == reg + str(j):
                rc = j
            if ins_split[2] == reg + str(j):
                ra = j
            if ins_split[3] == reg + str(j):
                rb = j
        rc = decimalToBinary(rc)
        ra = decimalToBinary(ra)
        rb = decimalToBinary(rb)
        ins = opcode+ra+rb+rc+comp+CZ
        # print(ins)
        f1.write(str(i)+' => ')
        f1.write('"'+ins+'",')
        f1.write('\n')
    if ins_split[0] == "lli":
        opcode = "0011"
        for j in range(8):
            reg = "r"
            if ins_split[1] == reg + str(j):
                ra = j
        ra = decimalToBinary(ra)
        ins = opcode+ra+imm9_conv(int(ins_split[2]))
        # print(ins)
        f1.write(str(i)+' => ')
        f1.write('"'+ins+'",')
        f1.write('\n')
    if ins_split[0] == "lw":
        opcode = "0100"
        for j in range(8):
            reg = "r"
            if ins_split[1] == reg + str(j):
                ra = j
            if ins_split[2] == reg + str(j):
                rb = j
        ra = decimalToBinary(ra)
        rb = decimalToBinary(rb)
        ins = opcode+ra+rb+imm6_conv(int(ins_split[3]))
        # print(ins)
        f1.write(str(i)+' => ')
        f1.write('"'+ins+'",')
        f1.write('\n')
    if ins_split[0] == "sw":
        opcode = "0101"
        for j in range(8):
            reg = "r"
            if ins_split[1] == reg + str(j):
                ra = j
            if ins_split[2] == reg + str(j):
                rb = j
        ra = decimalToBinary(ra)
        rb = decimalToBinary(rb)
        ins = opcode+ra+rb+imm6_conv(int(ins_split[3]))
        # print(ins)
        f1.write(str(i)+' => ')
        f1.write('"'+ins+'",')
        f1.write('\n')
    if ins_split[0] == "lm":
        opcode = "0110"
        for j in range(8):
            reg = "r"
            if ins_split[1] == reg + str(j):
                ra = j
        ra = decimalToBinary(ra)
        ins = opcode+ra+imm9_conv(int(ins_split[2]))
        # print(ins)
        f1.write(str(i)+' => ')
        f1.write('"'+ins+'",')
        f1.write('\n')
    if ins_split[0] == "sm":
        opcode = "0111"
        for j in range(8):
            reg = "r"
            if ins_split[1] == reg + str(j):
                ra = j
        ra = decimalToBinary(ra)
        ins = opcode+ra+imm9_conv(int(ins_split[2]))
        # print(ins)
        f1.write(str(i)+' => ')
        f1.write('"'+ins+'",')
        f1.write('\n')
    if ins_split[0] == "beq":
        opcode = "1000"
        for j in range(8):
            reg = "r"
            if ins_split[1] == reg + str(j):
                ra = j
            if ins_split[2] == reg + str(j):
                rb = j
        ra = decimalToBinary(ra)
        rb = decimalToBinary(rb)
        ins = opcode+ra+rb+imm6_conv(int(ins_split[3]))
        # print(ins)
        f1.write(str(i)+' => ')
        f1.write('"'+ins+'",')
        f1.write('\n')
    if ins_split[0] == "blt":
        opcode = "1001"
        for j in range(8):
            reg = "r"
            if ins_split[1] == reg + str(j):
                ra = j
            if ins_split[2] == reg + str(j):
                rb = j
        ra = decimalToBinary(ra)
        rb = decimalToBinary(rb)
        ins = opcode+ra+rb+imm6_conv(int(ins_split[3]))
        # print(ins)
        f1.write(str(i)+' => ')
        f1.write('"'+ins+'",')
        f1.write('\n')
    if ins_split[0] == "ble":  #opcode in project given wrong
        opcode = "1010"
        for j in range(8):
            reg = "r"
            if ins_split[1] == reg + str(j):
                ra = j
            if ins_split[2] == reg + str(j):
                rb = j
        ra = decimalToBinary(ra)
        rb = decimalToBinary(rb)
        ins = opcode+ra+rb+imm6_conv(int(ins_split[3]))
        # print(ins)
        f1.write(str(i)+' => ')
        f1.write('"'+ins+'",')
        f1.write('\n')
    if ins_split[0] == "jalr":
        opcode = "1100"
        for j in range(8):
            reg = "r"
            if ins_split[1] == reg + str(j):
                ra = j
        ra = decimalToBinary(ra)
        ins = opcode+ra+imm9_conv(int(ins_split[2]))
        # print(ins)
        f1.write(str(i)+' => ')
        f1.write('"'+ins+'",')
        f1.write('\n')
    if ins_split[0] == "jlr":
        opcode = "1101"
        for j in range(8):
            reg = "r"
            if ins_split[1] == reg + str(j):
                ra = j
            if ins_split[2] == reg + str(j):
                rb = j
        ra = decimalToBinary(ra)
        rb = decimalToBinary(rb)
        ins = opcode+ra+rb+'000000'
        # print(ins)
        f1.write(str(i)+' => ')
        f1.write('"'+ins+'",')
        f1.write('\n')
    if ins_split[0] == "jri":
        opcode = "1111"
        for j in range(8):
            reg = "r"
            if ins_split[1] == reg + str(j):
                ra = j
        ra = decimalToBinary(ra)
        ins = opcode+ra+imm9_conv(int(ins_split[2]))
        # print(ins)
        f1.write(str(i)+' => ')
        f1.write('"'+ins+'",')
        f1.write('\n')
    i = i+1

f1.close()
