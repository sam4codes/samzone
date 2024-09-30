class Employee:
    def __init__(self,fname,lname,code,salary):
        self.fname=fname
        self.lname=lname
        self.code=code
        self.salary=salary
    def __del__(self):
        print("objec is deleted")
    def tax (self):
        if self.salary<200000000:
            return 0
        else:
            return self.salary*0.1
    def insurance(self):
        return self.salary*0.07
    def payment(self):
        return self.salary-(self.tax()+self.insurance())
    def __str__(self):
        s="code"+self.code
        s+="\t\t first name:  "+self.fname
        s+="\t\t last name:   "+self.lname
        s+="\n salary :"+str(self.salary)
        s+="\n tax: "+str(self.tax())
        s+="\t\t insurance:"+str(self.insurance())
        s+="\n your payment is: "+str(self.payment)
        return s
class Teacher(Employee):
    def __init__(self,fname,lname,code,salary,course):
        super() .__init__(self,fname,lname,code,salary)
        self.course=course
        def course(self):
            print("i have a course")


fname=input("enter your fname pls:")
lname=input("enter your lname pls:")
code=input("enter your code pls:")
salary=input(input("enter your salary pls:"))
e=Teacher(fname,lname,code,salary)
print(str(e))
del e
