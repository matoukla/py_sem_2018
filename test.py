# Simple filter tests
import numpy as np
import filters as f
import load as l
#----------------------------------------------------------------------
path = "C:/Users/klarm/Documents/pyth/py_sem_2018/kvetina.jpg"
l.make_dir ( path )
data_0 = l.data_image( path )

f.inv ( data_0, path )
f.gs ( data_0, path )
f.rt ( data_0, 1, path )
f.rt ( data_0, 2, path )
f.rt ( data_0, 3, path )
