# fore-seg

This is a repository to extract the foreground from background in relatively noiseless images. A set of relatively noiseless images can be found here - https://goo.gl/QfSzz0

To get an extracted image from an input image, just run the following command:

    python foreground.py [path to input folder] 

This will create a file called output.png in your repo directory.

Known Bugs:
1. Will not work if the background is not noiseless.
2. Gives a buggy output if the foreground and background is very similar.
