import tkinter as tk
from tkinter import Canvas
from PIL import ImageTk, Image
import os
from tkinter import filedialog

# GUI application window
win = tk.Tk()
win.title('Img to Pdf converter application')
win.geometry('750x600')
win.iconphoto(False, tk.PhotoImage(file = 'images\\pdf.png'))
win.resizable(0,0)

def disable(btn):
    btn['state']='disabled'

def enable(btn):
    btn['state']='active'

files = {}
def upload_imgs():
    global files
    files['filename']=filedialog.askopenfilenames(filetypes=[('JPG','*.jpg'),('PNG','*.png'),('JPEG','*.jpeg')],
    initialdir = os.getcwd(), title='Select File/Files')
    if len(files['filename'])!=0:
        enable(download_button)
    

def saveas():
    try:
        img_list = []
        for file in files['filename']:
            img_list.append(Image.open(file).convert('RGB'))
        save_file_name = filedialog.asksaveasfilename(filetypes = [('PDF','*.pdf')], initialdir=os.getcwd(), title='Save File')
        img_list[0].save(f'{save_file_name}.pdf', save_all=True, append_images = img_list[1:])
        disable(download_button)
    except:
        return


# main img of application
canvas = Canvas(win, bg='white',width = 300, height=150)
canvas.grid(row =0,column=0, sticky=tk.N, padx=220, pady =25)

main_img = ImageTk.PhotoImage(Image.open('images\\img.jpg'))
canvas.create_image(150,75, image=main_img)

# info img of application
canvas_info = Canvas(win, bg='white', width = 700, height=180)
canvas_info.grid(row=1, column =0, padx =25)

info_img = ImageTk.PhotoImage(Image.open('images\\wlc.jpg'))
canvas_info.create_image(352,92, image =info_img)

# upload button
upload_button = tk.Button(win, text='UPLOAD IMAGES', width = 20, height =1,font=('arial',14,'bold'), bg='white',fg='green', command=upload_imgs)
upload_button.grid(row =2, column = 0, padx=200, pady =20)

# Download button
download_button = tk.Button(win, text='Download PDF', width = 20, height =1,font=('arial',14,'bold'), bg='white',fg='red', command=saveas)
download_button.grid(row=3, column=0)
disable(download_button)


win.mainloop()