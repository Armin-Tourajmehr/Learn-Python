import os
from tkinter import *
from tkinter import filedialog


def GUI():
    global text
    explore = Tk()
    explore.title('Explore file')
    explore.geometry('500x480')
    explore.resizable(width=False, height=False)

    text = StringVar()
    text.set('Welcome to EXPLORE file')
    label = Label(explore, textvariable=text, bg='white', anchor=CENTER, height=5, fg='darkcyan'
                  , font=('None', 10, 'bold'))
    label.pack(anchor=N, pady=10, fill=X)

    browser_button = Button(explore, text='Browser', width=20, fg='purple', relief=GROOVE, activeforeground='green',
                            command=File_name)
    browser_button.place(x=160, y=120)

    exit_button = Button(explore, text='Exit', width=20, fg='#272727', relief=GROOVE, activeforeground='black',
                         command=exit)
    exit_button.place(x=320, y=430)

    # Search file
    global file
    file = StringVar()
    entry = Entry(explore, textvariable=file, justify=LEFT, width=23, cursor='heart', font=('None', 15, 'bold'))
    entry.place(x=20, y=198.5)

    search_button = Button(explore, text='Search', width=20, fg='#FF4500', relief=GROOVE, activeforeground='#eb8000',
                           command=search_file)
    search_button.place(x=320, y=200)

    # Listbox
    global listbox

    listbox = Listbox(explore, relief=GROOVE, width=78)
    listbox.place(x=8, y=240)
    # this scroll sets to listbox
    scrollbar = Scrollbar(explore)
    scrollbar.place(x=480, y=240, height=165)
    # config listbox to scrollbar
    listbox.config(yscrollcommand=scrollbar.set)
    # config scrollbar to listbox
    scrollbar.config(command=listbox.yview)

    # this button for removing data or path from the listbox

    delete_button = Button(explore, text='Delete', width=20, fg='#FF4500', relief=GROOVE, activeforeground='red',
                           command=delete)
    delete_button.place(x=10, y=430)
    explore.mainloop()


def File_name():
    filename = filedialog.askopenfilename(initialdir='/', title='Select file',
                                          filetypes=(('Text files', "*.txt"), ('all files', "*.*")))
    text.set("File Opened: \n" + filename)


def search_file():
    global file
    # get file for searching from user by entry
    name = file.get()
    result = []
    for root, dir, files in os.walk("C:\\"):
        if name in files:
            # if find name in file, it puts it in result list
            result.append(os.path.join(root, name))
    # this loop gets index and name of list then insert in listbox
    # and you can see it or them
    for index, names in enumerate(result):
        listbox.insert(index, names)


# this function is for removing data or path from listbox by delete button
def delete():
    listbox.delete(ANCHOR)


if __name__ == '__main__':
    GUI()
