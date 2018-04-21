* Cover Page
    * A cover page containing your group member names, project title, course number, and semester
    * Github URL
    * Project Demo Presentation as Google Slide URL
Example:
# Space Shooter 2
## CS 110 Final Project
### Spring,2018

### Link to Github Repo:
[https://github.com/binghamtonuniversity-cs110/final-project-spr18-py-pandas.git](#)

### Link to Presentation Slides:
https://docs.google.com/presentation/d/12Tb9pJZSVkh1yvmBxMbkxDWFgUyJRNiqf-J5I8sy3Go/edit?usp=sharing(#)

### Team:
### PY pandas

***

## Project Description
The object of the project is to utilize the pygame library along with other built-in libraries to develop a 2D shooter game. In the game the user will be able to control a spaceship on a sci-fi themed game screen, shoot enemies or avoid the comets. The game time and the number of hits will be recorded as scores. If the spaceship get hit by an enemy or comet, the game will end. When the game ends, a game over screen will appear and inform the user with the scores, then return to the main menu.

***    

## User Interface Design
* Our basic concept of the GUI will include the following parts:
  * Title screen / start button
  * game interface
  * game over screen / scores / exit button

***        

## Program Design
### Class and File Relations(Flowchart)
![image](https://github.com/binghamtonuniversity-cs110/final-project-spr18-py-pandas/raw/master/assets/flowchart.png)

### List of classes

* **Player** - A class that defines the player - it is the active object the user can control to move in four directions to aviod obstacles and shoot enermies. It contains the image, the location of the plane and its speed, along with methods including update() to move the plane in the screen. The game is over when the plane collides with obstacles.


* **Enemies** - A class that defines the enermies that emerge on the other side of the screen and can be shoot by the plane. It contains the image and its location and speed, along with methods including update() to move forward. 


* **Bullets** - A class that defines the bullets shoot by the plane. It contains the image, its location and speed, along with the method update() to move forward. 


* **Rocks** - A class that defines the rocks coming from the other side of the screen. Rocks can not be shoot and the player has to avoid running into them. It consists of the image, the location, speed and update() method.

* **ScoreData** - A class that defines the best score record. It contains the file used to store score data, the best score read from the file and update() method to update the best record in the file .

* **GameMenu** - A class that defines the title screen, where users can interact with start button, help button and quit button. It is able to track the mouse and keyboard movement and inputs. Start button initializes the game and quit button will terminate the game process.

* **HelpMenu** - A class that defines the help menu, by clicking on the help button, a page introducing the game and controls will show up for the user's reference.


* **MenuItems** - A class that defines the items appear in th etitle screen. It cantains background color, font and color of the buttons.

***

## Tasks and Responsibilities

### Software Lead - Runzhuo Chi

Worked as integration specialist by helping organize the code for the main game into the proper format, which allowed all portions of the code to be run from a single file. Work very closely with the back end to develop the classes functionality, as well as establish the win- and fail-states for the main game. She also lead the implementation of the ‘sprite’ and ‘group’ classes of pygame into the back end code.

### Front End Specialist - Jinhua Xie

Front-end lead conducted significant research on using pygame to create visual aspects such as buttons and on-screen text. She used this information to design and program a consistent UI to help the player navigate the title screen, the instructions page, and the “GAME OVER” screen. In addition to implementing the wide majority of the visual element for the UI, she also collaborated with the Software Lead to create a jukebox function that played music and to add sound effects to the menu navigation buttons.

### Back End Specialist - Yuxin Lin

The back end specialist helped with the “Model” portion of BLOCKBUSTERS by writing the major classes that would be used in the main game, as well as implementing major pygame functionality into each of them. He also made headway in major game mechanics such as the basic paddle movement and advanced functionality such as the screen-wrap function for the paddle as it approached the ends of the screen. He collaborated with the Front End Specialist in the implementation of the classes into our Controller file, as well as develop our high-score database.

## Testing
* In general, our testing strategy is very practical. First we tested the functionality of the models, made sure they can be correctly initialized and variables will be passed down to the controller. With all models checked, we run the main file to see the game's performance. 

### Menu Testing

TBD

### Game Testing
TBD
