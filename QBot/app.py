from tkinter import *
from chat_gui import get_response, bot_name

clr_panel = '#404040'
clr_bg = '#282828'
clr_txt = '#ffffff'
clr_mbox = '#181818'
clr_send = '#8899a6'
header_txt = 'Welcome To QBot - GUI prototype for qworld.net'

font = 'Arial 14'
font_bold = 'Arial 13 bold'


class ChatApplication:
    def __init__(self):
        self.window = Tk()
        self._setup_main_window()

    def run(self):
        self.window.mainloop()

    def _setup_main_window(self):
        self.window.title(bot_name)
        self.window.resizable(width=True, height=True)
        self.window.configure(width = 450, height = 600, bg = clr_bg)
    
        #head
        head_label = Label(self.window, bg = clr_bg, fg= clr_txt, text= header_txt, font = font_bold, pady = 10)
        head_label.place(relwidth = 1)
        #divider
        line = Label(self.window, width = 500, bg = clr_panel)
        line.place(relwidth = 1, rely = 0.7, relheight = 0.015)
        #text
        self.text_widget = Text(self.window, width = 20, height = 2, bg = clr_bg, fg = clr_txt, font = font, padx = 5, pady = 5)
        self.text_widget.place(relheight = 0.745, relwidth = 1, rely = 0.08)
        self.text_widget.configure(cursor='arrow', state=DISABLED)
        #scroll
        scroller = Scrollbar(self.text_widget)
        scroller.place(relheight = 1, relx = 0.974)
        scroller.configure(command = self.text_widget.yview)
        #foot
        footer = Label(self.window, bg = clr_panel, height = 80)
        footer.place(relwidth = 1, rely =  0.825)
        #message_box
        self.mbox = Entry(footer, bg = clr_mbox, font= font, fg= clr_txt)
        self.mbox.place(relwidth= 0.74, relheight=0.06, relx= 0.011, rely= 0.008)
        self.mbox.focus()
        self.mbox.bind('<Return>', self._on_enter_pressed)
        #send_button
        self.send = Button(footer, text='Send', font=font_bold, width=20, bg=clr_send, command= lambda: self._on_enter_pressed(None))
        self.send.place(relwidth=0.22, relx = 0.77, rely=0.008, relheight=0.06)


    def _on_enter_pressed(self, event):
        msg = self.mbox.get()
        self._insert_msg(msg,'You')

    def _insert_msg(self, msg, sender):
        if not msg:
            return

        self.mbox.delete(0,END)
        usermsg = f'{sender}: {msg}\n\n'
        self.text_widget.configure(state=NORMAL)
        self.text_widget.insert(END, usermsg)
        self.text_widget.configure(state=DISABLED)

        botmsg = f'{bot_name}: {get_response(msg)}\n\n'
        self.text_widget.configure(state=NORMAL)
        self.text_widget.insert(END, botmsg)
        self.text_widget.configure(state=DISABLED)

        self.text_widget.see(END)



if __name__ == '__main__':
    app = ChatApplication()
    app.run()