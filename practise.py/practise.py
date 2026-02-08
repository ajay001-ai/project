# import os 
# path = r"C:\Users\91837\Downloads"
# items = os.listdir(path)
# for item in items:
#     print(item)

#seperating files and folders

# import os
# path = r"C:\Users\91837\Downloads"

# for item in os.listdir(path):
#     full_path = os.path.join(path,item)
#     if os.path.isfile(full_path):
#         print("File :",item)
#     else:
#         print("Folder :",item)

# import os
# path = r"C:\Users\91837\Downloads"
# for root, dirs, files in os.walk(path):
#     print("Current Folder :",root)
#     for dir in dirs:
#         print("Directories :",dir)
#         for file in files:
#             print("File :",file)

# import os
# path = r"C:\Users\91837\Downloads"
# for root,dirs,files in os.walk(path):
#     for file in files:
#         if file.endswith(".py"):  #it is used for .txt also
#             print(os.path.join(root,file))

# import os 
# path = r"C:\Users\91837\Downloads"
# for root,dirs,files in os.walk(path):
#     for file in files:
#         if file.endswith(".py"):
#             path1 = os.path.join(root,file)
#             print("\nReading :",path1)
#             with open(path1,"r") as f:
#                 print(f.read())

#counting files by extention

# import os
# count = {}
# path = r"C:\Users\91837\Downloads"
# for root,dirs,files in os.walk(path):
#     for file in files:
#         ext = file.split(".")[-1]
#         count[ext] = count.get(ext,0) + 1
# print(count)

# l1 = ["10","20","30"]
# marks = list(map(int,l1))
# print(marks)
# from datetime import datetime
# now = datetime.now()
# print(now)
# print(now.year)
# print(now.month)
# print(now.day)
# print(now.strftime("%d-%m-%Y %H:%M:%S"))
# date_str = "24-01-2026"
# d = datetime.strptime(date_str,"%d-%m-%Y")
# print(d)
# from datetime import date
# d1 = date(2026,1,24)
# d2 = date(2025,1,10)
# diff =  d1-d2
# print(diff.days)
import re
text = 'this is ajay kumar phone no 9876654321 , 9876554321'
pattern = r"\d{10}"
matchs = re.search(pattern,text)
print(matchs.group())
