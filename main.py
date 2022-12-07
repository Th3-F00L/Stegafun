from enums import RGB
from enums import Operation
from enums import EncodingMode
from enums import EncryptionOptions
import stegafun as stega

from tkinter import *
from tkinter import filedialog
from pathlib import Path


def len_of_longest_element(lst: list):
    max_len = -1
    for item in lst:
        if len(item) > max_len:
            max_len = len(item)
    return max_len


def generate_main_window() -> Tk:
    w = '800'
    h = '600'
    window = Tk()
    window.configure(bg=bg, )
    window.title('Stega-Fun')
    window.geometry(f'{w}x{h}')
    return window


def generate_dropdown(steg_enum, command, master) -> tuple[OptionMenu, StringVar]:
    enum_list = []
    for element in steg_enum:
        enum_list.append(element.name.title())

    var = StringVar()
    var.set(enum_list[0])
    drpdwn = OptionMenu(master, var, *enum_list, command=command)
    drpdwn.configure(font=('Courier', 14), bg=button_color, fg=fg,
                     width=len_of_longest_element(enum_list),
                     activeforeground=fg, activebackground=button_hover,
                     highlightbackground=bg, border=1)
    return drpdwn, var


def generate_checkbox(text: str, master) -> [Checkbutton, BooleanVar]:
    box_color = '#888888'
    var = BooleanVar()
    cbox = Checkbutton(master, text=text, variable=var)
    cbox.configure(font=('Courier', 12), bg=bg, fg=fg, selectcolor=box_color,
                   highlightbackground=bg, activebackground=bg, activeforeground=fg)
    return cbox, var


def generate_radiobutton(text: str, master) -> Radiobutton:
    rad_color = '#888888'
    rad = Radiobutton(master, text=text, variable=val_operation)
    rad.configure(font=('Courier', 12), bg=bg, fg=fg, selectcolor=rad_color,
                  highlightbackground=bg, activebackground=bg, activeforeground=fg)
    return rad


def generate_button(text: str, master):
    btn = Button(master, text=text, font=('Courier', 12), bg=bg, fg=fg, activeforeground=fg,
                 activebackground=button_hover, highlightbackground=bg, border=1)
    return btn


def generate_label(text: str, master) -> Label:
    label = Label(master, text=text, font="Courier", fg=fg, bg=bg)
    return label


def place_tbox_msg():
    tbox_msg.grid(row=0, column=0, ipady=10, ipadx=20, pady=10, padx=20, sticky='W')


def hide_tbox_msg():
    tbox_msg.grid_forget()


def toggle_operation():
    global operation
    operation = Operation(val_operation.get())
    btn_run.configure(text=f'{operation.name.title()} Image' )
    if operation == Operation.RECOVER:
        hide_tbox_msg()
    else:
        place_tbox_msg()


def update_rgb(event):
    rgb = RGB[val_rgb.get().upper()]
    drpdwn_rgb.configure(fg=val_rgb.get())

def invoke_file_dialog():
    file_types = [('PNGs', '*.png')]
    global filepath
    filepath = filedialog.askopenfilename(title='Please Select a PNG Image',
                                      initialdir=Path.home() / 'Pictures',
                                      filetypes=file_types)
    if filepath:
        btn_fileselect.configure(text=filepath, font=('Courier', 9))
    return filepath

def msg_onclick(event):
    tbox_msg.configure(state='normal')
    tbox_msg.delete(0, END)
    tbox_msg.unbind('<Button-1>', msg_clicked)

def run():
    if lbl_result.cget('text') != '':
        lbl_result.configure(text='')
    match operation:
        case Operation.CONCEAL:
            result=(stega.conceal_msg(val_msg.get(), filepath, rgb))
        case Operation.RECOVER:
            result = stega.recover_msg(filepath, rgb)
        case _:
            result = 'An Unkown error has occured!'
    lbl_result.configure(text=result)




#   [ PAYLOAD ]     #

operation = Operation.CONCEAL
rgb = RGB.RED
filepath = ''
bg = '#424242'
fg = '#FFFFFF'
button_color = '#494949'
button_hover = '#333333'
window = generate_main_window()

