from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

from tkinter import *
from tkinter import messagebox
import tkinter.font

from PIL import ImageTk
from PIL import Image

import os
import requests
import json

from menu import Menu

'''
    server parameters.
'''
STORE_ID = "1"
TABLE_ID = "1"
MENU_LIST_URL = "#" + STORE_ID + "/menu"
LOGIN_URL = "#"
TABLE_URL = "#" + STORE_ID + "/tables/" + TABLE_ID + "/tokens"
ORDER_URL = "#"

TOKEN = ""
TABLE_TOKEN = ""
TOKEN_ACCESS = FALSE



'''
    application class.
'''
class Application(Frame):
    def __init__(self, master=None):
        super().__init__(master)

        '''
            values.
        '''
        self.total_price = 0
        self.current_menu = []
        self.current_menu_num = []
        self.current_menu_text = StringVar()
        self.current_menu_id = []
        self.current_page = 0
        self.MAX_PAGE = 0

        self.total_menu_num = 0
        self.total_menu_name = []
        self.total_menu_price = []
        self.menu_id = []

        self.display_menu_info_01 = StringVar()
        self.display_menu_info_02 = StringVar()
        self.display_menu_info_03 = StringVar()
        self.display_menu_info_04 = StringVar()
        self.display_menu_info_05 = StringVar()
        self.display_menu_info_06 = StringVar()
        self.display_menu_info_07 = StringVar()
        self.display_menu_info_08 = StringVar()


        '''
            widgets.
        '''
        self.master = master
        self.window_settings()
        
        self.server_init()

        #self.pack()
        self.grid()

        self.create_widgets()

        
    def server_init(self):
        '''
            table init.
        '''
        global TABLE_TOKEN

        table_headers = {'Authorization': 'Bearer ' + TOKEN}
        table_response = requests.post(TABLE_URL, headers=table_headers)
        if (table_response.status_code == 200):
            temp_table_token = table_response.json()
            TABLE_TOKEN = temp_table_token['token']
        else:
            messagebox.showerror("error", "table token error")
        
        print(TABLE_TOKEN)


        '''
            menu_init.
        '''
        menu_response = requests.get(MENU_LIST_URL)
        menu_json = menu_response.json()


        for item in menu_json:
            self.total_menu_num += 1
            self.menu_id.append(item['no'])
            self.total_menu_name.append(item['name'])
            self.total_menu_price.append(str(item['price']))
            #print(menu_text)
        
        while(self.total_menu_num % 8 != 0):
            self.total_menu_num += 1
            self.total_menu_name.append("x")
            self.total_menu_price.append("x")

        self.MAX_PAGE = self.total_menu_num / 8
            
        print(self.MAX_PAGE)
        print(self.total_menu_name)
        print(self.total_menu_price)
        print(self.menu_id)

        return


    def create_widgets(self):
        # image read test.
        #pht = self.read_image()

        #jFont = tkinter.font.Font(family="맑은 고딕", size=15, slant="italic")
        
        '''
            menu info init.
        '''
        self.display_menu_info_01.set(self.total_menu_name[(self.current_page * 8) + 0] + "\n가격 " + self.total_menu_price[(self.current_page * 8)+ 0])
        self.display_menu_info_02.set(self.total_menu_name[(self.current_page * 8) + 1] + "\n가격 " + self.total_menu_price[(self.current_page * 8)+ 1])
        self.display_menu_info_03.set(self.total_menu_name[(self.current_page * 8) + 2] + "\n가격 " + self.total_menu_price[(self.current_page * 8)+ 2])
        self.display_menu_info_04.set(self.total_menu_name[(self.current_page * 8) + 3] + "\n가격 " + self.total_menu_price[(self.current_page * 8)+ 3])
        self.display_menu_info_05.set(self.total_menu_name[(self.current_page * 8) + 4] + "\n가격 " + self.total_menu_price[(self.current_page * 8)+ 4])
        self.display_menu_info_06.set(self.total_menu_name[(self.current_page * 8) + 5] + "\n가격 " + self.total_menu_price[(self.current_page * 8)+ 5])
        self.display_menu_info_07.set(self.total_menu_name[(self.current_page * 8) + 6] + "\n가격 " + self.total_menu_price[(self.current_page * 8)+ 6])
        self.display_menu_info_08.set(self.total_menu_name[(self.current_page * 8) + 7] + "\n가격 " + self.total_menu_price[(self.current_page * 8)+ 7])



        '''
            8 menu buttons.
        '''
        self.menu01 = Button(self, textvariable=self.display_menu_info_01, command=lambda:self.menu_button_cmd(self.total_menu_price[0 + (self.current_page * 8)], self.menu01['text'], (self.current_page * 8) + 1))
        self.menu01.config(width=15, height=10)
        #self.menu01.image = pht

        self.menu02 = Button(self, textvariable=self.display_menu_info_02, command=lambda:self.menu_button_cmd(self.total_menu_price[1 + (self.current_page * 8)], self.menu02['text'], (self.current_page * 8) + 2))
        self.menu02.config(width=15, height=10)

        self.menu03 = Button(self, textvariable=self.display_menu_info_03, command=lambda:self.menu_button_cmd(self.total_menu_price[2 + (self.current_page * 8)], self.menu03['text'], (self.current_page * 8) + 3))
        self.menu03.config(width=15, height=10)

        self.menu04 = Button(self, textvariable=self.display_menu_info_04, command=lambda:self.menu_button_cmd(self.total_menu_price[3 + (self.current_page * 8)], self.menu04['text'], (self.current_page * 8) + 4))
        self.menu04.config(width=15, height=10)

        self.menu05 = Button(self, textvariable=self.display_menu_info_05, command=lambda:self.menu_button_cmd(self.total_menu_price[4 + (self.current_page * 8)], self.menu05['text'], (self.current_page * 8) + 5))
        self.menu05.config(width=15, height=10)

        self.menu06 = Button(self, textvariable=self.display_menu_info_06, command=lambda:self.menu_button_cmd(self.total_menu_price[5 + (self.current_page * 8)], self.menu06['text'], (self.current_page * 8) + 6))
        self.menu06.config(width=15, height=10)

        self.menu07 = Button(self, textvariable=self.display_menu_info_07, command=lambda:self.menu_button_cmd(self.total_menu_price[6 + (self.current_page * 8)], self.menu07['text'], (self.current_page * 8) + 7))
        self.menu07.config(width=15, height=10)

        self.menu08 = Button(self, textvariable=self.display_menu_info_08, command=lambda:self.menu_button_cmd(self.total_menu_price[7 + (self.current_page * 8)], self.menu08['text'], (self.current_page * 8) + 8))
        self.menu08.config(width=15, height=10)


        '''
            page control widgets.
        '''
        self.page_down = Button(self, text="<<", command=lambda:self.page_button('0'))
        self.page_down.config(width=30)
        self.page_up = Button(self, text=">>", command=lambda:self.page_button('1'))
        self.page_up.config(width=30)


        '''
            current status widgets.
        '''
        self.current_menu_label = Label(self, textvariable=self.current_menu_text)


        self.price_entry = Entry(self, width=20)
        self.price_entry.insert(0, "주문금액: 0")

        self.order_button = Button(self, text="주 문", command=lambda:self.order_button_cmd(''))
        self.order_button.config(width=15, height=5)

        self.refresh_botton = Button(self, text="초기화", command=lambda:self.refresh_button_cmd(''))
        self.refresh_botton.config(width=15, height=3)

        '''
            layout settings.
        '''
        self.menu01.grid(row=0, column=1, padx=5, pady=5)
        self.menu02.grid(row=1, column=1, padx=5, pady=5)
        self.menu03.grid(row=0, column=2, padx=5, pady=5)
        self.menu04.grid(row=1, column=2, padx=5, pady=5)
        self.menu05.grid(row=0, column=3, padx=5, pady=5)
        self.menu06.grid(row=1, column=3, padx=5, pady=5)
        self.menu07.grid(row=0, column=4, padx=5, pady=5)
        self.menu08.grid(row=1, column=4, padx=5, pady=5)
        self.page_down.grid(row=2, column=1, columnspan=2)
        self.page_up.grid(row=2, column=3, columnspan=2)
        self.current_menu_label.grid(row=0, column=5, rowspan=2, sticky='n')
        self.price_entry.grid(row=1, column=5, sticky='n')
        self.order_button.grid(row=1, column=5)
        self.refresh_botton.grid(row=2, column=5)


    def window_settings(self):
        self.master.title("main")
        self.master.geometry("800x400+0+0")
        self.master.resizable(False, False)


    def menu_button_cmd(self, value, text, m_id):
        print(value)
        print(text)

        if (value == 'x' or text == 'x'):
            messagebox.showwarning("warning", "void menu")
            return

        temp_str = ""
        temp_cnt = 0
        int_value = int(value)
        self.total_price += int_value
        self.price_entry.delete(0, 'end')
        self.price_entry.insert(0, self.total_price)
        self.price_entry.insert(0, "주문금액: ")

        if any(text in s for s in self.current_menu):
            for idx, cur in enumerate(self.current_menu):
                if text in cur:
                    self.current_menu_num[idx] += 1
        else:
            self.current_menu.append(text)
            self.current_menu_id.append(m_id)
            self.current_menu_num.append(1)

        print(self.current_menu)
        print(self.current_menu_num)
        print(self.current_menu_id)

        for idx, val in enumerate(self.current_menu):
            temp_str += self.current_menu[idx] + " x " + str(self.current_menu_num[idx]) + "개\n"


        self.current_menu_text.set(temp_str)
        return


    def refresh_button_cmd(self, value):
        self.total_price = 0
        self.price_entry.delete(0, 'end')
        self.price_entry.insert(0, self.total_price)
        self.price_entry.insert(0, "주문금액: ")
        
        self.current_menu = []
        self.current_menu_num = []
        self.current_menu_id = []
        self.current_menu_text.set("")
        return

    
    def order_button_cmd(self, value):
        print(TABLE_TOKEN)
        
        order_dict = {
            "menus": [
                
            ],
            "token": TABLE_TOKEN
        }

        for idx in range(len(self.current_menu_id)):
            temp = {
                'amount': self.current_menu_num[idx],
                'no': self.current_menu_id[idx]
            }
            order_dict['menus'].append(temp)
        
        print(order_dict)

        order_data = json.dumps(order_dict)
        headers = {'Content-Type': 'application/json; charset=utf-8'}

        order_response = requests.post(ORDER_URL, data=order_data, headers=headers)
        if (order_response.status_code == 200):
            messagebox.showinfo("success", "order success")
            self.refresh_button_cmd('')
        else:
            messagebox.showerror("error", "order fail")

        print(order_response.text)

        return


    def page_button(self, value):
        if (value == '0'):
            if (self.current_page > 0):
                self.current_page -= 1
            else:
                messagebox.showwarning("warning", "page underflow")
                return
        elif (value == '1'):
            if (self.current_page < self.MAX_PAGE):
                    self.current_page += 1
            else:
                messagebox.showwarning("warning", "page overflow")
                return

        '''
            menu info reset.
        '''
        self.display_menu_info_01.set(self.total_menu_name[(self.current_page * 8) + 0] + "\n가격 " + self.total_menu_price[(self.current_page * 8)+ 0])
        self.display_menu_info_02.set(self.total_menu_name[(self.current_page * 8) + 1] + "\n가격 " + self.total_menu_price[(self.current_page * 8)+ 1])
        self.display_menu_info_03.set(self.total_menu_name[(self.current_page * 8) + 2] + "\n가격 " + self.total_menu_price[(self.current_page * 8)+ 2])
        self.display_menu_info_04.set(self.total_menu_name[(self.current_page * 8) + 3] + "\n가격 " + self.total_menu_price[(self.current_page * 8)+ 3])
        self.display_menu_info_05.set(self.total_menu_name[(self.current_page * 8) + 4] + "\n가격 " + self.total_menu_price[(self.current_page * 8)+ 4])
        self.display_menu_info_06.set(self.total_menu_name[(self.current_page * 8) + 5] + "\n가격 " + self.total_menu_price[(self.current_page * 8)+ 5])
        self.display_menu_info_07.set(self.total_menu_name[(self.current_page * 8) + 6] + "\n가격 " + self.total_menu_price[(self.current_page * 8)+ 6])
        self.display_menu_info_08.set(self.total_menu_name[(self.current_page * 8) + 7] + "\n가격 " + self.total_menu_price[(self.current_page * 8)+ 7])

        return


    def read_image(self):
        base_folder = os.path.dirname(__file__)
        image_path = os.path.join(base_folder, 'testimage.png')
        test = Image.open(image_path)
        test = test.resize((100, 100), Image.ANTIALIAS)
        print(image_path)
        pht = ImageTk.PhotoImage(test)
        return pht


