def flip_coin():
    import random as rd
    sides = ["Heads", "Tails"]
    player_1 = input("Heads or tails: ").capitalize()
    player_2 = input("Heads or tails: ").capitalize()
    if player_1 not in sides or player_2 not in sides or player_1 == player_2:
        print("Start over")
        return "F"
    H_win = 0 ; T_win = 0; counter = 0
    while counter < 3:
        rd.shuffle(sides)
        verdict = rd.choice(sides)
        if verdict == "Heads":
            H_win += 1
        elif verdict == "Tails":
            T_win += 1
        counter += 1
    if H_win > T_win:
        if player_1 == "Heads":
            return "P1"
        elif player_2 == "Heads":
            return "P2"
    elif T_win > H_win:
        if player_1 == "Tails":
            return "P1"
        elif player_2 == "Tails":
            return "P2"
def print_box(box, al):
    for i in range(1, 4):
        print(f"    {i}", end='')
    print()
    for i in range(len(box)):
        print(al[i], box[i], end="\n")
    return

def verdict(box):
    for i in box:  # straight check
        s_x = 0; s_o = 0
        for j in i:
            if j == "X":
                s_x += 1
            elif j == "o":
                s_o += 1
        if s_x == 3:
            return "X"
        if s_o == 3:
            return "O"

    for i in range(len(box)):  # long check
        l_x = 0; l_o = 0
        for j in range(len(box)):
            if box[j][i] == "X":
               l_x += 1
            elif box[j][i] == "o":
                l_o += 1
        if l_x == 3:
            return "X"
        elif l_o == 3:
            return "O"

    lr_x = lr_o = 0
    for i in range(len(box)):  #top left to bottom right
        if box[i][i] == "X":
            lr_x += 1
        elif box[i][i] == "o":
            lr_o += 1
    if lr_x == 3:
        return "X"
    elif lr_o == 3:
        return "O"

    rl_x = rl_o = 0; dc = 2
    for i in range(len(box)): # top right to bottom left
        if box[i][dc] == "X":
            rl_x += 1
            dc -= 1
        elif box[i][dc] == "o":
            rl_o += 1
            dc -= 1
    if rl_x == 3:
        return "X"
    elif rl_o == 3:
        return "O"
    return None


def user_input(text, record):
    inp = []
    for i in text:
        if i.isalpha():
            pass
        elif i.isdigit():
            temp = int(i)
            inp.append(temp)
    if len(inp) != 1:
        return "Invalid"
    return record[text.upper()], inp[0]-1  # (index of box, index to mark)

def record_box(al, size):
    dic = {}
    for i in al:
        for j in range(size):
            dic[f"{i}{j+1}"] = al.index(i)
    return dic

def tic_tac_toe():
    size = 3
    alphabets = ('A', 'B', 'C')
    box = [[" " for _ in range(size)] for _ in range(size)]
    record = record_box(alphabets, size)
    win = None
    while True:
        win = flip_coin()
        if win != "F":
            break
    print(win)
    if win == "P1":
        print("Player 1 won the toss and will be taking X and Player 2 will be taking o")
    else:
        print("Player 2 won the toss and will be taking X and Player 1 will be taking o")
    print_box(box, alphabets)
    i = 0
    while i < (size * size):
        print(win)
        if win == "P1":
            p1 = "X"
            p2 = "o"
            player_1 = input("Player 1, give your cell\n>")
            box_index, mark_index = user_input(player_1, record)
            if box[box_index][mark_index] == ' ':
                box[box_index][mark_index] = p1
                print_box(box, alphabets)
                if i >= 2:
                    game_outcome = verdict(box)
                    if game_outcome is None:
                        continue
                    else:
                        print(f"{game_outcome} won the match")
                        return
            else:
                print("Invalid Move. Try again")
            player_2 = input("Player 2, give your cell\n>")
            box_index, mark_index = user_input(player_2, record)
            if box[box_index][mark_index] == ' ':
                box[box_index][mark_index] = p2
                print_box(box, alphabets)
                if i >= 2:
                    game_outcome = verdict(box)
                    if game_outcome is None:
                        continue
                    else:
                        print(f"{game_outcome} won the match")
                        return
            else:
                print("Invalid Move. Try again")
        else:
            p2 = "X"
            p1 = "o"
            player_2 = input("Player 2, give your cell\n>")
            box_index, mark_index = user_input(player_2, record)
            if box[box_index][mark_index] == ' ':
                box[box_index][mark_index] = p2
                print_box(box, alphabets)
                if i >= 2:
                    game_outcome = verdict(box)
                    if game_outcome is None:
                        continue
                    else:
                        print(f"{game_outcome} won the match")
                        return
            else:
                print("Invalid Move. Try again")
            player_1 = input("Player 1, give your cell\n>")
            box_index, mark_index = user_input(player_1, record)
            if box[box_index][mark_index] == ' ':
                box[box_index][mark_index] = p1
                print_box(box, alphabets)
                if i >= 2:
                    game_outcome = verdict(box)
                    if game_outcome is None:
                        continue
                    else:
                        print(f"{game_outcome} won the match")
                        return
            else:
                print("Invalid Move. Try again")

        i += 1


tic_tac_toe()