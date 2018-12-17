from PIL import Image as ImagePIL
from PIL import ImageTk
from tkinter import *
from tkinter.filedialog import askopenfilename
import filters as f
import load as l
#----------------------------------------------------------------------
class App( Tk ):
    def __init__( sef ):
        Tk.__init__( self )
        self.filename = ""
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

        self.mainloop()
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
#----------------------------------------------------------------------
