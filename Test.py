#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v3.1.2),
    on July 02, 2019, at 15:31
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
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath='C:\\Users\\farerilab\\Downloads\\GamblingAdviceTask\\Test.py',
    savePickle=True, saveWideText=True,
    dataFileName=filename)
# save a log file for detail verbose info
logFile = logging.LogFile(filename+'.log', level=logging.EXP)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp

# Start Code - component code to be run before the window creation

# Setup the Window
win = visual.Window(
    size=[1536, 864], fullscr=True, screen=0, 
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

# Initialize components for Routine "code_2"
code_2Clock = core.Clock()
nRepsblock1=0
nRepsblock2=0

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
receive = visual.TextStim(win=win, name='receive',
    text='default text',
    font='Arial',
    pos=[0,0], height=1.0, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
ISI2 = visual.TextStim(win=win, name='ISI2',
    text='+',
    font='Arial',
    pos=(0, 0), height=0.08, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);

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

# Initialize components for Routine "askAd"
askAdClock = core.Clock()
text_3 = visual.TextStim(win=win, name='text_3',
    text='Y                 N',
    font='Arial',
    pos=(0, -0.2), height=0.09, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
ask = visual.TextStim(win=win, name='ask',
    text='Would you like to hear advice from your financial advisor?',
    font='Arial',
    pos=(0, 0.11), height=0.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
Advice = visual.TextStim(win=win, name='Advice',
    text='default text',
    font='Arial',
    pos=[0,0], height=1.0, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-4.0);

# Initialize components for Routine "Choice2Gain"
Choice2GainClock = core.Clock()
image_5 = visual.ImageStim(
    win=win,
    name='image_5', 
    image='sin', mask=None,
    ori=1.0, pos=[0,0], size=1.0,
    color=[1,1,1], colorSpace='rgb', opacity=1.0,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)
polygon_2 = visual.Line(
    win=win, name='polygon_2',
    start=(-[1.0, 1.0][0]/2.0, 0), end=(+[1.0, 1.0][0]/2.0, 0),
    ori=1.0, pos=[0,0],
    lineWidth=6, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=[1,1,1], fillColorSpace='rgb',
    opacity=1.0, depth=-2.0, interpolate=True)
checkL = visual.ImageStim(win=win, pos=(-0.19, 0), size= (0.25, 0.25) )
checkL.setImage('check.png')
checkR = visual.ImageStim(win=win, pos=(0.19, 0), size= (0.25, 0.25) )
checkR.setImage('check.png')

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
receive = visual.TextStim(win=win, name='receive',
    text='default text',
    font='Arial',
    pos=[0,0], height=1.0, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
ISI2 = visual.TextStim(win=win, name='ISI2',
    text='+',
    font='Arial',
    pos=(0, 0), height=0.08, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);

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

# Initialize components for Routine "askAd"
askAdClock = core.Clock()
text_3 = visual.TextStim(win=win, name='text_3',
    text='Y                 N',
    font='Arial',
    pos=(0, -0.2), height=0.09, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
ask = visual.TextStim(win=win, name='ask',
    text='Would you like to hear advice from your financial advisor?',
    font='Arial',
    pos=(0, 0.11), height=0.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
Advice = visual.TextStim(win=win, name='Advice',
    text='default text',
    font='Arial',
    pos=[0,0], height=1.0, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-4.0);

# Initialize components for Routine "Choice2Loss"
Choice2LossClock = core.Clock()
image_3 = visual.ImageStim(
    win=win,
    name='image_3', 
    image='sin', mask=None,
    ori=1.0, pos=[0,0], size=1.0,
    color=[1,1,1], colorSpace='rgb', opacity=1.0,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

# set up handler to look after randomisation of conditions etc
trials_4 = data.TrialHandler(nReps=1, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('ConditionsGain.csv'),
    seed=None, name='trials_4')
thisExp.addLoop(trials_4)  # add the loop to the experiment
thisTrial_4 = trials_4.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisTrial_4.rgb)
if thisTrial_4 != None:
    for paramName in thisTrial_4:
        exec('{} = thisTrial_4[paramName]'.format(paramName))

for thisTrial_4 in trials_4:
    currentLoop = trials_4
    # abbreviate parameter names if possible (e.g. rgb = thisTrial_4.rgb)
    if thisTrial_4 != None:
        for paramName in thisTrial_4:
            exec('{} = thisTrial_4[paramName]'.format(paramName))
    
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
    trials_5 = data.TrialHandler(nReps=nRepsblock1, method='sequential', 
        extraInfo=expInfo, originPath=-1,
        trialList=data.importConditions('ConditionsGain.csv'),
        seed=None, name='trials_5')
    thisExp.addLoop(trials_5)  # add the loop to the experiment
    thisTrial_5 = trials_5.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisTrial_5.rgb)
    if thisTrial_5 != None:
        for paramName in thisTrial_5:
            exec('{} = thisTrial_5[paramName]'.format(paramName))
    
    for thisTrial_5 in trials_5:
        currentLoop = trials_5
        # abbreviate parameter names if possible (e.g. rgb = thisTrial_5.rgb)
        if thisTrial_5 != None:
            for paramName in thisTrial_5:
                exec('{} = thisTrial_5[paramName]'.format(paramName))
        
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
        trials_5.addData('iSi.started', iSi.tStartRefresh)
        trials_5.addData('iSi.stopped', iSi.tStopRefresh)
        
        # ------Prepare to start Routine "Receive_money"-------
        t = 0
        Receive_moneyClock.reset()  # clock
        frameN = -1
        continueRoutine = True
        routineTimer.add(4.000000)
        # update component parameters for each repeat
        receive.setColor('white', colorSpace='rgb')
        receive.setPos((0.0, 0))
        receive.setText(Amount)
        receive.setFont('Arial')
        receive.setHeight(0.1)
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
        trials_5.addData('receive.started', receive.tStartRefresh)
        trials_5.addData('receive.stopped', receive.tStopRefresh)
        trials_5.addData('ISI2.started', ISI2.tStartRefresh)
        trials_5.addData('ISI2.stopped', ISI2.tStopRefresh)
        
        # ------Prepare to start Routine "trial"-------
        t = 0
        trialClock.reset()  # clock
        frameN = -1
        continueRoutine = True
        routineTimer.add(4.000000)
        # update component parameters for each repeat
        image.setOpacity(1)
        image.setPos((0, 0))
        image.setSize((1.3, 0.9))
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
        trials_5.addData('image.started', image.tStartRefresh)
        trials_5.addData('image.stopped', image.tStopRefresh)
        
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
        Advice.setColor('white', colorSpace='rgb')
        Advice.setPos((0, 0))
        Advice.setText('Advisor 1 says\n\n"Go with the safe option here!"')
        Advice.setFont('Arial')
        Advice.setHeight(0.08)
        # keep track of which components have finished
        askAdComponents = [text_3, ask, response, Advice]
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
            
            # *text_3* updates
            if t >= 0.0 and text_3.status == NOT_STARTED:
                # keep track of start time/frame for later
                text_3.tStart = t  # not accounting for scr refresh
                text_3.frameNStart = frameN  # exact frame index
                win.timeOnFlip(text_3, 'tStartRefresh')  # time at next scr refresh
                text_3.setAutoDraw(True)
            if text_3.status == STARTED and bool(Advice.status==STARTED):
                # keep track of stop time/frame for later
                text_3.tStop = t  # not accounting for scr refresh
                text_3.frameNStop = frameN  # exact frame index
                win.timeOnFlip(text_3, 'tStopRefresh')  # time at next scr refresh
                text_3.setAutoDraw(False)
            
            # *ask* updates
            if t >= 0.0 and ask.status == NOT_STARTED:
                # keep track of start time/frame for later
                ask.tStart = t  # not accounting for scr refresh
                ask.frameNStart = frameN  # exact frame index
                win.timeOnFlip(ask, 'tStartRefresh')  # time at next scr refresh
                ask.setAutoDraw(True)
            if ask.status == STARTED and bool(Advice.status==STARTED):
                # keep track of stop time/frame for later
                ask.tStop = t  # not accounting for scr refresh
                ask.frameNStop = frameN  # exact frame index
                win.timeOnFlip(ask, 'tStopRefresh')  # time at next scr refresh
                ask.setAutoDraw(False)
            
            # *response* updates
            if t >= 0.0 and response.status == NOT_STARTED:
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
            
            # *Advice* updates
            if (response.keys=='y') and Advice.status == NOT_STARTED:
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
        trials_5.addData('text_3.started', text_3.tStartRefresh)
        trials_5.addData('text_3.stopped', text_3.tStopRefresh)
        trials_5.addData('ask.started', ask.tStartRefresh)
        trials_5.addData('ask.stopped', ask.tStopRefresh)
        # check responses
        if response.keys in ['', [], None]:  # No response was made
            response.keys = None
        trials_5.addData('response.keys',response.keys)
        if response.keys != None:  # we had a response
            trials_5.addData('response.rt', response.rt)
        trials_5.addData('response.started', response.tStartRefresh)
        trials_5.addData('response.stopped', response.tStopRefresh)
        trials_5.addData('Advice.started', Advice.tStartRefresh)
        trials_5.addData('Advice.stopped', Advice.tStopRefresh)
        # the Routine "askAd" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # ------Prepare to start Routine "Choice2Gain"-------
        t = 0
        Choice2GainClock.reset()  # clock
        frameN = -1
        continueRoutine = True
        routineTimer.add(6.000000)
        # update component parameters for each repeat
        image_5.setOpacity(1)
        image_5.setPos((0, 0))
        image_5.setSize((1.3, 0.9))
        image_5.setOri(0)
        image_5.setImage(Gains2)
        resp = keyboard.Keyboard()
        polygon_2.setOpacity(1)
        polygon_2.setPos((-0.13, 0))
        polygon_2.setSize((1, 55))
        polygon_2.setOri(90)
        polygon_2.setLineWidth(6)
        if resp.keys == 'left':
            checkL.autoDraw=True
        elif resp.keys == 'right':
                checkR.autoDraw=False
        
        if resp.keys =='right':
            checkR.autoDraw=True
        elif resp.keys == 'left':
                checkL.autoDraw=False
        
        if polygon_2.status == FINISHED:
            checkL.autoDraw = False
        
        if polygon_2.status==FINISHED:
            checkR.autoDraw = False 
        # keep track of which components have finished
        Choice2GainComponents = [image_5, resp, polygon_2]
        for thisComponent in Choice2GainComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        
        # -------Start Routine "Choice2Gain"-------
        while continueRoutine and routineTimer.getTime() > 0:
            # get current time
            t = Choice2GainClock.getTime()
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *image_5* updates
            if t >= 0.0 and image_5.status == NOT_STARTED:
                # keep track of start time/frame for later
                image_5.tStart = t  # not accounting for scr refresh
                image_5.frameNStart = frameN  # exact frame index
                win.timeOnFlip(image_5, 'tStartRefresh')  # time at next scr refresh
                image_5.setAutoDraw(True)
            frameRemains = 0.0 + 4- win.monitorFramePeriod * 0.75  # most of one frame period left
            if image_5.status == STARTED and t >= frameRemains:
                # keep track of stop time/frame for later
                image_5.tStop = t  # not accounting for scr refresh
                image_5.frameNStop = frameN  # exact frame index
                win.timeOnFlip(image_5, 'tStopRefresh')  # time at next scr refresh
                image_5.setAutoDraw(False)
            
            # *resp* updates
            if t >= 0.0 and resp.status == NOT_STARTED:
                # keep track of start time/frame for later
                resp.tStart = t  # not accounting for scr refresh
                resp.frameNStart = frameN  # exact frame index
                win.timeOnFlip(resp, 'tStartRefresh')  # time at next scr refresh
                resp.status = STARTED
                # keyboard checking is just starting
                win.callOnFlip(resp.clock.reset)  # t=0 on next screen flip
                resp.clearEvents(eventType='keyboard')
            frameRemains = 0.0 + 4- win.monitorFramePeriod * 0.75  # most of one frame period left
            if resp.status == STARTED and t >= frameRemains:
                # keep track of stop time/frame for later
                resp.tStop = t  # not accounting for scr refresh
                resp.frameNStop = frameN  # exact frame index
                win.timeOnFlip(resp, 'tStopRefresh')  # time at next scr refresh
                resp.status = FINISHED
            if resp.status == STARTED:
                theseKeys = resp.getKeys(keyList=['left', 'right'], waitRelease=False)
                if len(theseKeys):
                    theseKeys = theseKeys[0]  # at least one key was pressed
                    
                    # check for quit:
                    if "escape" == theseKeys:
                        endExpNow = True
                    resp.keys = theseKeys.name  # just the last key pressed
                    resp.rt = theseKeys.rt
            
            # *polygon_2* updates
            if t >= 4 and polygon_2.status == NOT_STARTED:
                # keep track of start time/frame for later
                polygon_2.tStart = t  # not accounting for scr refresh
                polygon_2.frameNStart = frameN  # exact frame index
                win.timeOnFlip(polygon_2, 'tStartRefresh')  # time at next scr refresh
                polygon_2.setAutoDraw(True)
            frameRemains = 4 + 2- win.monitorFramePeriod * 0.75  # most of one frame period left
            if polygon_2.status == STARTED and t >= frameRemains:
                # keep track of stop time/frame for later
                polygon_2.tStop = t  # not accounting for scr refresh
                polygon_2.frameNStop = frameN  # exact frame index
                win.timeOnFlip(polygon_2, 'tStopRefresh')  # time at next scr refresh
                polygon_2.setAutoDraw(False)
            if resp.keys == 'left':
                checkL.autoDraw=True
            elif resp.keys == 'right':
                    checkR.autoDraw=False
            
            if resp.keys =='right':
                checkR.autoDraw=True
            elif resp.keys == 'left':
                    checkL.autoDraw=False
            
            
            
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
        trials_5.addData('image_5.started', image_5.tStartRefresh)
        trials_5.addData('image_5.stopped', image_5.tStopRefresh)
        # check responses
        if resp.keys in ['', [], None]:  # No response was made
            resp.keys = None
        trials_5.addData('resp.keys',resp.keys)
        if resp.keys != None:  # we had a response
            trials_5.addData('resp.rt', resp.rt)
        trials_5.addData('resp.started', resp.tStartRefresh)
        trials_5.addData('resp.stopped', resp.tStopRefresh)
        trials_5.addData('polygon_2.started', polygon_2.tStartRefresh)
        trials_5.addData('polygon_2.stopped', polygon_2.tStopRefresh)
        thisExp.nextEntry()
        
    # completed nRepsblock1 repeats of 'trials_5'
    
    
    # set up handler to look after randomisation of conditions etc
    trials_6 = data.TrialHandler(nReps=nRepsblock2, method='sequential', 
        extraInfo=expInfo, originPath=-1,
        trialList=data.importConditions('ConditionsGain.csv'),
        seed=None, name='trials_6')
    thisExp.addLoop(trials_6)  # add the loop to the experiment
    thisTrial_6 = trials_6.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisTrial_6.rgb)
    if thisTrial_6 != None:
        for paramName in thisTrial_6:
            exec('{} = thisTrial_6[paramName]'.format(paramName))
    
    for thisTrial_6 in trials_6:
        currentLoop = trials_6
        # abbreviate parameter names if possible (e.g. rgb = thisTrial_6.rgb)
        if thisTrial_6 != None:
            for paramName in thisTrial_6:
                exec('{} = thisTrial_6[paramName]'.format(paramName))
        
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
        trials_6.addData('iSi.started', iSi.tStartRefresh)
        trials_6.addData('iSi.stopped', iSi.tStopRefresh)
        
        # ------Prepare to start Routine "Receive_money"-------
        t = 0
        Receive_moneyClock.reset()  # clock
        frameN = -1
        continueRoutine = True
        routineTimer.add(4.000000)
        # update component parameters for each repeat
        receive.setColor('white', colorSpace='rgb')
        receive.setPos((0.0, 0))
        receive.setText(Amount)
        receive.setFont('Arial')
        receive.setHeight(0.1)
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
        trials_6.addData('receive.started', receive.tStartRefresh)
        trials_6.addData('receive.stopped', receive.tStopRefresh)
        trials_6.addData('ISI2.started', ISI2.tStartRefresh)
        trials_6.addData('ISI2.stopped', ISI2.tStopRefresh)
        
        # ------Prepare to start Routine "loseTrial"-------
        t = 0
        loseTrialClock.reset()  # clock
        frameN = -1
        continueRoutine = True
        routineTimer.add(4.000000)
        # update component parameters for each repeat
        image_2.setOpacity(1)
        image_2.setPos((0, 0))
        image_2.setSize((1.3, 0.9))
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
        trials_6.addData('image_2.started', image_2.tStartRefresh)
        trials_6.addData('image_2.stopped', image_2.tStopRefresh)
        
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
        Advice.setColor('white', colorSpace='rgb')
        Advice.setPos((0, 0))
        Advice.setText('Advisor 1 says\n\n"Go with the safe option here!"')
        Advice.setFont('Arial')
        Advice.setHeight(0.08)
        # keep track of which components have finished
        askAdComponents = [text_3, ask, response, Advice]
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
            
            # *text_3* updates
            if t >= 0.0 and text_3.status == NOT_STARTED:
                # keep track of start time/frame for later
                text_3.tStart = t  # not accounting for scr refresh
                text_3.frameNStart = frameN  # exact frame index
                win.timeOnFlip(text_3, 'tStartRefresh')  # time at next scr refresh
                text_3.setAutoDraw(True)
            if text_3.status == STARTED and bool(Advice.status==STARTED):
                # keep track of stop time/frame for later
                text_3.tStop = t  # not accounting for scr refresh
                text_3.frameNStop = frameN  # exact frame index
                win.timeOnFlip(text_3, 'tStopRefresh')  # time at next scr refresh
                text_3.setAutoDraw(False)
            
            # *ask* updates
            if t >= 0.0 and ask.status == NOT_STARTED:
                # keep track of start time/frame for later
                ask.tStart = t  # not accounting for scr refresh
                ask.frameNStart = frameN  # exact frame index
                win.timeOnFlip(ask, 'tStartRefresh')  # time at next scr refresh
                ask.setAutoDraw(True)
            if ask.status == STARTED and bool(Advice.status==STARTED):
                # keep track of stop time/frame for later
                ask.tStop = t  # not accounting for scr refresh
                ask.frameNStop = frameN  # exact frame index
                win.timeOnFlip(ask, 'tStopRefresh')  # time at next scr refresh
                ask.setAutoDraw(False)
            
            # *response* updates
            if t >= 0.0 and response.status == NOT_STARTED:
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
            
            # *Advice* updates
            if (response.keys=='y') and Advice.status == NOT_STARTED:
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
        trials_6.addData('text_3.started', text_3.tStartRefresh)
        trials_6.addData('text_3.stopped', text_3.tStopRefresh)
        trials_6.addData('ask.started', ask.tStartRefresh)
        trials_6.addData('ask.stopped', ask.tStopRefresh)
        # check responses
        if response.keys in ['', [], None]:  # No response was made
            response.keys = None
        trials_6.addData('response.keys',response.keys)
        if response.keys != None:  # we had a response
            trials_6.addData('response.rt', response.rt)
        trials_6.addData('response.started', response.tStartRefresh)
        trials_6.addData('response.stopped', response.tStopRefresh)
        trials_6.addData('Advice.started', Advice.tStartRefresh)
        trials_6.addData('Advice.stopped', Advice.tStopRefresh)
        # the Routine "askAd" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # ------Prepare to start Routine "Choice2Loss"-------
        t = 0
        Choice2LossClock.reset()  # clock
        frameN = -1
        continueRoutine = True
        # update component parameters for each repeat
        image_3.setOpacity(1)
        image_3.setPos((0, 0))
        image_3.setSize((1.3, 0.9))
        image_3.setOri(0)
        image_3.setImage(Loss2)
        key_resp = keyboard.Keyboard()
        # keep track of which components have finished
        Choice2LossComponents = [image_3, key_resp]
        for thisComponent in Choice2LossComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        
        # -------Start Routine "Choice2Loss"-------
        while continueRoutine:
            # get current time
            t = Choice2LossClock.getTime()
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *image_3* updates
            if t >= 0.0 and image_3.status == NOT_STARTED:
                # keep track of start time/frame for later
                image_3.tStart = t  # not accounting for scr refresh
                image_3.frameNStart = frameN  # exact frame index
                win.timeOnFlip(image_3, 'tStartRefresh')  # time at next scr refresh
                image_3.setAutoDraw(True)
            frameRemains = 0.0 + 4- win.monitorFramePeriod * 0.75  # most of one frame period left
            if image_3.status == STARTED and t >= frameRemains:
                # keep track of stop time/frame for later
                image_3.tStop = t  # not accounting for scr refresh
                image_3.frameNStop = frameN  # exact frame index
                win.timeOnFlip(image_3, 'tStopRefresh')  # time at next scr refresh
                image_3.setAutoDraw(False)
            
            # *key_resp* updates
            if t >= 0.0 and key_resp.status == NOT_STARTED:
                # keep track of start time/frame for later
                key_resp.tStart = t  # not accounting for scr refresh
                key_resp.frameNStart = frameN  # exact frame index
                win.timeOnFlip(key_resp, 'tStartRefresh')  # time at next scr refresh
                key_resp.status = STARTED
                # keyboard checking is just starting
                win.callOnFlip(key_resp.clock.reset)  # t=0 on next screen flip
                key_resp.clearEvents(eventType='keyboard')
            if key_resp.status == STARTED:
                theseKeys = key_resp.getKeys(keyList=['left', 'right'], waitRelease=False)
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
            for thisComponent in Choice2LossComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "Choice2Loss"-------
        for thisComponent in Choice2LossComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        trials_6.addData('image_3.started', image_3.tStartRefresh)
        trials_6.addData('image_3.stopped', image_3.tStopRefresh)
        # check responses
        if key_resp.keys in ['', [], None]:  # No response was made
            key_resp.keys = None
        trials_6.addData('key_resp.keys',key_resp.keys)
        if key_resp.keys != None:  # we had a response
            trials_6.addData('key_resp.rt', key_resp.rt)
        trials_6.addData('key_resp.started', key_resp.tStartRefresh)
        trials_6.addData('key_resp.stopped', key_resp.tStopRefresh)
        # the Routine "Choice2Loss" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        thisExp.nextEntry()
        
    # completed nRepsblock2 repeats of 'trials_6'
    
    thisExp.nextEntry()
    
# completed 1 repeats of 'trials_4'


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
