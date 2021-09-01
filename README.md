# Virtual-Drawing-Pad
#### Task:- Creating a virtual drawing pad which will track a object referred to as a "stylus" and sketch out its motion.

#### A) Assigning HSV values to the stylus
1. Use camera to capture the frames.
2. Create trackbars to find the lower and higher HSV range of the stylus.
3. Convert the frame from BGR to HSV.
4. Create an array of the HSV values obtained.
5. Make a mask which sees the lower and the higher HSV values of the stylus.

#### B) Creating the Virtual Drawing Pad
1. Create a drawing space.
2. Use camera to capture the frames.
3. Flip the frames horizontally to avoid lateral inversion.
4. Convert the frames from BGR to HSV.
5. Put the values of the lower and higher HSV values obtained in part A.
6. Create a mask using the values in point 5
7. Convert the mask from BGR to Grayscale and apply thresholding accordingly.
8. Applying closing on the mask to remove the noise present in the frames being captured.
9. Dilation is applied after closing to remove the dark areas in the mask and it is applied multiple times to get a consistent shade.
10. The contour of the image obtained after dilation is found.
11. Find the contour with the largest area and note down its index.
12. Find the moment and the centroid of the largest contour.
13. Allot an inital and a final condition to start the loop.
14. The centroid of the contour is tracked to draw the line.
15. Display the sheet and the frame.
16. If 'esc' is pressed, destroy all the windows.

### Contributors
#### Soumyadeep Ghosh
