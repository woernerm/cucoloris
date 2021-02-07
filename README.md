# Cucoloris
Cucoloris is a library that brings the well-known and beloved look of 
Bootstrap to [Kivy](https://kivy.org/). The library is 
named after a [device](https://en.wikipedia.org/wiki/Cucoloris) 
common in the film industry for simulating shadow patterns that give 
the scene a more natural look. <br />
Like Bootstrap, the library offers widgets that you can use for your 
application. The names are almost identical to those in Bootstrap. 
However, class names are written in camel-case instead of kebab-case, 
because Python does not allow for dashes in class names. This allows you
to refer to the Bootstrap documentation to try out and select the 
component you would like to add and quickly find it in Cucoloris as 
well. <br />
While the look of Cucoloris closely resembles that of Bootstrap, it also 
offers additional functionality that may not be part of Bootstrap.
For example, Cucoloris' FormControl (resembling form-control 
in Bootstrap) also offers the ability to enter formatted text and 
its scroll bar has rounded edges to better fit the component. <br />
<br/>
The development of Cucoloris is in an early stage and the API might
change. Thus far, the following widgets are available:

* Buttons
    * Default buttons like BtnPrimary, BtnSecondary, BtnSuccess, etc.
    * Outline buttons: BtnOutlinePrimary, BtnOutlineSecondary, 
    BtnOutlineSuccess, etc.
* Forms:
    * FormControl
