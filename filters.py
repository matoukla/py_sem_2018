from PIL import Image
import numpy as np
# This file contains all basic image operations and exports the result
# Uses numpy array from imported image
# Operations :
#   Invert
#   Grayscale
#   Rotate
#   Brighten/Darken
#   Mirror
#   BGR swap
#   Blur
#   Sharpen
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
def rt ( data, iterations, path ) :
    rot = data
    for i in range ( iterations ) :
        rot = np.rot90( rot )

    sv = path[0] + "/" + path[1].split('.')[0] + '/rt_'+ str( iterations ) + "_" + path[1]
    out = Image.fromarray( rot, mode = 'RGB' )
    out.save( sv )
    return sv
#----------------------------------------------------------------------
def bd ( data, extent, bright, path ) :
    val = float( extent ) / 100.0
    mult = 1.0

    if bright is True :
        mult += val
    else :
        mult -= val

    bd = data * mult
    bd[ bd > 255 ] = 255
    bd[ bd < 0 ] = 0

    sv = path[0] + "/" + path[1].split('.')[0] + '/bd_'+ str( int( bright ) ) + '_'+ path[1]
    out = Image.fromarray( bd.astype( dtype = np.uint8 ), mode ='RGB' )
    out.save( sv )
    return sv
#----------------------------------------------------------------------
