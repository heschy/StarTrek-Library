from tkinter import *;
import starfleet;

root                  = Tk();

# --------------------------------- Add Variables and Functions ---------------------------------

# --- Functions ---

def libexec():
    information_label['text'] = starfleet.library(search_entry.get());

def clear_entry():
    search_entry.delete(0);

# --- Images ---


img_starfleet         = PhotoImage(file='./__recources__/starfleet_logo.png');
img_enter             = PhotoImage(file='./__recources__/search_icon.png');
img_stop              = PhotoImage(file='./__recources__/stop_icon.png');


# --- Frames ---

search_frame          = Frame(root);

# --- Header ---

title                 = Label(  root,         text='Starfleet Command Library 1.0', font='Arial 15 bold' ,width=40, height=2);
subtitle              = Label(  root,         text='Programmed by HeSchy', fg='#555');

# --- Logo ---

main_logo             = Label(  root,         image=img_starfleet);

# --- Search Area ---

search_entry          = Entry(  search_frame, width=50 );
search_btn_enter      = Button( search_frame, image=img_enter,  command=libexec);
search_btn_delete     = Button( search_frame, image=img_stop,   command=clear_entry);

# --- Answer ---

information_label     = Label(root, text='Bitte geben sie suchparameter ein.', bg='#000', fg='#fff');

# --------------------------------- Change Preferences ---------------------------------

root.title('Starfleet Command Library');
root.resizable(False, False);

# --------------------------------- Locate the Widgets ---------------------------------

title.grid(row=1, column=1);
subtitle.grid(row=2, column=1);
main_logo.grid(row=3, column=2);
search_frame.grid(row=3, column=1, sticky="n");
search_btn_enter.grid(row=0, column=1);
search_btn_delete.grid(row=0, column=2);
search_entry.grid(row=0, column=0);
information_label.grid(row=4, column=0, columnspan=3);

# --------------------------------- Start the Main Loop ---------------------------------

root.mainloop();
