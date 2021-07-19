
# Hangman


This site is created as a Milestone project for Code Institute's Software Development course.

Here is a link to the live project: [Hangman](https://https://pp3-hangman.herokuapp.com/)


## The purpose for this site 
---
Hangman is a classic terminal based game that a lot of poeple are familiar with.
This game has same familiar structure and have three word categories that users can choose from upon starting the game.




Contents:


## User experience

### Target Audience

This game is created for anyone who wants to have fun playing a word game.


###  Strategy 
---

####  User goals 


####  Site owner’s goal 

The main objective for creating this site was to gain skill set to build a simple but fun terminal based game. 
Hangman game is widely available on the web so I have created extra user intractivity with user by giving them a choice of category. This narrows down possibility of the answer word hence the difficulty lavel goes down while by choosing all category gives more wide possibility of answer to make it harder to get a right answer.

###  User Stories 

This site is created following user’s expectations in mind.

* A first time user would like to:
    * Have a clear instruction on what the game objective and process
    * 


* A returning user would like to have the following additional 
   * Quick response time

* As a site creator I would like to provide:
  * Interactive game 
  * Clear feedback to user's response


###  Scope 


###  Structure 



###  Skeleton 

Initial design flowchart (ss_images/hangman_flowchart_ss.jpg)



##  Features 
---




###  Game process 

* 

#### Features Left to Implement

I am fully aware that the code wtitten in the program is not the most efficient way. The decision was made to focus on creating workaround solutions to build a fully functioning program with the code that I learned during the rather short space of time given for the course module completion and the project submission deadline.
When I gain more time and knowledge of the Python languege, I intend to come back to this program and try improving program efficiently and intractivity. 


##  Technologies 

###  Languages 

 * Python3

###  Other Technologies, Frameworks & Libraries 
random and time libraries are used in the code.
* Random is used to display a random choice from the list
* Time is used to control the dispay speed to prevent the text displaying too fast.
* Code Institute's full template for Python is used in oder for the program to dispay properly in deployed site on Heroku.

 
 
##  Testing 
Testing was carried out by creating each function at a time to minimise the small errors impacting the whole project.
* [Python Tutor](http://pythontutor.com/visualize.html#mode=edit) was used throughout the projet's building/testing stage to troubleshoot on errors.

*


### Here are some of the challenges I encountered and steps taken to fix.

1. Validating user input for category choises.
  try/except method is used to validate the user input for category choise however, it was throwing system error instead of preset printing messagge 
  This was fixed by changing the condition for the while loop.


2. Game completion with the answer that includes space between the words
  As function compares answer and correct user input list as set, empty space included in the answer was preventing the both list to match after all the letters were filled. 
  This issue was resolved by simply creating a new variabe with removed space and this new variable is used to be reffered instead.

3. category_choise function was repeating despite the user input being the right condition. 
I was spending quite some time changing the approach within the while loop in the function without any success.
 Thanks to Johann in Code Institure's tutor support who has pointed out the function being called in main function and then again when the return value is set to a variable. The solution was very simple just to remove it from main function.


###  Validating code 

The code is validted in PEP8 onine validator.

##  Deployment 
### Here is the procedre taken to deploy the project on Heroku

Prior to deply, two steps below are taken to prepare the project being deployed.
1. Ensure all input method texts ends with \n for the progam to display properly on Heroku site
2. All requirements are mentioned in requirements.txt file. This was done by typing following command in GitHub workspace terminal.
  pip3 freeze > requirements.txt
3. Sign up and log in to Heroku[heroku.com]
4. Click on Create new app button. 
5. In the next page displayed, enter the project name, pp3-hangman and select Europe as region, then click Create app button.
6. Open settings page by pressing settings tab. Following has to be done in exact order.
   In the Buildpack section of the setting page, press Add Buildpack button and choose python then, click save changes.
   Select Add Buildpack button again and choose nodejs then save changes
7. Navigate to deploy page by clicking the tab
   Choose GitHub then click Connect to GitHub button.
   In the popup window, click authorize and then input passowrd for GitHub
   Once my Git Hub repositries are connected, type in the name in the search for the project, hangman.
   When the repository is found, clikc connect button for the repository.
   GitHub button indicates connected when connection was successful.
8. As I wanted to have control when to deploy the version, I have chosen manual deployment by pressing Depoly branch button instead of Enable Automatic Deploys. 
9. once the deployment completed View button will appear. This View button will open the terminal game in the new window.

##  Credits 

####  Coding 

* https://enhancer298.net/2020/07/10/hangman1/    This site's tutorial of making Hangman game was used as a general guidance and their approach is used as a stepping stone for initial stage of this project. Also the image of the hangman stage is used from this site.

* https://www.python-izm.com/   Used for ganetal reference for python code

* [Python Tutor](http://pythontutor.com/visualize.html#mode=edit) This site was used to pinpoint where and why the errors are causing.



###  Media 

* https://diagrams.net/       This site was used to create the flowchart in the planning stage of the projet. 
* http://patorjk.com/software/taag/   Title ascii art was created in this site




