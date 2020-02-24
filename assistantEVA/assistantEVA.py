# -*- coding: utf-8 -*-

# https://towardsdatascience.com/build-your-first-voice-assistant-85a5a49f6cc1

from webBrowserSession import webBrowserSession
from string import Template
from pynput.keyboard import KeyCode, Controller, Key
import configparser
import consoleEVA
import pyttsx3
import speech_recognition as sr
import os
import sys
import re
import csv, smtplib, ssl
import requests
import subprocess
from pyowm import OWM
import urllib
from urllib.request import urlopen
import vlc
import json
from bs4 import BeautifulSoup as soup
import geocoder
import pytz
from datetime import datetime
from time import strftime

def read_template(filename):
    """
    Returns a Template object comprising the contents of the 
    file specified by filename.
    """
    
    with open(filename, 'r', encoding='utf-8') as template_file:
        template_file_content = template_file.read()
    return Template(template_file_content)

def sleepMode(audio):
    print('In sleep mode...')
    if 'eva' in audio:
        global sleep_mode
        sleep_mode = False
        assistantResponse('I am awake. What can I help you with?')
    
# Method to interpret voice commands
def myCommand():
    r = sr.Recognizer()
    r.pause_threshold = 0.8
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source, duration = 1)
        r.dynamic_energy_threshold = True  
        audio = r.listen(source)
        
    try:
        command = r.recognize_google(audio).lower().replace('-', ' ')
        # print(default['USER_NAME'] + ': ' + command + '\n')
        console.console_output(default['USER_NAME'] + ': ' + command)
           
    # Loop back to continue listening for voice commands if received speech
    # is unrecognizable   
    except sr.UnknownValueError:
        # print('......')
        console.console_output('......')
        command = myCommand()
        
    return command
        
# Method to convert text to speech
def assistantResponse(audio):
    global music_player
    music_player.pause() # pause any current music so user can hear Eva's response
    console.console_output(default['ASSISTANT_NAME'] + ': ' + audio)
    # print (default['ASSISTANT_NAME'] + ': ' + audio)
    speaker.say(audio)
    speaker.runAndWait()
    music_player.play() # resume current music
        
