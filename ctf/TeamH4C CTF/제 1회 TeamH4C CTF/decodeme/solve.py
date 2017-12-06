A = [0x47,0x7C,0x78,0x5F,0x55,0x65,0x58,0x5F,0x41,0x53,0x74,0x69,0x58,0x7B,0x3B,0x29,0x3D,0x51,0x81,0x6C,0xFB,0x76,0x3C,0x74,0x26,0x62,0x4A,0x1F,0x3E,0x2C,0x43,0x64,0x43,0x07,0x77,0x3F,0x3E,0x64,0x27,0xFA,0x38,0x09,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00]

B = []

for i in range(len(A)):
    X = A[i]

    if i & 1:
        if i % 3:
            # sub_4009A7(2 * i, (_BYTE *)(a1 + i))
            a1 = 2 * i
            if a1 == 23 + 31:
                X -= 31
            elif a1 > 39:
                if a1 & 1:
                    X ^= 61 - a1
                    X += 7
                else:
                    X += 1
            else:
                X -= 10
                X ^= 72 - a1

        else:
            # sub_4008CE((unsigned int)(3 * i), i + a1)
            a1 = 3 * i
            if (a1 & 5) == 0 and (a1 ^ 0xD) % 3:
                if (a1 & 7) == 0 and (a1 ^ 0x15) % 5:
                    X -= 3
                else:
                    X ^= a1 + 32
                    X += 2
            else:
                X ^= a1 + 28
                X += 1

    else:
        # sub_40084D((unsigned int)i, a1 + i);
        a1 = i
        if a1 % 3:
            X += 6
            X ^= a1 + 27
        else:
            X -= 5
            X ^= a1 + 42

    B.append(X)
    print(("0"+hex(X)[2:])[::-1][:2][::-1],end='')
    i += 1


# h4c{Decode_me_haha@@..success-very@@well}