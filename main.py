from tkinter import *;



# Variable deklaration

root                  = Tk();

img_starfleet         = PhotoImage(file='./__recources__/starfleet_logo.png');
img_enter             = PhotoImage(file='./__recources__/search_icon.png');
img_erase             = PhotoImage(file='./__recources__/erease_text.png');

search_frame          = Frame(root);

title                 = Label(root, text='Starfleet Command Library 1.0', font='Arial 15 bold' ,width=40, height=2);
subtitle              = Label(root, text='Programmed by HeSchy', fg='#555');
main_logo             = Label(root, image=img_starfleet);
search_btn_enter      = Button(search_frame, image=img_enter);
search_btn_delete     = Button(search_frame, image=img_erase);

# Settings

root.title('Starfleet Command Library');
root.resizable(False, False);




title.grid(row=1, column=1);
subtitle.grid(row=2, column=1);
main_logo.grid(row=3, column=2);
search_frame.grid(row=3, column=1, sticky="n");
search_btn_enter.grid(row=0, column=1);
search_btn_delete.grid(row=0, column=2);

root.mainloop();
