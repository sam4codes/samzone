telbook={}
print("1-create the contact")
print("2-show")
print("3-edit")
print("4-del")
print("5-exit")
def create():
    tedad=int(input("tedad"))
    for i in range(tedad):
        name=input("enter name")
        tel=input("enter your tel pls:")
        telbook[name]=tel
        return telbook
def show():
    print(telbook)
def edit():
    name=input("enter name for edit")
    newtel=input("tel")
    telbook[name]=newtel
    return telbook
def delete():
    name=input("enter name for del")
    del telbook[name]
    return telbook
while True:
    op=int(input("enter your choice pls"))
    if op==5:
        break
    elif op==1:
        create()
    elif op==2:
          show()
    elif op==3:
          edit()
    elif op==4:
        delete()
        name=input("enter name for del")
