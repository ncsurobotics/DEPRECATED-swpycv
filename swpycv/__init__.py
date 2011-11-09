
import cv
import ctypes
import os.path

package_dir = os.path.dirname(os.path.abspath(__file__))
_SWPYCV_PATH = "%s/swpycv.so" % (package_dir,)

class ImageProperties(ctypes.Structure):
    _fields_ = [
        ("width", ctypes.c_uint16),
        ("height", ctypes.c_uint16),
        ("depth", ctypes.c_uint8),
        ("channels", ctypes.c_uint8)
    ]

_swpycv = ctypes.cdll.LoadLibrary(_SWPYCV_PATH)
_swpycv.SWPYCV_getIplProperties.restype = ImageProperties
_swpycv.SWPYCV_getIplProperties.argtypes = [ctypes.c_void_p]
_swpycv.SWPYCV_getIplPointer.restype = ctypes.c_void_p
_swpycv.SWPYCV_getIplPointer.argtypes = [ctypes.py_object]
_swpycv.SWPYCV_copyIplToPyIpl.restype = None
_swpycv.SWPYCV_copyIplToPyIpl.argtypes = [ctypes.c_void_p, ctypes.py_object]
_swpycv.SWPYCV_copyPyIplToIpl.restype = None
_swpycv.SWPYCV_copyPyIplToIpl.argtypes = [ctypes.py_object, ctypes.c_void_p]
_swpycv.SWPYCV_releaseIpl.restype = None
_swpycv.SWPYCV_releaseIpl.argtypes = [ctypes.c_void_p]

def get_ipl_properties(ipl_ptr):
    return _swpycv.SWPYCV_getIplProperties(ipl_ptr)

def get_ipl_from_pyipl(pyipl_object):
    return _swpycv.SWPYCV_getIplPointer(pyipl_object)

def copy_ipl_to_pyipl(ipl_src, pyipl_dest):
    _swpycv.SWPYCV_copyIplToPyIpl(ipl_src, pyipl_dest)

def copy_pyipl_to_ipl(pyipl_src, ipl_dest):
    _swpycv.SWPYCV_copyPyIplToIpl(pyipl_src, ipl_dest)

def release_ipl(ipl_ptr):
    _swpycv.SWPYCV_releaseIpl(ipl_ptr)

def pyipl_from_ipl(ipl_ptr):
    prop = get_ipl_properties(ipl_ptr)
    pyipl = cv.CreateImage((prop.width, prop.height), prop.depth, prop.channels)
    copy_ipl_to_pyipl(ipl_ptr, pyipl)
    return pyipl
