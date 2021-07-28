class student:
    def __init__(self,name,rollNo, rank, remarks):
        self.name=name
        self.rollNo=rollNo
        self.rank=rank
        self.remarks=remarks
    
    def reportCard(self,name,remarks):
        print("The overall performance of "+name+" is "+ remarks)
    
        
student1=student("Aathmika",8109,"Ist","Good")

student1.reportCard("Aathmika","Good")

print(student1.name)
print(student1.rollNo)
