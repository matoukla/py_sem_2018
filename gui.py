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
#----------------------------------------------------------------------
