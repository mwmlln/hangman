
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

The main objective for creating this site was to gain skill set to build a simple but fun terminal based game


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

Initial design flowchart



##  Features 
---



###  How to Play page 



###  Game process 

* 

#### Features Left to Implement



##  Technologies 
--- 

###  Languages 

 * Python3

###  Other Technologies, Frameworks & Libraries 

 
 
##  Testing 
Testing was carried out by creating each function at a time to minimise the small errors impacting the whole project.

### Here are some of the challenges I encountered and steps taken to fix.

1. Validating user input for category choises.
  try/except method is used to validate the user input for category choise however, it was throwing system error instead of preset printing messagge 


###  Validating code 

PEP8

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
--- 

####  Coding 



###  Media 


