#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v3.2.4),
    on Wed Feb 19 10:40:38 2020
If you publish work using this script the most relevant publication is:

    Peirce J, Gray JR, Simpson S, MacAskill M, Höchenberger R, Sogo H, Kastman E, Lindeløv JK. (2019) 
        PsychoPy2: Experiments in behavior made easy Behav Res 51: 195. 
        https://doi.org/10.3758/s13428-018-01193-y

"""

from __future__ import absolute_import, division

from psychopy import locale_setup
from psychopy import prefs
from psychopy import sound, gui, visual, core, data, event, logging, clock
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER)

import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle
import os  # handy system and path functions
import sys  # to get file system encoding

from psychopy.hardware import keyboard

# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(_thisDir)

# Store info about the experiment session
psychopyVersion = '3.2.4'
expName = 'Test'  # from the Builder filename that created this script
expInfo = {'participant': '', 'session': '001', 'age': '', 'gender (0=male, 1 = female, 2 = other)': ''}
dlg = gui.DlgFromDict(dictionary=expInfo, sortKeys=False, title=expName)
if dlg.OK == False:
    core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName
expInfo['psychopyVersion'] = psychopyVersion

# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
filename = _thisDir + os.sep + u'data/%s_%s_%s' % (expInfo['participant'], expName, expInfo['date'])

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath='/Users/farerilab/Documents/GitHub/GamblingAdviceTask/GamblingAdviceTask1Final_lastrun.py',
    savePickle=True, saveWideText=True,
    dataFileName=filename)
# save a log file for detail verbose info
logFile = logging.LogFile(filename+'.log', level=logging.EXP)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp
frameTolerance = 0.001  # how close to onset before 'same' frame

# Start Code - component code to be run before the window creation

# Setup the Window
win = visual.Window(
    size=[1440, 900], fullscr=True, screen=0, 
    winType='pyglet', allowGUI=False, allowStencil=False,
    monitor='testMonitor', color=[-1,-1,-1], colorSpace='rgb',
    blendMode='avg', useFBO=True, 
    units='height')
# store frame rate of monitor if we can measure it
expInfo['frameRate'] = win.getActualFrameRate()
if expInfo['frameRate'] != None:
    frameDur = 1.0 / round(expInfo['frameRate'])
else:
    frameDur = 1.0 / 60.0  # could not measure, so guess

# create a default keyboard (e.g. to check for escape)
defaultKeyboard = keyboard.Keyboard()

# Initialize components for Routine "welcome"
welcomeClock = core.Clock()
text = visual.TextStim(win=win, name='text',
    text='Welcome to the gambling advice task. Here you will make a series of choices between accepting a monetary gamble or accepting a guaranteed monetary outcome. \n\nOn each trial, you can choose whether you want to recieve advice from your chosen advisor.\n\nPress the spacebar to move on to the practice trials.',
    font='Arial',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
key_resp_4 = keyboard.Keyboard()

# Initialize components for Routine "inst"
instClock = core.Clock()
instructions = visual.TextStim(win=win, name='instructions',
    text='\nWelcome to the study! \n\nOn the following page you will be instructed to choose an advisor. \n\nPress the space bar when you are ready to proceed.',
    font='Arial',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
space = keyboard.Keyboard()

# Initialize components for Routine "preBlock"
preBlockClock = core.Clock()
chooseInst = visual.TextStim(win=win, name='chooseInst',
    text='default text',
    font='Arial',
    pos=[0,0], height=1.0, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
Ad1 = visual.TextStim(win=win, name='Ad1',
    text='default text',
    font='Arial',
    pos=[0,0], height=1.0, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
Ad2 = visual.TextStim(win=win, name='Ad2',
    text='default text',
    font='Arial',
    pos=[0,0], height=1.0, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);
key_resp_3 = keyboard.Keyboard()
Ad1pic = visual.ImageStim(
    win=win,
    name='Ad1pic', 
    image='sin', mask=None,
    ori=1.0, pos=[0,0], size=1.0,
    color=[1,1,1], colorSpace='rgb', opacity=1.0,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-4.0)
Ad2pic = visual.ImageStim(
    win=win,
    name='Ad2pic', 
    image='avatar_2.png', mask=None,
    ori=0, pos=(.4, -0.06), size=(0.3, 0.3),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-5.0)
enter = keyboard.Keyboard()
import numpy.random

from numpy.random import choice

import pandas as pd

import xlrd

book = xlrd.open_workbook('Book1.xlsx')
sheet = book.sheet_by_index(0)



# Initialize components for Routine "ISI"
ISIClock = core.Clock()
iSi = visual.TextStim(win=win, name='iSi',
    text='+',
    font='Arial',
    pos=(0, 0), height=0.08, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "Receive_money"
Receive_moneyClock = core.Clock()
receiveMoneyPicture = visual.ImageStim(
    win=win,
    name='receiveMoneyPicture', 
    image='sin', mask=None,
    ori=1.0, pos=[0,0], size=1.0,
    color=[1,1,1], colorSpace='rgb', opacity=1.0,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)
ISI2 = visual.TextStim(win=win, name='ISI2',
    text='default text',
    font='Arial',
    pos=[0,0], height=1.0, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);

# Initialize components for Routine "trial"
trialClock = core.Clock()
ChoicePic = visual.ImageStim(
    win=win,
    name='ChoicePic', 
    image='sin', mask=None,
    ori=1.0, pos=[0,0], size=1.0,
    color=[1,1,1], colorSpace='rgb', opacity=1.0,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)

# Initialize components for Routine "askAd"
askAdClock = core.Clock()
response = keyboard.Keyboard()
yesNo = visual.TextStim(win=win, name='yesNo',
    text='default text',
    font='Arial',
    pos=[0,0], height=1.0, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
ask = visual.TextStim(win=win, name='ask',
    text='default text',
    font='Arial',
    pos=[0,0], height=1.0, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);

# Initialize components for Routine "getAd"
getAdClock = core.Clock()
gamAdRisk=0


getAdv = visual.TextStim(win=win, name='getAdv',
    text='default text',
    font='Arial',
    pos=[0,0], height=1.0, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
textForCode = visual.TextStim(win=win, name='textForCode',
    text='default text',
    font='Arial',
    pos=[0,0], height=1.0, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);

# Initialize components for Routine "Choice2Gain"
Choice2GainClock = core.Clock()
blank = visual.TextStim(win=win, name='blank',
    text='default text',
    font='Arial',
    pos=[0,0], height=1.0, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
ChoicePic2 = visual.ImageStim(
    win=win,
    name='ChoicePic2', 
    image='sin', mask=None,
    ori=1.0, pos=[0,0], size=1.0,
    color=[1,1,1], colorSpace='rgb', opacity=1.0,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-1.0)
resp = keyboard.Keyboard()
checkL1 = visual.ImageStim(
    win=win,
    name='checkL1', 
    image='sin', mask=None,
    ori=1.0, pos=[0,0], size=1.0,
    color='white', colorSpace='rgb', opacity=1.0,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-3.0)
checkR1 = visual.ImageStim(
    win=win,
    name='checkR1', 
    image='sin', mask=None,
    ori=1.0, pos=[0,0], size=1.0,
    color='white', colorSpace='rgb', opacity=1.0,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-4.0)

from PIL import Image
from psychopy import visual, core
nGamble=0
adFollow=0



# Initialize components for Routine "endprac"
endpracClock = core.Clock()
EndPrac = visual.TextStim(win=win, name='EndPrac',
    text='You have reached the end of the practice round.  \n\nIf you have any questions, please let the experimenter know now.\n\nOtherwise, please press the spacebar to begin.',
    font='Arial',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
key_resp = keyboard.Keyboard()

# Initialize components for Routine "preBlock"
preBlockClock = core.Clock()
chooseInst = visual.TextStim(win=win, name='chooseInst',
    text='default text',
    font='Arial',
    pos=[0,0], height=1.0, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
Ad1 = visual.TextStim(win=win, name='Ad1',
    text='default text',
    font='Arial',
    pos=[0,0], height=1.0, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
Ad2 = visual.TextStim(win=win, name='Ad2',
    text='default text',
    font='Arial',
    pos=[0,0], height=1.0, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);
key_resp_3 = keyboard.Keyboard()
Ad1pic = visual.ImageStim(
    win=win,
    name='Ad1pic', 
    image='sin', mask=None,
    ori=1.0, pos=[0,0], size=1.0,
    color=[1,1,1], colorSpace='rgb', opacity=1.0,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-4.0)
Ad2pic = visual.ImageStim(
    win=win,
    name='Ad2pic', 
    image='avatar_2.png', mask=None,
    ori=0, pos=(.4, -0.06), size=(0.3, 0.3),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-5.0)
enter = keyboard.Keyboard()
import numpy.random

from numpy.random import choice

import pandas as pd

import xlrd

book = xlrd.open_workbook('Book1.xlsx')
sheet = book.sheet_by_index(0)



# Initialize components for Routine "ISI"
ISIClock = core.Clock()
iSi = visual.TextStim(win=win, name='iSi',
    text='+',
    font='Arial',
    pos=(0, 0), height=0.08, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "Receive_money"
Receive_moneyClock = core.Clock()
receiveMoneyPicture = visual.ImageStim(
    win=win,
    name='receiveMoneyPicture', 
    image='sin', mask=None,
    ori=1.0, pos=[0,0], size=1.0,
    color=[1,1,1], colorSpace='rgb', opacity=1.0,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)
ISI2 = visual.TextStim(win=win, name='ISI2',
    text='default text',
    font='Arial',
    pos=[0,0], height=1.0, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);

# Initialize components for Routine "trial"
trialClock = core.Clock()
ChoicePic = visual.ImageStim(
    win=win,
    name='ChoicePic', 
    image='sin', mask=None,
    ori=1.0, pos=[0,0], size=1.0,
    color=[1,1,1], colorSpace='rgb', opacity=1.0,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)

# Initialize components for Routine "askAd"
askAdClock = core.Clock()
response = keyboard.Keyboard()
yesNo = visual.TextStim(win=win, name='yesNo',
    text='default text',
    font='Arial',
    pos=[0,0], height=1.0, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
ask = visual.TextStim(win=win, name='ask',
    text='default text',
    font='Arial',
    pos=[0,0], height=1.0, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);

# Initialize components for Routine "getAd"
getAdClock = core.Clock()
gamAdRisk=0


getAdv = visual.TextStim(win=win, name='getAdv',
    text='default text',
    font='Arial',
    pos=[0,0], height=1.0, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
textForCode = visual.TextStim(win=win, name='textForCode',
    text='default text',
    font='Arial',
    pos=[0,0], height=1.0, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);

# Initialize components for Routine "Choice2Gain"
Choice2GainClock = core.Clock()
blank = visual.TextStim(win=win, name='blank',
    text='default text',
    font='Arial',
    pos=[0,0], height=1.0, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
ChoicePic2 = visual.ImageStim(
    win=win,
    name='ChoicePic2', 
    image='sin', mask=None,
    ori=1.0, pos=[0,0], size=1.0,
    color=[1,1,1], colorSpace='rgb', opacity=1.0,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-1.0)
resp = keyboard.Keyboard()
checkL1 = visual.ImageStim(
    win=win,
    name='checkL1', 
    image='sin', mask=None,
    ori=1.0, pos=[0,0], size=1.0,
    color='white', colorSpace='rgb', opacity=1.0,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-3.0)
checkR1 = visual.ImageStim(
    win=win,
    name='checkR1', 
    image='sin', mask=None,
    ori=1.0, pos=[0,0], size=1.0,
    color='white', colorSpace='rgb', opacity=1.0,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-4.0)

from PIL import Image
from psychopy import visual, core
nGamble=0
adFollow=0



# Initialize components for Routine "Feedback"
FeedbackClock = core.Clock()
endText = visual.TextStim(win=win, name='endText',
    text='default text',
    font='Arial',
    pos=[0,0], height=1.0, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
key_resp_2 = keyboard.Keyboard()

# Initialize components for Routine "Ending"
EndingClock = core.Clock()
Ending_ = visual.TextStim(win=win, name='Ending_',
    text='You have reached the end of the experiment. Thank you for participating :)',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

# ------Prepare to start Routine "welcome"-------
# update component parameters for each repeat
key_resp_4.keys = []
key_resp_4.rt = []
# keep track of which components have finished
welcomeComponents = [text, key_resp_4]
for thisComponent in welcomeComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
welcomeClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1
continueRoutine = True

# -------Run Routine "welcome"-------
while continueRoutine:
    # get current time
    t = welcomeClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=welcomeClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text* updates
    if text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text.frameNStart = frameN  # exact frame index
        text.tStart = t  # local t and not account for scr refresh
        text.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text, 'tStartRefresh')  # time at next scr refresh
        text.setAutoDraw(True)
    
    # *key_resp_4* updates
    waitOnFlip = False
    if key_resp_4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_resp_4.frameNStart = frameN  # exact frame index
        key_resp_4.tStart = t  # local t and not account for scr refresh
        key_resp_4.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp_4, 'tStartRefresh')  # time at next scr refresh
        key_resp_4.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp_4.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp_4.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp_4.status == STARTED and not waitOnFlip:
        theseKeys = key_resp_4.getKeys(keyList=['space'], waitRelease=False)
        if len(theseKeys):
            theseKeys = theseKeys[0]  # at least one key was pressed
            
            # check for quit:
            if "escape" == theseKeys:
                endExpNow = True
            key_resp_4.keys = theseKeys.name  # just the last key pressed
            key_resp_4.rt = theseKeys.rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in welcomeComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "welcome"-------
for thisComponent in welcomeComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('text.started', text.tStartRefresh)
thisExp.addData('text.stopped', text.tStopRefresh)
# check responses
if key_resp_4.keys in ['', [], None]:  # No response was made
    key_resp_4.keys = None
thisExp.addData('key_resp_4.keys',key_resp_4.keys)
if key_resp_4.keys != None:  # we had a response
    thisExp.addData('key_resp_4.rt', key_resp_4.rt)
thisExp.addData('key_resp_4.started', key_resp_4.tStartRefresh)
thisExp.addData('key_resp_4.stopped', key_resp_4.tStopRefresh)
thisExp.nextEntry()
# the Routine "welcome" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "inst"-------
# update component parameters for each repeat
space.keys = []
space.rt = []
# keep track of which components have finished
instComponents = [instructions, space]
for thisComponent in instComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
instClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1
continueRoutine = True

# -------Run Routine "inst"-------
while continueRoutine:
    # get current time
    t = instClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=instClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *instructions* updates
    if instructions.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        instructions.frameNStart = frameN  # exact frame index
        instructions.tStart = t  # local t and not account for scr refresh
        instructions.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(instructions, 'tStartRefresh')  # time at next scr refresh
        instructions.setAutoDraw(True)
    
    # *space* updates
    waitOnFlip = False
    if space.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        space.frameNStart = frameN  # exact frame index
        space.tStart = t  # local t and not account for scr refresh
        space.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(space, 'tStartRefresh')  # time at next scr refresh
        space.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(space.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(space.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if space.status == STARTED and not waitOnFlip:
        theseKeys = space.getKeys(keyList=['space'], waitRelease=False)
        if len(theseKeys):
            theseKeys = theseKeys[0]  # at least one key was pressed
            
            # check for quit:
            if "escape" == theseKeys:
                endExpNow = True
            space.keys = theseKeys.name  # just the last key pressed
            space.rt = theseKeys.rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in instComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "inst"-------
for thisComponent in instComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('instructions.started', instructions.tStartRefresh)
thisExp.addData('instructions.stopped', instructions.tStopRefresh)
# check responses
if space.keys in ['', [], None]:  # No response was made
    space.keys = None
thisExp.addData('space.keys',space.keys)
if space.keys != None:  # we had a response
    thisExp.addData('space.rt', space.rt)
thisExp.addData('space.started', space.tStartRefresh)
thisExp.addData('space.stopped', space.tStopRefresh)
thisExp.nextEntry()
# the Routine "inst" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "preBlock"-------
# update component parameters for each repeat
chooseInst.setColor('white', colorSpace='rgb')
chooseInst.setPos((0, 0.4))
chooseInst.setText('Please choose which person you would want to receive financial advice from, and then press enter.')
chooseInst.setFont('Arial')
chooseInst.setHeight(0.04)
Ad1.setColor('white', colorSpace='rgb')
Ad1.setPos((-0.4, -0.05))
Ad1.setText('\n  Advisor 1: (Left Arrow)\n\n\n\n\n\n\n\n\nAdelphi University MBA student,\ninterning at Chase Bank ')
Ad1.setFont('Arial')
Ad1.setHeight(0.04)
Ad2.setColor('white', colorSpace='rgb')
Ad2.setPos((0.4, -0.05))
Ad2.setText('\nAdvisor 2: (Right arrow)\n\n\n\n\n\n\n\n \nAdelphi University\nundergraduate biology major')
Ad2.setFont('Arial')
Ad2.setHeight(0.04)
key_resp_3.keys = []
key_resp_3.rt = []
Ad1pic.setOpacity(1)
Ad1pic.setPos((-.4, -0.06))
Ad1pic.setSize((0.3, 0.3))
Ad1pic.setOri(0)
Ad1pic.setImage('avatar_1.png')
border_right = visual.Circle(win,radius = 0.38, edges = 90,lineColor='green',lineColorSpace = 'rgb', fillColor = None, pos = (0.4, -0.09), opacity = 1, lineWidth = 5.0)
border_left = visual.Circle(win,radius = 0.38, edges = 90,lineColor='green',lineColorSpace = 'rgb', fillColor = None, pos = (-0.4, -0.09), opacity = 1, lineWidth = 5.0)

enter.keys = []
enter.rt = []


cond = pd.read_excel('Book1.xlsx')

# keep track of which components have finished
preBlockComponents = [chooseInst, Ad1, Ad2, key_resp_3, Ad1pic, Ad2pic, enter]
for thisComponent in preBlockComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
preBlockClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1
continueRoutine = True

# -------Run Routine "preBlock"-------
while continueRoutine:
    # get current time
    t = preBlockClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=preBlockClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *chooseInst* updates
    if chooseInst.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        chooseInst.frameNStart = frameN  # exact frame index
        chooseInst.tStart = t  # local t and not account for scr refresh
        chooseInst.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(chooseInst, 'tStartRefresh')  # time at next scr refresh
        chooseInst.setAutoDraw(True)
    
    # *Ad1* updates
    if Ad1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        Ad1.frameNStart = frameN  # exact frame index
        Ad1.tStart = t  # local t and not account for scr refresh
        Ad1.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Ad1, 'tStartRefresh')  # time at next scr refresh
        Ad1.setAutoDraw(True)
    
    # *Ad2* updates
    if Ad2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        Ad2.frameNStart = frameN  # exact frame index
        Ad2.tStart = t  # local t and not account for scr refresh
        Ad2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Ad2, 'tStartRefresh')  # time at next scr refresh
        Ad2.setAutoDraw(True)
    
    # *key_resp_3* updates
    waitOnFlip = False
    if key_resp_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_resp_3.frameNStart = frameN  # exact frame index
        key_resp_3.tStart = t  # local t and not account for scr refresh
        key_resp_3.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp_3, 'tStartRefresh')  # time at next scr refresh
        key_resp_3.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp_3.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp_3.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp_3.status == STARTED and not waitOnFlip:
        theseKeys = key_resp_3.getKeys(keyList=['left', 'right'], waitRelease=False)
        if len(theseKeys):
            theseKeys = theseKeys[0]  # at least one key was pressed
            
            # check for quit:
            if "escape" == theseKeys:
                endExpNow = True
            key_resp_3.keys = theseKeys.name  # just the last key pressed
            key_resp_3.rt = theseKeys.rt
    
    # *Ad1pic* updates
    if Ad1pic.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        Ad1pic.frameNStart = frameN  # exact frame index
        Ad1pic.tStart = t  # local t and not account for scr refresh
        Ad1pic.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Ad1pic, 'tStartRefresh')  # time at next scr refresh
        Ad1pic.setAutoDraw(True)
    
    # *Ad2pic* updates
    if Ad2pic.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        Ad2pic.frameNStart = frameN  # exact frame index
        Ad2pic.tStart = t  # local t and not account for scr refresh
        Ad2pic.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Ad2pic, 'tStartRefresh')  # time at next scr refresh
        Ad2pic.setAutoDraw(True)
    if key_resp_3.keys == 'left':
        border_left.autoDraw=True
    
    if key_resp_3.keys =='right':
        border_right.autoDraw=True
    
    if chooseInst.status == FINISHED:
        border_right.autoDraw = False 
        border_left.autoDraw = False
    
    
    
    # *enter* updates
    waitOnFlip = False
    if enter.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        enter.frameNStart = frameN  # exact frame index
        enter.tStart = t  # local t and not account for scr refresh
        enter.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(enter, 'tStartRefresh')  # time at next scr refresh
        enter.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(enter.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(enter.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if enter.status == STARTED and not waitOnFlip:
        theseKeys = enter.getKeys(keyList=['return'], waitRelease=False)
        if len(theseKeys):
            theseKeys = theseKeys[0]  # at least one key was pressed
            
            # check for quit:
            if "escape" == theseKeys:
                endExpNow = True
            enter.keys = theseKeys.name  # just the last key pressed
            enter.rt = theseKeys.rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in preBlockComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "preBlock"-------
for thisComponent in preBlockComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('chooseInst.started', chooseInst.tStartRefresh)
thisExp.addData('chooseInst.stopped', chooseInst.tStopRefresh)
thisExp.addData('Ad1.started', Ad1.tStartRefresh)
thisExp.addData('Ad1.stopped', Ad1.tStopRefresh)
thisExp.addData('Ad2.started', Ad2.tStartRefresh)
thisExp.addData('Ad2.stopped', Ad2.tStopRefresh)
# check responses
if key_resp_3.keys in ['', [], None]:  # No response was made
    key_resp_3.keys = None
thisExp.addData('key_resp_3.keys',key_resp_3.keys)
if key_resp_3.keys != None:  # we had a response
    thisExp.addData('key_resp_3.rt', key_resp_3.rt)
thisExp.addData('key_resp_3.started', key_resp_3.tStartRefresh)
thisExp.addData('key_resp_3.stopped', key_resp_3.tStopRefresh)
thisExp.nextEntry()
thisExp.addData('Ad1pic.started', Ad1pic.tStartRefresh)
thisExp.addData('Ad1pic.stopped', Ad1pic.tStopRefresh)
thisExp.addData('Ad2pic.started', Ad2pic.tStartRefresh)
thisExp.addData('Ad2pic.stopped', Ad2pic.tStopRefresh)
if chooseInst.status == FINISHED:
    border_right.autoDraw = False 
    border_left.autoDraw = False
# check responses
if enter.keys in ['', [], None]:  # No response was made
    enter.keys = None
thisExp.addData('enter.keys',enter.keys)
if enter.keys != None:  # we had a response
    thisExp.addData('enter.rt', enter.rt)
thisExp.addData('enter.started', enter.tStartRefresh)
thisExp.addData('enter.stopped', enter.tStopRefresh)
thisExp.nextEntry()

if key_resp_3.keys == 'left':
    text = 'Advisor 1 says:'
    text2 = 'Advisor 1'
    
if key_resp_3.keys == 'right':
    text = 'Advisor 2 says:'
    text2 = 'Advisor 2'
# the Routine "preBlock" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
practice = data.TrialHandler(nReps=1, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('practice.xlsx'),
    seed=None, name='practice')
thisExp.addLoop(practice)  # add the loop to the experiment
thisPractice = practice.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisPractice.rgb)
if thisPractice != None:
    for paramName in thisPractice:
        exec('{} = thisPractice[paramName]'.format(paramName))

for thisPractice in practice:
    currentLoop = practice
    # abbreviate parameter names if possible (e.g. rgb = thisPractice.rgb)
    if thisPractice != None:
        for paramName in thisPractice:
            exec('{} = thisPractice[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "ISI"-------
    routineTimer.add(2.000000)
    # update component parameters for each repeat
    # keep track of which components have finished
    ISIComponents = [iSi]
    for thisComponent in ISIComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    ISIClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    continueRoutine = True
    
    # -------Run Routine "ISI"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = ISIClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=ISIClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *iSi* updates
        if iSi.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            iSi.frameNStart = frameN  # exact frame index
            iSi.tStart = t  # local t and not account for scr refresh
            iSi.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(iSi, 'tStartRefresh')  # time at next scr refresh
            iSi.setAutoDraw(True)
        if iSi.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > iSi.tStartRefresh + 2-frameTolerance:
                # keep track of stop time/frame for later
                iSi.tStop = t  # not accounting for scr refresh
                iSi.frameNStop = frameN  # exact frame index
                win.timeOnFlip(iSi, 'tStopRefresh')  # time at next scr refresh
                iSi.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in ISIComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "ISI"-------
    for thisComponent in ISIComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    practice.addData('iSi.started', iSi.tStartRefresh)
    practice.addData('iSi.stopped', iSi.tStopRefresh)
    
    # ------Prepare to start Routine "Receive_money"-------
    routineTimer.add(3.000000)
    # update component parameters for each repeat
    receiveMoneyPicture.setOpacity(1)
    receiveMoneyPicture.setPos((0, -0.05))
    receiveMoneyPicture.setSize((1.5, 1.1))
    receiveMoneyPicture.setOri(0)
    receiveMoneyPicture.setImage(Amount)
    ISI2.setColor('white', colorSpace='rgb')
    ISI2.setPos((0, 0))
    ISI2.setText('+')
    ISI2.setFont('Arial')
    ISI2.setHeight(0.08)
    # keep track of which components have finished
    Receive_moneyComponents = [receiveMoneyPicture, ISI2]
    for thisComponent in Receive_moneyComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    Receive_moneyClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    continueRoutine = True
    
    # -------Run Routine "Receive_money"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = Receive_moneyClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=Receive_moneyClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *receiveMoneyPicture* updates
        if receiveMoneyPicture.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            receiveMoneyPicture.frameNStart = frameN  # exact frame index
            receiveMoneyPicture.tStart = t  # local t and not account for scr refresh
            receiveMoneyPicture.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(receiveMoneyPicture, 'tStartRefresh')  # time at next scr refresh
            receiveMoneyPicture.setAutoDraw(True)
        if receiveMoneyPicture.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > receiveMoneyPicture.tStartRefresh + 1.5-frameTolerance:
                # keep track of stop time/frame for later
                receiveMoneyPicture.tStop = t  # not accounting for scr refresh
                receiveMoneyPicture.frameNStop = frameN  # exact frame index
                win.timeOnFlip(receiveMoneyPicture, 'tStopRefresh')  # time at next scr refresh
                receiveMoneyPicture.setAutoDraw(False)
        
        # *ISI2* updates
        if ISI2.status == NOT_STARTED and tThisFlip >= 1.5-frameTolerance:
            # keep track of start time/frame for later
            ISI2.frameNStart = frameN  # exact frame index
            ISI2.tStart = t  # local t and not account for scr refresh
            ISI2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(ISI2, 'tStartRefresh')  # time at next scr refresh
            ISI2.setAutoDraw(True)
        if ISI2.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > ISI2.tStartRefresh + 1.5-frameTolerance:
                # keep track of stop time/frame for later
                ISI2.tStop = t  # not accounting for scr refresh
                ISI2.frameNStop = frameN  # exact frame index
                win.timeOnFlip(ISI2, 'tStopRefresh')  # time at next scr refresh
                ISI2.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in Receive_moneyComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "Receive_money"-------
    for thisComponent in Receive_moneyComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    practice.addData('receiveMoneyPicture.started', receiveMoneyPicture.tStartRefresh)
    practice.addData('receiveMoneyPicture.stopped', receiveMoneyPicture.tStopRefresh)
    practice.addData('ISI2.started', ISI2.tStartRefresh)
    practice.addData('ISI2.stopped', ISI2.tStopRefresh)
    
    # ------Prepare to start Routine "trial"-------
    routineTimer.add(2.000000)
    # update component parameters for each repeat
    ChoicePic.setOpacity(1)
    ChoicePic.setPos((0, 0))
    ChoicePic.setSize((1.3, 0.9))
    ChoicePic.setOri(0)
    ChoicePic.setImage(Choice)
    # keep track of which components have finished
    trialComponents = [ChoicePic]
    for thisComponent in trialComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    trialClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    continueRoutine = True
    
    # -------Run Routine "trial"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = trialClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=trialClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *ChoicePic* updates
        if ChoicePic.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            ChoicePic.frameNStart = frameN  # exact frame index
            ChoicePic.tStart = t  # local t and not account for scr refresh
            ChoicePic.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(ChoicePic, 'tStartRefresh')  # time at next scr refresh
            ChoicePic.setAutoDraw(True)
        if ChoicePic.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > ChoicePic.tStartRefresh + 2-frameTolerance:
                # keep track of stop time/frame for later
                ChoicePic.tStop = t  # not accounting for scr refresh
                ChoicePic.frameNStop = frameN  # exact frame index
                win.timeOnFlip(ChoicePic, 'tStopRefresh')  # time at next scr refresh
                ChoicePic.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in trialComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "trial"-------
    for thisComponent in trialComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    practice.addData('ChoicePic.started', ChoicePic.tStartRefresh)
    practice.addData('ChoicePic.stopped', ChoicePic.tStopRefresh)
    
    # ------Prepare to start Routine "askAd"-------
    routineTimer.add(3.000000)
    # update component parameters for each repeat
    response.keys = []
    response.rt = []
    yesNo.setColor('white', colorSpace='rgb')
    yesNo.setPos((0, -0.2))
    yesNo.setText('Y=1                 N=2')
    yesNo.setFont('Arial')
    yesNo.setHeight(0.09)
    ask.setColor('white', colorSpace='rgb')
    ask.setPos((0, 0.11))
    ask.setText('Would you like to hear advice from your financial advisor? \n')
    ask.setFont('Arial')
    ask.setHeight(0.06)
    # keep track of which components have finished
    askAdComponents = [response, yesNo, ask]
    for thisComponent in askAdComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    askAdClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    continueRoutine = True
    
    # -------Run Routine "askAd"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = askAdClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=askAdClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *response* updates
        waitOnFlip = False
        if response.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            response.frameNStart = frameN  # exact frame index
            response.tStart = t  # local t and not account for scr refresh
            response.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(response, 'tStartRefresh')  # time at next scr refresh
            response.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(response.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(response.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if response.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > response.tStartRefresh + 3-frameTolerance:
                # keep track of stop time/frame for later
                response.tStop = t  # not accounting for scr refresh
                response.frameNStop = frameN  # exact frame index
                win.timeOnFlip(response, 'tStopRefresh')  # time at next scr refresh
                response.status = FINISHED
        if response.status == STARTED and not waitOnFlip:
            theseKeys = response.getKeys(keyList=['1', '2'], waitRelease=False)
            if len(theseKeys):
                theseKeys = theseKeys[0]  # at least one key was pressed
                
                # check for quit:
                if "escape" == theseKeys:
                    endExpNow = True
                response.keys = theseKeys.name  # just the last key pressed
                response.rt = theseKeys.rt
                # a response ends the routine
                continueRoutine = False
        
        # *yesNo* updates
        if yesNo.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            yesNo.frameNStart = frameN  # exact frame index
            yesNo.tStart = t  # local t and not account for scr refresh
            yesNo.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(yesNo, 'tStartRefresh')  # time at next scr refresh
            yesNo.setAutoDraw(True)
        if yesNo.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > yesNo.tStartRefresh + 3-frameTolerance:
                # keep track of stop time/frame for later
                yesNo.tStop = t  # not accounting for scr refresh
                yesNo.frameNStop = frameN  # exact frame index
                win.timeOnFlip(yesNo, 'tStopRefresh')  # time at next scr refresh
                yesNo.setAutoDraw(False)
        
        # *ask* updates
        if ask.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            ask.frameNStart = frameN  # exact frame index
            ask.tStart = t  # local t and not account for scr refresh
            ask.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(ask, 'tStartRefresh')  # time at next scr refresh
            ask.setAutoDraw(True)
        if ask.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > ask.tStartRefresh + 3-frameTolerance:
                # keep track of stop time/frame for later
                ask.tStop = t  # not accounting for scr refresh
                ask.frameNStop = frameN  # exact frame index
                win.timeOnFlip(ask, 'tStopRefresh')  # time at next scr refresh
                ask.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in askAdComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "askAd"-------
    for thisComponent in askAdComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # check responses
    if response.keys in ['', [], None]:  # No response was made
        response.keys = None
    practice.addData('response.keys',response.keys)
    if response.keys != None:  # we had a response
        practice.addData('response.rt', response.rt)
    practice.addData('response.started', response.tStartRefresh)
    practice.addData('response.stopped', response.tStopRefresh)
    practice.addData('yesNo.started', yesNo.tStartRefresh)
    practice.addData('yesNo.stopped', yesNo.tStopRefresh)
    practice.addData('ask.started', ask.tStartRefresh)
    practice.addData('ask.stopped', ask.tStopRefresh)
    
    # ------Prepare to start Routine "getAd"-------
    # update component parameters for each repeat
    followAd = []
    
    
    if response.keys == '1':
        continueRoutine = True 
    if response.keys == '2':
        continueRoutine = False 
    if response.keys == None:
        continueRoutine = False
    
    
    getAdv.setColor('white', colorSpace='rgb')
    getAdv.setPos((0, 0))
    getAdv.setText(text + AdviceVar1)
    getAdv.setFont('Arial')
    getAdv.setHeight(0.08)
    textForCode.setColor([-1.000,-1.000,-1.000], colorSpace='rgb')
    textForCode.setPos((-0.9, 0))
    textForCode.setText(GambleAdviceType)
    textForCode.setFont('Arial')
    textForCode.setHeight(0.01)
    # keep track of which components have finished
    getAdComponents = [getAdv, textForCode]
    for thisComponent in getAdComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    getAdClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    continueRoutine = True
    
    # -------Run Routine "getAd"-------
    while continueRoutine:
        # get current time
        t = getAdClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=getAdClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        if response.keys == '1':
            continueRoutine = True 
        if response.keys == '2':
            continueRoutine = False 
        if response.keys == None:
            continueRoutine = False
        
        
        
        # *getAdv* updates
        if getAdv.status == NOT_STARTED and continueRoutine == True:
            # keep track of start time/frame for later
            getAdv.frameNStart = frameN  # exact frame index
            getAdv.tStart = t  # local t and not account for scr refresh
            getAdv.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(getAdv, 'tStartRefresh')  # time at next scr refresh
            getAdv.setAutoDraw(True)
        if getAdv.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > getAdv.tStartRefresh + 2-frameTolerance:
                # keep track of stop time/frame for later
                getAdv.tStop = t  # not accounting for scr refresh
                getAdv.frameNStop = frameN  # exact frame index
                win.timeOnFlip(getAdv, 'tStopRefresh')  # time at next scr refresh
                getAdv.setAutoDraw(False)
        
        # *textForCode* updates
        if textForCode.status == NOT_STARTED and continueRoutine == True:
            # keep track of start time/frame for later
            textForCode.frameNStart = frameN  # exact frame index
            textForCode.tStart = t  # local t and not account for scr refresh
            textForCode.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(textForCode, 'tStartRefresh')  # time at next scr refresh
            textForCode.setAutoDraw(True)
        if textForCode.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > textForCode.tStartRefresh + 1-frameTolerance:
                # keep track of stop time/frame for later
                textForCode.tStop = t  # not accounting for scr refresh
                textForCode.frameNStop = frameN  # exact frame index
                win.timeOnFlip(textForCode, 'tStopRefresh')  # time at next scr refresh
                textForCode.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in getAdComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "getAd"-------
    for thisComponent in getAdComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    #gambleAdvice = int(GambleAdviceNum)
    
    
    if response.keys == '1':
        continueRoutine = True 
    if response.keys == '2':
        continueRoutine = False 
    if response.keys == None:
        continueRoutine = False
    
    
    if continueRoutine == True and GambleAdviceType == 'risk':
        gamAdRisk += 1
        followAd = 'risk'
        
    print(gamAdRisk)
    practice.addData('getAdv.started', getAdv.tStartRefresh)
    practice.addData('getAdv.stopped', getAdv.tStopRefresh)
    practice.addData('textForCode.started', textForCode.tStartRefresh)
    practice.addData('textForCode.stopped', textForCode.tStopRefresh)
    # the Routine "getAd" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "Choice2Gain"-------
    # update component parameters for each repeat
    blank.setColor([-1.000,-1.000,-1.000], colorSpace='rgb')
    blank.setPos((0, 0))
    blank.setText('I')
    blank.setFont('Arial')
    blank.setHeight(0.01)
    ChoicePic2.setOpacity(1)
    ChoicePic2.setPos((0, 0))
    ChoicePic2.setSize((1.3, 0.9))
    ChoicePic2.setOri(0)
    ChoicePic2.setImage(Choice2)
    resp.keys = []
    resp.rt = []
    checkL1.setColor([1,1,1], colorSpace='rgb')
    checkL1.setOpacity(1)
    checkL1.setPos((0, 0))
    checkL1.setSize((2, 1))
    checkL1.setOri(0)
    checkL1.setImage('check2.png')
    checkL1.setMask('None')
    checkR1.setColor([1,1,1], colorSpace='rgb')
    checkR1.setOpacity(1)
    checkR1.setPos((0, 0))
    checkR1.setSize((2, 1))
    checkR1.setOri(0)
    checkR1.setImage('check3.png')
    checkR1.setMask('None')
    # keep track of which components have finished
    Choice2GainComponents = [blank, ChoicePic2, resp, checkL1, checkR1]
    for thisComponent in Choice2GainComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    Choice2GainClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    continueRoutine = True
    
    # -------Run Routine "Choice2Gain"-------
    while continueRoutine:
        # get current time
        t = Choice2GainClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=Choice2GainClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *blank* updates
        if blank.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            blank.frameNStart = frameN  # exact frame index
            blank.tStart = t  # local t and not account for scr refresh
            blank.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(blank, 'tStartRefresh')  # time at next scr refresh
            blank.setAutoDraw(True)
        if blank.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > blank.tStartRefresh + 2-frameTolerance:
                # keep track of stop time/frame for later
                blank.tStop = t  # not accounting for scr refresh
                blank.frameNStop = frameN  # exact frame index
                win.timeOnFlip(blank, 'tStopRefresh')  # time at next scr refresh
                blank.setAutoDraw(False)
        
        # *ChoicePic2* updates
        if ChoicePic2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            ChoicePic2.frameNStart = frameN  # exact frame index
            ChoicePic2.tStart = t  # local t and not account for scr refresh
            ChoicePic2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(ChoicePic2, 'tStartRefresh')  # time at next scr refresh
            ChoicePic2.setAutoDraw(True)
        if ChoicePic2.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > ChoicePic2.tStartRefresh + 2-frameTolerance:
                # keep track of stop time/frame for later
                ChoicePic2.tStop = t  # not accounting for scr refresh
                ChoicePic2.frameNStop = frameN  # exact frame index
                win.timeOnFlip(ChoicePic2, 'tStopRefresh')  # time at next scr refresh
                ChoicePic2.setAutoDraw(False)
        
        # *resp* updates
        waitOnFlip = False
        if resp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            resp.frameNStart = frameN  # exact frame index
            resp.tStart = t  # local t and not account for scr refresh
            resp.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(resp, 'tStartRefresh')  # time at next scr refresh
            resp.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(resp.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if resp.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > resp.tStartRefresh + 2-frameTolerance:
                # keep track of stop time/frame for later
                resp.tStop = t  # not accounting for scr refresh
                resp.frameNStop = frameN  # exact frame index
                win.timeOnFlip(resp, 'tStopRefresh')  # time at next scr refresh
                resp.status = FINISHED
        if resp.status == STARTED and not waitOnFlip:
            theseKeys = resp.getKeys(keyList=['left', 'right'], waitRelease=False)
            if len(theseKeys):
                theseKeys = theseKeys[0]  # at least one key was pressed
                
                # check for quit:
                if "escape" == theseKeys:
                    endExpNow = True
                resp.keys = theseKeys.name  # just the last key pressed
                resp.rt = theseKeys.rt
        
        # *checkL1* updates
        if checkL1.status == NOT_STARTED and resp.keys == 'left':
            # keep track of start time/frame for later
            checkL1.frameNStart = frameN  # exact frame index
            checkL1.tStart = t  # local t and not account for scr refresh
            checkL1.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(checkL1, 'tStartRefresh')  # time at next scr refresh
            checkL1.setAutoDraw(True)
        if checkL1.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > checkL1.tStartRefresh + 1-frameTolerance:
                # keep track of stop time/frame for later
                checkL1.tStop = t  # not accounting for scr refresh
                checkL1.frameNStop = frameN  # exact frame index
                win.timeOnFlip(checkL1, 'tStopRefresh')  # time at next scr refresh
                checkL1.setAutoDraw(False)
        
        # *checkR1* updates
        if checkR1.status == NOT_STARTED and resp.keys == 'right':
            # keep track of start time/frame for later
            checkR1.frameNStart = frameN  # exact frame index
            checkR1.tStart = t  # local t and not account for scr refresh
            checkR1.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(checkR1, 'tStartRefresh')  # time at next scr refresh
            checkR1.setAutoDraw(True)
        if checkR1.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > checkR1.tStartRefresh + 1-frameTolerance:
                # keep track of stop time/frame for later
                checkR1.tStop = t  # not accounting for scr refresh
                checkR1.frameNStop = frameN  # exact frame index
                win.timeOnFlip(checkR1, 'tStopRefresh')  # time at next scr refresh
                checkR1.setAutoDraw(False)
        checkL1.autoLog=False
        checkR1.autoLog=False
        
        
        if resp.keys == 'left':
            checkL1.autoDraw=True
        
        
        if resp.keys == 'right':
            checkR1.autoDraw=True
        
        
        if blank.status == FINISHED:
            checkR1.autoDraw=False
            checkL1.autoDraw=False
            continueRoutine=False
        
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in Choice2GainComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "Choice2Gain"-------
    for thisComponent in Choice2GainComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    practice.addData('blank.started', blank.tStartRefresh)
    practice.addData('blank.stopped', blank.tStopRefresh)
    practice.addData('ChoicePic2.started', ChoicePic2.tStartRefresh)
    practice.addData('ChoicePic2.stopped', ChoicePic2.tStopRefresh)
    # check responses
    if resp.keys in ['', [], None]:  # No response was made
        resp.keys = None
    practice.addData('resp.keys',resp.keys)
    if resp.keys != None:  # we had a response
        practice.addData('resp.rt', resp.rt)
    practice.addData('resp.started', resp.tStartRefresh)
    practice.addData('resp.stopped', resp.tStopRefresh)
    practice.addData('checkL1.started', checkL1.tStartRefresh)
    practice.addData('checkL1.stopped', checkL1.tStopRefresh)
    practice.addData('checkR1.started', checkR1.tStartRefresh)
    practice.addData('checkR1.stopped', checkR1.tStopRefresh)
    checkL1.autoLog=False
    checkR1.autoLog=False
    
    
    
    if resp.keys == 'left':
        checkL1.autoDraw=True
    
    
    if resp.keys =='right':
        checkR1.autoDraw=True
    
    
    if blank.status == FINISHED:
        checkR1.autoDraw=False
        checkL1.autoDraw=False
    
    #trials.addData('nGamble', nGamble)
    if resp.keys == 'right':
        nGamble += 1
    
    
    if followAd == 'risk' and resp.keys == 'right':
        adFollow += 1
        
    
    
    
    # the Routine "Choice2Gain" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 1 repeats of 'practice'


# ------Prepare to start Routine "endprac"-------
# update component parameters for each repeat
key_resp.keys = []
key_resp.rt = []
# keep track of which components have finished
endpracComponents = [EndPrac, key_resp]
for thisComponent in endpracComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
endpracClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1
continueRoutine = True

# -------Run Routine "endprac"-------
while continueRoutine:
    # get current time
    t = endpracClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=endpracClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *EndPrac* updates
    if EndPrac.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        EndPrac.frameNStart = frameN  # exact frame index
        EndPrac.tStart = t  # local t and not account for scr refresh
        EndPrac.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(EndPrac, 'tStartRefresh')  # time at next scr refresh
        EndPrac.setAutoDraw(True)
    
    # *key_resp* updates
    waitOnFlip = False
    if key_resp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_resp.frameNStart = frameN  # exact frame index
        key_resp.tStart = t  # local t and not account for scr refresh
        key_resp.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp, 'tStartRefresh')  # time at next scr refresh
        key_resp.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp.status == STARTED and not waitOnFlip:
        theseKeys = key_resp.getKeys(keyList=['space'], waitRelease=False)
        if len(theseKeys):
            theseKeys = theseKeys[0]  # at least one key was pressed
            
            # check for quit:
            if "escape" == theseKeys:
                endExpNow = True
            key_resp.keys = theseKeys.name  # just the last key pressed
            key_resp.rt = theseKeys.rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in endpracComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "endprac"-------
for thisComponent in endpracComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('EndPrac.started', EndPrac.tStartRefresh)
thisExp.addData('EndPrac.stopped', EndPrac.tStopRefresh)
# check responses
if key_resp.keys in ['', [], None]:  # No response was made
    key_resp.keys = None
thisExp.addData('key_resp.keys',key_resp.keys)
if key_resp.keys != None:  # we had a response
    thisExp.addData('key_resp.rt', key_resp.rt)
thisExp.addData('key_resp.started', key_resp.tStartRefresh)
thisExp.addData('key_resp.stopped', key_resp.tStopRefresh)
thisExp.nextEntry()
# the Routine "endprac" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
trials_2 = data.TrialHandler(nReps=10, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=[None],
    seed=None, name='trials_2')
thisExp.addLoop(trials_2)  # add the loop to the experiment
thisTrial_2 = trials_2.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisTrial_2.rgb)
if thisTrial_2 != None:
    for paramName in thisTrial_2:
        exec('{} = thisTrial_2[paramName]'.format(paramName))

for thisTrial_2 in trials_2:
    currentLoop = trials_2
    # abbreviate parameter names if possible (e.g. rgb = thisTrial_2.rgb)
    if thisTrial_2 != None:
        for paramName in thisTrial_2:
            exec('{} = thisTrial_2[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "preBlock"-------
    # update component parameters for each repeat
    chooseInst.setColor('white', colorSpace='rgb')
    chooseInst.setPos((0, 0.4))
    chooseInst.setText('Please choose which person you would want to receive financial advice from, and then press enter.')
    chooseInst.setFont('Arial')
    chooseInst.setHeight(0.04)
    Ad1.setColor('white', colorSpace='rgb')
    Ad1.setPos((-0.4, -0.05))
    Ad1.setText('\n  Advisor 1: (Left Arrow)\n\n\n\n\n\n\n\n\nAdelphi University MBA student,\ninterning at Chase Bank ')
    Ad1.setFont('Arial')
    Ad1.setHeight(0.04)
    Ad2.setColor('white', colorSpace='rgb')
    Ad2.setPos((0.4, -0.05))
    Ad2.setText('\nAdvisor 2: (Right arrow)\n\n\n\n\n\n\n\n \nAdelphi University\nundergraduate biology major')
    Ad2.setFont('Arial')
    Ad2.setHeight(0.04)
    key_resp_3.keys = []
    key_resp_3.rt = []
    Ad1pic.setOpacity(1)
    Ad1pic.setPos((-.4, -0.06))
    Ad1pic.setSize((0.3, 0.3))
    Ad1pic.setOri(0)
    Ad1pic.setImage('avatar_1.png')
    border_right = visual.Circle(win,radius = 0.38, edges = 90,lineColor='green',lineColorSpace = 'rgb', fillColor = None, pos = (0.4, -0.09), opacity = 1, lineWidth = 5.0)
    border_left = visual.Circle(win,radius = 0.38, edges = 90,lineColor='green',lineColorSpace = 'rgb', fillColor = None, pos = (-0.4, -0.09), opacity = 1, lineWidth = 5.0)
    
    enter.keys = []
    enter.rt = []
    
    
    cond = pd.read_excel('Book1.xlsx')
    
    # keep track of which components have finished
    preBlockComponents = [chooseInst, Ad1, Ad2, key_resp_3, Ad1pic, Ad2pic, enter]
    for thisComponent in preBlockComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    preBlockClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    continueRoutine = True
    
    # -------Run Routine "preBlock"-------
    while continueRoutine:
        # get current time
        t = preBlockClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=preBlockClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *chooseInst* updates
        if chooseInst.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            chooseInst.frameNStart = frameN  # exact frame index
            chooseInst.tStart = t  # local t and not account for scr refresh
            chooseInst.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(chooseInst, 'tStartRefresh')  # time at next scr refresh
            chooseInst.setAutoDraw(True)
        
        # *Ad1* updates
        if Ad1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Ad1.frameNStart = frameN  # exact frame index
            Ad1.tStart = t  # local t and not account for scr refresh
            Ad1.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Ad1, 'tStartRefresh')  # time at next scr refresh
            Ad1.setAutoDraw(True)
        
        # *Ad2* updates
        if Ad2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Ad2.frameNStart = frameN  # exact frame index
            Ad2.tStart = t  # local t and not account for scr refresh
            Ad2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Ad2, 'tStartRefresh')  # time at next scr refresh
            Ad2.setAutoDraw(True)
        
        # *key_resp_3* updates
        waitOnFlip = False
        if key_resp_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            key_resp_3.frameNStart = frameN  # exact frame index
            key_resp_3.tStart = t  # local t and not account for scr refresh
            key_resp_3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_resp_3, 'tStartRefresh')  # time at next scr refresh
            key_resp_3.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_resp_3.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(key_resp_3.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if key_resp_3.status == STARTED and not waitOnFlip:
            theseKeys = key_resp_3.getKeys(keyList=['left', 'right'], waitRelease=False)
            if len(theseKeys):
                theseKeys = theseKeys[0]  # at least one key was pressed
                
                # check for quit:
                if "escape" == theseKeys:
                    endExpNow = True
                key_resp_3.keys = theseKeys.name  # just the last key pressed
                key_resp_3.rt = theseKeys.rt
        
        # *Ad1pic* updates
        if Ad1pic.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Ad1pic.frameNStart = frameN  # exact frame index
            Ad1pic.tStart = t  # local t and not account for scr refresh
            Ad1pic.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Ad1pic, 'tStartRefresh')  # time at next scr refresh
            Ad1pic.setAutoDraw(True)
        
        # *Ad2pic* updates
        if Ad2pic.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Ad2pic.frameNStart = frameN  # exact frame index
            Ad2pic.tStart = t  # local t and not account for scr refresh
            Ad2pic.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Ad2pic, 'tStartRefresh')  # time at next scr refresh
            Ad2pic.setAutoDraw(True)
        if key_resp_3.keys == 'left':
            border_left.autoDraw=True
        
        if key_resp_3.keys =='right':
            border_right.autoDraw=True
        
        if chooseInst.status == FINISHED:
            border_right.autoDraw = False 
            border_left.autoDraw = False
        
        
        
        # *enter* updates
        waitOnFlip = False
        if enter.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            enter.frameNStart = frameN  # exact frame index
            enter.tStart = t  # local t and not account for scr refresh
            enter.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(enter, 'tStartRefresh')  # time at next scr refresh
            enter.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(enter.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(enter.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if enter.status == STARTED and not waitOnFlip:
            theseKeys = enter.getKeys(keyList=['return'], waitRelease=False)
            if len(theseKeys):
                theseKeys = theseKeys[0]  # at least one key was pressed
                
                # check for quit:
                if "escape" == theseKeys:
                    endExpNow = True
                enter.keys = theseKeys.name  # just the last key pressed
                enter.rt = theseKeys.rt
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in preBlockComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "preBlock"-------
    for thisComponent in preBlockComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    trials_2.addData('chooseInst.started', chooseInst.tStartRefresh)
    trials_2.addData('chooseInst.stopped', chooseInst.tStopRefresh)
    trials_2.addData('Ad1.started', Ad1.tStartRefresh)
    trials_2.addData('Ad1.stopped', Ad1.tStopRefresh)
    trials_2.addData('Ad2.started', Ad2.tStartRefresh)
    trials_2.addData('Ad2.stopped', Ad2.tStopRefresh)
    # check responses
    if key_resp_3.keys in ['', [], None]:  # No response was made
        key_resp_3.keys = None
    trials_2.addData('key_resp_3.keys',key_resp_3.keys)
    if key_resp_3.keys != None:  # we had a response
        trials_2.addData('key_resp_3.rt', key_resp_3.rt)
    trials_2.addData('key_resp_3.started', key_resp_3.tStartRefresh)
    trials_2.addData('key_resp_3.stopped', key_resp_3.tStopRefresh)
    trials_2.addData('Ad1pic.started', Ad1pic.tStartRefresh)
    trials_2.addData('Ad1pic.stopped', Ad1pic.tStopRefresh)
    trials_2.addData('Ad2pic.started', Ad2pic.tStartRefresh)
    trials_2.addData('Ad2pic.stopped', Ad2pic.tStopRefresh)
    if chooseInst.status == FINISHED:
        border_right.autoDraw = False 
        border_left.autoDraw = False
    # check responses
    if enter.keys in ['', [], None]:  # No response was made
        enter.keys = None
    trials_2.addData('enter.keys',enter.keys)
    if enter.keys != None:  # we had a response
        trials_2.addData('enter.rt', enter.rt)
    trials_2.addData('enter.started', enter.tStartRefresh)
    trials_2.addData('enter.stopped', enter.tStopRefresh)
    
    if key_resp_3.keys == 'left':
        text = 'Advisor 1 says:'
        text2 = 'Advisor 1'
        
    if key_resp_3.keys == 'right':
        text = 'Advisor 2 says:'
        text2 = 'Advisor 2'
    # the Routine "preBlock" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # set up handler to look after randomisation of conditions etc
    trials = data.TrialHandler(nReps=1, method='random', 
        extraInfo=expInfo, originPath=-1,
        trialList=data.importConditions('Book1.xlsx', selection=choice(40, size=20, replace=False)),
        seed=None, name='trials')
    thisExp.addLoop(trials)  # add the loop to the experiment
    thisTrial = trials.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
    if thisTrial != None:
        for paramName in thisTrial:
            exec('{} = thisTrial[paramName]'.format(paramName))
    
    for thisTrial in trials:
        currentLoop = trials
        # abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
        if thisTrial != None:
            for paramName in thisTrial:
                exec('{} = thisTrial[paramName]'.format(paramName))
        
        # ------Prepare to start Routine "ISI"-------
        routineTimer.add(2.000000)
        # update component parameters for each repeat
        # keep track of which components have finished
        ISIComponents = [iSi]
        for thisComponent in ISIComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        ISIClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        continueRoutine = True
        
        # -------Run Routine "ISI"-------
        while continueRoutine and routineTimer.getTime() > 0:
            # get current time
            t = ISIClock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=ISIClock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *iSi* updates
            if iSi.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                iSi.frameNStart = frameN  # exact frame index
                iSi.tStart = t  # local t and not account for scr refresh
                iSi.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(iSi, 'tStartRefresh')  # time at next scr refresh
                iSi.setAutoDraw(True)
            if iSi.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > iSi.tStartRefresh + 2-frameTolerance:
                    # keep track of stop time/frame for later
                    iSi.tStop = t  # not accounting for scr refresh
                    iSi.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(iSi, 'tStopRefresh')  # time at next scr refresh
                    iSi.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in ISIComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "ISI"-------
        for thisComponent in ISIComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        trials.addData('iSi.started', iSi.tStartRefresh)
        trials.addData('iSi.stopped', iSi.tStopRefresh)
        
        # ------Prepare to start Routine "Receive_money"-------
        routineTimer.add(3.000000)
        # update component parameters for each repeat
        receiveMoneyPicture.setOpacity(1)
        receiveMoneyPicture.setPos((0, -0.05))
        receiveMoneyPicture.setSize((1.5, 1.1))
        receiveMoneyPicture.setOri(0)
        receiveMoneyPicture.setImage(Amount)
        ISI2.setColor('white', colorSpace='rgb')
        ISI2.setPos((0, 0))
        ISI2.setText('+')
        ISI2.setFont('Arial')
        ISI2.setHeight(0.08)
        # keep track of which components have finished
        Receive_moneyComponents = [receiveMoneyPicture, ISI2]
        for thisComponent in Receive_moneyComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        Receive_moneyClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        continueRoutine = True
        
        # -------Run Routine "Receive_money"-------
        while continueRoutine and routineTimer.getTime() > 0:
            # get current time
            t = Receive_moneyClock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=Receive_moneyClock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *receiveMoneyPicture* updates
            if receiveMoneyPicture.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                receiveMoneyPicture.frameNStart = frameN  # exact frame index
                receiveMoneyPicture.tStart = t  # local t and not account for scr refresh
                receiveMoneyPicture.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(receiveMoneyPicture, 'tStartRefresh')  # time at next scr refresh
                receiveMoneyPicture.setAutoDraw(True)
            if receiveMoneyPicture.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > receiveMoneyPicture.tStartRefresh + 1.5-frameTolerance:
                    # keep track of stop time/frame for later
                    receiveMoneyPicture.tStop = t  # not accounting for scr refresh
                    receiveMoneyPicture.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(receiveMoneyPicture, 'tStopRefresh')  # time at next scr refresh
                    receiveMoneyPicture.setAutoDraw(False)
            
            # *ISI2* updates
            if ISI2.status == NOT_STARTED and tThisFlip >= 1.5-frameTolerance:
                # keep track of start time/frame for later
                ISI2.frameNStart = frameN  # exact frame index
                ISI2.tStart = t  # local t and not account for scr refresh
                ISI2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(ISI2, 'tStartRefresh')  # time at next scr refresh
                ISI2.setAutoDraw(True)
            if ISI2.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > ISI2.tStartRefresh + 1.5-frameTolerance:
                    # keep track of stop time/frame for later
                    ISI2.tStop = t  # not accounting for scr refresh
                    ISI2.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(ISI2, 'tStopRefresh')  # time at next scr refresh
                    ISI2.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in Receive_moneyComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "Receive_money"-------
        for thisComponent in Receive_moneyComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        trials.addData('receiveMoneyPicture.started', receiveMoneyPicture.tStartRefresh)
        trials.addData('receiveMoneyPicture.stopped', receiveMoneyPicture.tStopRefresh)
        trials.addData('ISI2.started', ISI2.tStartRefresh)
        trials.addData('ISI2.stopped', ISI2.tStopRefresh)
        
        # ------Prepare to start Routine "trial"-------
        routineTimer.add(2.000000)
        # update component parameters for each repeat
        ChoicePic.setOpacity(1)
        ChoicePic.setPos((0, 0))
        ChoicePic.setSize((1.3, 0.9))
        ChoicePic.setOri(0)
        ChoicePic.setImage(Choice)
        # keep track of which components have finished
        trialComponents = [ChoicePic]
        for thisComponent in trialComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        trialClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        continueRoutine = True
        
        # -------Run Routine "trial"-------
        while continueRoutine and routineTimer.getTime() > 0:
            # get current time
            t = trialClock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=trialClock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *ChoicePic* updates
            if ChoicePic.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                ChoicePic.frameNStart = frameN  # exact frame index
                ChoicePic.tStart = t  # local t and not account for scr refresh
                ChoicePic.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(ChoicePic, 'tStartRefresh')  # time at next scr refresh
                ChoicePic.setAutoDraw(True)
            if ChoicePic.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > ChoicePic.tStartRefresh + 2-frameTolerance:
                    # keep track of stop time/frame for later
                    ChoicePic.tStop = t  # not accounting for scr refresh
                    ChoicePic.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(ChoicePic, 'tStopRefresh')  # time at next scr refresh
                    ChoicePic.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in trialComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "trial"-------
        for thisComponent in trialComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        trials.addData('ChoicePic.started', ChoicePic.tStartRefresh)
        trials.addData('ChoicePic.stopped', ChoicePic.tStopRefresh)
        
        # ------Prepare to start Routine "askAd"-------
        routineTimer.add(3.000000)
        # update component parameters for each repeat
        response.keys = []
        response.rt = []
        yesNo.setColor('white', colorSpace='rgb')
        yesNo.setPos((0, -0.2))
        yesNo.setText('Y=1                 N=2')
        yesNo.setFont('Arial')
        yesNo.setHeight(0.09)
        ask.setColor('white', colorSpace='rgb')
        ask.setPos((0, 0.11))
        ask.setText('Would you like to hear advice from your financial advisor? \n')
        ask.setFont('Arial')
        ask.setHeight(0.06)
        # keep track of which components have finished
        askAdComponents = [response, yesNo, ask]
        for thisComponent in askAdComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        askAdClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        continueRoutine = True
        
        # -------Run Routine "askAd"-------
        while continueRoutine and routineTimer.getTime() > 0:
            # get current time
            t = askAdClock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=askAdClock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *response* updates
            waitOnFlip = False
            if response.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                # keep track of start time/frame for later
                response.frameNStart = frameN  # exact frame index
                response.tStart = t  # local t and not account for scr refresh
                response.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(response, 'tStartRefresh')  # time at next scr refresh
                response.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(response.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(response.clearEvents, eventType='keyboard')  # clear events on next screen flip
            if response.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > response.tStartRefresh + 3-frameTolerance:
                    # keep track of stop time/frame for later
                    response.tStop = t  # not accounting for scr refresh
                    response.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(response, 'tStopRefresh')  # time at next scr refresh
                    response.status = FINISHED
            if response.status == STARTED and not waitOnFlip:
                theseKeys = response.getKeys(keyList=['1', '2'], waitRelease=False)
                if len(theseKeys):
                    theseKeys = theseKeys[0]  # at least one key was pressed
                    
                    # check for quit:
                    if "escape" == theseKeys:
                        endExpNow = True
                    response.keys = theseKeys.name  # just the last key pressed
                    response.rt = theseKeys.rt
                    # a response ends the routine
                    continueRoutine = False
            
            # *yesNo* updates
            if yesNo.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                yesNo.frameNStart = frameN  # exact frame index
                yesNo.tStart = t  # local t and not account for scr refresh
                yesNo.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(yesNo, 'tStartRefresh')  # time at next scr refresh
                yesNo.setAutoDraw(True)
            if yesNo.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > yesNo.tStartRefresh + 3-frameTolerance:
                    # keep track of stop time/frame for later
                    yesNo.tStop = t  # not accounting for scr refresh
                    yesNo.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(yesNo, 'tStopRefresh')  # time at next scr refresh
                    yesNo.setAutoDraw(False)
            
            # *ask* updates
            if ask.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                ask.frameNStart = frameN  # exact frame index
                ask.tStart = t  # local t and not account for scr refresh
                ask.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(ask, 'tStartRefresh')  # time at next scr refresh
                ask.setAutoDraw(True)
            if ask.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > ask.tStartRefresh + 3-frameTolerance:
                    # keep track of stop time/frame for later
                    ask.tStop = t  # not accounting for scr refresh
                    ask.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(ask, 'tStopRefresh')  # time at next scr refresh
                    ask.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in askAdComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "askAd"-------
        for thisComponent in askAdComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # check responses
        if response.keys in ['', [], None]:  # No response was made
            response.keys = None
        trials.addData('response.keys',response.keys)
        if response.keys != None:  # we had a response
            trials.addData('response.rt', response.rt)
        trials.addData('response.started', response.tStartRefresh)
        trials.addData('response.stopped', response.tStopRefresh)
        trials.addData('yesNo.started', yesNo.tStartRefresh)
        trials.addData('yesNo.stopped', yesNo.tStopRefresh)
        trials.addData('ask.started', ask.tStartRefresh)
        trials.addData('ask.stopped', ask.tStopRefresh)
        
        # ------Prepare to start Routine "getAd"-------
        # update component parameters for each repeat
        followAd = []
        
        
        if response.keys == '1':
            continueRoutine = True 
        if response.keys == '2':
            continueRoutine = False 
        if response.keys == None:
            continueRoutine = False
        
        
        getAdv.setColor('white', colorSpace='rgb')
        getAdv.setPos((0, 0))
        getAdv.setText(text + AdviceVar1)
        getAdv.setFont('Arial')
        getAdv.setHeight(0.08)
        textForCode.setColor([-1.000,-1.000,-1.000], colorSpace='rgb')
        textForCode.setPos((-0.9, 0))
        textForCode.setText(GambleAdviceType)
        textForCode.setFont('Arial')
        textForCode.setHeight(0.01)
        # keep track of which components have finished
        getAdComponents = [getAdv, textForCode]
        for thisComponent in getAdComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        getAdClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        continueRoutine = True
        
        # -------Run Routine "getAd"-------
        while continueRoutine:
            # get current time
            t = getAdClock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=getAdClock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            if response.keys == '1':
                continueRoutine = True 
            if response.keys == '2':
                continueRoutine = False 
            if response.keys == None:
                continueRoutine = False
            
            
            
            # *getAdv* updates
            if getAdv.status == NOT_STARTED and continueRoutine == True:
                # keep track of start time/frame for later
                getAdv.frameNStart = frameN  # exact frame index
                getAdv.tStart = t  # local t and not account for scr refresh
                getAdv.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(getAdv, 'tStartRefresh')  # time at next scr refresh
                getAdv.setAutoDraw(True)
            if getAdv.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > getAdv.tStartRefresh + 2-frameTolerance:
                    # keep track of stop time/frame for later
                    getAdv.tStop = t  # not accounting for scr refresh
                    getAdv.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(getAdv, 'tStopRefresh')  # time at next scr refresh
                    getAdv.setAutoDraw(False)
            
            # *textForCode* updates
            if textForCode.status == NOT_STARTED and continueRoutine == True:
                # keep track of start time/frame for later
                textForCode.frameNStart = frameN  # exact frame index
                textForCode.tStart = t  # local t and not account for scr refresh
                textForCode.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(textForCode, 'tStartRefresh')  # time at next scr refresh
                textForCode.setAutoDraw(True)
            if textForCode.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > textForCode.tStartRefresh + 1-frameTolerance:
                    # keep track of stop time/frame for later
                    textForCode.tStop = t  # not accounting for scr refresh
                    textForCode.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(textForCode, 'tStopRefresh')  # time at next scr refresh
                    textForCode.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in getAdComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "getAd"-------
        for thisComponent in getAdComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        #gambleAdvice = int(GambleAdviceNum)
        
        
        if response.keys == '1':
            continueRoutine = True 
        if response.keys == '2':
            continueRoutine = False 
        if response.keys == None:
            continueRoutine = False
        
        
        if continueRoutine == True and GambleAdviceType == 'risk':
            gamAdRisk += 1
            followAd = 'risk'
            
        print(gamAdRisk)
        trials.addData('getAdv.started', getAdv.tStartRefresh)
        trials.addData('getAdv.stopped', getAdv.tStopRefresh)
        trials.addData('textForCode.started', textForCode.tStartRefresh)
        trials.addData('textForCode.stopped', textForCode.tStopRefresh)
        # the Routine "getAd" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # ------Prepare to start Routine "Choice2Gain"-------
        # update component parameters for each repeat
        blank.setColor([-1.000,-1.000,-1.000], colorSpace='rgb')
        blank.setPos((0, 0))
        blank.setText('I')
        blank.setFont('Arial')
        blank.setHeight(0.01)
        ChoicePic2.setOpacity(1)
        ChoicePic2.setPos((0, 0))
        ChoicePic2.setSize((1.3, 0.9))
        ChoicePic2.setOri(0)
        ChoicePic2.setImage(Choice2)
        resp.keys = []
        resp.rt = []
        checkL1.setColor([1,1,1], colorSpace='rgb')
        checkL1.setOpacity(1)
        checkL1.setPos((0, 0))
        checkL1.setSize((2, 1))
        checkL1.setOri(0)
        checkL1.setImage('check2.png')
        checkL1.setMask('None')
        checkR1.setColor([1,1,1], colorSpace='rgb')
        checkR1.setOpacity(1)
        checkR1.setPos((0, 0))
        checkR1.setSize((2, 1))
        checkR1.setOri(0)
        checkR1.setImage('check3.png')
        checkR1.setMask('None')
        # keep track of which components have finished
        Choice2GainComponents = [blank, ChoicePic2, resp, checkL1, checkR1]
        for thisComponent in Choice2GainComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        Choice2GainClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        continueRoutine = True
        
        # -------Run Routine "Choice2Gain"-------
        while continueRoutine:
            # get current time
            t = Choice2GainClock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=Choice2GainClock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *blank* updates
            if blank.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                blank.frameNStart = frameN  # exact frame index
                blank.tStart = t  # local t and not account for scr refresh
                blank.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(blank, 'tStartRefresh')  # time at next scr refresh
                blank.setAutoDraw(True)
            if blank.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > blank.tStartRefresh + 2-frameTolerance:
                    # keep track of stop time/frame for later
                    blank.tStop = t  # not accounting for scr refresh
                    blank.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(blank, 'tStopRefresh')  # time at next scr refresh
                    blank.setAutoDraw(False)
            
            # *ChoicePic2* updates
            if ChoicePic2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                ChoicePic2.frameNStart = frameN  # exact frame index
                ChoicePic2.tStart = t  # local t and not account for scr refresh
                ChoicePic2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(ChoicePic2, 'tStartRefresh')  # time at next scr refresh
                ChoicePic2.setAutoDraw(True)
            if ChoicePic2.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > ChoicePic2.tStartRefresh + 2-frameTolerance:
                    # keep track of stop time/frame for later
                    ChoicePic2.tStop = t  # not accounting for scr refresh
                    ChoicePic2.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(ChoicePic2, 'tStopRefresh')  # time at next scr refresh
                    ChoicePic2.setAutoDraw(False)
            
            # *resp* updates
            waitOnFlip = False
            if resp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                resp.frameNStart = frameN  # exact frame index
                resp.tStart = t  # local t and not account for scr refresh
                resp.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(resp, 'tStartRefresh')  # time at next scr refresh
                resp.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(resp.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
            if resp.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > resp.tStartRefresh + 2-frameTolerance:
                    # keep track of stop time/frame for later
                    resp.tStop = t  # not accounting for scr refresh
                    resp.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(resp, 'tStopRefresh')  # time at next scr refresh
                    resp.status = FINISHED
            if resp.status == STARTED and not waitOnFlip:
                theseKeys = resp.getKeys(keyList=['left', 'right'], waitRelease=False)
                if len(theseKeys):
                    theseKeys = theseKeys[0]  # at least one key was pressed
                    
                    # check for quit:
                    if "escape" == theseKeys:
                        endExpNow = True
                    resp.keys = theseKeys.name  # just the last key pressed
                    resp.rt = theseKeys.rt
            
            # *checkL1* updates
            if checkL1.status == NOT_STARTED and resp.keys == 'left':
                # keep track of start time/frame for later
                checkL1.frameNStart = frameN  # exact frame index
                checkL1.tStart = t  # local t and not account for scr refresh
                checkL1.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(checkL1, 'tStartRefresh')  # time at next scr refresh
                checkL1.setAutoDraw(True)
            if checkL1.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > checkL1.tStartRefresh + 1-frameTolerance:
                    # keep track of stop time/frame for later
                    checkL1.tStop = t  # not accounting for scr refresh
                    checkL1.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(checkL1, 'tStopRefresh')  # time at next scr refresh
                    checkL1.setAutoDraw(False)
            
            # *checkR1* updates
            if checkR1.status == NOT_STARTED and resp.keys == 'right':
                # keep track of start time/frame for later
                checkR1.frameNStart = frameN  # exact frame index
                checkR1.tStart = t  # local t and not account for scr refresh
                checkR1.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(checkR1, 'tStartRefresh')  # time at next scr refresh
                checkR1.setAutoDraw(True)
            if checkR1.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > checkR1.tStartRefresh + 1-frameTolerance:
                    # keep track of stop time/frame for later
                    checkR1.tStop = t  # not accounting for scr refresh
                    checkR1.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(checkR1, 'tStopRefresh')  # time at next scr refresh
                    checkR1.setAutoDraw(False)
            checkL1.autoLog=False
            checkR1.autoLog=False
            
            
            if resp.keys == 'left':
                checkL1.autoDraw=True
            
            
            if resp.keys == 'right':
                checkR1.autoDraw=True
            
            
            if blank.status == FINISHED:
                checkR1.autoDraw=False
                checkL1.autoDraw=False
                continueRoutine=False
            
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in Choice2GainComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "Choice2Gain"-------
        for thisComponent in Choice2GainComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        trials.addData('blank.started', blank.tStartRefresh)
        trials.addData('blank.stopped', blank.tStopRefresh)
        trials.addData('ChoicePic2.started', ChoicePic2.tStartRefresh)
        trials.addData('ChoicePic2.stopped', ChoicePic2.tStopRefresh)
        # check responses
        if resp.keys in ['', [], None]:  # No response was made
            resp.keys = None
        trials.addData('resp.keys',resp.keys)
        if resp.keys != None:  # we had a response
            trials.addData('resp.rt', resp.rt)
        trials.addData('resp.started', resp.tStartRefresh)
        trials.addData('resp.stopped', resp.tStopRefresh)
        trials.addData('checkL1.started', checkL1.tStartRefresh)
        trials.addData('checkL1.stopped', checkL1.tStopRefresh)
        trials.addData('checkR1.started', checkR1.tStartRefresh)
        trials.addData('checkR1.stopped', checkR1.tStopRefresh)
        checkL1.autoLog=False
        checkR1.autoLog=False
        
        
        
        if resp.keys == 'left':
            checkL1.autoDraw=True
        
        
        if resp.keys =='right':
            checkR1.autoDraw=True
        
        
        if blank.status == FINISHED:
            checkR1.autoDraw=False
            checkL1.autoDraw=False
        
        #trials.addData('nGamble', nGamble)
        if resp.keys == 'right':
            nGamble += 1
        
        
        if followAd == 'risk' and resp.keys == 'right':
            adFollow += 1
            
        
        
        
        # the Routine "Choice2Gain" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        thisExp.nextEntry()
        
    # completed 1 repeats of 'trials'
    
    
    # ------Prepare to start Routine "Feedback"-------
    # update component parameters for each repeat
    import random
    
    nGam = str(nGamble)
    print('nGam')
    gamAdvRisk = str(gamAdRisk)
    advFollow = str(adFollow)
    
    
    GamblePercent = [20, 25, 30, 35, 40, 45, 50, 60, 65, 70, 75, 80, 85, 90, 95]
    randomGam = random.choice(GamblePercent)
    if nGam=='0':
        GamblePer = '0'
    else:
        GamblePer = str(randomGam)
    endText.setColor('white', colorSpace='rgb')
    endText.setPos((-0.06, 0))
    endText.setText(text2 + " told you to gamble " + gamAdvRisk + " times. \n \n" 

"You followed their advice to gamble " + advFollow + " times. \n \n"


"You gambled " + nGam + " times. \n \n"


"You won the gambles " + GamblePer + "% of the time. \n \n"


"Please press enter to move on to the next block of trials. \n")
    endText.setFont('Arial')
    endText.setHeight(0.05)
    key_resp_2.keys = []
    key_resp_2.rt = []
    # keep track of which components have finished
    FeedbackComponents = [endText, key_resp_2]
    for thisComponent in FeedbackComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    FeedbackClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    continueRoutine = True
    
    # -------Run Routine "Feedback"-------
    while continueRoutine:
        # get current time
        t = FeedbackClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=FeedbackClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        #import random
        
        
        #GamblePercent = [20, 25, 30, 35, 40, 45, 50, 60, 65, 70, 75, 80, 85, 90, 95]
        #randomGam = random.choice(GamblePercent)
        #GamblePer = str(randomGam)
        
        # *endText* updates
        if endText.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            endText.frameNStart = frameN  # exact frame index
            endText.tStart = t  # local t and not account for scr refresh
            endText.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(endText, 'tStartRefresh')  # time at next scr refresh
            endText.setAutoDraw(True)
        
        # *key_resp_2* updates
        waitOnFlip = False
        if key_resp_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            key_resp_2.frameNStart = frameN  # exact frame index
            key_resp_2.tStart = t  # local t and not account for scr refresh
            key_resp_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_resp_2, 'tStartRefresh')  # time at next scr refresh
            key_resp_2.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_resp_2.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(key_resp_2.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if key_resp_2.status == STARTED and not waitOnFlip:
            theseKeys = key_resp_2.getKeys(keyList=['return'], waitRelease=False)
            if len(theseKeys):
                theseKeys = theseKeys[0]  # at least one key was pressed
                
                # check for quit:
                if "escape" == theseKeys:
                    endExpNow = True
                key_resp_2.keys = theseKeys.name  # just the last key pressed
                key_resp_2.rt = theseKeys.rt
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in FeedbackComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "Feedback"-------
    for thisComponent in FeedbackComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    trials_2.addData('endText.started', endText.tStartRefresh)
    trials_2.addData('endText.stopped', endText.tStopRefresh)
    # check responses
    if key_resp_2.keys in ['', [], None]:  # No response was made
        key_resp_2.keys = None
    trials_2.addData('key_resp_2.keys',key_resp_2.keys)
    if key_resp_2.keys != None:  # we had a response
        trials_2.addData('key_resp_2.rt', key_resp_2.rt)
    trials_2.addData('key_resp_2.started', key_resp_2.tStartRefresh)
    trials_2.addData('key_resp_2.stopped', key_resp_2.tStopRefresh)
    nGamble=0
    gamAdRisk=0
    gamAdSafe=0
    adFollow=0
    
    
    # the Routine "Feedback" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 10 repeats of 'trials_2'


# ------Prepare to start Routine "Ending"-------
# update component parameters for each repeat
# keep track of which components have finished
EndingComponents = [Ending_]
for thisComponent in EndingComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
EndingClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1
continueRoutine = True

# -------Run Routine "Ending"-------
while continueRoutine:
    # get current time
    t = EndingClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=EndingClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *Ending_* updates
    if Ending_.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        Ending_.frameNStart = frameN  # exact frame index
        Ending_.tStart = t  # local t and not account for scr refresh
        Ending_.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Ending_, 'tStartRefresh')  # time at next scr refresh
        Ending_.setAutoDraw(True)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in EndingComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "Ending"-------
for thisComponent in EndingComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('Ending_.started', Ending_.tStartRefresh)
thisExp.addData('Ending_.stopped', Ending_.tStopRefresh)
# the Routine "Ending" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# Flip one final time so any remaining win.callOnFlip() 
# and win.timeOnFlip() tasks get executed before quitting
win.flip()

# these shouldn't be strictly necessary (should auto-save)
thisExp.saveAsWideText(filename+'.csv')
thisExp.saveAsPickle(filename)
logging.flush()
# make sure everything is closed down
thisExp.abort()  # or data files will save again on exit
win.close()
core.quit()
