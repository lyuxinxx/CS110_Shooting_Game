
# Space Shooter 2
## CS 110 Final Project
### Spring,2018

### Link to Github Repo:
[https://github.com/binghamtonuniversity-cs110/final-project-spr18-py-pandas.git](#)

### Link to Presentation Slides:
https://docs.google.com/presentation/d/1PspHvenVy_4sVxTc_uWgVJ-C84bJDG0MLpbYyIenlXc/edit#slide=id.p

### Team:

PY pandas

### Team Members:

Runzhuo Chi, Jinhua Xie, Yuxin Lin

***

## Project Description
The object of the project is to utilize the pygame library along with other built-in libraries to develop a 2D shooter game. In the game the user will be able to control a spaceship on a sci-fi themed game screen, shoot enemies or avoid the comets. The game time and the number of hits will be recorded as scores. If the spaceship get hit by an enemy or comet, the game will end. When the game ends, a game over screen will appear and inform the user with the scores, then return to the main menu.

### Game Background

Outer Space Octopuses are invading your planet for a rare metal darmstadtium. You, a well-trained spaceship captain, undertake the task of destroying the intruders and defending your planet. Now, it is time for you to show your power and fight for your homeland!

***    

## User Interface Design
* Our basic concept of the GUI will include the following parts:

### GUI Wireframe

![image](https://github.com/binghamtonuniversity-cs110/final-project-spr18-py-pandas/raw/master/assets/Screenshots/wireframe.PNG)

### 1. Main Menu/Start Screen

The game initiates with a welcome screen with “Space Shooter 2” and a Main Menu displayed. Three buttons, “Start”, “Help”, and “Quit”, are for game start, game instructions, and game exit, respectively. The player can move mouse or press “UP” or “DOWN” key to select. Once selected, the button will change from white to red color and become italic. Then, the player can click mouse or press “ENTER” or “SPACE” to enter. 
![image](https://github.com/binghamtonuniversity-cs110/final-project-spr18-py-pandas/raw/master/assets/Screenshots/menuscreen.png)

### 2. Instructions Screen

This screen tells the player how to play the game and the background is introduced. Also, the animations of spaceship, missile, Outer Space Octopuses, and comet are displayed with corresponding instructions. After 5 seconds, the screen will automatically return to Main Menu screen. 
![image](https://github.com/binghamtonuniversity-cs110/final-project-spr18-py-pandas/raw/master/assets/HelpMenu.png)

### 3. The Game Screen

This screen is where the actual game of “Space Shooter 2” takes place. The player can press “UP”, “DOWN”, “LEFT”, and “RIGHT” keys to move the spaceship. A press of “SPACE” bar launches a missile towards Outer Space Octopus. For each Octopus destroyed by missile, the player will get 2 points. For each second passed, the player will get 1 point. The total score is the sum of the two. The game is over when the spaceship is hit by an Octopus or a comet.
![image](https://github.com/binghamtonuniversity-cs110/final-project-spr18-py-pandas/raw/master/assets/Screenshots/gamescreen.png)

### 4. Game Over Screen

This screen displays “Game Over”, the highest score record, and the score the player just got. After 3 second, the screen will automatically return to Main Menu screen. 
![image](https://github.com/binghamtonuniversity-cs110/final-project-spr18-py-pandas/raw/master/assets/Screenshots/GameOver.png)


***        

## Program Design
### Class and File Relations(Flowchart)
![image](https://github.com/binghamtonuniversity-cs110/final-project-spr18-py-pandas/raw/master/assets/flowchart.png)

### List of classes

* **Player [Yuxin]** - A class that defines the player - it is the active object the user can control to move in four directions to aviod obstacles and shoot enermies. It contains the image, the location of the plane and its speed, along with methods including update() to move the plane in the screen. The game is over when the plane collides with obstacles.


* **Enemies [Yuxin]** - A class that defines the enermies that emerge on the other side of the screen and can be shoot by the plane. It contains the image and its location and speed, along with methods including update() to move forward. 


* **Bullets [Yuxin]** - A class that defines the bullets shoot by the plane. It contains the image, its location and speed, along with the method update() to move forward. 


* **Rocks [Yuxin]** - A class that defines the rocks coming from the other side of the screen. Rocks can not be shoot and the player has to avoid running into them. It consists of the image, the location, speed and update() method.

* **ScoreData [Yuxin]** - A class that defines the best score record. It contains the file used to store score data, the best score read from the file and update() method to update the best record in the file .

* **GameMenu [Jinhua, Runzhuo]** - A class that defines the title screen, where users can interact with start button, help button and quit button. It is able to track the mouse and keyboard movement and inputs. Start button initializes the game and quit button will terminate the game process.

* **HelpMenu [Jinhua, Runzhuo]** - A class that defines the help menu, by clicking on the help button, a page introducing the game and controls will show up for the user's reference.


* **MenuItems [Jinhua, Runzhuo]** - A class that defines the items appear in th etitle screen. It cantains background color, font and color of the buttons.

### Non-Standard Libraries and Modules Used

* Pygame (https://www.pygame.org/) - A module set incorporating many common game development functions into python, developed by Pete Shinners and Pygame Community. Includes crucial graphical elements as well as a musical playback functionality.

***

## Tasks and Responsibilities

### Software Lead - Runzhuo Chi

Worked as an integration specialist by helping organize the code for the main game into the proper format, which allowed all portions of the code to be run from a single file. Worked very closely with the back-end to develop and test the classes functionality, as well as establish the different states for the main game. She also worked with the front-end specialist to implement the menu classes for the user interface.

### Front End Specialist - Jinhua Xie

The front-end specialist conducted significant research on using pygame to create visual aspects such as buttons, on-screen texts, game backgrounds and “GAME OVER” screen. She used various resources to design and program a consistent graphical UI to help the player navigate the game menu screen, the instructions screen, and the “GAME OVER” screen.

### Back End Specialist - Yuxin Lin

The back-end specialist was in charge of developing the “Model” portion of the game. He wrote the major classes that would be used in the main game, as well as implemented major pygame functionality into each of them. He also developed the major game mechanics such as the spaceship movements and advanced features including shooting, enemy generating and score recording. He also developed our highest-score database.

## Testing
* In general, our testing strategy is very practical. First we tested the functionality of the models using a test.py file, made sure they can be correctly initialized and variables will be passed down to the controller. With all models checked, we run the main.py file to see the game's performance. 

### Menu Testing

In this part of the test, the three functions of the main game menu will be tested: Start, Help and Quit. First, we run the main program to open the menu window. We then hover the mouse over each button to test the mouse selection function, as expected, the button turns red and italic. Then we press direction keys to test the keyboard selection function, each button can be “highlighted” as expected. As is shown in this screenshot:

![image](https://github.com/binghamtonuniversity-cs110/final-project-spr18-py-pandas/raw/master/assets/Screenshots/menuscreen.png)

We then click on the Start button on the menu. The game starts normally, and the background music starts to play, the score indicators, spaceship (player character), enemies and comets appeared on the screen.

![image](https://github.com/binghamtonuniversity-cs110/final-project-spr18-py-pandas/raw/master/assets/Screenshots/gamescreen.png)

When the game is in progress, by clicking on the X on the upper right corner of the window, we can return to the menu. Next, we click on the Help button, the help page showed up as expected, it stays visible for 5 seconds for the player to read the instructions. Then the window automatically switches back to the menu screen.

![image](https://github.com/binghamtonuniversity-cs110/final-project-spr18-py-pandas/raw/master/assets/HelpMenu.png)


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
