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
def blur ( data, lvl, path ) :
    x = data.shape[0]
    y = data.shape[1]
    tmp = []
    blurr = np.copy ( data )

    for i in range( 0, x ):
        tmp.append( [] )
        for j in range( 0, y ):
            tmp[i].append( data[i, j] )
    for i in range( 0, x - 1 ):
        for j in range( 0, y - 1 ):
            r = 0
            g = 0
            b = 0
            for k in range( -1 * lvl, lvl + 1 ):
                for h in range ( -1 * lvl, lvl + 1 ):
                    if ( i + k < x - 1 and
                         j + h < y - 1 and
                         i + k >= 0 and j + h >= 0):
                        r = r + ( tmp[i+k][j+h][0] ) * (1 / float((2*lvl+1)*(2*lvl+1)))
                        g = g + ( tmp[i+k][j+h][1] ) * (1 / float((2*lvl+1)*(2*lvl+1)))
                        b = b + ( tmp[i+k][j+h][2] ) * (1 / float((2*lvl+1)*(2*lvl+1)))
                    else:
                        break
            blurr[i, j] = [ int(r), int(g), int(b) ]

    return blurr
#----------------------------------------------------------------------
def blr ( data, lvl, path ) :
    sv = path[0] + "/" + path[1].split('.')[0] + '/blur_' + path[1]
    out = Image.fromarray( blur( data, lvl, path ), mode = 'RGB' )
    out.save( sv )
    return sv
#----------------------------------------------------------------------
def shrp ( data, lvl, amount, threshold, path ) :
    blurr = blur( data, lvl, path )
    sh = float( amount + 1 ) * data - float( amount ) * blurr

    sh = np.maximum( sh, np.zeros( sh.shape ))
    sh = np.minimum( sh, 255 * np.ones( sh.shape ))
    sh = sh.round().astype( np.uint8 )

    if threshold > 0 :
        low_contrast = np.absolute( data - blurr ) < threshold
        np.copyto( sh, data, where = low_contrast )

    sv = path[0] + "/" + path[1].split('.')[0] + '/sharp_' + path[1]
    out = Image.fromarray( sh, mode = 'RGB' )
    out.save( sv )
    return sv