def assistant(command):
    # Declaring global variables
    global resource_path
    global browser
    global music_player
    
    # ------------------------------------------------------------------
    # Function 1: Send email
    # Contacts and email addresses are stored in "Email_contact.csv" file
    # ------------------------------------------------------------------
    if 'send email' in command:               
        reg_ex = re.search('send email to (.*)', command)
  
        if reg_ex:
            recipient = reg_ex.group(1)
            context = ssl.create_default_context()
            with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
                server.login(default['EMAIL_SENDER'], default['EMAIL_PWD'])
                with open(os.path.join(resource_path, 'Email_contact.csv')) as file:
                    reader = csv.reader(file)
                    next(reader)  # Skip header row
                    for name, email, grade in reader:
                        name.lower()
                        if recipient in name:
                            assistantResponse('What is the subject of the email?')
                            SUBJECT = myCommand()
                            assistantResponse('Ok. What message do you want to send to %s?' % name)
                            message_body = myCommand()
                            message_template = read_template(os.path.join(resource_path, 'message_format.txt'))
                            TEXT = message_template.substitute(RECIPIENT=name, EMAIL_BODY=message_body)
                            message = 'Subject: {}\n\n{}'.format(SUBJECT, TEXT)
                            assistantResponse('Ok. The following email will be sent to %s.' % name)
                            
                            console.console_output('\n' + message + '\n')
                            assistantResponse('Do you want to send the email?')
                            
                            while (1):
                                user_response = myCommand()
                            
                                if user_response == 'yes' or user_response == 'send':
                                    server.sendmail(default['EMAIL_SENDER'], email, message)
                                    assistantResponse('Email has been sent to ' + recipient) 
                                    server.quit()
                                    break
                                
                                elif user_response == 'no':
                                    assistantResponse('Deleting draft email') 
                                    server.quit()
                                    break  
        
        else:
            assistantResponse('Who do you want to send the email to?')
            recipient = myCommand()
            
            context = ssl.create_default_context()
            with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
                server.login(default['EMAIL_SENDER'], default['EMAIL_PWD'])
                with open(os.path.join(resource_path, 'Email_contact.csv')) as file:
                    reader = csv.reader(file)
                    next(reader)  # Skip header row
                    for name, email, grade in reader:
                        name.lower()
                        if recipient in name:
                            assistantResponse('What is the subject of the email?')
                            SUBJECT = myCommand()
                            assistantResponse('Ok. What message do you want to send to %s?' % name)
                            message_body = myCommand()
                            message_template = read_template(os.path.join(resource_path, 'message_format.txt'))
                            TEXT = message_template.substitute(RECIPIENT=name, EMAIL_BODY=message_body)
                            message = 'Subject: {}\n\n{}'.format(SUBJECT, TEXT)
                            assistantResponse('Ok. The following email will be sent to %s.' % name)
                            
                            console.console_output('\n' + message + '\n')
                            assistantResponse('Do you want to send the email?')
                            
                            while (1):
                                user_response = myCommand()
                            
                                if user_response == 'yes' or user_response == 'send':
                                    server.sendmail(default['EMAIL_SENDER'], email, message)
                                    assistantResponse('Email has been sent to ' + recipient) 
                                    server.quit()
                                    break
                                
                                elif user_response == 'no':
                                    assistantResponse('Deleting draft email') 
                                    server.quit()
                                    break   
                   
    # ------------------------------------------------------------------
    # Function 2: Obtain current weather information for specified location
    # ------------------------------------------------------------------
    elif 'current weather' in command:
        reg_ex = re.search('current weather in (.*)', command)
        if reg_ex:
            city = reg_ex.group(1)
            owm = OWM(API_key='ab0d5e80e8dafb2cb81fa9e82431c1fa')
            obs = owm.weather_at_place(city)
            w = obs.get_weather()
            k = w.get_status()
            x = w.get_temperature(unit='celsius')
            assistantResponse('Current weather in %s is %s. The maximum temperature is %0.2f and the minimum temperature is %0.2f degree celcius' % (city, k, x['temp_max'], x['temp_min']))
    
    # ------------------------------------------------------------------
    # Function 3: Get current time for specified location
    # ------------------------------------------------------------------
    elif 'current time' in command:
        reg_ex = re.search('current time in (.*)', command)
        city = reg_ex.group(1)
        for tz in pytz.all_timezones:
            tz_proc = tz.replace('_', ' ').replace('-', ' ').lower()
            if city in tz_proc:
                city_tz = tz
                location = pytz.timezone(city_tz)
                now = datetime.now(location)
                assistantResponse('Current time in %s is %d hours %d minutes' % (city, now.hour, now.minute))
                break
            
    # ------------------------------------------------------------------
    # Function 4: Greet or shut down assistant script
    # ------------------------------------------------------------------
    elif 'hello' in command:
        day_time = int(strftime('%H'))
        if day_time < 12:
            assistantResponse('Hello Sir. Good morning')
        elif 12 <= day_time < 18:
            assistantResponse('Hello Sir. Good afternoon')
        else:
            assistantResponse('Hello Sir. Good evening')
    # to terminate the program
    elif 'shut down' in command:
         assistantResponse('Shutting down. Have a nice day sir')
         browser.quitSession()
         music_player.stop()
         del music_player
         sys.exit()
         
    # ------------------------------------------------------------------
    # Function 5a: Play song in library on VLC
    # ------------------------------------------------------------------
    elif 'play song' in command:
        path = default['MUSIC_DIR']
        folder = path
        
        song_found = False
                
        reg_ex = re.search('play song (.*)', command)
        if reg_ex:
            song_name = reg_ex.group(1)
            for song_file in os.listdir(folder):
                song_file_proc = song_file.lower()
                if song_name in song_file_proc:
                    song_found = True
                    song_file_path = os.path.join(folder, song_file)
                    assistantResponse('Now playing ' + song_file[:song_file.rfind(".")])
                    
                    # Stops current music and deletes instance associated with that music
                    # to ensure that only one music track is played at all time
                    music_player.stop()
                    
                    music_player.set_mrl(song_file_path)
                    # music_player = vlc.MediaPlayer(song_file_path)
                    music_player.play()
                    break
            
            if song_found == False:
                assistantResponse('Sorry. I could not find the song title you are looking for')
        
        else:
           assistantResponse('What song do you want to play?')
           song_name = myCommand()
           for song_file in os.listdir(folder):
                song_file_proc = song_file.lower()
                if song_name in song_file_proc:
                    song_found = True
                    song_file_path = os.path.join(folder, song_file)
                    assistantResponse('Now playing ' + song_file[:song_file.rfind(".")])
                    
                    # Stops current music and deletes instance associated with that music
                    # to ensure that only one music track is played at all time
                    music_player.stop()
                    
                    music_player.set_mrl(song_file_path)
                    # music_player = vlc.MediaPlayer(song_file_path)
                    music_player.play()
                    break
                
           if song_found == False:
                assistantResponse('Sorry. I could not find the song title you are looking for')
    
    # ------------------------------------------------------------------
    # Function 5b: Pause, stop or resume song being played on VLC
    # ------------------------------------------------------------------
    elif 'pause song' in command:
        music_player.pause()
    elif 'stop song' in command:
        music_player.stop()
    elif 'resume song' in command:
        music_player.play()
        
    # ------------------------------------------------------------------
    # Function 6: Get news for today
    # ------------------------------------------------------------------
    elif 'news for today' in command:
        try:
            news_url="https://news.google.com/news/rss"
            Client=urlopen(news_url)
            xml_page=Client.read()
            Client.close()
            soup_page=soup(xml_page,"xml")
            news_list=soup_page.findAll("item")
            for news in news_list[:15]:
                assistantResponse(news.title.text.encode('utf-8'))
        except Exception as e:
                print(e)
                
    # ------------------------------------------------------------------
    # Function 7: Scrolling up or down
    # ------------------------------------------------------------------
    elif 'go up' in command:
        keyboard.press(Key.page_up)
        
    elif 'go down' in command:
        keyboard.press(Key.page_down)
        
    # ------------------------------------------------------------------
    # Function 8: WebBrowser functions according to webBrowserSession.py
    # ------------------------------------------------------------------
    elif 'google search' in command:       
        reg_ex = re.search('search for (.*)', command)
        
        if reg_ex:
            query = reg_ex.group(1)
            assistantResponse('Performing Google search for: ' + query)
            browser.googleSearch(query)
            
        else:
            assistantResponse('What topic do you want to search for?')
            query = myCommand() 
            assistantResponse('Performing Google search for: ' + query)
            
            browser.googleSearch(query)
        
    elif 'google maps' in command:
        assistantResponse('Where do you want to go?')
        destination = myCommand().replace(' ', '+')
        if destination == 'home':
            destination = default['HOME_LOCATION'].replace(' ', '+')
        
        assistantResponse('Where is the starting location?')
        origin_location = myCommand().replace(' ', '+')
        if origin_location == 'current location':
            g = geocoder.ip('me')
            origin_location = str(g.latlng[0]) + ',' + str(g.latlng[1])
        elif origin_location == 'home':
            origin_location = default['HOME_LOCATION'].replace(' ', '+')
                  
        browser.googleMapsNav(origin_location, destination)
        assistantResponse('Here are the possible routes I found')
        
    elif 'youtube search' in command:   
        reg_ex = re.search('search for (.*)', command)
        
        if reg_ex:
            query = reg_ex.group(1)
            assistantResponse('Searching YouTube for: ' + query)
        
            browser.youtubeSearch(query)
         
        else:
            assistantResponse('What YouTube video do you want to search for?')
            query = myCommand() 
            assistantResponse('Searching YouTube for: ' + query)
        
        browser.youtubeSearch(query)
        
    elif 'click on' in command:
        reg_ex = re.search('click on (.*)', command)
        if reg_ex:
            target = reg_ex.group(1)            
            browser.clickOn(target)
        
    elif 'new tab' in command:
        browser.makeNewTab()
        
    elif 'close tab' in command:
        browser.closeCurrentTab()
     
    elif 'next chapter' in command:
        browser.nextChapter()
        
    elif 'previous chapter' in command:
        browser.prevChapter()
        
    elif 'bookmark page' in command:
        browser.makeBookmark(resource_path)
        assistantResponse('Page bookmarked')
        
    elif 'open bookmark' in command:
        assistantResponse('Opening bookmark')
        browser.openBookmark(resource_path)
     
    elif 'go forward' in command:
        browser.goForward()
        
    elif 'go back' in command:
        browser.goBack()
        
    elif 'refresh page' in command:
        browser.refreshPage()
        
    elif 'go' in command and 'tab' in command:
        reg_ex = re.search('go to (.+?) tab', command)
        if reg_ex:
            tabNum = reg_ex.group(1)
            browser.switchTab(tabNum)
        else:
            pass
             
    # ------------------------------------------------------------------
    # Function 9: Pause/resume video
    # ------------------------------------------------------------------
    elif 'pause video' in command or 'play video' in command:
        keyboard.press(KeyCode.from_vk(0xB3))
      
    # ------------------------------------------------------------------
    # Function 10: Activate sleep mode
    # Assistant will ignore all other speech input except for 'hello eva'
    # which will deactivate sleep mode
    # ------------------------------------------------------------------
    elif 'sleep mode' in command:
        global sleep_mode
        sleep_mode = True
        assistantResponse('Going into sleep mode. Call me if you need something')
        
    else:
        assistantResponse('Sorry. I did not get that')
        

