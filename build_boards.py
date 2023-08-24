#!/usr/bin/env python3

rows = 6
cols = 7

print("building boards")

for board_row in range(0, rows):
    for board_col in range(0, 4):
        with open(f"boards/h_{board_row}_{board_col}.txt", "w") as _out:
            for row in range(0, rows):
                for col in range(0, cols):
                    if row == board_row:
                        if board_col <= col and col < board_col + 4:
                            _out.write("W")
                        else:
                            _out.write("0")
                    else:
                        _out.write("0")
                _out.write("\n")

for board_col in range(0, cols):
    for board_row in range(0, 3):
        with open(f"boards/v_{board_row}_{board_col}.txt", "w") as _out:
            for row in range(0, rows):
                for col in range(0, cols):
                    if col == board_col:
                        if board_row <= row and row < board_row + 4:
                            _out.write("W")
                        else:
                            _out.write("0")
                    else:
                        _out.write("0")
                _out.write("\n")


for board_row in range(0, rows + 4):
    for board_col in range(0, cols):
        do_output = False
        payload = ""
        connects = 0
        for row in range(0, rows):
            offset = 0
            for col in range(0, cols):
                target_row = board_row - offset
                if target_row == row:
                    if board_col >= col and board_col < col + 4:
                        if col + 3 > 0:
                            connects += 1
                            payload += "W"
                        else:
                            payload += "0"
                    else:
                        payload += "0"
                else:
                    payload += "0"
                offset += 1
            payload += "\n"
            if connects >= 4:
                do_output = True
        if do_output == True:
            with open(f"boards/dl_{board_row}_{board_col}.txt", "w") as _out:
                _out.write(payload)


for board_row in range(-4, rows + 4):
    for board_col in range(0, cols):
        do_output = False
        payload = ""
        connects = 0
        for row in range(0, rows):
            offset = 0
            for col in range(0, cols):
                target_row = board_row + offset
                if target_row == row:
                    if board_col >= col and board_col < col + 4:
                        if col + 3 > 0:
                            connects += 1
                            payload += "W"
                        else:
                            payload += "0"
                    else:
                        payload += "0"
                else:
                    payload += "0"
                offset += 1
            payload += "\n"
            if connects >= 4:
                do_output = True
        if do_output == True:
            with open(f"boards/dr_{board_row}_{board_col}.txt", "w") as _out:
                _out.write(payload)

print("done")
