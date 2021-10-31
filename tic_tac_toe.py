board=list() 
size_input=int(input("Size--> "))
game_ongoing=True
winner = None

def board_initialization(): 
    global board
    for i in range(0,size_input**2):
        board.append(i)

def show_board():
    i = 0
    while i < size_input**2:
        j=0
        while j <size_input:
            print(board[i+j], end="\t")
            j+=1
        print("\n")
        i+=size_input

def player_turn(i):
    global board
    if(i%2 == 0): 
        p = int(input("X--> "))
        board[p] = 'X'
    else:
        q = int(input("O--> "))
        board[q] = 'O'
    show_board()
    check_win()
#    check_columns()


def check_rows():
    k = 0
    global winner
    while (k < size_input**2):
        l = 0
        while(l < size_input-1):
            if(board[k+l] == board[k+l+1]==board[k]):
                    winner=board[k+l]
                    l+=1
            else:
                winner = None
                l += 1
        if(winner is not None):
            break
        else:
            k += size_input
    if(winner is not None):
        return True

def check_columns():
    global winner
    k=0
    while(k < size_input):
        l=0
        l_incr=size_input
        while(l < size_input**2):
            if(board[k+l] == board[k+l_incr] == board[k]):
                winner = board[k+l]
                l+=l_incr
            else:
                winner = None
                l+=l_incr
        if(winner is not None):
            break
        else:
            k+=1
    if(winner is not None):
        return True

def check_left_diagonal():
    global winner
    m = 0
    m_incr=size_input+1
    ld=list()
    while(m<size_input**2):
        ld.append(board[m])
        m+= m_incr
#check for X
    x = list()
    for i in ld:
        if (i == "X"):
            x.append(True)
        else:
            x.append(False)
#check for O
    o= list()
    for i in ld:
        if(i == "O"):
            o.append(True)
        else:
            o.append(False)
    if(all(x)):
        winner = "X"
        return True
    elif(all(o)):
        winner = "O"
        return True
    

def check_right_diagonal():
    global winner
    m=size_input-1
    m_incr =size_input-1
    rd=list()
    while(m<size_input**2-1):
        rd.append(board[m])
        m+=m_incr
#check for X
    x = list()
    for i in rd:
        if (i == "X"):
            x.append(True)
        else:
            x.append(False)
#check for O
    o= list()
    for i in rd:
        if(i == "O"):
            o.append(True)
        else:
            o.append(False)
    if(all(x)):
        winner = "X"
        return True
    elif(all(o)):
        winner = "O"
        return True


def play_game():
    for i in range(0, size_input**2):
        if(game_ongoing == False):
            break
        player_turn(i)

def check_win():
    global game_ongoing
    if check_rows():
        game_ongoing = False
    elif check_columns():
        game_ongoing = False
    elif(check_left_diagonal() == True):
        game_ongoing = False
    elif(check_right_diagonal() == True):
        game_ongoing = False

board_initialization()
show_board()
play_game()

print("winner:", winner)

 




