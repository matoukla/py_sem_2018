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
def mr ( data, axis, path ) :
    mirror = np.flip( data, axis )

    sv = path[0] + "/" + path[1].split('.')[0] + '/mr_' + str( axis ) + "_" + path[1]
    out = Image.fromarray( mirror, mode = 'RGB' )
    out.save( sv )
    return sv
#----------------------------------------------------------------------
def bgr ( data, path ) :
    B, G, R = data.T
    rgb = np.array((R, G, B)).T

    sv = path[0] +"/" + path[1].split('.')[0] +'/bgr_' + path[1]
    out = Image.fromarray( rgb, mode ='RGB' )
    out.save( sv )
    return sv
#----------------------------------------------------------------------
def blur( data, path ):
    l = []
    kernel = np.array( [[1.0,2.0,1.0],
                        [2.0,4.0,2.0],
                        [1.0,2.0,1.0]] )
    kernel = kernel / np.sum( kernel )

    for y in range( 3 ):
        tmp_Y = np.copy( data )
        tmp_Y = np.roll( tmp_Y, y - 1, axis = 0)
        for x in range( 3 ):
            tmp_X = np.copy( tmp_Y )
            tmp_X = np.roll( tmp_X, x - 1, axis = 1) * kernel[y,x]
            l.append( tmp_X )

    l = np.array( l )
    l_sum = np.sum( l, axis = 0 )
    return l_sum
#----------------------------------------------------------------------
def shrp ( data, lvl, amount, threshold, path ) :
    blurr = blur( data, path )
    sh = float( amount + 1 ) * data - float( amount ) * blurr

    sh = np.maximum( sh, np.zeros( sh.shape ))
    sh = np.minimum( sh, 255 * np.ones( sh.shape ))
    sh = sh.round().astype( np.uint8 )

    sv = path[0] + "/" + path[1].split('.')[0] + '/sharp_' + path[1]
    out = Image.fromarray( sh, mode = 'RGB' )
    out.save( sv )
    return sv
