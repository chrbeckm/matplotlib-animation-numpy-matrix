all: animation.gif

animation.gif: animation.py data.dat | build
	python animation.py

build:
	mkdir -p build

clean:
	rm -rf build

.PHONY: all clean
