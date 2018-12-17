from PIL import Image as ImagePIL
from PIL import ImageTk
from tkinter import *
from tkinter.filedialog import askopenfilename
import filters as f
import load as l
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
