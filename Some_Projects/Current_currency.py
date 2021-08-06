# Current Currency
import requests
import tkinter as Tk
from tkinter import ttk
from tkinter import messagebox
import re


class Current_currency:
    def __init__(self, url):
        self.data = requests.get(url).json()
        self.currencies = self.data['rates']

    def convert(self, from_currency, to_currency, amount):
        # first convert to USD if not USD because
        # our base currency is USD
        if from_currency != 'USD':
            amount = amount / self.currencies[from_currency]
        amount = round(amount * self.currencies[to_currency], 4)
        return amount


class Currency(Tk.Tk):
    def __init__(self, converter):
        Tk.Tk.__init__(self)
        self.title('Currency Converter')
        # You can add an .ico file
        self.iconbitmap('currency.ico')
        # set size
        self.geometry('600x400')
        # windows can't change else
        self.resizable(width=False, height=False)
        self.config(bg='#333333')
        self.Current_currency = converter

        # Labels ======================================
        # set label in the top of application
        self.label_welcome = Tk.Label(self, text='Welcome To Realtime Currency Convert',
                                      font=('Dela Gothic One', 12, 'bold'), relief=Tk.GROOVE,
                                      justify=Tk.CENTER, background='#eef7da', height=2, width=35,
                                      border=5)

        self.label_welcome.pack(anchor=Tk.N, pady=10, fill=Tk.BOTH)

        # set USD and Iranian Rial
        self.label_iranian_rial = Tk.Label(self,
                                           text=f'Iranian Rial\t =\t '
                                                f'{self.Current_currency.convert("IRR", "USD", 42105.00)} USD\n\n'
                                                f'date\t\t  :\t {self.Current_currency.data["date"]}',
                                           font=('Dela Gothic One', 12, 'bold'),
                                           width=35, relief=Tk.SUNKEN, border=5, justify=Tk.CENTER, bg='#e2fafa')

        self.label_iranian_rial.pack(anchor=Tk.N, ipady=10)

        # dropdown for from_currency
        self.from_currency_variable = Tk.StringVar(self)
        self.from_currency_variable.set('IRR')
        font = ('Dela Gothic One', 12, 'bold')
        self.option_add('*TCombobox*Listbox.font', font)

        self.from_currency_dropdown = ttk.Combobox(self, textvariable=self.from_currency_variable,
                                                   values=list(self.Current_currency.currencies.keys()),
                                                   font=font, state='normal', justify=Tk.CENTER)
        self.from_currency_dropdown.place(x=20, y=200, relheight=0.1)

        # dropdown for To_currency ========================================
        self.To_currency_variable = Tk.StringVar(self)
        self.To_currency_variable.set('USD')
        font = ('Dela Gothic One', 12, 'bold')
        self.option_add('*TCombobox*Listbox.font', font)

        self.To_currency_dropdown = ttk.Combobox(self, textvariable=self.To_currency_variable,
                                                 values=list(self.Current_currency.currencies.keys()),
                                                 font=font, state='noraml', justify=Tk.CENTER)

        self.To_currency_dropdown.place(x=380, y=200, relheight=0.1)

        # Entry box ======================================================
        # if your pointer come on it,its color will be change
        def change_color_enter1(button):
            button['bg'] = '#F0FFF0'

        # if your pointer leave it, its color get back to original of color
        def change_color_leave1(button):
            button['bg'] = 'SystemButtonFace'

        self.amount_field = Tk.Entry(self, bd=3, font=('Dela Gothic One', 20, 'bold'), relief=Tk.RIDGE,
                                     justify=Tk.CENTER, validate='key',
                                     selectbackground='black', width=11)
        self.amount_field.bind('<Enter>', func=lambda e: change_color_enter1(self.amount_field))
        self.amount_field.bind('<Leave>', func=lambda e: change_color_leave1(self.amount_field))
        self.amount_field.place(x=30, y=260, height=38)

        # Label for convert currency==================================================

        self.convert_amount_field = Tk.Label(self, text='', font=('Dela Gothic One', 20, 'bold'), bd=3,
                                             relief=Tk.RIDGE, justify=Tk.CENTER, width=10)
        self.convert_amount_field.place(x=400, y=260)

        # button =================================================================

        self.button_convert = Tk.Button(self, text='Convert', bg='#96ddc2', font=font, fg='black',
                                        bd=0, relief=Tk.FLAT, justify=Tk.CENTER,
                                        activebackground='#9ACD32', activeforeground='black',
                                        width=10, command=self.perform)
        self.button_convert.place(x=245, y=270)

        self.button_quit = Tk.Button(self, text='quit', bg='#ff8282', font=font, width=10, fg='white',
                                     bd=0, relief=Tk.FLAT, justify=Tk.CENTER,
                                     activebackground='#ff0000', activeforeground='white', command=self.destroy)
        self.button_quit.place(x=50, y=360)

    # function ==========================================================

    def perform(self):
        amount = str(self.amount_field.get())
        from_currency = self.from_currency_variable.get()
        to_currency = self.To_currency_variable.get()
        # return Error if input character or symbol
        regex = re.search(r"[a-zA-Z]", amount)
        if regex:
            self.error_message()
        else:
            amount = float(amount)
            converted_amount = self.Current_currency.convert(from_currency, to_currency, amount)
            converted_amount = round(converted_amount, 2)
            self.convert_amount_field.config(text=str(converted_amount))

    # this function handle Error and gets back show info message

    def error_message(self):
        Tk.messagebox.showerror('Error', 'Entrance is not Invalid')


if __name__ == '__main__':
    url = 'https://api.exchangerate-api.com/v4/latest/USD'
    converter = Current_currency(url)
    Currency(converter)

    Tk.mainloop()
