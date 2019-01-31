# Colour_detection_python
Used masking to find out the dominant colour in a photo clicked using the PiCam.
Works on the Raspberry Pi directly.
Algorithm :
1. Import image.
2. FInd the total no. of pixels by multiplying width and height.
3. Mask the image in colours of ranges (RED, GREEN, BLUE)
4. Calculate the no. of non zeros for each specific colour.
5. Compare the non zeros of each specific colour to find the highest colour density.
6. Speech output the dominant colour in the picture.

