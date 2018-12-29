curl https://raw.githubusercontent.com/MicrosoftLearning/intropython/master/elements1_20.txt -o elements1_20.txt 
elements = open("elements1_20.txt",'r') 
element_names = [] 
element_lines = elements.readlines()
elements.seek(0)
for number in range(0,len(element_lines)):
    element_names.append(elements.readline().strip().lower())

def get_names():
     count = 0
     names_list = []
     while count <5:
         user_input = input("Enter the name of an element: ")
         if user_input == "":
             print("please enter a name: ")
         elif user_input in names_list:
             print(user_input,'was already entered')
         else:
             names_list.append(user_input)
             count +=1
     return(names_list)

names_list = get_names()  
found = [] 
not_found = [] 
count = 0 

while count<5:
     if names_list[count] in element_names:
         found.append(names_list[count])
         count +=1     
     else:
         not_found.append(names_list[count])
         count +=1  

print() 
space = ", " 
score = 20*int(len(found)) 
print(score,"% correct") 
print("Found:",space.join(found))   
print("Not found:",space.join(not_found))  
elements.close() 