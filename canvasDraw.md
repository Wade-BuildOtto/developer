the purpose of the web based application is to draw lines on a canvas with options set by dat.gui controls

#### index.html
- contains the canvas and script.js 
- include dat.gui from cdnjs
- the body has styling of no margin or padding

#### script.js
- the javascript should be written in a prototypal Instantiation pattern and not classes and be ES6 compatible
- the main function is named canvasDraw and is exposed to window for console access
- make sure to set the default canvas width and height to match the pages diamentions and scale, update it if the window resize fires
- when the mouse on drag start a new line entry is created and drawing a line on the canvas is started
- as thse mouse moves in any direction, once the mouse goes beyond a defined distance from the previous point to the current mouse position is a new point is created
- a solid gray circle of 4px centered is drawn and maintained and centered for each point on the line, and is used a reference for each point
- at drag stop the circles are removed 
- as the mouse is dragging and moves the canvas is re-drawn maintains the drawn lines on the canvas, including the active point to the mouse
- the lines are draw smooth lines with bezier curve with a round end cap
- each line is stored as a new line object with and random id, color, line_thickness and stores the points in an object array called pts. 
- the lines are redraw with requestAnimationFrame()
- updates to the features of the line come from the dat.gui controls

#### dat.gui
- the gui is default as open on the html page
- distance: a sliders option for adjusting the distance default of 30px with a range of min of 5 to max of 200
- line thickness: defaults to 3px with a range of min: 1px to max: 40px and should update the line thickness
- line color: a color picker to set the color of the next drawn line with a default of black
- clear canvas button: clears the canvas and erases the line data
- export png button: saves the canvas to a png toDataURL and sets it to automically download
- changes from these controls update to new lines drawn