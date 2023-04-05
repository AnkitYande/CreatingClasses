# Creating Classes

## Select one of the following projects to code:

## Option 1:  Falling Boxes
![Falling Objects Example](assets/FallingObjects.mp4)
### Objective of Falling Boxes:
The player, positioned at the bottom of the screen, must maneuver left and right to avoid objects falling from the top of the screen. The game ends upon collision of a falling object with the player.

### Required Elements:
- ***Falling_Object Class***:
	- **constructor**
	 	- Use the ***random*** module to generate a random x and y coordinate for each Falling_Object object at the start of the program. The Falling_Object should be positioned above the playing area and hidden.
   		- The constructor should assign a shape, speed and color to the object
	- **move()**
		- This method moves a block down by some amount every time the method is called on a block object.
  		- The Falling_Object should only be visible when it is within the playing area.
		- In the move() method of the Falling_Object class, check if the y coordinate is below -250. If it is, generate new random x and y coordinates and continue the falling movement.


- ***Player Class***.
	- **constructor**
		- The Player object should be position near the bottom of the playing area.
    	- The constructor should assign color, speed and shape
	- **move_left()**
		- moves the Player left as along as it remains in the playing area.
	- **move_right()**
		- Moves the Player right as long as it remains in the playing area.
	- **delete()**
    	- The Player object is hidden if it collides with a Falling_Object object.


- ***A List Of At Least 10 Falling Objects***

- ***Collision Detection***

  
### Falling Boxes Demo

### Rubric - FallingBox Class
|Description|Points|
|---|---|
|**Falling Objects** 
|Falling objects instantiate at random coordinates above the playing area.|1|
|Falling objects continuously fall from the "sky".|2|
|Falling objects are only visible while they are within the designated playing area.|1|
|**Player Class**||
|The player can move right and left within the playing area. It cannot leave the playing area.|2|
|The player earns a point for every falling object that it avoids.|1|
|The player dies if it collides with a box.|1|
|**Score**||
|The score will be displayed throughout the game|2|
|**Extra Credit** - Limited to 2 extra points||
|The FallingBlock objects to increase their speed every five seconds |1|
|Allow players to shoot straight up to destroy boxes|2|


## Option 2: Shooting Gallery
![example](assets/ShootingGallery.mp4)
### Objective of Shooting Gallery:
The player must shoot out the blocks positioned in rows at the top of the playing area.

The player, located at the bottom of the screen, must rotate left and right to aim its shots. The player can fire up to ten bullets at once. The blocks, located in rows at the top of the playing field, must be hit three times before they are destroyed and removed from the screen. The color of the blocks will change with each hit until they are destroyed.

### Required Elements:
- ***Block Class***
	- constructor
		- Attributes:
		    - list of colors: list contains the sequence of colors that the block switches to after each hit
	        - hits: starts at 0; used to keep track of the number of times the block is hit by a bullet
    - strike()
	    - increments the hit count
        - changes the block's color after each hit
        - calls on delete() when the hit count reaches 3 
    - delete()
	    - hides the block
        - removes the block from the list of blocks
- ***Player Class***
	- constructor
	  - list of bullets
	  - key binding to turn player object and fire bullets
  	- turn_left()
	  	- rotates the player left unless its heading is greater than 150
  	- turn_right()
	  	- rotates the player right unless its heading is less than 30.
  	- fire()
- ***Bullet Class***
	- constructor
	  - positions the new bullet object directly in front of the player when it is instantiated.
	  - sets the heading to the player's heading
	- move()
	  - moves the bullet forward with the intial heading of the player which fired it.
	  - bullet should reflect of the sides of the playing area
	  - bullet will delete itself if it travels above upper limit of the playing area.
	- delete()
    	- hides the bullet and removes it from the player's bullets list
- ***List of Blocks***


### Rubric - FallingBox Class
|Description|Points|
|---|---|
|**Blocks**||
|The playing area will feature at least three rows of blocks, with each row containing at least 10 blocks.|2|
|Blocks will disappear after being struck|2|
|**Player/Players**||
|The user will be able to rotate the player left and right using key bindings.|1|
|The player's rotation range should be limited to 120 degrees.|1|
|The player can fire(instantiate) bullets.|2|
|**Bullets**||
|Bullets will appear directly in front of the player that fired them.|1|
|Bullets will have the same initial heading and color as the player that fired them.|1|
|Bullets will travel in straight lines. |1|
|Bullets will disappear upon collision with a block or when they travel beyond the top of the playing area.|1|
|**Score**||
|A player will earn a point for every block that they eliminate from the playing area|1|
|Each player's score will be displayed on the screen|1|
|**Extra Credit** - Limited to 2 extra points||
|In case of a collision with the side of the playing area, they will reflect off the sides.|1|
|Blocks disappear after being struck 3 times instead of once.|1|
|Blocks change color after the first two bullet strikes.|1|
|Limit the Player to 3 bullets on the screen at a time.|2|
