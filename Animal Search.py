import requests
from Tkinter import *
from tkMessageBox import *
import json

root=Tk()
root.title("Breed Search")
root.minsize(width=666, height=666)
root.maxsize(width=666, height=666)
Label(root,text="Enter A Term").pack()
e=Entry(root)
e.pack()


def parse_json(data):
    json_response=json.loads(data)
    if int(json_response['petfinder']['header']['status']['code']['$t']) == 100:
        scrollbar = Scrollbar(root)
        scrollbar.pack( side = RIGHT, fill = Y )
        breed_list = Listbox(root, yscrollcommand = scrollbar.set)
        for breed_name in json_response['petfinder']['breeds']['breed']:
            breed_list.insert(END, breed_name['$t'])
        breed_list.pack( side = LEFT, fill = BOTH,expand=1 )
        scrollbar.config( command = breed_list.yview )
    else:
        showerror("Not Found","Searched Animal Not Found");

    
def search():
    try:
        request = requests.get('http://api.petfinder.com/breed.list?key=ad4e5f02703f7faf7945ab02d55fa136&format=json&animal='+str(e.get()))
    
        if request.status_code == 200:
            parse_json(request.text)
        else:
            showerror("Error","Api Error Response Code"+request.status_code);
    except requests.exceptions.RequestException as error:    
        showerror("Error","No Working Internet Connection");
Button(root,text="Search",command=search).pack()
root.mainloop()
