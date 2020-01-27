# pyMetronomeSync #
This is a basic Python 3implementation of the spreadsheet presented in [this video](https://www.youtube.com/watch?v=J4PO7NbdKXg), in which Matt Parker demonstrates the mathematical synchronisation of three metronones in a spreadsheet. Feeling the need to add something more to my To-Do list,  I thought I'd have a go at creating this in Python.

Currently the model allows forchanging of the start parameters:
* inc - the increment of each step
* k - the constant used for the Kuramoto model
* xlim - Your limit in the X direction.
* mncount - How many metronomes would you like

When initialising the Metronome, a random integer offset between 0 and 42 will be chosen for the initial offset of the instance> No real reason other than I like 42...

It's far from perfect at the moment, I want to add a UI for a bit more user-friendly fiddling, as well as adding an implementation for the Out-of-Sync variant discovered in the video, and maybe a sync indicator

## Usage ##
More documentation to follow, but after ensuring you have Python3, numpy and matplotlib installed on your system:
```
python3 metronome.py
```
Should give you a window showing a dynamically updating graph with a line representing each metronome