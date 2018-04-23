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

In this part of the test, the three functions of the main game menu will be tested: Start, Help and Quit. First, we run the main program to open the menu window. We then hover the mouse over each button to test the mouse selection function, as expected, the button turns red and italic. Then we press direction keys to test the keyboard selection function, each button can be “highlighted” as expected. As is shown in this screenshot:

![image](https://github.com/binghamtonuniversity-cs110/final-project-spr18-py-pandas/raw/master/assets/Screenshots/menuscreen.png)

We then click on the Start button on the menu. The game starts normally, and the background music starts to play, the score indicators, spaceship (player character), enemies and comets appeared on the screen.

![image](https://github.com/binghamtonuniversity-cs110/final-project-spr18-py-pandas/raw/master/assets/Screenshots/gamescreen.png)

When the game is in progress, by clicking on the X on the upper right corner of the window, we can return to the menu. Next, we click on the Help button, the help page showed up as expected, it stays visible for 2 seconds for the player to read the instructions. Then the window automatically switches back to the menu screen.

![image](https://github.com/binghamtonuniversity-cs110/final-project-spr18-py-pandas/raw/master/assets/Screenshots/helpscreen.png)


### Game Testing

When the Controller() is called by selecting the Start button on the game menu, the game will launch normally. The game includes the following features: move the spaceship, shoot bullets, increase enemy’s speed, and game over. Test on the four features will be discussed in following paragraphs. 

First, we press each of the four direction keys once, the spaceship moves and stops as expected. We then press and hold the direction keys, the spaceship keeps moving until the key is released. When the spaceship is moved all the way to the edge of the game screen, it will not go beyond the edge or appear on the other side of the screen. 

As the movement of the spaceship is tested, we continue the game and test the shooting function. When blank space key is pressed, one bullet shows up and moves forward along the x-axis from the spaceship. We then press the blank space key multiple times, every time it is pressed, one bullet is launched. After that, we tested the bullet’s functions. We shoot bullets towards enemies. When a bullet hits an enemy, the enemy will disappear, then the bullet keeps moving until it hit the right edge of the screen and disappear. The score indicator increase by 1 every time an enemy is destroyed. Then we shoot bullets towards comets, comets will not be destroyed upon the collision with a bullet. 

Then we try to reach 30 points in the game. After the player’s score reaches 30, the speed of enemies and comets will increase. The speed of enemies and comet will increase further when the player’s score reaches 50 and 75.

Finally, we test the Game Over functions. The game has no win state. Once the spaceship collides with a comet or an enemy, the game is over. We move the spaceship towards a comet and touches it, the Game Over screen shows up along with the player’s score and the player’s best score in this game. The Game Over screen will stay for 2 seconds. Then the program is re-initialized, the player is sent back to the menu screen. 

## Acceptance Test Procedure

![image](https://github.com/binghamtonuniversity-cs110/final-project-spr18-py-pandas/raw/master/assets/Screenshots/ATP_page1.png)
![image](https://github.com/binghamtonuniversity-cs110/final-project-spr18-py-pandas/raw/master/assets/Screenshots/ATP_page2.png)
![image](https://github.com/binghamtonuniversity-cs110/final-project-spr18-py-pandas/raw/master/assets/Screenshots/ATP_page3.png)
