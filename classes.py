import tkinter as tk 
import ctypes
import tkinter.font as font
import functions as f 

class root:
    def __init__(self):
        # root window
        self.root = tk.Tk()
        self.root.title('Minesweeper ZS 2.0')
        self.root.configure(bg='light goldenrod')

        # boolean that tells when the game is started
        self.gameStart = False

        # screen size
        user32 = ctypes.windll.user32
        self.user32_x = user32.GetSystemMetrics(0)
        self.user32_y = user32.GetSystemMetrics(1)
        
        self.root.minsize(800,800)
        self.newSize(0,0,1) # normal size is maximised

        # other widgets

        # title font
        self.font = font.Font(family='Helvetica', size=20, weight='bold')

        # name of the game
        self.name = tk.Label(self.root, text="Minesweeper", background='goldenrod', font=self.font, relief="solid")
        self.name.pack()
        self.name.place(x=self.current_x_size/2 - 250, y=self.current_y_size/7, width=500, height=100)

        # starting button
        self.start = tk.Button(self.root, text='Start the game!', background='goldenrod', activebackground='goldenrod', command = lambda:f.start_game(self))
        self.start.pack()
        self.start.place(x=self.current_x_size/2-150, y=self.current_y_size/2-100, height=100, width = 300)

        # name of the creator
        self.prop = tk.Label(self.root, text="Made by Sylvain Masclet",font=self.font, background='light goldenrod')
        self.prop.pack()
        self.prop.place(x=0,y=(self.current_y_size - 75))

        # settings button
        self.settings = tk.Button(self.root, text='Settings', background='goldenrod', activebackground='goldenrod', command = lambda:f.toSettings(self))
        self.settings.pack()
        self.settings.place(x=self.current_x_size/2-150, y=self.current_y_size/2+50, height=100, width = 300)

        # exit button
        self.exit = tk.Button(self.root, text="Quit", background='goldenrod', activebackground='goldenrod', command=self.quit)
        self.exit.pack()
        self.exit.place(x=self.current_x_size - 158, y=self.current_y_size/20, width = 80, height = 50)
        
        # label that displays the number of flags
        self.nbr_flags = tk.Label()

        # label that displays the number of bombs
        self.display_nbrbombs = tk.Label()

        #settings attributes
        self.sizel = tk.Listbox()
        self.rootS = tk.Frame()
        self.applyS = tk.Button()
        self.quitS = tk.Button()
        self.sizet = tk.Label()
        
        #settings difficulty
        self.diff = tk.IntVar() # index of difficulty
        self.diff.set(0)
        self.difflist = tk.Listbox()
        self.difft = tk.Label()

        #self.root.mainloop()


    #//////////////////////////////////////////  functions  //////////////////////////////////////#
    
    def quit(self): # stops the game
        self.root.destroy()
    
    def newSize(self,x,y,is_wind): # chooses throught the int is_wind if the window is in window mode, maximized mode or fullscreen mode.
        """
        if(is_wind == 0):
            self.current_x_size = x
            self.current_y_size = y

            self.offset_x=int((self.user32_x/2) - self.current_x_size/2)
            self.offset_y=int((self.user32_y/2) - self.current_y_size/2)

            self.root.geometry(str(self.current_x_size)+'x'+str(self.current_y_size)+'+'+str(self.offset_x)+'+'+str(self.offset_y))
            self.windowed = 0
        """
        self.current_x_size = self.user32_x
        self.current_y_size = self.user32_y
        
        if(is_wind == 1):
            self.root.attributes('-fullscreen',False)
            self.root.state('zoomed')
            self.windowed = 1

        elif(is_wind == 2):

            self.root.attributes('-fullscreen',True)
            self.windowed = 2
