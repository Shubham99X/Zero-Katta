from tkinter import * 
from tkinter import messagebox


root = Tk()
root.title("Zero Katta")
root.geometry("281x303")

chance = True
moves = 0
game_over = False

def disable_btns():
    b1.config(state=DISABLED)
    b2.config(state=DISABLED)
    b3.config(state=DISABLED)
    b4.config(state=DISABLED)
    b5.config(state=DISABLED)
    b6.config(state=DISABLED)
    b7.config(state=DISABLED)
    b8.config(state=DISABLED)
    b9.config(state=DISABLED)

def change_btn(u1,u2,u3):
    global game_over
    winner = u1['text']
    u1.config(bg='green')
    u2.config(bg='green')
    u3.config(bg='green')
    game_over = True
    messagebox.showinfo('Congratulations !!',f'{winner} won the game !!')
    disable_btns()

def if_won():
    global b1,b2,b3,b4,b5,b6,b7,b8,b9
    if b1['text'] == b2['text'] and b2['text'] == b3['text'] and b1['text'] != ' ':
        change_btn(b1,b2,b3)
    elif b4['text'] == b5['text'] and b5['text'] == b6['text'] and b4['text'] != ' ':
        change_btn(b4,b5,b6)
    elif b7['text'] == b8['text'] and b8['text'] == b9['text'] and b7['text'] != ' ':
        change_btn(b7,b8,b9)
    elif b1['text'] == b4['text'] and b4['text'] == b7['text'] and b1['text'] != ' ':
        change_btn(b1,b4,b7)
    elif b2['text'] == b5['text'] and b5['text'] == b8['text'] and b2['text'] != ' ':
        change_btn(b2,b5,b8)
    elif b3['text'] == b6['text'] and b6['text'] == b9['text'] and b3['text'] != ' ':
        change_btn(b3,b6,b9)
    elif b1['text'] == b5['text'] and b5['text'] == b9['text'] and b1['text'] != ' ':
        change_btn(b1,b5,b9)
    elif b3['text'] == b5['text'] and b5['text'] == b7['text'] and b3['text'] != ' ':
        change_btn(b3,b5,b7)

    

def clicked(b):
    global chance, moves, game_over
    if b['text'] == ' ':
        if chance == True:
            b['text'] = 'O'
            chance = False
        else:
            b['text'] = 'X'
            chance = True
        moves+=1
        if_won()
        if moves == 9 and game_over == False:
            game_over = True
            messagebox.showinfo('Game Over !!','Its a tie !!')
            disable_btns()
    else:
        messagebox.showwarning("Oops !!","Please select different box !!")

def reset_game():
    global b1,b2,b3,b4,b5,b6,b7,b8,b9,chance,moves,game_over
    
    chance = True
    moves = 0
    game_over = False
    
    b1.config(text=" ", bg="white", font=("Helvetica",9,'bold'), state=ACTIVE)
    b2.config(text=" ", bg="white", font=("Helvetica",9,'bold'), state=ACTIVE)
    b3.config(text=" ", bg="white", font=("Helvetica",9,'bold'), state=ACTIVE)
    
    b4.config(text=" ", bg="white", font=("Helvetica",9,'bold'), state=ACTIVE)
    b5.config(text=" ", bg="white", font=("Helvetica",9,'bold'), state=ACTIVE)
    b6.config(text=" ", bg="white", font=("Helvetica",9,'bold'), state=ACTIVE)
    
    b7.config(text=" ", bg="white", font=("Helvetica",9,'bold'), state=ACTIVE)
    b8.config(text=" ", bg="white", font=("Helvetica",9,'bold'), state=ACTIVE)
    b9.config(text=" ", bg="white", font=("Helvetica",9,'bold'), state=ACTIVE)
    


b1 = Button(root,text=" ", bg="white", font=("Helvetica",9,'bold'), height=6, width=12, command=lambda : clicked(b1))
b2 = Button(root,text=" ", bg="white", font=("Helvetica",9,'bold'), height=6, width=12, command=lambda : clicked(b2))
b3 = Button(root,text=" ", bg="white", font=("Helvetica",9,'bold'), height=6, width=12, command=lambda : clicked(b3))

b4 = Button(root,text=" ", bg="white", font=("Helvetica",9,'bold'), height=6, width=12, command=lambda : clicked(b4))
b5 = Button(root,text=" ", bg="white", font=("Helvetica",9,'bold'), height=6, width=12, command=lambda : clicked(b5))
b6 = Button(root,text=" ", bg="white", font=("Helvetica",9,'bold'), height=6, width=12, command=lambda : clicked(b6))

b7 = Button(root,text=" ", bg="white", font=("Helvetica",9,'bold'), height=6, width=12, command=lambda : clicked(b7))
b8 = Button(root,text=" ", bg="white", font=("Helvetica",9,'bold'), height=6, width=12, command=lambda : clicked(b8))
b9 = Button(root,text=" ", bg="white", font=("Helvetica",9,'bold'), height=6, width=12, command=lambda : clicked(b9))

b1.grid(row=0, column=0,)
b2.grid(row=0, column=1)
b3.grid(row=0, column=2)

b4.grid(row=1, column=0)
b5.grid(row=1, column=1)
b6.grid(row=1, column=2)

b7.grid(row=2, column=0)
b8.grid(row=2, column=1)
b9.grid(row=2, column=2)

#menu for restarting the game

my_menu = Menu(root)
root.config(menu=my_menu)

#restart option
option_menu = Menu(my_menu, tearoff=False)
my_menu.add_cascade(menu=option_menu, label='Options')
option_menu.add_command(label='Restart Game',command=reset_game)

root.resizable(0,0)
root.mainloop()