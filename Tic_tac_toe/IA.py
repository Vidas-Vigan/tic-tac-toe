import jeux

board = ["X", "X", "-",
         "X", "-", "X",
         "X", "X", "-"
        ]


#Impression du tableau de jeux
def printboard(board):
    print(board[0] + " | " + board[1] + " | " + board[2])
    print("----------")
    print(board[3] + " | " + board[4] + " | " + board[5])
    print("----------")
    print(board[6] + " | " + board[7] + " | " + board[8])

def ialigne():
    if board[0] + board[1] + board[2] == "XX-":
        board[2] = "O"
    elif board[0] + board[1] + board[2] == "X-X":
        board[1] = "O"
    elif board[0] + board[1] + board[2] == "X-X":


        
        ialigne() 
    printboard(board)