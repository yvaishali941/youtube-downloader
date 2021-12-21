from tkinter.font import BOLD
import pytube
from pytube import YouTube
import os
from tkinter import *
from tkinter import messagebox as tmsg
from tkinter import filedialog as fd
import requests


class convert(Tk):
    def __init__(self) :
        super().__init__()

        self.title("YTD Audio-Video Downloader")
        self.geometry("700x600")
        #self.config(bg="pink")
        global directory

        def openfolder():

            global directory
            directory=fd.askdirectory()


        def download():
            sbar.config(text="your file downloading...............")
            sbar.update()
            y=url_entry.get()
            yt= YouTube(y)

            x=title.get()


            if x== "50 kbps-Audio":
                stream=yt.streams.get_by_itag(249)
        
            elif x== "70 kbps-Audio":
                stream=yt.streams.get_by_itag(250)
            
            elif x== "128 kbps-Audio":

                stream=yt.streams.get_by_itag(140)
            elif x== "160 kbps-Audio":

                stream=yt.streams.get_by_itag(251)
            elif x== "360P-Video":

                stream=yt.streams.get_by_itag(18)
            elif x== "360P-Video":

                stream=yt.streams.get_by_itag(22)

            else:

                stream=yt.streams.get_by_itag(137)

            openfolder()
            out_file = stream.download(directory)
            base,ext=os.path.splitext(out_file)
            audio= base+".mp3"
            os.rename(out_file,audio)
            sbar.config(text="your file downloaded.....")
            sbar.update()
            tmsg.showinfo(title="download status",message= yt.title+"your file sucessfully downloaded")
            print(yt.title+"your file sucessfully downloaded")

        def click(event):
            url_entry.config(state=NORMAL)
            url_entry.delete(0,END)

        mainframe=Frame(self,height=30)
        mainframe.pack(pady=50)
        url_entry=Entry(mainframe,font=("timesnewroman",30),relief=RIDGE)
        url_entry.insert(0,"paste your link here")
        url_entry.config(state=DISABLED)
        url_entry.bind("<Button-1>",click)
        url_entry.pack(side=LEFT)

        
        

        title=StringVar()
        title.set("download_option")
        progressive=["50 kbps-Audio","70 kbps-Audio","128 kbps-Audio","160 kbps-Audio","360P-Video","7200P-Video","1080P-Video"]

        download_option = OptionMenu(mainframe,title, *progressive)
        download_option.config(height=2,background="green")
        download_option.pack(side=LEFT)
        sbar=Label(self,text="YTD downloader is ready",font=("times new roman",12,BOLD),relief=SUNKEN,anchor="e")
        sbar.pack(side=BOTTOM,fill="x")


        button=Button(self,text="submit",command=download)
        button.pack()



if __name__ == "__main__":
    convert=convert()
    convert.mainloop()

