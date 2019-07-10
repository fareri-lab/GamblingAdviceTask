#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v3.1.2),
    on July 02, 2019, at 13:13
If you publish work using this script please cite the PsychoPy publications:
    Peirce, JW (2007) PsychoPy - Psychophysics software in Python.
        Journal of Neuroscience Methods, 162(1-2), 8-13.
    Peirce, JW (2009) Generating stimuli for neuroscience using PsychoPy.
        Frontiers in Neuroinformatics, 2:10. doi: 10.3389/neuro.11.010.2008
"""

from __future__ import absolute_import, division
from psychopy import locale_setup, sound, gui, visual, core, data, event, logging, clock
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
psychopyVersion = '3.1.2'
expName = 'Test'  # from the Builder filename that created this script
expInfo = {'participant': '', 'session': '001'}
dlg = gui.DlgFromDict(dictionary=expInfo, sortKeys=False, title=expName)
if dlg.OK == False:
    core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName
expInfo['psychopyVersion'] = psychopyVersion

# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
filename = _thisDir + os.sep + u'data/%s_%s_%s' % (expInfo['participant'], expName, expInfo['date'])

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='', extraInfo=expInfo, runtimeInfo=None, originPath='C:\\Users\\farerilab\\Downloads\\GamblingAdviceTask\\Test_lastrun.py', savePickle=True, saveWideText=True, dataFileName=filename)
# save a log file for detail verbose info
logFile = logging.LogFile(filename+'.log', level=logging.EXP)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp

# Start Code - component code to be run before the window creation

# Setup the Window
win = visual.Window(
    size=[1536, 864], fullscr=True, screen=0, winType='pyglet', allowGUI=False, allowStencil=False, monitor='testMonitor', color=[-1,-1,-1], colorSpace='rgb', blendMode='avg', useFBO=True, units='height')
# store frame rate of monitor if we can measure it
expInfo['frameRate'] = win.getActualFrameRate()
if expInfo['frameRate'] != None:
    frameDur = 1.0 / round(expInfo['frameRate'])
else:
    frameDur = 1.0 / 60.0  # could not measure, so guess

# create a default keyboard (e.g. to check for escape)
defaultKeyboard = keyboard.Keyboard()

# Initialize components for Routine "ISI"
ISIClock = core.Clock()
iSi = visual.TextStim(win=win, name='iSi', text='+', font='Arial', pos=(0, 0), height=0.08, wrapWidth=None, ori=0, color='white', colorSpace='rgb', opacity=1, languageStyle='LTR', depth=0.0);

# Initialize components for Routine "Receive_money"
Receive_moneyClock = core.Clock()
receive = visual.TextStim(win=win, name='receive', text='RECEIVE  $100', font='Arial', pos=(0.0, 0), height=0.1, wrapWidth=None, ori=0, color='white', colorSpace='rgb', opacity=1, languageStyle='LTR', depth=0.0);
ISI2 = visual.TextStim(win=win, name='ISI2', text='+', font='Arial', pos=(0, 0), height=0.08, wrapWidth=None, ori=0, color='white', colorSpace='rgb', opacity=1, languageStyle='LTR', depth=-1.0);

# Initialize components for Routine "pi_2"
pi_2Clock = core.Clock()
image_4 = visual.ImageStim(win=win, name='image_4', image='20.png', mask=None, ori=0, pos=(0.32, 0.06), size=(1.39, 0.73), color=[1,1,1], colorSpace='rgb', opacity=1, flipHoriz=False, flipVert=False, texRes=128, interpolate=True, depth=0.0)
polygon = visual.Line( win=win, name='polygon', start=(-(15, 0)[0]/2.0, 0), end=(+(15, 0)[0]/2.0, 0), ori=90, pos=(-0.15, 0), lineWidth=5, lineColor=[1,1,1], lineColorSpace='rgb', fillColor=[1,1,1], fillColorSpace='rgb', opacity=1, depth=-1.0, interpolate=True)
text = visual.TextStim(win=win, name='text', text='KEEP\n $80 ', font='Arial', pos=(-0.45, -0.02), height=0.12, wrapWidth=None, ori=0, color='white', colorSpace='rgb', opacity=1, languageStyle='LTR', depth=-2.0);
gamble = visual.TextStim(win=win, name='gamble', text='GAMBLE', font='Arial', pos=(0.32, 0.05), height=0.12, wrapWidth=None, ori=0, color='white', colorSpace='rgb', opacity=1, languageStyle='LTR', depth=-3.0);
greenRec = visual.Rect(win=win, name='greenRec',width=(0.08, 0.04)[0], height=(0.08, 0.04)[1], ori=0, pos=(0.47, -0.37),lineWidth=1, lineColor=[-1.000,-1.000,-1.000], lineColorSpace='rgb', fillColor=[-1.000,0.184,-1.000], fillColorSpace='rgb',    opacity=1, depth=-4.0, interpolate=True)
redRec = visual.Rect( win=win, name='redRec', width=(0.08, 0.04)[0], height=(0.08, 0.04)[1],ori=0, pos=(0.47, -0.42), lineWidth=1, lineColor=[-1.000,-1.000,-1.000], lineColorSpace='rgb', fillColor=[1.000,-1.000,-1.000], fillColorSpace='rgb', opacity=1, depth=-5.0, interpolate=True)
keepAll = visual.TextStim(win=win, name='keepAll', text='keep all', font='Arial', pos=(0.6, -0.37), height=0.035, wrapWidth=None, ori=0, color='white', colorSpace='rgb', opacity=1, languageStyle='LTR',depth=-6.0);
loseAll = visual.TextStim(win=win, name='loseAll',text='lose all', font='Arial', pos=(0.6, -0.41), height=0.035, wrapWidth=None, ori=0, color='white', colorSpace='rgb', opacity=1, languageStyle='LTR', depth=-7.0);

# Initialize components for Routine "askAd"
askAdClock = core.Clock()
ask = visual.TextStim(win=win, name='ask',
    text='Would you like to hear advice from your financial advisor?',
    font='Arial',
    pos=(0, 0.11), height=0.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
text_3 = visual.TextStim(win=win, name='text_3',
    text='Y                 N',
    font='Arial',
    pos=(0, -0.2), height=0.09, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
Advice = visual.TextStim(win=win, name='Advice',
    text='Advisor 1 Says\n\n"Go with the safe option here!"',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-4.0);

# Initialize components for Routine "code_2"
code_2Clock = core.Clock()
nRepsblock1=0
nRepsblock2=0

# Initialize components for Routine "trial"
trialClock = core.Clock()
image = visual.ImageStim(
    win=win,
    name='image', 
    image='sin', mask=None,
    ori=1.0, pos=[0,0], size=1.0,
    color=[1,1,1], colorSpace='rgb', opacity=1.0,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)

# Initialize components for Routine "loseTrial"
loseTrialClock = core.Clock()
image_2 = visual.ImageStim(
    win=win,
    name='image_2', 
    image='sin', mask=None,
    ori=1.0, pos=[0,0], size=1.0,
    color=[1,1,1], colorSpace='rgb', opacity=1.0,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

# ------Prepare to start Routine "ISI"-------
t = 0
ISIClock.reset()  # clock
frameN = -1
continueRoutine = True
routineTimer.add(3.000000)
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

# -------Start Routine "ISI"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = ISIClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *iSi* updates
    if t >= 0.0 and iSi.status == NOT_STARTED:
        # keep track of start time/frame for later
        iSi.tStart = t  # not accounting for scr refresh
        iSi.frameNStart = frameN  # exact frame index
        win.timeOnFlip(iSi, 'tStartRefresh')  # time at next scr refresh
        iSi.setAutoDraw(True)
    frameRemains = 0.0 + 3- win.monitorFramePeriod * 0.75  # most of one frame period left
    if iSi.status == STARTED and t >= frameRemains:
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
thisExp.addData('iSi.started', iSi.tStartRefresh)
thisExp.addData('iSi.stopped', iSi.tStopRefresh)

# ------Prepare to start Routine "Receive_money"-------
t = 0
Receive_moneyClock.reset()  # clock
frameN = -1
continueRoutine = True
routineTimer.add(4.000000)
# update component parameters for each repeat
# keep track of which components have finished
Receive_moneyComponents = [receive, ISI2]
for thisComponent in Receive_moneyComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "Receive_money"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = Receive_moneyClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *receive* updates
    if t >= 0.0 and receive.status == NOT_STARTED:
        # keep track of start time/frame for later
        receive.tStart = t  # not accounting for scr refresh
        receive.frameNStart = frameN  # exact frame index
        win.timeOnFlip(receive, 'tStartRefresh')  # time at next scr refresh
        receive.setAutoDraw(True)
    frameRemains = 0.0 + 2- win.monitorFramePeriod * 0.75  # most of one frame period left
    if receive.status == STARTED and t >= frameRemains:
        # keep track of stop time/frame for later
        receive.tStop = t  # not accounting for scr refresh
        receive.frameNStop = frameN  # exact frame index
        win.timeOnFlip(receive, 'tStopRefresh')  # time at next scr refresh
        receive.setAutoDraw(False)
    
    # *ISI2* updates
    if t >= 2 and ISI2.status == NOT_STARTED:
        # keep track of start time/frame for later
        ISI2.tStart = t  # not accounting for scr refresh
        ISI2.frameNStart = frameN  # exact frame index
        win.timeOnFlip(ISI2, 'tStartRefresh')  # time at next scr refresh
        ISI2.setAutoDraw(True)
    frameRemains = 2 + 2- win.monitorFramePeriod * 0.75  # most of one frame period left
    if ISI2.status == STARTED and t >= frameRemains:
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
thisExp.addData('receive.started', receive.tStartRefresh)
thisExp.addData('receive.stopped', receive.tStopRefresh)
thisExp.addData('ISI2.started', ISI2.tStartRefresh)
thisExp.addData('ISI2.stopped', ISI2.tStopRefresh)

# ------Prepare to start Routine "pi_2"-------
t = 0
pi_2Clock.reset()  # clock
frameN = -1
continueRoutine = True
routineTimer.add(3.000000)
# update component parameters for each repeat
# keep track of which components have finished
pi_2Components = [image_4, polygon, text, gamble, greenRec, redRec, keepAll, loseAll]
for thisComponent in pi_2Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "pi_2"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = pi_2Clock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *image_4* updates
    if t >= 0.0 and image_4.status == NOT_STARTED:
        # keep track of start time/frame for later
        image_4.tStart = t  # not accounting for scr refresh
        image_4.frameNStart = frameN  # exact frame index
        win.timeOnFlip(image_4, 'tStartRefresh')  # time at next scr refresh
        image_4.setAutoDraw(True)
    frameRemains = 0.0 + 3- win.monitorFramePeriod * 0.75  # most of one frame period left
    if image_4.status == STARTED and t >= frameRemains:
        # keep track of stop time/frame for later
        image_4.tStop = t  # not accounting for scr refresh
        image_4.frameNStop = frameN  # exact frame index
        win.timeOnFlip(image_4, 'tStopRefresh')  # time at next scr refresh
        image_4.setAutoDraw(False)
    
    # *polygon* updates
    if t >= 0.0 and polygon.status == NOT_STARTED:
        # keep track of start time/frame for later
        polygon.tStart = t  # not accounting for scr refresh
        polygon.frameNStart = frameN  # exact frame index
        win.timeOnFlip(polygon, 'tStartRefresh')  # time at next scr refresh
        polygon.setAutoDraw(True)
    frameRemains = 0.0 + 3- win.monitorFramePeriod * 0.75  # most of one frame period left
    if polygon.status == STARTED and t >= frameRemains:
        # keep track of stop time/frame for later
        polygon.tStop = t  # not accounting for scr refresh
        polygon.frameNStop = frameN  # exact frame index
        win.timeOnFlip(polygon, 'tStopRefresh')  # time at next scr refresh
        polygon.setAutoDraw(False)
    
    # *text* updates
    if t >= 0.0 and text.status == NOT_STARTED:
        # keep track of start time/frame for later
        text.tStart = t  # not accounting for scr refresh
        text.frameNStart = frameN  # exact frame index
        win.timeOnFlip(text, 'tStartRefresh')  # time at next scr refresh
        text.setAutoDraw(True)
    frameRemains = 0.0 + 3- win.monitorFramePeriod * 0.75  # most of one frame period left
    if text.status == STARTED and t >= frameRemains:
        # keep track of stop time/frame for later
        text.tStop = t  # not accounting for scr refresh
        text.frameNStop = frameN  # exact frame index
        win.timeOnFlip(text, 'tStopRefresh')  # time at next scr refresh
        text.setAutoDraw(False)
    
    # *gamble* updates
    if t >= 0.0 and gamble.status == NOT_STARTED:
        # keep track of start time/frame for later
        gamble.tStart = t  # not accounting for scr refresh
        gamble.frameNStart = frameN  # exact frame index
        win.timeOnFlip(gamble, 'tStartRefresh')  # time at next scr refresh
        gamble.setAutoDraw(True)
    frameRemains = 0.0 + 3- win.monitorFramePeriod * 0.75  # most of one frame period left
    if gamble.status == STARTED and t >= frameRemains:
        # keep track of stop time/frame for later
        gamble.tStop = t  # not accounting for scr refresh
        gamble.frameNStop = frameN  # exact frame index
        win.timeOnFlip(gamble, 'tStopRefresh')  # time at next scr refresh
        gamble.setAutoDraw(False)
    
    # *greenRec* updates
    if t >= 0.0 and greenRec.status == NOT_STARTED:
        # keep track of start time/frame for later
        greenRec.tStart = t  # not accounting for scr refresh
        greenRec.frameNStart = frameN  # exact frame index
        win.timeOnFlip(greenRec, 'tStartRefresh')  # time at next scr refresh
        greenRec.setAutoDraw(True)
    frameRemains = 0.0 + 3- win.monitorFramePeriod * 0.75  # most of one frame period left
    if greenRec.status == STARTED and t >= frameRemains:
        # keep track of stop time/frame for later
        greenRec.tStop = t  # not accounting for scr refresh
        greenRec.frameNStop = frameN  # exact frame index
        win.timeOnFlip(greenRec, 'tStopRefresh')  # time at next scr refresh
        greenRec.setAutoDraw(False)
    
    # *redRec* updates
    if t >= 0.0 and redRec.status == NOT_STARTED:
        # keep track of start time/frame for later
        redRec.tStart = t  # not accounting for scr refresh
        redRec.frameNStart = frameN  # exact frame index
        win.timeOnFlip(redRec, 'tStartRefresh')  # time at next scr refresh
        redRec.setAutoDraw(True)
    frameRemains = 0.0 + 3- win.monitorFramePeriod * 0.75  # most of one frame period left
    if redRec.status == STARTED and t >= frameRemains:
        # keep track of stop time/frame for later
        redRec.tStop = t  # not accounting for scr refresh
        redRec.frameNStop = frameN  # exact frame index
        win.timeOnFlip(redRec, 'tStopRefresh')  # time at next scr refresh
        redRec.setAutoDraw(False)
    
    # *keepAll* updates
    if t >= 0.0 and keepAll.status == NOT_STARTED:
        # keep track of start time/frame for later
        keepAll.tStart = t  # not accounting for scr refresh
        keepAll.frameNStart = frameN  # exact frame index
        win.timeOnFlip(keepAll, 'tStartRefresh')  # time at next scr refresh
        keepAll.setAutoDraw(True)
    frameRemains = 0.0 + 3- win.monitorFramePeriod * 0.75  # most of one frame period left
    if keepAll.status == STARTED and t >= frameRemains:
        # keep track of stop time/frame for later
        keepAll.tStop = t  # not accounting for scr refresh
        keepAll.frameNStop = frameN  # exact frame index
        win.timeOnFlip(keepAll, 'tStopRefresh')  # time at next scr refresh
        keepAll.setAutoDraw(False)
    
    # *loseAll* updates
    if t >= 0.0 and loseAll.status == NOT_STARTED:
        # keep track of start time/frame for later
        loseAll.tStart = t  # not accounting for scr refresh
        loseAll.frameNStart = frameN  # exact frame index
        win.timeOnFlip(loseAll, 'tStartRefresh')  # time at next scr refresh
        loseAll.setAutoDraw(True)
    frameRemains = 0.0 + 3- win.monitorFramePeriod * 0.75  # most of one frame period left
    if loseAll.status == STARTED and t >= frameRemains:
        # keep track of stop time/frame for later
        loseAll.tStop = t  # not accounting for scr refresh
        loseAll.frameNStop = frameN  # exact frame index
        win.timeOnFlip(loseAll, 'tStopRefresh')  # time at next scr refresh
        loseAll.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in pi_2Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "pi_2"-------
for thisComponent in pi_2Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('image_4.started', image_4.tStartRefresh)
thisExp.addData('image_4.stopped', image_4.tStopRefresh)
thisExp.addData('polygon.started', polygon.tStartRefresh)
thisExp.addData('polygon.stopped', polygon.tStopRefresh)
thisExp.addData('text.started', text.tStartRefresh)
thisExp.addData('text.stopped', text.tStopRefresh)
thisExp.addData('gamble.started', gamble.tStartRefresh)
thisExp.addData('gamble.stopped', gamble.tStopRefresh)
thisExp.addData('greenRec.started', greenRec.tStartRefresh)
thisExp.addData('greenRec.stopped', greenRec.tStopRefresh)
thisExp.addData('redRec.started', redRec.tStartRefresh)
thisExp.addData('redRec.stopped', redRec.tStopRefresh)
thisExp.addData('keepAll.started', keepAll.tStartRefresh)
thisExp.addData('keepAll.stopped', keepAll.tStopRefresh)
thisExp.addData('loseAll.started', loseAll.tStartRefresh)
thisExp.addData('loseAll.stopped', loseAll.tStopRefresh)

# ------Prepare to start Routine "askAd"-------
t = 0
askAdClock.reset()  # clock
frameN = -1
continueRoutine = True
# update component parameters for each repeat
response = keyboard.Keyboard()
if response.keys == 'y':
    continueRoutine = True
elif response.keys == 'n':
    continueRoutine = False 
# keep track of which components have finished
askAdComponents = [ask, text_3, response, Advice]
for thisComponent in askAdComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "askAd"-------
while continueRoutine:
    # get current time
    t = askAdClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *ask* updates
    if t >= 0.0 and ask.status == NOT_STARTED:
        # keep track of start time/frame for later
        ask.tStart = t  # not accounting for scr refresh
        ask.frameNStart = frameN  # exact frame index
        win.timeOnFlip(ask, 'tStartRefresh')  # time at next scr refresh
        ask.setAutoDraw(True)
    
    # *text_3* updates
    if t >= 0.0 and text_3.status == NOT_STARTED:
        # keep track of start time/frame for later
        text_3.tStart = t  # not accounting for scr refresh
        text_3.frameNStart = frameN  # exact frame index
        win.timeOnFlip(text_3, 'tStartRefresh')  # time at next scr refresh
        text_3.setAutoDraw(True)
    
    # *response* updates
    if t >= 1 and response.status == NOT_STARTED:
        # keep track of start time/frame for later
        response.tStart = t  # not accounting for scr refresh
        response.frameNStart = frameN  # exact frame index
        win.timeOnFlip(response, 'tStartRefresh')  # time at next scr refresh
        response.status = STARTED
        # keyboard checking is just starting
        win.callOnFlip(response.clock.reset)  # t=0 on next screen flip
        response.clearEvents(eventType='keyboard')
    if response.status == STARTED:
        theseKeys = response.getKeys(keyList=['y', 'n'], waitRelease=False)
        if len(theseKeys):
            theseKeys = theseKeys[0]  # at least one key was pressed
            
            # check for quit:
            if "escape" == theseKeys:
                endExpNow = True
            response.keys = theseKeys.name  # just the last key pressed
            response.rt = theseKeys.rt
            # a response ends the routine
            continueRoutine = False
    
    # *Advice* updates
    if () and Advice.status == NOT_STARTED:
        # keep track of start time/frame for later
        Advice.tStart = t  # not accounting for scr refresh
        Advice.frameNStart = frameN  # exact frame index
        win.timeOnFlip(Advice, 'tStartRefresh')  # time at next scr refresh
        Advice.setAutoDraw(True)
    if Advice.status == STARTED and t >= (Advice.tStart + 3):
        # keep track of stop time/frame for later
        Advice.tStop = t  # not accounting for scr refresh
        Advice.frameNStop = frameN  # exact frame index
        win.timeOnFlip(Advice, 'tStopRefresh')  # time at next scr refresh
        Advice.setAutoDraw(False)
    
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
thisExp.addData('ask.started', ask.tStartRefresh)
thisExp.addData('ask.stopped', ask.tStopRefresh)
thisExp.addData('text_3.started', text_3.tStartRefresh)
thisExp.addData('text_3.stopped', text_3.tStopRefresh)
# check responses
if response.keys in ['', [], None]:  # No response was made
    response.keys = None
thisExp.addData('response.keys',response.keys)
if response.keys != None:  # we had a response
    thisExp.addData('response.rt', response.rt)
thisExp.addData('response.started', response.tStartRefresh)
thisExp.addData('response.stopped', response.tStopRefresh)
thisExp.nextEntry()
thisExp.addData('Advice.started', Advice.tStartRefresh)
thisExp.addData('Advice.stopped', Advice.tStopRefresh)
# the Routine "askAd" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
trials_3 = data.TrialHandler(nReps=1, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('ConditionsGain.xlsx'),
    seed=None, name='trials_3')
thisExp.addLoop(trials_3)  # add the loop to the experiment
thisTrial_3 = trials_3.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisTrial_3.rgb)
if thisTrial_3 != None:
    for paramName in thisTrial_3:
        exec('{} = thisTrial_3[paramName]'.format(paramName))

for thisTrial_3 in trials_3:
    currentLoop = trials_3
    # abbreviate parameter names if possible (e.g. rgb = thisTrial_3.rgb)
    if thisTrial_3 != None:
        for paramName in thisTrial_3:
            exec('{} = thisTrial_3[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "code_2"-------
    t = 0
    code_2Clock.reset()  # clock
    frameN = -1
    continueRoutine = True
    # update component parameters for each repeat
    if selectBlock==1:
     nRepsblock1=1
     nRepsblock2=0
    elif selectBlock==2:
     nRepsblock1=0
     nRepsblock2=1
    # keep track of which components have finished
    code_2Components = []
    for thisComponent in code_2Components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    # -------Start Routine "code_2"-------
    while continueRoutine:
        # get current time
        t = code_2Clock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in code_2Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "code_2"-------
    for thisComponent in code_2Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # the Routine "code_2" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # set up handler to look after randomisation of conditions etc
    trials = data.TrialHandler(nReps=nRepsblock1, method='random', 
        extraInfo=expInfo, originPath=-1,
        trialList=data.importConditions('ConditionsGain.xlsx'),
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
        
        # ------Prepare to start Routine "trial"-------
        t = 0
        trialClock.reset()  # clock
        frameN = -1
        continueRoutine = True
        routineTimer.add(4.000000)
        # update component parameters for each repeat
        image.setOpacity(1)
        image.setPos((0, 0))
        image.setSize((1.5, 1))
        image.setOri(0)
        image.setImage(Gain)
        # keep track of which components have finished
        trialComponents = [image]
        for thisComponent in trialComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        
        # -------Start Routine "trial"-------
        while continueRoutine and routineTimer.getTime() > 0:
            # get current time
            t = trialClock.getTime()
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *image* updates
            if t >= 0.0 and image.status == NOT_STARTED:
                # keep track of start time/frame for later
                image.tStart = t  # not accounting for scr refresh
                image.frameNStart = frameN  # exact frame index
                win.timeOnFlip(image, 'tStartRefresh')  # time at next scr refresh
                image.setAutoDraw(True)
            frameRemains = 0.0 + 4- win.monitorFramePeriod * 0.75  # most of one frame period left
            if image.status == STARTED and t >= frameRemains:
                # keep track of stop time/frame for later
                image.tStop = t  # not accounting for scr refresh
                image.frameNStop = frameN  # exact frame index
                win.timeOnFlip(image, 'tStopRefresh')  # time at next scr refresh
                image.setAutoDraw(False)
            
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
        trials.addData('image.started', image.tStartRefresh)
        trials.addData('image.stopped', image.tStopRefresh)
        thisExp.nextEntry()
        
    # completed nRepsblock1 repeats of 'trials'
    
    
    # set up handler to look after randomisation of conditions etc
    trials_2 = data.TrialHandler(nReps=nRepsblock2, method='random', 
        extraInfo=expInfo, originPath=-1,
        trialList=data.importConditions('ConditionsGain.xlsx'),
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
        
        # ------Prepare to start Routine "loseTrial"-------
        t = 0
        loseTrialClock.reset()  # clock
        frameN = -1
        continueRoutine = True
        routineTimer.add(4.000000)
        # update component parameters for each repeat
        image_2.setOpacity(1)
        image_2.setPos((0, 0))
        image_2.setSize((1.5, 1))
        image_2.setOri(0)
        image_2.setImage(Loss)
        # keep track of which components have finished
        loseTrialComponents = [image_2]
        for thisComponent in loseTrialComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        
        # -------Start Routine "loseTrial"-------
        while continueRoutine and routineTimer.getTime() > 0:
            # get current time
            t = loseTrialClock.getTime()
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *image_2* updates
            if t >= 0.0 and image_2.status == NOT_STARTED:
                # keep track of start time/frame for later
                image_2.tStart = t  # not accounting for scr refresh
                image_2.frameNStart = frameN  # exact frame index
                win.timeOnFlip(image_2, 'tStartRefresh')  # time at next scr refresh
                image_2.setAutoDraw(True)
            frameRemains = 0.0 + 4- win.monitorFramePeriod * 0.75  # most of one frame period left
            if image_2.status == STARTED and t >= frameRemains:
                # keep track of stop time/frame for later
                image_2.tStop = t  # not accounting for scr refresh
                image_2.frameNStop = frameN  # exact frame index
                win.timeOnFlip(image_2, 'tStopRefresh')  # time at next scr refresh
                image_2.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in loseTrialComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "loseTrial"-------
        for thisComponent in loseTrialComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        trials_2.addData('image_2.started', image_2.tStartRefresh)
        trials_2.addData('image_2.stopped', image_2.tStopRefresh)
        thisExp.nextEntry()
        
    # completed nRepsblock2 repeats of 'trials_2'
    
    thisExp.nextEntry()
    
# completed 1 repeats of 'trials_3'


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
