﻿* Cover Page
    * A cover page containing your group member names, project title, course number, and semester
    * Github URL
    * Project Demo Presentation as Google Slide URL
Example:
# Pygame shooter game
## CS 110 Final Project
### Fall,2018

[https://github.com/binghamtonuniversity-cs110/final-project-spr18-py-pandas.git](#)

[link to demo presentation slides TBD](#)

### Team:
#### PY pandas

***

## Project Description
The object of the project is to utilize the pygame library along with other built-in libraries to develop a 2D shooter game. In the game the user will be able to control a flying object on the window, shoot or avoid the incoming projectiles. The flying distance and the number of hit will be recorded as scores. If the flying object get hit by projectile, the game will end.

***    

## User Interface Design
* Our basic concept of the GUI will include the following parts:
  * Title screen / start button
  * game interface
  * game over screen / scores / exit button

***        

## Program Design
* TBD

***

## Tasks and Responsibilities
* You must outline the team member roles and who was responsible for each class/method, both individual and collaborative.
    * Example:
### Software Lead - Runzhuo Chi

Worked as integration specialist by helping organize the code for the main game into the proper MVC format, which allowed all portions of the code to be run from a single file. He worked very closely with the back end to develop the high-score database functionality, as well as establish the win- and fail-states for the main game. He also lead the implementation of the ‘sprite’ and ‘group’ classes of pygame into the back end code.

### Front End Specialist - [name]

Front-end lead conducted significant research on using pygame to create visual aspects such as buttons and on-screen text. She used this information to design and program a consistent UI to help the player navigate the title screen, the instructions page, and the “GAME OVER” screen. In addition to implementing the wide majority of the visual element for the UI, she also collaborated with the Software Lead to create a jukebox function that played music and to add sound effects to the menu navigation buttons.

### Back End Specialist - [name]

The back end specialist helped with the “Model” portion of BLOCKBUSTERS by writing the major classes that would be used in the main game, as well as implementing major pygame functionality into each of them. He also made headway in major game mechanics such as the basic paddle movement and advanced functionality such as the screen-wrap function for the paddle as it approached the ends of the screen. He collaborated with the Front End Specialist in the implementation of the classes into our Controller file, as well as develop our high-score database.

## Testing
* TBD

### Menu Testing

First, we run Controller()  and ensure the main menu opens normally, the musical score begins playing and that hovering the mouse over each button changes the color to the “highlighted” shade. Next, we click the Instructions button to ensure the INSTRUCTIONS menu opens, and the buttons are highlighted when hovered over as well. We also check to see if the music playback continues and that the sound effect is played when the button is pressed.

We then press the MAIN MENU button and return, checking that the same functionality with button hover, music and sound effects as before are present. Afterwards, we test that both of the QUIT buttons on the Main Menu and Instructions Menu properly close the game.We then test the PLAY buttons on the Instructions and Main Menu pages to make sure that the Game screen opens properly both times. We then move


### Game Testing

When the Game screen boots up , we test if spacebar starts the game and launches the ball, so we test to see if this remains true. From there, in the middle of play, we will test the single-press and holding of both the left and right arrow buttons to make sure movement works in single presses and continues to move when a key is held. We then move all the way to the left and right of the screen to see if it causes the paddle to appear on the other side - our wrap-around function.

From here, we conduct normal playtesting to ensure that the collisions, the speed of the ball, and the dynamic bounding and angles are all working together meaningfully and without any obvious error, especially in regards to the ball reflecting off of the corners and edges of the paddle. We also check to make sure the music plays throughout and that the destruction of a brick does in fact increase the score.

We then try to reach a win state, to check if it resets the game with an increase in ball speed, without resetting the score. If successful, we then purposefully reach three consecutive fail-states, one to test each of the GAME OVER screens’ three buttons - Play Again, Main Menu, and Quit - with the same functionality as before. Finally, we check that the “X” button on the window does in fact close the window. This concludes the testing protocol.

* A copy of your ATP

| Step                  | Procedure     | Expected Results  | Actual Results |
| ----------------------|:-------------:| -----------------:| -------------- |
|  1  | Run Counter Program  | GUI window appears with count = 0  |          |
|  2  | click count button  | display changes to count = 1 |                 |
etc...
