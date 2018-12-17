from PIL import Image as ImagePIL
from PIL import ImageTk
from tkinter import *
from tkinter.filedialog import askopenfilename
import filters as f
import load as l
import os
# This is file that contains class that manages the GUI of the app
# For GUI is used Tkinter
#----------------------------------------------------------------------
class App( Tk ):
    def __init__( sef ):
        Tk.__init__( self )
        self.filename = ""
        self.formats = [ ('JPEG','*.jpg'),
                         ('Windows Bitmap','*.bmp'),
                         ('Portable Network Graphics','*.png') ]
        self.options = ( 'invert', 'greyscale', 'rotate', 'bgr',
                         'brighten', 'darken', 'mirror', 'blur', 'sharp' )
        self.loptions = StringVar( value = self.options )
        # --------------------------------------L1
        self.l1 = Label( self, text = "basic image edits ©",
                               foreground = "blue",
                               font = ( "Times New Roman", 13 ) )
        self.l1.pack()
        # --------------------------------------B1
        self.b1 = Button( self, text = "Browse",
                                width = 25,
                                command = self.OpenFile )
        self.b1.pack( side = TOP )
        # --------------------------------------B2
        self.b2 = Button( self, text = "Exit",
                                width = 25,
                                command = lambda:exit() )
        self.b2.pack( side = TOP )

        self.mainloop()
    #------------------------------------------------------------------
    def NewWindow ( self, nf ) :
        window = Toplevel( self )
        window.title( "Result" )

        img = ImagePIL.open( nf )
        photo = ImageTk.PhotoImage( img )
        self.l3 = Label( window, image = photo )
        self.l3.image = photo
        self.l3.pack()
    #------------------------------------------------------------------
    def ProccessOption ( self ) :
        item = self.lbox.curselection()
        nf = ""

        if item[0] == 0 :
            nf = f.inv( self.data_0, self.path )
        if item[0] == 1 :
            nf = f.gs( self.data_0, self.path )
        if item[0] == 2 :
            nf = f.rt( self.data_0, int ( self.s1.get() ), self.path )
        if item[0] == 3 :
            nf = f.bgr( self.data_0, self.path )
        if item[0] == 4 :
            nf = f.bd( self.data_0, int ( self.w1.get() ), True, self.path )
        if item[0] == 5 :
            nf = f.bd( self.data_0, int ( self.w1.get() ), False, self.path )
        if item[0] == 6 :
            nf = f.mr( self.data_0, int ( self.vx.get() ) , self.path )
        if item[0] == 7 :
            nf = f.blr( self.data_0, 1, self.path )
        if item[0] == 8 :
            nf = f.shrp( self.data_0, 1, 1.0, 0, self.path )
        else :
            pass

        self.NewWindow( nf )
        self.l3 = Label( self, text = "Exported to " + nf,
                               foreground = "black",
                               font = ( "Times New Roman", 10 ) )
        self.l3.pack()
    #------------------------------------------------------------------
    def Details ( self ) :
        item = self.lbox.curselection()
        self.lbox.config( state = DISABLED )
        self.b4.config( state = DISABLED )
        self.vx = IntVar()

        if item[0] == 2 :
            self.ls1 = Label( self, text = "iterations:" ).pack()
            self.s1 = Spinbox( self, from_ = 1, to = 3 )
            self.s1.pack()
        if item[0] == 4 :
            self.ls1 = Label( self, text = "range:" ).pack()
            self.w1 = Scale( self, from_ = 0, to = 100, orient = HORIZONTAL )
            self.w1.pack()
        if item[0] == 5 :
            self.ls1 = Label( self, text = "range:" ).pack()
            self.w1 = Scale( self, from_= 0, to = 100, orient = HORIZONTAL )
            self.w1.pack()
        if item[0] == 6 :
            self.ls1 = Label( self, text = "axis:" ).pack()
            self.r1 = Radiobutton( self, text ='X', variable = self.vx, value = 0).pack()
            self.r2 = Radiobutton( self, text ='Y', variable = self.vx, value = 1).pack()
        else :
            pass

        self.b3 = Button ( self, text = "Go!",
                                 width = 25,
                                 command = self.ProcessOption )
        self.b3.pack()
    #------------------------------------------------------------------
    def ChooseOption( self ) :
        self.lbox = Listbox( self, listvariable = self.loptions,
                                   font = ( 'Arial', 10 ),
                                   height = 9 )
        self.lbox.pack( side = LEFT )
        self.lbox.select_set( 0 )

        self.b4 = Button ( self, text = "Choose",
                                 width = 25,
                                 command = self.Details )
        self.b4.pack( side = TOP )
    #------------------------------------------------------------------
    def LoadImage( self ) :
        img = ImagePIL.open( self.filename )
        photo = ImageTk.PhotoImage( img )
        self.l2 = Label( self, image = photo )
        self.l2.image = photo
        self.l2.pack()
        self.b1.config( state = DISABLED )
    #------------------------------------------------------------------
    def OpenFile( self ) :
        self.filename = askopenfilename (
                         initialdir = "C:/Users/klarm/Documents/pyth",
                         filetypes = self.formats,
                         title = "Choose file" )
        try :
            with open( self.filename, 'r' ) as UseFile :
                pass

            self.path = os.path.split( self.filename )
            l.make_dir ( self.filename )
            self.data_0 = l.data_image( self.filename )

            self.LoadImage()
            self.ChooseOption()
            self.geometry("800x650")

        except :
            self.OpenFile()
#----------------------------------------------------------------------
