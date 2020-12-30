#Importing required packages
import json  
import time 
import os
import sys

class Functions:
    def __init__(self):
        self.t={}
        if not os.path.isfile('crd.json'):
            #Creating empty json file if it is not present 
            with open('crd.json','w') as fileWrite:
                json.dump({},fileWrite)
        else:
            #Loading data from the json file
            with open('crd.json','r') as fileRead:
                data_load=json.load(fileRead)
                self.t=data_load 

    def create(self):
        #Getting key from the user to add the value to the file
        key=input('Enter key to add value in file: ')

        #Checking whether key is capped at 32 chars
        while len(key)>32:
            print('Error : Key length should be less than 32')
            key=input('Enter key of length should not exceed 32 characters: ')

        if key in self.t:
            #if key is already present checking whether it is expired
            if self.t[key]['time']!=0 and int(round(time.time() * 1000))>self.t[key]['time']:
                #if the key is expired delete it from the file
                del(self.t[key])
                with open('crd.json','w') as fileWrite:
                    json.dump(self.t,fileWrite)
            else:
                #if the key is not expired displaying the appropriate error message
                while key in self.t:
                    print('Error : Key is already present ')
                    key=input('Please enter unique key to add value in file: ')

        #Getting the values from the user
        name=input('Please enter the name: ')
        age=int(input('Please enter the age: '))
        address=input('Please enter the address: ')
        number=int(input('Please enter the mobile number: '))
        d={"name":name,"age":age,"address":address,"mobile number":number}

        #Checking whether the file exceeds size of 1GB 
        if os.path.getsize('crd.json')+sys.getsizeof(d)>1073741824:
            print('The file has exceeds 1GB So the value is not added to the file')
            quit() 
        
        #Checking whether value is capped at 16KB
        while sys.getsizeof(d)>16384:
            print('Please enter the value with less than 16KB')
            name=input('Please enter the name: ')
            age=int(input('Please enter the age: '))
            address=input('Please enter the address: ')
            number=int(input('Please enter the mobile number: '))
            d={"name":name,"age":age,"address":address,"mobile number":number} 
        
        #Setting the time to live property to the key
        ti=input('Do you want to set expiry time to the key enter yes/no: ')
        if ti=='yes' :
            Time=int(input('Enter the time in seconds'))
            d["time"]=int(round(time.time() * 1000))+(Time*1000) 
        else:
            d["time"]=0
        self.t[key]=d 

        #Loading data to the json file
        with open('crd.json','w') as fileWrite:
            json.dump(self.t,fileWrite)
        print('Values added to file successfully')

    def read(self):
        #Getting key from the user to read the value from the file
        key=input('Enter key to read the value from file: ')
        
        #Checking whether key is capped at 32 chars
        while len(key)>32:
            print('Error : Key length should be less than 32')
            key=input('Enter key of length should not exceed 32 characters: ')

        #Checking whether key is present in file or not    
        while key not in self.t:
            print('Error: Key is not present in the file')
            key=input('Enter the correct key: ')

        #Checking whether key is expired or not    
        if self.t[key]['time']!=0 and int(round(time.time() * 1000))>self.t[key]['time']:
            #if the key is expired delete it from the file
            del(self.t[key])
            with open('crd.json','w') as fileWrite:
                json.dump(self.t,fileWrite)
            print('Key has been expired')
        else:
            #if the key is not expired display the value to the user
            di={}
            print('Value to the corresponding key is')
            for i,j in self.t[key].items():
                if i!='time':
                    di[i]=j 
            data=json.dumps(di,indent=4)
            print(data)

    def delete(self):
        #Getting key from the user to delete the value from the file
        key=input('Enter key to delete the value in file: ')
        
        #Checking whether key is capped at 32 chars
        while len(key)>32:
            print('Error : Key length should be less than 32')
            key=input('Enter key of length should not exceed 32 characters: ')

        #Checking whether key is present in file or not
        while key not in self.t:
            print('Key is not present in the file')
            key=input('Enter the correct key: ')

        #Checking whether key is expired or not
        if self.t[key]['time']!=0 and int(round(time.time() * 1000))>self.t[key]['time']:
            #if the key is expired delete the value from the file and display the appropriate error message
            del(self.t[key])
            with open('crd.json','w') as fileWrite:
                json.dump(self.t,fileWrite)
            print('Key has been expired')
        else:
            #if the key is not expired delete the value from the file
            del(self.t[key])
            with open('crd.json','w') as fileWrite:
                json.dump(self.t,fileWrite)
            print('Value deleted from the file successfully')