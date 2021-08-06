from tkinter import *
from math import sin, cos, tan, factorial, sqrt, pow, exp, log10


class calculator:
    full_stop = 1
    bracket = 0
    for_calculate = None

    # construction function
    def __init__(self, root):
        self.root = root
        self.root.title('Calculator')
        self.root.geometry('400x535')
        self.root.resizable(width=False, height=False)
        self.root.config(bg='#474747')
        self.root.iconbitmap('icon.ico')

    # =========================== FUNCTION OF APP ===============================

    def label_number(self):
        self.expression = StringVar(root, '0')
        self.calculate = StringVar(root)

        entry = Entry(master=self.root, textvariable=self.expression, justify=RIGHT,
                      font=('Dela Gothic One', 25, 'bold'),
                      fg='white', bd=3, bg='#474747', relief=FLAT)
        entry.pack(pady=5, anchor=N, padx=2, fill=X)

        screen_label = Label(master=self.root, textvariable=self.calculate, font=('Dela Gothic One', 25, 'bold'),
                             fg='white', bd=3, anchor=E, justify=RIGHT, bg='#474747', relief=FLAT)
        screen_label.pack(pady=5, anchor=N, padx=6, fill=X)

    def first_row(self):
        # hover text , when cursor goes on icon , it changes its color
        def change_color_enter(button):
            button['bg'] = '#505050'

        def change_color_leave(button):
            button['bg'] = '#333333'

        # create Frame
        first_frame = Frame(master=self.root, bg='#474747')

        # button of sin
        button_sin = Button(first_frame, text='sin', font=('Dela Gothic One', 12, 'bold'),
                            bd=0, relief=FLAT, justify=CENTER, bg='#333333', fg='white', activebackground='#747474',
                            activeforeground='white', width=9, height=2)
        button_sin.config(command=self.sin)
        button_sin.bind('<Enter>', func=lambda e: change_color_enter(button_sin))
        button_sin.bind('<Leave>', func=lambda e: change_color_leave(button_sin))
        button_sin.pack(side=LEFT, padx=1, pady=1, fill=X)

        # button of cos
        button_cos = Button(first_frame, text='cos', font=('Dela Gothic One', 12, 'bold'),
                            bd=0, relief=FLAT, justify=CENTER, bg='#333333', fg='white', activebackground='#747474',
                            activeforeground='white', width=9, height=2)
        button_cos.config(command=self.cos)
        button_cos.bind('<Enter>', func=lambda e: change_color_enter(button_cos))
        button_cos.bind('<Leave>', func=lambda e: change_color_leave(button_cos))
        button_cos.pack(side=LEFT, padx=1, pady=1, fill=X)

        # button of tan
        button_tan = Button(first_frame, text='tan', font=('Dela Gothic One', 12, 'bold'),
                            bd=0, relief=FLAT, justify=CENTER, bg='#333333', fg='white', activebackground='#747474',
                            activeforeground='white', width=9, height=2)
        button_tan.config(command=self.tan)
        button_tan.bind('<Enter>', func=lambda e: change_color_enter(button_tan))
        button_tan.bind('<Leave>', func=lambda e: change_color_leave(button_tan))
        button_tan.pack(side=LEFT, padx=1, pady=1, fill=X)

        # button of cot
        button_cot = Button(first_frame, text='cot', font=('Dela Gothic One', 12, 'bold'),
                            bd=0, relief=FLAT, justify=CENTER, bg='#333333', fg='white', activebackground='#747474',
                            activeforeground='white', width=9, height=2)
        button_cot.config(command=self.cot)
        button_cot.bind('<Enter>', func=lambda e: change_color_enter(button_cot))
        button_cot.bind('<Leave>', func=lambda e: change_color_leave(button_cot))
        button_cot.pack(side=LEFT, padx=1, pady=1, fill=X)

        first_frame.pack(side=TOP, anchor=NW, padx=5, fill=BOTH)

    def second_row(self):
        def change_color_enter(button):
            button['bg'] = '#505050'

        def change_color_leave(button):
            button['bg'] = '#333333'

        second_frame = Frame(master=self.root, bg='#474747')

        # button of pow
        button_pow = Button(second_frame, text='x²', font=('Dela Gothic One', 12, 'bold'),
                            bd=0, relief=FLAT, justify=CENTER, bg='#333333', fg='white', activebackground='#747474',
                            activeforeground='white', width=9, height=2)
        button_pow.config(command=self.Pow)
        button_pow.bind('<Enter>', func=lambda e: change_color_enter(button_pow))
        button_pow.bind('<Leave>', func=lambda e: change_color_leave(button_pow))
        button_pow.pack(side=LEFT, padx=1, pady=1, fill=X)

        # button of 10 ^ x
        button_powOften = Button(second_frame, text='10ª', font=('Dela Gothic One', 12, 'bold'),
                                 bd=0, relief=FLAT, justify=CENTER, bg='#333333', fg='white',
                                 activebackground='#747474', activeforeground='white', width=9, height=2)
        button_powOften.config(command=self.ten)
        button_powOften.bind('<Enter>', func=lambda e: change_color_enter(button_powOften))
        button_powOften.bind('<Leave>', func=lambda e: change_color_leave(button_powOften))
        button_powOften.pack(side=LEFT, padx=1, pady=1, fill=X)

        # log based of 10
        button_log = Button(second_frame, text='log', font=('Dela Gothic One', 12, 'bold'),
                            bd=0, relief=FLAT, justify=CENTER, bg='#333333', fg='white', activebackground='#747474',
                            activeforeground='white', width=9, height=2)
        button_log.config(command=self.Logarythm)
        button_log.bind('<Enter>', func=lambda e: change_color_enter(button_log))
        button_log.bind('<Leave>', func=lambda e: change_color_leave(button_log))
        button_log.pack(side=LEFT, padx=1, pady=1, fill=X)

        # exp = 2.718281828459045
        button_exp = Button(second_frame, text='exp', font=('Dela Gothic One', 12, 'bold'),
                            bd=0, relief=FLAT, justify=CENTER, bg='#333333', fg='white', activebackground='#747474',
                            activeforeground='white', width=9, height=2)
        button_exp.config(command=self.Exores)
        button_exp.bind('<Enter>', func=lambda e: change_color_enter(button_exp))
        button_exp.bind('<Leave>', func=lambda e: change_color_leave(button_exp))
        button_exp.pack(side=LEFT, padx=1, pady=1, fill=X)

        second_frame.pack(side=TOP, padx=5, anchor=NW, fill=BOTH)

    def third_row(self):
        def change_color_enter(button):
            button['bg'] = '#505050'

        def change_color_leave(button):
            button['bg'] = '#333333'

        third_frame = Frame(master=self.root, bg='#474747')

        # button of n! = n(n-1)(n-2)....
        button_factorial = Button(third_frame, text='n!', font=('Dela Gothic One', 12, 'bold'),
                                  bd=0, relief=FLAT, justify=CENTER, bg='#333333', fg='white',
                                  activebackground='#747474',
                                  activeforeground='white', width=9, height=2)
        button_factorial.config(command=self.fact)
        button_factorial.bind('<Enter>', func=lambda e: change_color_enter(button_factorial))
        button_factorial.bind('<Leave>', func=lambda e: change_color_leave(button_factorial))
        button_factorial.pack(side=LEFT, padx=1, pady=1, fill=X)

        # button of square root
        button_sr = Button(third_frame, text='sqrt', font=('Dela Gothic One', 12, 'bold'),
                           bd=0, relief=FLAT, justify=CENTER, bg='#333333', fg='white', activebackground='#747474',
                           activeforeground='white', width=9, height=2)
        button_sr.config(command=self.SQRT)
        button_sr.bind('<Enter>', func=lambda e: change_color_enter(button_sr))
        button_sr.bind('<Leave>', func=lambda e: change_color_leave(button_sr))
        button_sr.pack(side=LEFT, padx=1, pady=1, fill=X)

        button_C = Button(third_frame, text='«', font=('Dela Gothic One', 12, 'bold'),
                          bd=0, relief=FLAT, justify=CENTER, bg='#333333', fg='white', activebackground='#747474',
                          activeforeground='white', width=9, height=2)
        button_C.config(command=self.delete)
        button_C.bind('<Enter>', func=lambda e: change_color_enter(button_C))
        button_C.bind('<Leave>', func=lambda e: change_color_leave(button_C))
        button_C.pack(side=LEFT, padx=1, pady=1, fill=X)

        button_c = Button(third_frame, text='±', font=('Dela Gothic One', 12, 'bold'),
                          bd=0, relief=FLAT, justify=CENTER, bg='#333333', fg='white', activebackground='#747474',
                          activeforeground='white', width=9, height=2)
        button_c.config(command=self.revers)
        button_c.bind('<Enter>', func=lambda e: change_color_enter(button_c))
        button_c.bind('<Leave>', func=lambda e: change_color_leave(button_c))
        button_c.pack(side=LEFT, padx=1, pady=1, fill=X)

        third_frame.pack(side=TOP, padx=5, anchor=NW, fill=BOTH)

    def fourth_row(self):
        def change_color_enter(button):
            button['bg'] = '#505050'

        def change_color_leave(button):
            button['bg'] = '#000000'

        fourth_frame = Frame(master=self.root, bg='#474747')

        button_1 = Button(fourth_frame, text='1', font=('Dela Gothic One', 12, 'bold'),
                          bd=0, relief=FLAT, justify=CENTER, bg='#000000', fg='white', activebackground='#747474',
                          activeforeground='white', width=9, height=2)
        button_1.config(command=self.one)
        button_1.bind('<Enter>', func=lambda e: change_color_enter(button_1))
        button_1.bind('<Leave>', func=lambda e: change_color_leave(button_1))
        button_1.pack(side=LEFT, padx=1, pady=1, fill=X)

        button_2 = Button(fourth_frame, text='2', font=('Dela Gothic One', 12, 'bold'),
                          bd=0, relief=FLAT, justify=CENTER, bg='#000000', fg='white', activebackground='#747474',
                          activeforeground='white', width=9, height=2)
        button_2.config(command=self.two)
        button_2.bind('<Enter>', func=lambda e: change_color_enter(button_2))
        button_2.bind('<Leave>', func=lambda e: change_color_leave(button_2))
        button_2.pack(side=LEFT, padx=1, pady=1, fill=X)

        button_3 = Button(fourth_frame, text='3', font=('Dela Gothic One', 12, 'bold'),
                          bd=0, relief=FLAT, justify=CENTER, bg='#000000', fg='white', activebackground='#747474',
                          activeforeground='white', width=9, height=2)
        button_3.config(command=self.three)
        button_3.bind('<Enter>', func=lambda e: change_color_enter(button_3))
        button_3.bind('<Leave>', func=lambda e: change_color_leave(button_3))
        button_3.pack(side=LEFT, padx=1, pady=1, fill=X)

        def change_color_enter1(button):
            button['bg'] = '#f1ae1e'

        def change_color_leave1(button):
            button['bg'] = '#333333'

        button_multi = Button(fourth_frame, text='x', font=('Dela Gothic One', 12, 'bold'),
                              bd=0, relief=FLAT, justify=CENTER, bg='#333333', fg='white', activebackground='#f8cb6e',
                              activeforeground='white', width=9, height=2)
        button_multi.config(command=self.multiply)
        button_multi.bind('<Enter>', func=lambda e: change_color_enter1(button_multi))
        button_multi.bind('<Leave>', func=lambda e: change_color_leave1(button_multi))
        button_multi.pack(side=LEFT, padx=1, pady=1, fill=X)

        fourth_frame.pack(side=TOP, padx=5, anchor=NW, fill=BOTH)

    def fifth_row(self):
        def change_color_enter(button):
            button['bg'] = '#505050'

        def change_color_leave(button):
            button['bg'] = '#000000'

        fifth_frame = Frame(master=self.root, bg='#474747')

        button_4 = Button(fifth_frame, text='4', font=('Dela Gothic One', 12, 'bold'),
                          bd=0, relief=FLAT, justify=CENTER, bg='#000000', fg='white', activebackground='#747474',
                          activeforeground='white', width=9, height=2)
        button_4.config(command=self.four)
        button_4.bind('<Enter>', func=lambda e: change_color_enter(button_4))
        button_4.bind('<Leave>', func=lambda e: change_color_leave(button_4))
        button_4.pack(side=LEFT, padx=1, pady=1, fill=X)

        button_5 = Button(fifth_frame, text='5', font=('Dela Gothic One', 12, 'bold'),
                          bd=0, relief=FLAT, justify=CENTER, bg='#000000', fg='white', activebackground='#747474',
                          activeforeground='white', width=9, height=2)
        button_5.config(command=self.five)
        button_5.bind('<Enter>', func=lambda e: change_color_enter(button_5))
        button_5.bind('<Leave>', func=lambda e: change_color_leave(button_5))
        button_5.pack(side=LEFT, padx=1, pady=1, fill=X)

        button_6 = Button(fifth_frame, text='6', font=('Dela Gothic One', 12, 'bold'),
                          bd=0, relief=FLAT, justify=CENTER, bg='#000000', fg='white', activebackground='#747474',
                          activeforeground='white', width=9, height=2)
        button_6.config(command=self.six)
        button_6.bind('<Enter>', func=lambda e: change_color_enter(button_6))
        button_6.bind('<Leave>', func=lambda e: change_color_leave(button_6))
        button_6.pack(side=LEFT, padx=1, pady=1, fill=X)

        def change_color_enter1(button):
            button['bg'] = '#f1ae1e'

        def change_color_leave1(button):
            button['bg'] = '#333333'

        button_div = Button(fifth_frame, text='÷', font=('Dela Gothic One', 12, 'bold'),
                            bd=0, relief=FLAT, justify=CENTER, bg='#333333', fg='white', activebackground='#f8cb6e',
                            activeforeground='white', width=9, height=2)
        button_div.config(command=self.divide)
        button_div.bind('<Enter>', func=lambda e: change_color_enter1(button_div))
        button_div.bind('<Leave>', func=lambda e: change_color_leave1(button_div))
        button_div.pack(side=LEFT, padx=1, pady=1, fill=X)

        fifth_frame.pack(side=TOP, padx=5, anchor=NW, fill=BOTH)

    def sixth_row(self):
        def change_color_enter(button):
            button['bg'] = '#505050'

        def change_color_leave(button):
            button['bg'] = '#000000'

        sixth_frame = Frame(master=self.root, bg='#474747')

        button_7 = Button(sixth_frame, text='7', font=('Dela Gothic One', 12, 'bold'),
                          bd=0, relief=FLAT, justify=CENTER, bg='#000000', fg='white', activebackground='#747474',
                          activeforeground='white', width=9, height=2)
        button_7.config(command=self.seven)
        button_7.bind('<Enter>', func=lambda e: change_color_enter(button_7))
        button_7.bind('<Leave>', func=lambda e: change_color_leave(button_7))
        button_7.pack(side=LEFT, padx=1, pady=1, fill=X)

        button_8 = Button(sixth_frame, text='8', font=('Dela Gothic One', 12, 'bold'),
                          bd=0, relief=FLAT, justify=CENTER, bg='#000000', fg='white', activebackground='#747474',
                          activeforeground='white', width=9, height=2)
        button_8.config(command=self.eight)
        button_8.bind('<Enter>', func=lambda e: change_color_enter(button_8))
        button_8.bind('<Leave>', func=lambda e: change_color_leave(button_8))
        button_8.pack(side=LEFT, padx=1, pady=1, fill=X)

        button_9 = Button(sixth_frame, text='9', font=('Dela Gothic One', 12, 'bold'),
                          bd=0, relief=FLAT, justify=CENTER, bg='#000000', fg='white', activebackground='#747474',
                          activeforeground='white', width=9, height=2)
        button_9.config(command=self.nine)
        button_9.bind('<Enter>', func=lambda e: change_color_enter(button_9))
        button_9.bind('<Leave>', func=lambda e: change_color_leave(button_9))
        button_9.pack(side=LEFT, padx=1, pady=1, fill=X)

        def change_color_enter1(button):
            button['bg'] = '#f1ae1e'

        def change_color_leave1(button):
            button['bg'] = '#333333'

        button_sum = Button(sixth_frame, text='+', font=('Dela Gothic One', 12, 'bold'),
                            bd=0, relief=FLAT, justify=CENTER, bg='#333333', fg='white', activebackground='#f8cb6e',
                            activeforeground='white', width=9, height=2)
        button_sum.config(command=self.add)
        button_sum.bind('<Enter>', func=lambda e: change_color_enter1(button_sum))
        button_sum.bind('<Leave>', func=lambda e: change_color_leave1(button_sum))
        button_sum.pack(side=LEFT, padx=1, pady=1, fill=X)

        sixth_frame.pack(side=TOP, padx=5, anchor=NW, fill=BOTH)

    def seventh_row(self):
        def change_color_enter0(button):
            button['bg'] = '#505050'

        def change_color_leave0(button):
            button['bg'] = '#333333'

        seventh_frame = Frame(master=self.root, bg='#474747')

        button_CE = Button(seventh_frame, text='CE', font=('Dela Gothic One', 12, 'bold'),
                           bd=0, relief=FLAT, justify=CENTER, bg='#333333', fg='white', activebackground='#747474',
                           activeforeground='white', width=9, height=2)
        button_CE.config(command=self.reset)
        button_CE.bind('<Enter>', func=lambda e: change_color_enter0(button_CE))
        button_CE.bind('<Leave>', func=lambda e: change_color_leave0(button_CE))
        button_CE.pack(side=LEFT, padx=1, pady=1, fill=X)

        def change_color_enter(button):
            button['bg'] = '#505050'

        def change_color_leave(button):
            button['bg'] = '#000000'

        button_0 = Button(seventh_frame, text='0', font=('Dela Gothic One', 12, 'bold'),
                          bd=0, relief=FLAT, justify=CENTER, bg='#000000', fg='white', activebackground='#747474',
                          activeforeground='white', width=9, height=2)

        button_0.config(command=self.zero)
        button_0.bind('<Enter>', func=lambda e: change_color_enter(button_0))
        button_0.bind('<Leave>', func=lambda e: change_color_leave(button_0))
        button_0.pack(side=LEFT, padx=1, pady=1, fill=X)

        button_slash = Button(seventh_frame, text='.', font=('Dela Gothic One', 12, 'bold'),
                              bd=0, relief=FLAT, justify=CENTER, bg='#333333', fg='white', activebackground='#747474',
                              activeforeground='white', width=9, height=2)
        button_slash.config(command=self.point)
        button_slash.bind('<Enter>', func=lambda e: change_color_enter0(button_slash))
        button_slash.bind('<Leave>', func=lambda e: change_color_leave0(button_slash))
        button_slash.pack(side=LEFT, padx=1, pady=1, fill=X)

        def change_color_enter1(button):
            button['bg'] = '#f1ae1e'

        def change_color_leave1(button):
            button['bg'] = '#333333'

        button_neg = Button(seventh_frame, text='-', font=('Dela Gothic One', 12, 'bold'),
                            bd=0, relief=FLAT, justify=CENTER, bg='#333333', fg='white', activebackground='#f8cb6e',
                            activeforeground='white', width=9, height=2)
        button_neg.config(command=self.substract)
        button_neg.bind('<Enter>', func=lambda e: change_color_enter1(button_neg))
        button_neg.bind('<Leave>', func=lambda e: change_color_leave1(button_neg))
        button_neg.pack(side=LEFT, padx=1, pady=1, fill=X)

        seventh_frame.pack(side=TOP, padx=5, anchor=NW, fill=BOTH)

    def last_row(self):
        def change_color_enter0(button):
            button['bg'] = '#ff0000'

        def change_color_leave0(button):
            button['bg'] = '#ff8282'

        last_frame = Frame(master=self.root, bg='#474747')

        button_quit = Button(last_frame, text='quit', font=('Dela Gothic One', 12, 'bold'),
                             bd=0, relief=FLAT, justify=CENTER, bg='#ff8282', fg='white', activebackground='#ff0000',
                             activeforeground='white', width=9, height=2)
        button_quit.config(command=self.root.destroy)
        button_quit.bind('<Enter>', func=lambda e: change_color_enter0(button_quit))
        button_quit.bind('<Leave>', func=lambda e: change_color_leave0(button_quit))
        button_quit.pack(side=LEFT, padx=1, pady=1, fill=X)

        def change_color_enter(button):
            button['bg'] = '#505050'

        def change_color_leave(button):
            button['bg'] = '#333333'

        button_1 = Button(last_frame, text='(', font=('Dela Gothic One', 12, 'bold'),
                          bd=0, relief=FLAT, justify=CENTER, bg='#333333', fg='white', activebackground='#747474',
                          activeforeground='white', width=9, height=2)
        button_1.config(command=self.paratenses)
        button_1.bind('<Enter>', func=lambda e: change_color_enter(button_1))
        button_1.bind('<Leave>', func=lambda e: change_color_leave(button_1))
        button_1.pack(side=LEFT, padx=1, pady=1, fill=X)

        button_2 = Button(last_frame, text=')', font=('Dela Gothic One', 12, 'bold'),
                          bd=0, relief=FLAT, justify=CENTER, bg='#333333', fg='white', activebackground='#747474',
                          activeforeground='white', width=9, height=2)
        button_2.config(command=self.paratenses1)
        button_2.bind('<Enter>', func=lambda e: change_color_enter(button_2))
        button_2.bind('<Leave>', func=lambda e: change_color_leave(button_2))
        button_2.pack(side=LEFT, padx=1, pady=1, fill=X)

        def change_color_enter1(button):
            button['bg'] = '#044e1c'

        def change_color_leave1(button):
            button['bg'] = '#0eae3a'

        button_neg = Button(last_frame, text='=', font=('Dela Gothic One', 12, 'bold'),
                            bd=0, relief=FLAT, justify=CENTER, bg='#0eae3a', fg='white', activebackground='#044e1c',
                            activeforeground='white', width=9, height=2)
        button_neg.config(command=self.calculated)
        button_neg.bind('<Enter>', func=lambda e: change_color_enter1(button_neg))
        button_neg.bind('<Leave>', func=lambda e: change_color_leave1(button_neg))
        button_neg.pack(side=LEFT, padx=1, pady=1, fill=X)

        last_frame.pack(side=TOP, padx=5, anchor=NW, fill=BOTH)

    # ========================== NUMBER FO FUNCTION =========================================
    def zero(self, event=''):
        if self.expression.get().startswith('0') and len(self.expression.get()) == 1:
            self.expression.set('')
        if len(self.expression.get()) < 30:
            self.expression.set(self.expression.get() + '0')

    def one(self, event=''):
        if self.expression.get().startswith('0') and len(self.expression.get()) == 1:
            self.expression.set('')
        if len(self.expression.get()) < 30:
            self.expression.set(self.expression.get() + '1')

    def two(self, event=''):
        if self.expression.get().startswith('0') and len(self.expression.get()) == 1:
            self.expression.set('')
        if len(self.expression.get()) < 30:
            self.expression.set(self.expression.get() + '2')

    def three(self, event=''):
        if self.expression.get().startswith('0') and len(self.expression.get()) == 1:
            self.expression.set('')
        if len(self.expression.get()) < 30:
            self.expression.set(self.expression.get() + '3')

    def four(self, event=''):
        if self.expression.get().startswith('0') and len(self.expression.get()) == 1:
            self.expression.set('')
        if len(self.expression.get()) < 30:
            self.expression.set(self.expression.get() + '4')

    def five(self, event=''):
        if self.expression.get().startswith('0') and len(self.expression.get()) == 1:
            self.expression.set('')
        if len(self.expression.get()) < 30:
            self.expression.set(self.expression.get() + '5')

    def six(self, event=''):
        if self.expression.get().startswith('0') and len(self.expression.get()) == 1:
            self.expression.set('')
        if len(self.expression.get()) < 30:
            self.expression.set(self.expression.get() + '6')

    def seven(self, event=''):
        if self.expression.get().startswith('0') and len(self.expression.get()) == 1:
            self.expression.set('')
        if len(self.expression.get()) < 30:
            self.expression.set(self.expression.get() + '7')

    def eight(self, event=''):
        if self.expression.get().startswith('0') and len(self.expression.get()) == 1:
            self.expression.set('')
        if len(self.expression.get()) < 30:
            self.expression.set(self.expression.get() + '8')

    def nine(self, event=''):
        if self.expression.get().startswith('0') and len(self.expression.get()) == 1:
            self.expression.set('')
        if len(self.expression.get()) < 30:
            self.expression.set(self.expression.get() + '9')

    # ====================== NUMBERS FUNCTIONS OVER AND THE ENTRY CAN ONLY TAKE UP TO 30 CHARACTERS ============

    # Operators Functions
    def add(self, event=''):
        if len(self.expression.get()) < 30 and not self.expression.get().endswith('.'):
            if self.expression.get().endswith('+'):
                self.expression.set(self.expression.get()[:-1] + '+')
            elif self.expression.get().endswith('-'):
                self.expression.set(self.expression.get()[:-1] + '+')
            elif self.expression.get().endswith('x'):
                self.expression.set(self.expression.get()[:-1] + '+')
            elif self.expression.get().endswith('÷'):
                self.expression.set(self.expression.get()[:-1] + '+')
            else:
                self.expression.set(self.expression.get() + '+')
            self.full_stop = 1

    def substract(self, event=''):
        if len(self.expression.get()) < 30 and not self.expression.get().endswith('.'):
            if self.expression.get().endswith('+'):
                self.expression.set(self.expression.get()[:-1] + '-')
            elif self.expression.get().endswith('-'):
                self.expression.set(self.expression.get()[:-1] + '-')
            elif self.expression.get().endswith('x'):
                self.expression.set(self.expression.get()[:-1] + '-')
            elif self.expression.get().endswith('÷'):
                self.expression.set(self.expression.get()[:-1] + '-')
            else:
                self.expression.set(self.expression.get() + '-')
            self.full_stop = 1

    def multiply(self, event=''):
        if len(self.expression.get()) < 30 and not self.expression.get().endswith('.'):
            if self.expression.get().endswith('+'):
                self.expression.set(self.expression.get()[:-1] + 'x')
            elif self.expression.get().endswith('-'):
                self.expression.set(self.expression.get()[:-1] + 'x')
            elif self.expression.get().endswith('x'):
                self.expression.set(self.expression.get()[:-1] + 'x')
            elif self.expression.get().endswith('÷'):
                self.expression.set(self.expression.get()[:-1] + 'x')
            else:
                self.expression.set(self.expression.get() + 'x')
            self.full_stop = 1

    def divide(self, event=''):
        if len(self.expression.get()) < 30 and not self.expression.get().endswith('.'):
            if self.expression.get().endswith('+'):
                self.expression.set(self.expression.get()[:-1] + '÷')
            elif self.expression.get().endswith('-'):
                self.expression.set(self.expression.get()[:-1] + '÷')
            elif self.expression.get().endswith('x'):
                self.expression.set(self.expression.get()[:-1] + '÷')
            elif self.expression.get().endswith('÷'):
                self.expression.set(self.expression.get()[:-1] + '÷')
            else:
                self.expression.set(self.expression.get() + '÷')
            self.full_stop = 1

    # OTHERS FUNCTIONS
    def point(self, event=''):
        if len(self.expression.get()) < 30 and self.full_stop == 1:
            if not self.expression.get().endswith(('+', '_', 'x', '÷', '(', ')')):
                self.expression.set(self.expression.get() + '.')
                self.full_stop = 0

    def paratenses(self, event=''):
        if self.expression.get() == '0':
            self.expression.set('(')
        else:
            self.expression.set(self.expression.get() + '(')
        self.bracket += 1

    def paratenses1(self, event=''):
        if self.bracket != 0 and not self.expression.get() == '0':
            self.expression.set(self.expression.get() + ')')
            self.bracket -= 1

    # this function will make 1st positive number to negative or vice versa
    def revers(self, event=''):
        if not self.expression.get().startswith('-') and not self.expression.get().startswith('0') and len(
                self.expression.get()) < 30:
            self.expression.set('-' + self.expression.get())
        elif self.expression.get().startswith('-'):
            self.expression.set(self.expression.get()[1:])

    def delete(self, event=''):
        self.expression.set(self.expression.get()[:-1])
        if self.expression.get() == '':
            self.expression.set('0')

    def reset(self, event=''):
        self.expression.set('0')
        self.for_calculate = None
        self.calculate.set('')

    # =============== below function to calcute ==========================
    def calculated(self, event=''):
        self.for_calculate = self.expression.get().replace('x', '*').replace('÷', '/')
        self.calculate.set(eval(self.for_calculate))
        self.expression.set('0')
        if str(self.calculate.get()[int(len(self.calculate.get()) - 2):]) == '.0':
            self.calculate.set(self.calculate.get()[:-2])
        self.expression.set('0')

    # =================== Function for sin , cos , .......... ================================
    def sin(self):
        if len(self.expression.get()) < 30 and not self.expression.get().endswith('.'):
            expr = sin(float(self.expression.get()))
            self.calculate.set(expr)
            self.expression.set(str(round(expr, 5)))

    def cos(self):
        if len(self.expression.get()) < 30 and not self.expression.get().endswith('.'):
            expr = cos(float(self.expression.get()))
            self.calculate.set(expr)
            self.expression.set(str(round(expr, 5)))

    def tan(self):
        if len(self.expression.get()) < 30 and not self.expression.get().endswith('.'):
            expr = tan(float(self.expression.get()))
            self.calculate.set(expr)
            self.expression.set(str(round(expr, 5)))

    def cot(self):
        if len(self.expression.get()) < 30 and not self.expression.get().endswith('.'):
            expr = 1 / tan(float(self.expression.get()))
            self.calculate.set(expr)
            self.expression.set(str(round(expr, 5)))

    def Pow(self):
        if len(self.expression.get()) < 30 and not self.expression.get().endswith('.'):
            expr = pow(float(self.expression.get()), 2)
            self.calculate.set(str(expr))
            self.expression.set(str(expr))

    def ten(self):
        if len(self.expression.get()) < 30 and not self.expression.get().endswith('.'):
            if len(self.expression.get()) > 200:
                self.calculate.set('Long Number')
            elif len(self.expression.get()) < 200:
                expr = pow(10, int(self.expression.get()))
                if len(str(int(expr))) > 30:
                    self.expression.set('0')
                    self.calculate.set('Long Number')
                else:
                    self.calculate.set(str(int(expr)))
                    self.expression.set(str(int(expr)))

    def Logarythm(self):
        if len(self.expression.get()) < 30 and not self.expression.get().endswith('.'):
            expr = log10(float(self.expression.get()))
            self.calculate.set(str(expr))
            self.expression.set(str(expr))


    def Exores(self):
        if len(self.expression.get()) < 30 and not self.expression.get().endswith('.'):
            expr = exp(float(self.expression.get()))
            self.calculate.set(str(expr))
            self.expression.set(str(expr))

    def fact(self):
        if len(self.expression.get()) < 30 and not self.expression.get().endswith('.'):
            if len(self.expression.get()) > 200:
                self.calculate.set('Long Number')
            elif len(self.expression.get()) < 200:
                expr = factorial(int(self.expression.get()))
                if len(str(int(expr))) > 30:
                    self.expression.set('0')
                    self.calculate.set('Long Number')
                else:
                    self.calculate.set(str(expr))
                    self.expression.set(str(expr))
    def SQRT(self):
        if len(self.expression.get()) < 30 and not self.expression.get().endswith('.'):
            if len(self.expression.get()) > 200:
                self.calculate.set('Long Number')
            elif len(self.expression.get()) < 200:
                expr = sqrt(int(self.expression.get()))
                if len(str(int(expr))) > 30:
                    self.expression.set('0')
                    self.calculate.set('Long Number')
                else:
                    self.calculate.set(str(expr))
                    self.expression.set(str(expr))

root = Tk()
calc = calculator(root)
calc.label_number()
calc.first_row()
calc.second_row()
calc.third_row()
calc.fourth_row()
calc.fifth_row()
calc.sixth_row()
calc.seventh_row()
calc.last_row()
root.mainloop()
