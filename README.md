# 310-tkinter-review
## Review of creating a gui with tkinter

TKinter is an object oriented interface that uses a CLASS to build a framework for a GUI Interface.  We will be using tkinter  to demonstrate how classes can be instantiated to build objects, and how those objects can interact with other objects within a program.

Today we will discuss the use of the Canvas widget for drawing shapes and will bind keystroke events that will update the position of objects on the screen.

* Create Canvas objects in the tkinter window
* Add simple shapes to the Canvas
* Add image icons to the Canvas
* Bind callback functions to keys
* Use callback functions to update objects on the canvas

One very important widget is the canvas, which allows us to draw objects in a window and go beyond the basic widgets.  While we can't specifically bind an event to a drawing object, we can bind an event to the canvas and see if the mouse position is inside the drawing object's coordinates.


Task 1 Basic Drawing
Create a canvas and draw a picture using the basic tkinter canvas shapes.  You should use different fill colors and outline colors
A good resource can be found at https://www.askpython.com/python-modules/tkinter/draw-shapes but Google is also a good place to look

Task 2 Moving the square
Use example2 as a guide.  Modify the existing code so that the square can not be moved off the canvas.

Task 3 Efficient Code
As you add more and more key bindings, you add more and more callback functions.  To prevent a massive number of callback functions being created, we can use a single callback function that instead retrieves data about the event.  Modify the task3.py to use a single callback function to move your object around the screen.

Task 4 Collisions
Add the code that moves the square around the screen.  Add a collision detector to see if the objects overlap. The square is not allowed to move in a way that makes it overlap with the black rectangle.
