from PIL import Image
import numpy as np
#----------------------------------------------------------------------
def data_image ( open_img ) :
    i = Image.open( open_img ).convert( 'RGB' )
    return np.asarray( i )
#----------------------------------------------------------------------
def make_dir ( p ) :
    dir = p.split( '.' )
    if not os.path.exists( dir[0] ) :
        os.mkdir( dir[0] )
#----------------------------------------------------------------------
