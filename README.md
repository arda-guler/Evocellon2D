# Evocellon2D
2D cellular automota. Simple to use and customize.

![evocellon2d](https://user-images.githubusercontent.com/80536083/173090237-2b42cf06-da4c-415d-86e7-2aa7e6fdd926.gif)

## How to Run
 - Run main.py.
 - Press (and hold) Enter to progress the cellular automaton.

## How to Code New Automatons
### Your Own Algorithm
 - Open autorules.py for editing.
 - Define new function with parameters in this order: 
   * Time (integer) 
   * center (current) cell 
   * All the neighboring cells, one by one, in this order: NW, N, NE, W, E, SW, S, SE. There are a total of 8 neighboring cells, as in the case of Moore neighborhood.
 - Write your algorithm to return a value for each cell. You may use or not use any parameters you wish. Just make sure that you define a return value for all cells, including those whose states are not changed.
 - Open main.py for editing.
 - Pass the name of your function as the update_func parameter into the init() function.
### Your Own Starting Conditions
 - Open autorules.py for editing.
 - Define new function to assign values to each individual cell.
 - Open main.py for editing.
 - Pass the name of your function as the init_func parameter into the init() function.
