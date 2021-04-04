from functools import partial
from tkinter import *
from tkinter import messagebox as msg
import os.path
from os import path
import os
import random
turn=0
global board,p1,p2 

board=[[" " for x in range(3)]for y in range(3)]
#print(board)

#for checking the winner
def winner(b,l):
    return((b[0][0] == l and b[0][1] == l and b[0][2] == l) or
            (b[1][0] == l and b[1][1] == l and b[1][2] == l) or
            (b[2][0] == l and b[2][1] == l and b[2][2] == l) or
            (b[0][0] == l and b[1][0] == l and b[2][0] == l) or
            (b[0][1] == l and b[1][1] == l and b[2][1] == l) or
            (b[0][2] == l and b[1][2] == l and b[2][2] == l) or
            (b[0][0] == l and b[1][1] == l and b[2][2] == l) or
            (b[0][2] == l and b[1][1] == l and b[2][0] == l))
def get_text_fun(i,j,gb,p1,p2):
    '''
    getting text and change the turn
    '''
    global turn
    if board[i][j]==' ':
        if turn %2 ==0:
            #print(turn)
            
            p1.config(state=DISABLED)
            p2.config(state=ACTIVE)
            board[i][j]="X"
            #print(board[i][j])
        else:
            
            p2.config(state=DISABLED)
            p1.config(state=ACTIVE)
            board[i][j]="O"
        turn = turn+1
        button[i][j].config(text=board[i][j])
        #print(board)
    if winner(board,"X"):
        #print(turn)
        box=msg.showinfo("WINNER","PLAYER X WON THE GAME") 
        reset()
           
    elif winner(board,"O"):
        box=msg.showinfo("WINNER","PLAYER O WON THE GAME")
        reset()
       
    elif (isfull()):
        box=msg.showinfo("TIE ","ITS A TIE")
        reset()
            
def free(i,j):
    return board[i][j]==" "
def isfull():
    flag=True
    for i in board:
        if(i.count(' ')>0):
            flag=False
    return flag 

def reset():
    '''
    reset the game board
    '''
    for i in range(3):
        for j in range(3):
            board[i][j]=" "
            button[i][j].config(text = ' ',state=NORMAL)
def name():
    '''
    enter the player name
    '''
    
    game_board=Tk()
    game_board.geometry("250x250")
    play1=Label(game_board,text="player1 Name")
    play1.place(x=10,y=110)
    play2=Label(game_board,text="player2 Name")
    play2.place(x=10,y=150)
    play1_entry=Entry(game_board)
    play1_entry.insert(0,"Player 1 ")
    play1_entry.place(x=95,y=110)
    play2_entry=Entry(game_board)
    play2_entry.insert(0,"player 2 ")
    play2_entry.place(x=95,y=150)
    
    def create():
        p1=play1_entry.get()
        p2=play2_entry.get()
        path="D:/data_bankManagement/game/"
        file1=open(path+"file.txt","w")
        file1.write(p1+"\n"+p2)
    
    start=Button(game_board,text=" Start ",command=lambda:[create(),player(game_board)])
    start.place(x=105,y=30)
    
   

def board_player(game_board,p1,p2):
    global button
    button=[]
    def remove():
        path1="D:/data_bankManagement/game/"
        file1="file.txt"
    
        if path.exists(path1+file1):
            
            os.remove(path1+file1)
            game_board.destroy()
            play()

    back=Button(game_board,text="Back",command=remove)
    back.place(x=150,y=3)
    
    for i in range(3):
        m=3+i
        button.append(i)
        button[i]=[]
        
        for j in range(3):
            n=j
            button[i].append(j)
            
            get_text=partial(get_text_fun,i,j,game_board,p1,p2)
            button[i][j]=Button(game_board,height=4,width=8,command=get_text)
            button[i][j].grid(row=m, column=n)
           
    game_board.mainloop()  


def player( game_board):
    
    game_board.destroy()
    
    game_board=Tk()
    #game_board.geometry("250x250")
    game_board.title("Tic Tac Toe")
    path1="D:/data_bankManagement/game/"
    file="file.txt"
    
    if path.exists(path1+file):
            file1=open(path1+"file.txt","r")
            file_read=file1.readlines()
            pl1=file_read[0]
            pl2=file_read[1]
            file1.close()     

    p1=Button(game_board,text=pl1+": X ")
    p1.grid(row=1,column=1)
    p2=Button(game_board,text=pl2+": O ",state=DISABLED)
    p2.grid(row=2,column=1)
    
    board_player(game_board,p1,p2)
  




def play():
    root = Tk()
    root.geometry("250x250")
    root.title("Tic Tac Toe")
    
    #with_player=partial(withplayer,root)
    head=Label(root,text="WELCOME TO THE GAME")
    head.pack(side='top')
    
    multi=Button(root,text=" Multi Player ",width=12,command=lambda:[root.destroy(),name()])
    multi.place(x=75,y=50)
    ex=Button(root,text=" Exit",width=12,command=lambda:[root.destroy()])
    ex.place(x=77,y=100)
    
    
    

    root.mainloop()

if __name__=='__main__':
    play()