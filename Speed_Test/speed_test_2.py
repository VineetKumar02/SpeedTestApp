from tkinter import *
import speedtest

root = Tk()   #main Window is called 'root'
root.title("Internet Speed Test")   #Giving Title to window 'root'
root.resizable(False, False)   #can't rescale the window
root.configure(bg = "#141527")   #set dark background color

#Dimensions for the Window
w = 500
h = 800

#Code to get coordinates to place window at center
ws = root.winfo_screenwidth()
hs = root.winfo_screenheight()
x = (ws/2) - (w/2)
y = (hs/2) - (h/2)

root.geometry('%dx%d+%d+%d' % (w, h, x, y))   #place the window 'root'


def Test():
    test = speedtest.Speedtest()
    servernames = []
    test.get_servers(servernames)
    data = test.get_config()
    service_data = data['client']['isp']
    ip_data = data['client']['ip']
    uploading = round(test.upload()/(1024*1024),2)
    downloading = round(test.download()/(1024*1024),2)

    upload.config(text = uploading)
    download.config(text = downloading)
    Download.config(text = downloading)
    ping.config(text=test.results.ping)
    service.config(text=service_data)
    ip.config(text=ip_data)
    # Loading.config(text = "")

def Check():
    # Loading.config(text = "Loading...")
    Test()

# #Set all data to 00
def Reset():
    Download.config(text = "00")
    upload.config(text = "00") 
    download.config(text = "00")
    Download.config(text = "00")
    ping.config(text = "00")   
    service.config(text = "- - -")   
    ip.config(text = "- - - - - - - -")   


#icon for window
image_icon = PhotoImage(file = "images/logo.png")
root.iconphoto(False,image_icon)

#Images for UI and buttons
Top = PhotoImage(file = "images/background.png")
Label(root,image = Top,bg="#141527").place(x=0,y=0)


Reset_Image = PhotoImage(file="images/reset.png")
Reset_Button = Button(root,image=Reset_Image,bg="#141527",bd=0,activebackground="#141527",cursor="hand2",command=Reset)
Reset_Button.place(x=215,y=618)

Test_Image = PhotoImage(file="images/button.png")
Test_Button = Button(root,image=Test_Image,bg="#141527",bd=0,activebackground="#141527",cursor="hand2",command=Check)
Test_Button.place(x=150,y=700)



#Labels to show values
ping = Label(root,text="00",font="arial 20",bg="#141527",fg="#e9b342")
ping.place(x=110,y=240,anchor="center")

download = Label(root,text="00",font="arial 20",bg="#141527",fg="#0cf107")
download.place(x=250,y=240,anchor="center")

upload = Label(root,text="00",font="arial 20",bg="#141527",fg="#e61c25")
upload.place(x=390,y=240,anchor="center")

Download = Label(root,text="00",font="arial 30",bg="#141527",fg="#00FFFF")
Download.place(x=250,y=480,anchor="center")

service = Label(root,text="- - -",font="arial 12",bg="#141527",fg="white")
service.place(x=65,y=670,anchor="center")

ip = Label(root,text="- - - - - - - -",font="arial 12",bg="#141527",fg="white")
ip.place(x=425,y=670,anchor="center")

# Loading = Label(root,text="",font="arial 10 ",bg="#141527",fg="#00FF00")
# Loading.place(x=200,y=470,anchor="center")


root.mainloop()