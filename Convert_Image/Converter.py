"""this program changes
the format of images to the other format"""

from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from tkinter import messagebox
from PIL import Image
import os

# create an instance
convert = Tk()
convert.title('converter')
convert.geometry('600x400')
# don't change its size
convert.resizable(width=False, height=False)
# get icon
convert.iconbitmap('converter.ico')
convert.config(bg='#fbede7')

# Label ========================================================================
welcome_label = Label(master=convert, text='Welcome to converter', font=('Dela Gothic One', 12, 'bold'),
                      anchor=CENTER, fg='#e14d1a', bg='#fbede7')
welcome_label.pack(anchor=N, pady=10, fill=BOTH)

# Label for getting url ============================================================
get_url = StringVar()


# if your pointer come on it,its color will be change
def change_color_enter1(button):
    button['bg'] = '#fbedf0'


# if your pointer leave it, its color get back to original of color
def change_color_leave1(button):
    button['bg'] = 'white'


url_label = Label(master=convert, textvariable=get_url, font=('Dela Gothic One', 8, 'bold'),
                  anchor=W, bg='white', width=80, border=2, relief=GROOVE)
url_label.bind('<Enter>', func=lambda i: change_color_enter1(url_label))
url_label.bind('<Leave>', func=lambda i: change_color_leave1(url_label))
url_label.place(x=20, y=50, relheight=0.07)


# this function is used for open path of image
def open_program():
    global my_program
    my_program = filedialog.askopenfilename(title='Select file',
                                            filetypes=(
                                                ("png files", "*.png"), ("jpg files", "*.jpg"), ("all files", "*.")))
    global path, image
    try:
        # get name image
        image = Image.open(my_program)
        path = os.path.split(my_program)[1]
        url_label.config(get_url.set(path))
        # open the program
        # os.system('"%s"' % my_program)
    except:
        messagebox.showinfo(title='Message Box', message='Invalid file',
                            detail='Choose : JPEG, PNG, ICO, thumbnail', icon='error')


browser = Button(master=convert, text='Browse', font=('Dela Gothic One', 10, 'bold'),
                 width=20, activebackground='#fdf6f6', bg='#925353', fg='white', activeforeground='#925353',
                 command=open_program)
browser.place(x=20, y=100, relheight=0.07)

# List box (JPEG,ICO,PNG,THUMBNAIL)
format_image = StringVar()
format_image.set('jpeg')
font = ('Dela Gothic One', 12, 'bold')
list_box_format = ttk.Combobox(convert, textvariable=format_image,
                               values=('png', 'ico', 'jpeg', 'thumbnail'), font=font,
                               state='normal', justify=CENTER)
list_box_format.option_add('*TCombobox*Listbox.font', font)
list_box_format.place(x=382, y=100)


# CONVERT BUTTON ================================================
# this FUNCTION changes images to another format that you want
def change_format():
    global get_format
    # get format from listbox
    get_format = format_image.get()
    if get_format == 'thumbnail':
        return convert_format.set(path)

    else:
        # change the format
        get_path = path.split('.')[0] + '.' + get_format
        convert_format.set(get_path)
        return get_path


# this function is for saving image
def save_image():
    if get_format == 'thumbnail':
        # change image to thumbnail
        image.thumbnail((90, 90), resample=Image.BICUBIC)
        # get path (path,name of image + its format)
        path = os.path.splitext(my_program)[1]
        path_file = filedialog.asksaveasfilename(title='save file', initialfile='thumbnail', defaultextension=path)
        image.save(path_file)
    else:
        # get format from change_format() function
        set_format = change_format()
        # get format of image
        new_set = set_format.split('.')[1]
        # add "." to before the format of image
        new_set = '.' + new_set
        path_file = filedialog.asksaveasfilename(title='save file', initialfile=set_format, defaultextension=new_set)
        image.save(path_file)


# this is a button to convert the image to another format
convert_button = Button(convert, text='Convert', font=('Dela Gothic One', 15, 'bold'),
                        width=15, activebackground='white', bg='#0f5e5e', fg='white', activeforeground='#0f5e5e',
                        borderwidth=1, command=change_format)
convert_button.place(x=190, y=170)

# LABEL FOR CONVERT ==========================================
convert_format = StringVar()

last_label = Label(convert, textvariable=convert_format, font=('Dela Gothic One', 8, 'bold'),
                   anchor=W, bg='white', width=80, border=2, relief=GROOVE)
last_label.place(x=20, y=250, relheight=0.07)

# BUTTON QUIT AND SAVE
# if you click this button, it leaves the program
QUIT = Button(convert, text='Quit', font=('Dela Gothic One', 15, 'bold'),
              width=10, activebackground='white', bg='#e32d2a', fg='white', activeforeground='#e32d2a',
              borderwidth=1, command=convert.destroy)
QUIT.place(x=20, y=320)

# this item using for save image
SAVE = Button(convert, text='Save', font=('Dela Gothic One', 15, 'bold'),
              width=10, activebackground='white', bg='#003200', fg='white', activeforeground='#003200',
              borderwidth=1, command=save_image)
SAVE.place(x=458, y=320)

convert.mainloop()
