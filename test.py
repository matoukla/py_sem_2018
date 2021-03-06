# Simple filter tests
import numpy as np
import filters as f
import load as l
import os
#----------------------------------------------------------------------
path_0 = "C:/Users/klarm/Documents/pyth/py_sem_2018/kvetina.jpg"
path = os.path.split( path_0 )
l.make_dir ( path_0 )
data_0 = l.data_image( path_0 )

f.inv ( data_0, path )
f.gs ( data_0, path )
f.rt ( data_0, 1, path )
f.rt ( data_0, 2, path )
f.rt ( data_0, 3, path )
f.bd ( data_0, 50, True, path )
f.bd ( data_0, 50, False, path )
f.mr ( data_0, 0, path )
f.mr ( data_0, 1, path )
f.bgr ( data_0, path )
f.shrp ( data_0, 1, 1.0, 0, path )
