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

        self.mainloop()
    #------------------------------------------------------------------
    def OpenFile( self ) :
        self.filename = askopenfilename (
                 initialdir = "C:/Users/klarm/Documents/pyth",
                 filetypes = self.formats,
                 title = "Choose file" )
                 
        self.path = os.path.split( self.filename )
        l.make_dir ( self.filename )
        self.data_0 = l.data_image( self.filename )
#----------------------------------------------------------------------
