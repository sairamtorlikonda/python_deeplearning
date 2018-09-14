class classemp:
  empcnt=0
  def __init__(self,name,fam,dep,sal):
      self.name=name
      self.fam=fam
      self.sal=sal
      self.dep=dep
      classemp.empcnt+=1

  def display(self):
      print("name:",self.name,"\tFamily name:",self.fam,"\tDepartment:",self.dep,"\tsalary:",self.sal)

class fulltimeemp(classemp):
    def __init__(self,n,f,d,s):
        classemp.__init__(self,n,f,d,s)

employee1=classemp("venkat","K","cs",3000)
employee2=classemp("siva","K","it",3500)
employee3=classemp("sai","K","ECE",4000)
employee4=fulltimeemp("ram","K","civil",5000)
employee1.display()
employee2.display()
employee3.display()
employee4.display()
average=((employee1.sal+employee2.sal+employee3.sal+employee4.sal)/classemp.empcnt)
print("Average salary is:",average)
print("total employees", classemp.empcnt)