lbl_title = generate_label("Welcome To Stega-Fun!", window)
lbl_title.configure(font=("Courier", 36, 'bold'))
lbl_title.grid(row=0, column=0, columnspan=5, padx=5, pady=10)

lbl_whitespace1 = generate_label('', window)
lbl_whitespace1.grid(row=1, column=0, columnspan=5)

# RGB Section
frame_rgb = Frame(window, borderwidth=1, bg=bg, relief="solid")
frame_rgb.grid(row=2, column=0, padx=25, sticky='w')

lbl_rgb = generate_label("Which RGB value should\n we hide the message in?", frame_rgb)
lbl_rgb.grid(row=0, column=0, ipadx=10, ipady=10, padx=(0, 20), )

drpdwn_rgb, val_rgb = generate_dropdown(RGB, update_rgb, frame_rgb)
drpdwn_rgb.configure(fg=rgb.name)
drpdwn_rgb.grid(row=0, column=1, padx=(0, 20))

val_operation = IntVar()

# Radio Button Section
frame_operation = Frame(window, borderwidth=1, bg=bg, relief="solid")
frame_operation.grid(row=2, column=1, padx=25, sticky='w')

lbl_operation = generate_label('Choose an Operation:', window)
lbl_operation.configure(font=('Courier', 12))
lbl_operation.grid(row=1, column=1)


rad_conceal = generate_radiobutton('Conceal Message', frame_operation)
rad_conceal.configure(command=toggle_operation, variable=val_operation,
                      value=Operation.CONCEAL.value)
rad_conceal.grid(row=0, column=0, ipady=2.5, ipadx=20)

rad_recover = generate_radiobutton('Recover Message', frame_operation)
rad_recover.configure(command=toggle_operation, variable=val_operation,
                      value=Operation.RECOVER.value)
rad_recover.grid(row=1, column=0, ipady=2.5, ipadx=20)

# payload section

frame_payload = Frame(window, borderwidth=1, bg=bg, relief="solid")
frame_payload.grid(row=3, column=0, padx=25, pady=50, columnspan=5, sticky='W')

btn_fileselect = generate_button('Please Select a PNG to Work With...', frame_payload)
btn_fileselect.configure(command=invoke_file_dialog)
btn_fileselect.grid(row=1, column=0, ipady=10, ipadx=10, padx=(20), pady=10)

btn_run = generate_button(f'{operation.name.title()} Image', frame_payload)
btn_run.configure(command=run)
btn_run.grid(row=1, column=1, ipady=10, ipadx=20, pady=10, padx=20)

val_msg = StringVar()
tbox_msg = Entry(frame_payload, width=50, textvariable=val_msg)
val_msg.set('Please Enter Your Secret Message')
place_tbox_msg()
msg_clicked = tbox_msg.bind('<Button-1>', msg_onclick)

lbl_result = generate_label('', window)
lbl_result.configure(font=('Courier', 14), fg='cyan', wraplength=500, anchor='w', justify='left')
lbl_result.grid(row=5, column=0, sticky='w')

window.mainloop()

# Future Code

# drpdwn_mode, val_mode = generate_dropdown(EncodingMode)
# drpdwn_mode.grid(row=1, column=0)
#
# drpdwn_encryption, val_encryption = generate_dropdown(EncryptionOptions)
# drpdwn_encryption.grid(row=1, column=1)

# modes = []
# for option in Encoding_Mode:
#     modes.append(option.name.title())
# mode_clicked = StringVar()
# mode_clicked.set(modes[0])
# drpdwn_mode = tkinter.OptionMenu(window, mode_clicked, *modes)
# drpdwn_mode.configure(font=('Courier', 18), width=max(modes, key=len))
# drpdwn_mode.grid(row=1, column=0)

# drpdwn_encryption = tkinter.OptionMenu(window)
# drpdwn_encryption.grid(row=2, column=0)
#
# drpdwn_color = tkinter.OptionMenu(window)
# drpdwn_color.grid(row=1, column=0)