class Login(Frame):
    def __init__(self, master=None):
        super().__init__(master)

        '''
            values.
        '''
        self.user_id = StringVar()
        self.password = StringVar()
        self.login_flag = StringVar()

        '''
            widgets.
        '''
        self.master = master
        self.window_settings()
        

        #self.pack()
        self.grid()
        self.login_form()
    
    def login_form(self):
        self.login_flag.set("False")
        jFont = tkinter.font.Font(family="맑은 고딕", size=40, slant="italic")

        self.user_id_label = Label(self, text="ID: ", font=jFont).grid(row=0, column=0)
        self.user_id_entry = Entry(self, textvariable=self.user_id, font=jFont).grid(row=0, column=1)
        self.password_label = Label(self, text="Password: ", font=jFont).grid(row=1, column=0)
        self.password_entry = Entry(self, textvariable=self.password, show='*', font=jFont).grid(row=1, column=1)
        self.login_button = Button(self, text="Login", font=jFont, command=lambda:self.login_button_cmd()).grid(row=4, column=0)


        return

    
    def login_button_cmd(self):
        global TOKEN

        
        local_user_id = self.user_id.get()
        local_password = self.password.get()
            
        login_dict = {
            'id': local_user_id,
            'password': local_password
        }

        login_data = json.dumps(login_dict)
        headers = {'Content-Type': 'application/json; charset=utf-8'}

        print(login_data)

        login_respose = requests.post(LOGIN_URL, data=login_data, headers=headers)
        print(login_respose.status_code)
        if (login_respose.status_code == 200):
            temp_token = login_respose.json()
            TOKEN = temp_token['token']
            TOKEN_ACCESS = TRUE
            print(TOKEN)
            messagebox.showinfo("success", "login success")
            self.master.destroy()
        else:
            messagebox.showerror("error", "login fail")
            
        

        return


    def window_settings(self):
        self.master.title("login")
        self.master.geometry("800x400+0+0")
        self.master.resizable(False, False)


def main():
    '''
        login
    '''
    root_login = Tk()
    login = Login(master=root_login)
    login.mainloop()

    '''
        main
    '''
    root = Tk()
    app = Application(master=root)
    app.mainloop()



if __name__ == '__main__':
    main()
