# Convert to PNG Tool
This is a python command line tool to convert images to pngs. This tool utilized args and opencv modules.

# Requirements
 * Python 2.7
 * Opencv installed in python 2.7

# Usage
 * in command line use basic usage: 

`python.exe img_conversion_console.py -r image.jpg`

This will produce a converted image in the same location of the original image. without replacing the original image.

* usage with custom destination

`python.exe img_conversion_console.py -r image.jpg -s 'c:\converted_image.png`

This will put the resulted image in drive c or which ever drive specifies with -s

* usage with verbose and image show

`python.exe img_conversion_console.py -r image.jpg -w -v`

This will produce detailed output of every step in the code and will also show a window with the image resulted

* for help: 

`python.exe img_conversion_console.py -h`
