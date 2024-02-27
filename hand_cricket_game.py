from tkinter import *
import tkinter as tk
from random import randint

from tkinter import messagebox
def play_hand_cricket():
    user_score =0
    computer_score =0
    def batting_window():
        bat_window =tk.Toplevel(top)
        bat_window.title("----BATTING----")
        bat_window.geometry("400x400")
        input_entry = tk.Entry(bat_window)
        input_entry.pack(side='top')
        result_label = tk.Label(bat_window)
        result_label.pack(side='top')
        result_label.config(text="---YOU ARE BATTING NOW---")
        instructions_label = tk.Label(bat_window, text="ENTER THE NUMBER FROM 1 TO 10 ",height=2)
        instructions_label.pack()
        def batting(score):
            nonlocal user_score
            nonlocal computer_score
            computer_choice=randint(1,10)
            
            if score >10:
                result_label.config(text=f"INVALID ENTRY")
                score=0
            elif score == computer_choice:
                result_label.config(text=f"\nYOUR CHOICE:{score}\nCOMPUTER'S CHOICE:{computer_choice} \nYOUR SCORE: {user_score}")
                result=messagebox.showerror("RESULT","THAT'S !! OUT ")
                submit_button.config(state=tk.DISABLED)
                bat_button.config(state=tk.DISABLED)
                result=messagebox.showwarning("RESULT"," * YOU COMPLETED BATTING !!\n*  NEXT BOWLLING TURN \n* IF BOTH ARE COMPLETED CHECK YOUR RESULT")
                
            else:
                user_score += score

                result_label.config(text=f" \nYOUR CHOICE:{score} \nCOMPUTER'S CHOICE:{computer_choice} \nYOUR SCORE: {user_score}")
            

        
        
        submit_button = tk.Button(bat_window, text="Submit",activeforeground='grey59',bg='beige',font='Bold',command=lambda: batting(int(input_entry.get())))
        submit_button.pack()
       
    def bowling_window():
        bowl_window =tk.Toplevel(top)
        bowl_window.title("----BOWLING----")
        bowl_window.geometry("400x400")
        
        def bowling(score):
            nonlocal user_score
            nonlocal computer_score
            computer_choice=randint(1,10)
            if score >10:
                result_label.config(text=f"INVALID ENTRY")
                score=0
            elif score == computer_choice:
                result_label.config(text=f"\nYOUR CHOICE:{score} \n\nCOMPUTER'S CHOICE:{computer_choice} \n\nCOMPUTER SCORE: {computer_score}")
                result=messagebox.showerror("RESULT","THAT'S  OUT!!")
                result=messagebox.showwarning("RESULT","\n * YOU COMPLETED BOWLING !!\n* NEXT BATTING TURN \n* IF BOTH ARE COMPLETED CHECK YOUR RESULT")
                submit_button.config(state=tk.DISABLED)
                bowl_button.config(state=tk.DISABLED)
            else:
                computer_score += computer_choice
                result_label.config(text=f" \nYOUR CHOICE:{score} \nCOMPUTER'S CHOICE:{computer_choice} \nCOMPUTER SCORE: {computer_score}")
        result_label = tk.Label(bowl_window)
        result_label.pack()
        result_label.config(text="---YOU ARE BOWLING NOW---")
        instructions_label = tk.Label(bowl_window, text="ENTER THE NUMBER FROM 1 TO 10 ",height=2)
        instructions_label.pack()
        input_entry = tk.Entry(bowl_window)
        input_entry.pack()
        submit_button = tk.Button(bowl_window, text="Submit",activeforeground='grey59',bg='beige',font='Bold',command=lambda: bowling(int(input_entry.get())))
        submit_button.pack()
    
    def result():
        nonlocal user_score
        nonlocal computer_score
        if bat_button['state'] == tk.DISABLED  and  bowl_button['state'] == tk.DISABLED:
            if user_score >computer_score:
                result=messagebox.showinfo("RESULT","YOU WON")
                    
            elif user_score < computer_score:
                result=messagebox.showinfo("RESULT","COMPUTER WON")
            else:
                result=messagebox.showinfo("RESULT","-MATCH TIED-")
        else:
            result=messagebox.showerror("RESULT","--GAME  IS NOT YET COMPLETED-- ") 
    top = tk.Tk()
    top.title("HAND CRICKET")
    top.geometry("400x400")
    bat_button = tk.Button(top, text="BAT",relief=SUNKEN,width=10,height=2,activeforeground='grey59',bg='beige',font='Bold',command= batting_window)
    bat_button.pack()
    bowl_button =tk.Button(top, text="BOWL",relief=RAISED,width=10,height=2,activeforeground='grey59',bg='beige',font='Bold',command= bowling_window)
    bowl_button.pack()
    result_button= tk.Button(top,text="RESULT",relief=GROOVE,width=10,height=2,activeforeground='grey59',bg='beige',font='Bold',command=result)
    result_button.pack(side="bottom")
   
    top.mainloop()
    
play_hand_cricket()




