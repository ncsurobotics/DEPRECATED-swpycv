
CC ?= gcc
PYTHON ?= python
PREFIX ?= /usr/local

LIB_NAME = swpycv/swpycv.so

OPENCV_FLAGS = $(strip $(shell pkg-config --libs --cflags opencv))
PYTHON_FLAGS = $(strip $(shell $(PYTHON)-config --includes))

SHORT_NAME = lib$(LIB_NAME).so

$(LIB_NAME): swpycv.c
	$(CC) $(OPENCV_FLAGS) $(PYTHON_FLAGS) -fPIC --shared -Wl,-soname,$(LIB_NAME) $< -o $@

install: $(LIB_NAME)
	$(PYTHON) setup.py install

clean:
	rm $(LIB_NAME)

.PHONY: clean
