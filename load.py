from PIL import Image
import numpy as np

#----------------------------------------------------------------------
def data_image ( open_img ) :
    i = Image.open( open_img ).convert( 'RGB' )
    return np.asarray( i )
