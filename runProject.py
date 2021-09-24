import sys
# insert at 1, 0 is the script path (or '' in REPL)
sys.path.insert (0,'../Controller')

import Hg

    
def edit():
    while(True):
        f = open('./gesture_db.txt',"r")
        lines = f.readlines()
        #print(lines[3])
        
        print('Current key assignments: ')
        line_number = 1
        for line in lines:
            print(line_number,"finger(s) is used as",line)
            line_number+=1
            
        
        print('Enter the finger number you want to edit.\nPress 0 to go back to main menu: ')
        new_number = input()
        if(new_number == "0"):
            break
        new_item = ['space\n','left arrow\n','right arrow\n','up arrow\n','down arrow\n']
        print('\nEnter one of the following key assignments: ')
        print('1 for space')
        print('2 for left arrow')
        print('3 for right arrow')
        print('4 for up arrow')
        print('5 for down arrow')
        new_item_number = input()
        
        lines[int(new_number)-1] = new_item[int(new_item_number)-1]
        f.close()
        with open('../Model/gesture_db.txt','w') as file:
            file.writelines(lines)
        
        

def execute():
    Hg.run()
    
    
while(True):
    choice = input("Press\n0 to exit\n1 to execute\n2 to edit your gesture bank\nInput: ")
    
    if(choice == "2"):
        edit()
    elif(choice == "1"):
        execute()
    else:
        break