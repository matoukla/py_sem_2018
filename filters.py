from PIL import Image
import numpy as np
#------------------------------------------------------------------------------
def inv ( data, path ) :
    neg = 255 - data

    sv = path[0] + "/" + path[1].split('.')[0] + '/inv_'+ path[1]
    out = Image.fromarray( neg, mode = 'RGB' )
    out.save( sv )
    return sv
#----------------------------------------------------------------------
def gs ( data, path ) :
    gs = ( 0.299, 0.587, 0.114 ) * data
    gss = np.sum( gs, axis = 2 )

    sv = path[0] + "/" + path[1].split('.')[0] + '/gs_' + path[1]
    out = Image.fromarray( (gss + 0.5).astype( dtype = np.uint8 ),'L' )
    out.save( sv )
    return sv
#----------------------------------------------------------------------
