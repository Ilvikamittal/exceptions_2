from tkinter import*
from tkinter import messagebox
root=Tk()

root.title("expetions handling")
root.geometry("400x400")

list=["snow white","rupanzel","jasmine","frozen","cindrella"]
dic_2={
       "name":"kshitij",
       "age":"13"
       }



try:
    print(dic_2["address"])
    print(list[8])
    

except KeyError: 
    print("address not found")
    
    messagebox.showwarning("key error","The key does not exist")
    
except IndexError:
    print("Index does not exist")
    messagebox.showinfo("index error","the index does not exist")
          

root.mainloop()