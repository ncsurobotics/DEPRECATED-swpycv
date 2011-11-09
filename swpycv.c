
#include <Python.h>
#include <cv.h>

/* Representation of OpenCV IplImage within Python. Pulled from OpenCV Python
   interface code (modules/python/cv.cpp) */
struct iplimage_t {
    PyObject_HEAD
    IplImage *a;
    PyObject *data;
    size_t offset;
};

struct ImageProperties {
    uint16_t width;
    uint16_t height;
    uint8_t depth;
    uint8_t channels;
};

/**
 * Extract the basic properties from the given IplImage. This is useful when a
 * function returns IplImage* and a Python IplImage must be created with the
 * same properties before copying the data
 */
struct ImageProperties SWPYCV_getIplProperties(IplImage* img) {
    struct ImageProperties properties;

    properties.width = img->width;
    properties.height = img->height;
    properties.depth = img->depth;
    properties.channels = img->nChannels;

    return properties;
}

/**
 * Extract the IplImage* from a Python IplImage. This is useful for interfacing
 * to functions that take IplImage* as arguments (either input or output)
 */
IplImage* SWPYCV_getIplPointer(struct iplimage_t* img) {
    return img->a;
}

/**
 * Copy the contents of an IplImage* to a Python IplImage
 */
void SWPYCV_copyIplToPyIpl(IplImage* src, struct iplimage_t* dest) {
    memcpy(dest->a->imageData, src->imageData, src->imageSize);
}

/**
 * Copy the contents of a Python IplImage to a IplImage*
 */
void SWPYCV_copyPyIplToIpl(struct iplimage_t* src, IplImage* dest) {
    memcpy(dest->imageData, src->a->imageData, dest->imageSize);
}

/**
 * Release the IplImage*
 */
void SWPYCV_releaseIpl(IplImage* src) {
    cvReleaseImage(&src);
}
