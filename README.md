# DataYoink <br />
A plot digitizer for battery discharge plots and dQdV plots from scientific literature <br />
### Use Cases: <br />
1.	Extract datapoints from battery discharge curves <br />
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;a.	Target Users: Researchers in the battery field <br />
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;b.	Input: .jpeg images of battery discharge figures <br />
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;c.	Output: Coordinates of datapoints on the discharge figures and axes labels <br />
2.	Extract datapoints from battery dQdV curves <br />
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;a.	Target Users: Researchers in the battery field <br />
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;b.	Input: .jpeg images of battery dQdV figures <br />
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;c.	Output: Coordinates of datapoints on the dQdV figures and axes labels <br />
3.	Extract legend and axis labels from generic scientific plots <br />
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;a.	Target Users: Researchers in any scientific field <br />
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;b.	Input: Generic 2D scientific figures with an x axis and a y axis <br />
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;c.	Output: Labels, units, and ranges of the x and y axes. <br />
4.	Clean up and digitize blurry battery discharge curves or dQdV curves <br />
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;a.	Target Users: Researchers in the battery field <br />
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;b.	Input: .jepg image of a blurry battery discharge plot or dQdV plot<br />
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;c.	Output: Coordinates of the datapoints and axis labels and range <br />
5.	Build new plot digitizer for a different scientific figure based on existing structure <br />
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;a.	Target Users: Researchers in any scientific field <br />
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;b.	Input: Trained neural network that identifies the locations of datapoints on certain types of figures <br />
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;c.	Output: A plot digitizer for a new figure type <br />
