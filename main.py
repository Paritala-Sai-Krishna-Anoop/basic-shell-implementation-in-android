from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.config import Config
from kivy.uix.textinput import TextInput
from kivy.uix.popup import Popup
import os
from datetime import date
import shutil

Config.set('graphics', 'width', '800')
Config.set('graphics', 'height', '1300')

class Layout(FloatLayout):
    def __init__(self,**kwargs):
        super().__init__(**kwargs)
        
        
        self.heading=Label(text=".......CDSS PROJECT BASIC SHELL.......",font_size ='40sp',size_hint=(.5,.5),
        pos_hint={"x":0.25,"y":.57}, bold=True)
        
        self.label1=Label(text="Please Enter the Grammar",font_size ='40sp',size_hint=(.2,.2),
        pos_hint={"x":0.4,"y":.57})
        
        self.command=TextInput(text="",multiline=False,size_hint=(.5,.05),
        pos_hint={"x":0.2,"y":.57})
        
        
        self.check=Button(text='CHECK',size_hint=(.2,.05),bold=True,
        pos_hint={"x":0.5,"y":.33})
        self.check.bind(on_press=self.call_popup)
        
        self.popup=Popup(title="Output",size_hint=(.5,.5),content=Label(text=""))

        self.enter=Button(text='ENTER',size_hint=(.2,.05),bold=True,
        pos_hint={"x":0.5,"y":.11})
        
        self.echotext=TextInput(text="Enter the text to echo",multiline=False,size_hint=(.5,.05),
        pos_hint={"x":0.2,"y":.2})
        
        self.add_widget(self.command)
        self.add_widget(self.heading)
        self.add_widget(self.label1)
        self.add_widget(self.check)
        
    def extra_text(self,elements):
        if self.command.text =="echo":
                    self.popup.content.text=self.echotext.text+"\n\n\n\n CLICK ANYWHERE OUTSIDE THE POPUP TO EXIT"
        elif self.command.text =="isdir":
            self.popup.content.text=str(os.path.isdir(self.echotext.text))+"\n\n\n\n CLICK ANYWHERE OUTSIDE THE POPUP TO EXIT"
        elif self.command.text =="cat":
            try:
                f = open(self.echotext.text,"w+")
                f.close()
                self.popup.content.text="File Created Successfully"+"\n\n\n\n CLICK ANYWHERE OUTSIDE THE POPUP TO EXIT"
            except OSError as error:
                self.popup.content.text=str(error)+"\n\n\n\n CLICK ANYWHERE OUTSIDE THE POPUP TO EXIT"
        elif self.command.text =="Cat":
            try:
                f = open(self.echotext.text,"r+")
                contents = f.read()
                self.popup.content.text=str(contents)+"\n\n\n\n CLICK ANYWHERE OUTSIDE THE POPUP TO EXIT"
                f.close()
            except OSError as error:
                self.popup.content.text=str(error)+"\n\n\n\n CLICK ANYWHERE OUTSIDE THE POPUP TO EXIT"
        elif self.command.text =="rm":#remove
            try:
              
                os.remove(self.echotext.text)
                self.popup.content.text="File was successfully removed\n\n\n\n CLICK ANYWHERE OUTSIDE THE POPUP TO EXIT"
            except OSError as error:
                self.popup.content.text=error+"\n\n\n\n CLICK ANYWHERE OUTSIDE THE POPUP TO EXIT"
        elif self.command.text =="cp":#copy
            try:
                a = self.echotext.text.split(" ")[0]
                b = self.echotext.text.split(" ")[1]
                shutil.copy(a,b)
                self.popup.content.text="File copied Successfully\n\n\n\n CLICK ANYWHERE OUTSIDE THE POPUP TO EXIT"
            except OSError as error:
                self.popup.content.text=str(error)+"\n\n\n\n CLICK ANYWHERE OUTSIDE THE POPUP TO EXIT"
        elif self.command.text =="mv":#move basefile destination file
            try:
                a = self.echotext.text.split(" ")[0]
                b = self.echotext.text.split(" ")[1]
                shutil.move(a,b)
                self.popup.content.text="File moved Successfully\n\n\n\n CLICK ANYWHERE OUTSIDE THE POPUP TO EXIT"
            except OSError as error:
                self.popup.content.text=str(error)+"\n\n\n\n CLICK ANYWHERE OUTSIDE THE POPUP TO EXIT"
        elif self.command.text =="isfile":#to check whether the file is present or not
            self.popup.content.text=str(os.path.isfile(self.echotext.text))+"\n\n\n\n CLICK ANYWHERE OUTSIDE THE POPUP TO EXIT"
        elif self.command.text =="mkdir":# make directory        
              try: 
                os.mkdir(self.echotext.text) 
                self.popup.content.text="Directory "+self.echotext.text+" is created\n\n\n\n CLICK ANYWHERE OUTSIDE THE POPUP TO EXIT" 
              except OSError as error:                   
                self.popup.content.text=str(error)+"\n\n\n\n CLICK ANYWHERE OUTSIDE THE POPUP TO EXIT"
        elif self.command.text== "rmdir": #remove directory
            try:
                os.rmdir(self.echotext.text)
                self.popup.content.text="Directory "+self.echotext.text+" is removed\n\n\n\n CLICK ANYWHERE OUTSIDE THE POPUP TO EXIT" 
            except OSError as error:
                self.popup.content.text=str(error)+"\n\n\n\n CLICK ANYWHERE OUTSIDE THE POPUP TO EXIT" 
        self.popup.open()
        self.command.text=""
        self.echotext.text=""
        self.remove_widget(self.echotext)
        self.remove_widget(self.enter)
    def call_popup(self,elements):
        if self.command.text=="name":
            self.popup.content.text=str(os.name)+"\n\n\n\n CLICK ANYWHERE OUTSIDE THE POPUP TO EXIT"
            self.popup.open()
            self.command.text=""
        elif self.command.text=="date":
            self.popup.content.text=str(date.today())+"\n\n\n\n CLICK ANYWHERE OUTSIDE THE POPUP TO EXIT"
            self.popup.open()
            self.command.text=""
        elif self.command.text=="gid":
            self.popup.content.text=str(os.getgid())+"\n\n\n\n CLICK ANYWHERE OUTSIDE THE POPUP TO EXIT"
            self.popup.open()
            self.command.text=""
        elif self.command.text=="pwd":
            self.popup.content.text=str(os.getcwd())+"\n\n\n\n CLICK ANYWHERE OUTSIDE THE POPUP TO EXIT"
            self.popup.open()
            self.command.text=""
        elif self.command.text=="pid":
            self.popup.content.text=str(os.getpid())+"\n\n\n\n CLICK ANYWHERE OUTSIDE THE POPUP TO EXIT"
            self.popup.open()
            self.command.text=""
        elif self.command.text =="ls":
            self.popup.content.text=str(os.system("ls"))+"\n\n\n\n CLICK ANYWHERE OUTSIDE THE POPUP TO EXIT"
            self.popup.open()
            self.command.text=""
        elif self.command.text =="echo" or "isdir" or "cat" or "Cat" or "rm" or "cp" or "mv" or "isfile" or "mkdir" or "rmdir" or "exit":
            self.add_widget(self.echotext)
            self.add_widget(self.enter)
            self.enter.bind(on_press=self.extra_text)
        elif self.command.text == "exit":
            App.get_running_app().stop()
        else:
            self.popup.content.text="Bash!!.. command not found..\n\n\n\n CLICK ANYWHERE OUTSIDE THE POPUP TO EXIT"
            self.popup.open()
            self.command.text=""
class CDSSApp(App):

    def build(self):
        return Layout()
CDSSApp().run()
