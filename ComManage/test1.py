# from tkinter import *
# from pandastable import Table

# root = Tk()
# frame = Frame(root)
# frame.pack()
# pt = Table(frame)
# pt.show()
# root.mainloop()

# def infinite_seq():
#     num=0
#     while True:
#         yield num
#         num+=1

# t= infinite_seq()
# print(t)

def infinite_seq():
    num= 'I am first'
    yield num
    num='I am second'
    yield num

t= infinite_seq()
print(next(t))


# def infinite_seq1():
#     num=0
#     while True:
#         num+=1
#         print(num)
        

# t= infinite_seq1()

