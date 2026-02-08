import datetime
class Student:
    def __init__(self,student_id,name,total_workings,present_days):
        self.student_id = student_id
        self.name = name
        self.total_workings = total_workings
        self.present_days = present_days

    def attendance_percentage(self):
        return (self.present_days / self.total_workings) * 100

    def is_eligible(self):
        return self.attendance_percentage() >= 75
    

    def generate_report(self):
        status="Eligible" if self.is_eligible() else "Not Eligible"
        print(f"Student ID :{self.student_id}")
        print(f"Name : {self.name}")
        print(f"Attendance : {self.attendance_percentage():.2f}%")
        print(f"status : {status}\n")



    def log_status(self):
            status="Eligible" if self.is_eligible() else "Not Eligible"
            timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H %M %S")

            with open("data_log.txt","a") as file:
                file.write(f"{timestamp}|{self.student_id}|{self.name} {self.attendance_percentage():.2f}% {status}\n")


s1=Student(5291,"Ajay",120,65)
s2=Student(5292,"Koushik",120,110)
s3=Student(5293,"Varun",120,90)
s4=Student(5294,"Rohith",120,85)

students = [s1,s2,s3,s4] 

for s in students:
    s.generate_report()
    s.log_status()

        