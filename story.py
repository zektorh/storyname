x = ["hossein", "reza", "ali"]           
print(x)
y = input("enter a name from a list: ")


def story(name):
    if name == x[0]:
        print("hossein is born in iran, arak and he is a developer!")
    elif name == x[1]:
        print("reza is born in tehran and he work in giftshop and he has a wife")
    elif name == x[2]:
        print("ali was born in kordestan and he is a worker he get 22 tomarow!")
    else:
        print("your name is not on a list!!!")
story(y)
while True:
    
    t = input("enter an ohter name: ")
    story(t)

 # این برنامه جوری هست که اگه بهش اسم های درون لیست را بدی داستان زندگی شون را میگه