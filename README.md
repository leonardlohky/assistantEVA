# assistantEVA
EVA (Electronic Voice Assistant) is a voice-powered virtual assistant for your PC. The purpose is to handle tasks on behalf of users through voice commands, allowing them to concentrate on more demanding tasks at hand.

# Configuring EVA
Before you start using EVA, it is important to configure her according to your own personal settings. To do this, open the configuration INI file, which can be found in the folder at `assistantEVA\assistantEVA\config\config.ini`

In the INI file, you will find the following setting variables which can be tuned:
    [DEFAULT]
    ASSISTANT_NAME = Eva
    USER_NAME = YOUR_NAME
    HOME_LOCATION = YOUR_HOME_LOCATION
    GOOGLE_API_KEY = YOUR_GOOGLE_API_KEY
    MUSIC_DIR = YOUR_MUSIC_DIR_PATH
    EMAIL_SENDER = YOUR_EMAIL
    EMAIL_PWD = YOUR_EMAIL_PWD

Once you have changed the variables accordingly, save the file.

# Running EVA
## By executable
EVA has been packaged into a Python exe application, which can be found in `assistantEVA\assistantEVA\dist\assistantEVA.exe`. Simply double click on the exe file to run EVA. 

**Note: The exe file is currently not available through my Github since it exceeds the maximum 100MB size. Will have to create a ZIP file to be downloaded through external means (Probably Google Drive...)**

## By script
If you have a Python IDE, EVA and be ran as a script which is found at `assistantEVA\assistantEVA\assistantEVA.py`

# Functions that EVA can perform
EVA is able to perform a variety of functions, which are executed based on key words detected in your speech. The functions that EVA can perform and the key words which are used to trigger them accordingly are as follows:

##1: Send emails
**Key word to execute: "send email" or "send email to XXX"**
Ensure that you have set your email and password beforehand in the INI file. EVA stores all your contact names and emails in a CSV file, which is located in `assistantEVA\assistantEVA\resources\Email_contact.csv`. 

To add new contacts, open the file using Excel (or any other suitable programs) and add their names and email addresses.

To have EVA send an email, say "send email" or "send email to XXX". If no name is specified, EVA will automatically prompt for one. If a matching name is found, tell EVA the subject and content of the email that you want to send. A preview of the email will be displayed on the console. After that, tell EVA whether or not to send the email by saying "Yes/Send" or "No"

## 2: Get weather information
**Key word to execute:  "current weather in XXX"**
EVA can tell you the weather information for a specified city. To do this, say to EVA "current weather in XXX". E.g.
  **You:** current weather in singapore
** Eva: **The current weather in singapore is rain. The maximum temperature is 28.00
and the minimum temperature is 26.00 degree celcius

## 3: Get current time for location
**Key word to execute:  "current time in XXX"**

Example:
  **You:** current time in London
** Eva: **Current time in London is 15 hours 45 minutes

## 4a: Play song from your music folder
**Key word to execute:  "play song" or "play song XXX"**

Ensure that you have set the path to where your music files are stored in the INI configuration file beforehand. Also, VLC is required to be installed on your PC as EVA uses VLC to play songs. To get EVA to play a song, say to EVA "play song" or "play song XXX", where XXX is the title of the song.

### 4b: Pause/stop/resume song
**Key word to execute: "Pause song", "stop song" or "resume song"**

## 5: Get News for today
**Key word to execute: "news for today"**
EVA will search

## 6: Scrolling up and down
**Key word to execute: "go up" or "go down"**
EVA will search

## 7: Google Chrome Web Browsing

### 7a: Google search
**Key word to execute: "google search" or "google search for"**
EVA will execute a google search for the subject XXX as specified

### 7b: Google Maps navigation
**Key word to execute: "google maps"**
EVA will prompt you for the destination and origin. After that, a Google Maps webpage will open up showing you the possible routes that can be taken

### 7c: YouTube search
**Key word to execute:"youtube search" or "youtube search for XXX"**
EVA will search YouTube for the subject XXX as specified

### 7d: Click on XXX
**Key word to execute:"click on XXX"**
EVA will scour the webpage for a clickable element that has "XXX" in its text string. If found, it will automatically click on it for the user.

### 7e: Open new tab/close tab
**Key word to execute: "new tab" or "close tab"**
EVA will automatically create new tabs or close the current tab that the user is on based on the command given.

### 7f: Navigate through tabs
**Key word to execute: "go to XXX tab"**
EVA is able to navigate through tabs (max up to 10) to the desired tab. For example, saying "go to fourth tab" will make EVA bring the fourth tab into focus

### 7g: Bookmark page/open bookmarked page
**Key word to execute: "bookmark page" or "open bookmark"**
By saying "bookmark page", EVA will store the URL of the webpage to be bookmarked in a txt file found in `assistantEVA\assistantEVA\resources\bookmark.txt`. 

Say "open bookmark" to make EVA open the last bookmarked page.

### 7h: Go forward/Go back/Refresh page
**Key word to execute: "go forward", "go back" or "refresh page"**

## 8: Pause/Resume Video
**Key word to execute: "pause video" or "resume/play video"**
EVA is able to automatically pause and resume any video that is being played

## 9: Sleep Mode
**Key word to execute: "sleep mode"**
EVA features a "sleep mode", where it will ignore all other speech input by the user. This is to allow users to have a conversation with others without accidentally triggering any of EVA's functions.

To wake EVA from "sleep mode", simply say "EVA"

## 10: Shut down
**Key word to execute: "shut down"**
To close down EVA, say "shut down"