if __name__ == '__main__':
    
    # determine if application is a script file or frozen exe
    # and get path to 'config.ini' file and 'resources' folder
    if getattr(sys, 'frozen', False):
        application_path = os.path.dirname(sys.executable)
        config_path = os.path.join(application_path, '..\config\config.ini')
        resource_path = os.path.join(application_path, '..\\resources')
    elif __file__:
        application_path = os.path.dirname(__file__)
        config_path = os.path.join(application_path, 'config\config.ini')
        resource_path = os.path.join(application_path, 'resources')

    # Parse INI file settings
    config = configparser.ConfigParser()
    config.read(config_path)
    default = config['DEFAULT']
    
    speaker = pyttsx3.init("sapi5")
    voices = speaker.getProperty('voices')
    speaker.setProperty('voice', voices[1].id)
    keyboard = Controller()
    console = consoleEVA.consoleEVA()
    
    # os.environ["VLC_PLUGIN_PATH"] = "/usr/lib64/vlc/plugins"
    music_player = vlc.MediaPlayer() # Empty dummy vlc object
    browser = webBrowserSession.webBrowserSession() # Setting up webBrowser instance
    
    sleep_mode = False
    assistantResponse('Hello Sir. I am ' + default['ASSISTANT_NAME'] + ', your personal voice assistant. What can I help you with?')
    
    while True:
        if sleep_mode == True:
            sleepMode(myCommand())
        else:
            assistant(myCommand())
        
    
    
