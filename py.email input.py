class person:
    def __init__(self,fname,lname):
        self.fname=fname
        self.lname=lname
    def full_name(self):
        return f'(self.name)(self.lname)'
    @property

    def email (self):

        return f'(self.fname)(input("which char?")(self.lname)'
    a= int(input("how many people?"))
    for i in range (a):
           f=input("name")
           l=input("last name")

           m=person(f,1)
           print(m.email)
