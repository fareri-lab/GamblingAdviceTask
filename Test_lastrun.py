#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy2 Experiment Builder (v1.85.2),
    on July 09, 2019, at 11:10
If you publish work using this script please cite the PsychoPy publications:
    Peirce, JW (2007) PsychoPy - Psychophysics software in Python.
        Journal of Neuroscience Methods, 162(1-2), 8-13.
    Peirce, JW (2009) Generating stimuli for neuroscience using PsychoPy.
        Frontiers in Neuroinformatics, 2:10. doi: 10.3389/neuro.11.010.2008
"""

from __future__ import absolute_import, division
from psychopy import locale_setup, sound, gui, visual, core, data, event, logging
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER)
import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle
import os  # handy system and path functions
import sys  # to get file system encoding

# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__)).decode(sys.getfilesystemencoding())
os.chdir(_thisDir)

# Store info about the experiment session
expName = 'Test'  # from the Builder filename that created this script
expInfo = {'participant': '', 'session': '001'}
dlg = gui.DlgFromDict(dictionary=expInfo, title=expName)
if dlg.OK == False:
    core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName

# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
filename = _thisDir + os.sep + u'data/%s_%s_%s' % (expInfo['participant'], expName, expInfo['date'])

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath=u'C:\\Users\\farerilab\\Downloads\\GamblingAdviceTask\\Test.psyexp',
    savePickle=True, saveWideText=True,
    dataFileName=filename)
# save a log file for detail verbose info
logFile = logging.LogFile(filename+'.log', level=logging.EXP)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp

# Start Code - component code to be run before the window creation

# Setup the Window
win = visual.Window(
    size=(1920, 1080), fullscr=True, screen=0,
    allowGUI=False, allowStencil=False,
    monitor='testMonitor', color=[-1,-1,-1], colorSpace='rgb',
    blendMode='avg', useFBO=True,
    units='height')
# store frame rate of monitor if we can measure it
expInfo['frameRate'] = win.getActualFrameRate()
if expInfo['frameRate'] != None:
    frameDur = 1.0 / round(expInfo['frameRate'])
else:
    frameDur = 1.0 / 60.0  # could not measure, so guess

# Initialize components for Routine "code_2"
code_2Clock = core.Clock()
nRepsblock1=0
nRepsblock2=0

# Initialize components for Routine "isi"
isiClock = core.Clock()
ISI = visual.TextStim(win=win, name='ISI',
    text='default text',
    font='Arial',
    pos=[0,0], height=1.0, wrapWidth=None, ori=0, 
    color=1.0, colorSpace='rgb', opacity=1,
    depth=0.0);
text_2 = visual.TextStim(win=win, name='text_2',
    text='default text',
    font='Arial',
    pos=[0,0], height=1.0, wrapWidth=None, ori=0, 
    color=1.0, colorSpace='rgb', opacity=1,
    depth=-1.0);
text_4 = visual.TextStim(win=win, name='text_4',
    text='default text',
    font='Arial',
    pos=[0,0], height=1.0, wrapWidth=None, ori=0, 
    color=1.0, colorSpace='rgb', opacity=1,
    depth=-2.0);

# Initialize components for Routine "trial"
trialClock = core.Clock()
image = visual.ImageStim(
    win=win, name='image',
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
    depth=0.0);
ask = visual.TextStim(win=win, name='ask',
    text='Would you like to hear advice from your financial advisor?',
    font='Arial',
    pos=(0, 0.11), height=0.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=-1.0);

Advice = visual.TextStim(win=win, name='Advice',
    text='default text',
    font='Arial',
    pos=[0,0], height=1.0, wrapWidth=None, ori=0, 
    color=1.0, colorSpace='rgb', opacity=1,
    depth=-4.0);

# Initialize components for Routine "Choice2Gain"
Choice2GainClock = core.Clock()
text1 = visual.TextStim(win=win, name='text1',
    text='default text',
    font='Arial',
    pos=[0,0], height=1.0, wrapWidth=None, ori=0, 
    color=1.0, colorSpace='rgb', opacity=1,
    depth=0.0);
image_5 = visual.ImageStim(
    win=win, name='image_5',
    image='sin', mask=None,
    ori=1.0, pos=[0,0], size=1.0,
    color=[1,1,1], colorSpace='rgb', opacity=1.0,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-1.0)
checkL1 = visual.ImageStim(
    win=win, name='checkL1',
    image='sin', mask=None,
    ori=1.0, pos=[0,0], size=1.0,
    color=1.0, colorSpace='rgb', opacity=1.0,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-3.0)
checkR1 = visual.ImageStim(
    win=win, name='checkR1',
    image='sin', mask=None,
    ori=1.0, pos=[0,0], size=1.0,
    color=1.0, colorSpace='rgb', opacity=1.0,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-4.0)

from PIL import Image
from psychopy import visual, core

# Initialize components for Routine "isi"
isiClock = core.Clock()
ISI = visual.TextStim(win=win, name='ISI',
    text='default text',
    font='Arial',
    pos=[0,0], height=1.0, wrapWidth=None, ori=0, 
    color=1.0, colorSpace='rgb', opacity=1,
    depth=0.0);
text_2 = visual.TextStim(win=win, name='text_2',
    text='default text',
    font='Arial',
    pos=[0,0], height=1.0, wrapWidth=None, ori=0, 
    color=1.0, colorSpace='rgb', opacity=1,
    depth=-1.0);
text_4 = visual.TextStim(win=win, name='text_4',
    text='default text',
    font='Arial',
    pos=[0,0], height=1.0, wrapWidth=None, ori=0, 
    color=1.0, colorSpace='rgb', opacity=1,
    depth=-2.0);

# Initialize components for Routine "loseTrial"
loseTrialClock = core.Clock()
image_2 = visual.ImageStim(
    win=win, name='image_2',
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
    depth=0.0);
ask = visual.TextStim(win=win, name='ask',
    text='Would you like to hear advice from your financial advisor?',
    font='Arial',
    pos=(0, 0.11), height=0.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=-1.0);

Advice = visual.TextStim(win=win, name='Advice',
    text='default text',
    font='Arial',
    pos=[0,0], height=1.0, wrapWidth=None, ori=0, 
    color=1.0, colorSpace='rgb', opacity=1,
    depth=-4.0);

# Initialize components for Routine "Choice2Loss"
Choice2LossClock = core.Clock()
text2 = visual.TextStim(win=win, name='text2',
    text='default text',
    font='Arial',
    pos=[0,0], height=1.0, wrapWidth=None, ori=0, 
    color=1.0, colorSpace='rgb', opacity=1,
    depth=0.0);
image_3 = visual.ImageStim(
    win=win, name='image_3',
    image='sin', mask=None,
    ori=1.0, pos=[0,0], size=1.0,
    color=[1,1,1], colorSpace='rgb', opacity=1.0,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-1.0)
checkR = visual.ImageStim(
    win=win, name='checkR',
    image='sin', mask=None,
    ori=1.0, pos=[0,0], size=1.0,
    color=[1,1,1], colorSpace='rgb', opacity=1.0,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-3.0)
checkL = visual.ImageStim(
    win=win, name='checkL',
    image='sin', mask=None,
    ori=1.0, pos=[0,0], size=1.0,
    color=[1,1,1], colorSpace='rgb', opacity=1.0,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-4.0)
#checkL = visual.ImageStim(win=win, pos=(-0.19, 0), size= (0.25, 0.25) )
#checkL.setImage('check.png')
#checkR = visual.ImageStim(win=win, pos=(0.19, 0), size= (0.25, 0.25) )
#checkR.setImage('check.png')

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

# set up handler to look after randomisation of conditions etc
trials_3 = data.TrialHandler(nReps=1, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions(u'Conditions.csv'),
    seed=None, name='trials_3')
thisExp.addLoop(trials_3)  # add the loop to the experiment
thisTrial_3 = trials_3.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisTrial_3.rgb)
if thisTrial_3 != None:
    for paramName in thisTrial_3.keys():
        exec(paramName + '= thisTrial_3.' + paramName)

for thisTrial_3 in trials_3:
    currentLoop = trials_3
    # abbreviate parameter names if possible (e.g. rgb = thisTrial_3.rgb)
    if thisTrial_3 != None:
        for paramName in thisTrial_3.keys():
            exec(paramName + '= thisTrial_3.' + paramName)
    
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
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    # -------Start Routine "code_2"-------
    while continueRoutine:
        # get current time
        t = code_2Clock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in code_2Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
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
        trialList=data.importConditions(u'Conditions.csv'),
        seed=None, name='trials')
    thisExp.addLoop(trials)  # add the loop to the experiment
    thisTrial = trials.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
    if thisTrial != None:
        for paramName in thisTrial.keys():
            exec(paramName + '= thisTrial.' + paramName)
    
    for thisTrial in trials:
        currentLoop = trials
        # abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
        if thisTrial != None:
            for paramName in thisTrial.keys():
                exec(paramName + '= thisTrial.' + paramName)
        
        # ------Prepare to start Routine "isi"-------
        t = 0
        isiClock.reset()  # clock
        frameN = -1
        continueRoutine = True
        routineTimer.add(5.000000)
        # update component parameters for each repeat
        ISI.setColor(u'white', colorSpace='rgb')
        ISI.setText(u'+')
        ISI.setPos((0, 0))
        ISI.setFont(u'Arial')
        ISI.setHeight(0.08)
        text_2.setColor(u'white', colorSpace='rgb')
        text_2.setText(u'RECEIVE    $')
        text_2.setPos((-0.05, 0))
        text_2.setFont(u'Arial')
        text_2.setHeight(0.1)
        text_4.setColor(u'white', colorSpace='rgb')
        text_4.setText(Amount)
        text_4.setPos((0.05, 0))
        text_4.setFont(u'Arial')
        text_4.setHeight(0.1)
        # keep track of which components have finished
        isiComponents = [ISI, text_2, text_4]
        for thisComponent in isiComponents:
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        
        # -------Start Routine "isi"-------
        while continueRoutine and routineTimer.getTime() > 0:
            # get current time
            t = isiClock.getTime()
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *ISI* updates
            if t >= 0.0 and ISI.status == NOT_STARTED:
                # keep track of start time/frame for later
                ISI.tStart = t
                ISI.frameNStart = frameN  # exact frame index
                ISI.setAutoDraw(True)
            frameRemains = 0.0 + 3- win.monitorFramePeriod * 0.75  # most of one frame period left
            if ISI.status == STARTED and t >= frameRemains:
                ISI.setAutoDraw(False)
            
            # *text_2* updates
            if t >= 3 and text_2.status == NOT_STARTED:
                # keep track of start time/frame for later
                text_2.tStart = t
                text_2.frameNStart = frameN  # exact frame index
                text_2.setAutoDraw(True)
            frameRemains = 3 + 2- win.monitorFramePeriod * 0.75  # most of one frame period left
            if text_2.status == STARTED and t >= frameRemains:
                text_2.setAutoDraw(False)
            
            # *text_4* updates
            if t >= 3 and text_4.status == NOT_STARTED:
                # keep track of start time/frame for later
                text_4.tStart = t
                text_4.frameNStart = frameN  # exact frame index
                text_4.setAutoDraw(True)
            frameRemains = 3 + 2- win.monitorFramePeriod * 0.75  # most of one frame period left
            if text_4.status == STARTED and t >= frameRemains:
                text_4.setAutoDraw(False)
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in isiComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # check for quit (the Esc key)
            if endExpNow or event.getKeys(keyList=["escape"]):
                core.quit()
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "isi"-------
        for thisComponent in isiComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        
        # ------Prepare to start Routine "trial"-------
        t = 0
        trialClock.reset()  # clock
        frameN = -1
        continueRoutine = True
        routineTimer.add(4.000000)
        # update component parameters for each repeat
        image.setImage(Gain)
        image.setPos((0, 0))
        image.setSize((1.3, 0.9))
        image.setOpacity(1)
        image.setOri(0)
        # keep track of which components have finished
        trialComponents = [image]
        for thisComponent in trialComponents:
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
                image.tStart = t
                image.frameNStart = frameN  # exact frame index
                image.setAutoDraw(True)
            frameRemains = 0.0 + 4- win.monitorFramePeriod * 0.75  # most of one frame period left
            if image.status == STARTED and t >= frameRemains:
                image.setAutoDraw(False)
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in trialComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # check for quit (the Esc key)
            if endExpNow or event.getKeys(keyList=["escape"]):
                core.quit()
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "trial"-------
        for thisComponent in trialComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        
        # ------Prepare to start Routine "askAd"-------
        t = 0
        askAdClock.reset()  # clock
        frameN = -1
        continueRoutine = True
        # update component parameters for each repeat
        response = event.BuilderKeyResponse()
        
        Advice.setColor('white', colorSpace='rgb')
        Advice.setPos((0, 0))
        Advice.setHeight(0.08)
        Advice.setFont('Arial')
        Advice.setText('Advisor 1 says\n\n"Go with the safe option here!"')
        # keep track of which components have finished
        askAdComponents = [text_3, ask, response, Advice]
        for thisComponent in askAdComponents:
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
                text_3.tStart = t
                text_3.frameNStart = frameN  # exact frame index
                text_3.setAutoDraw(True)
            if text_3.status == STARTED and bool(Advice.status==STARTED):
                text_3.setAutoDraw(False)
            
            # *ask* updates
            if t >= 0.0 and ask.status == NOT_STARTED:
                # keep track of start time/frame for later
                ask.tStart = t
                ask.frameNStart = frameN  # exact frame index
                ask.setAutoDraw(True)
            if ask.status == STARTED and bool(Advice.status==STARTED):
                ask.setAutoDraw(False)
            
            # *response* updates
            if t >= 0 and response.status == NOT_STARTED:
                # keep track of start time/frame for later
                response.tStart = t
                response.frameNStart = frameN  # exact frame index
                response.status = STARTED
                # keyboard checking is just starting
                win.callOnFlip(response.clock.reset)  # t=0 on next screen flip
                event.clearEvents(eventType='keyboard')
            frameRemains = 0 + 4- win.monitorFramePeriod * 0.75  # most of one frame period left
            if response.status == STARTED and t >= frameRemains:
                response.status = STOPPED
            if response.status == STARTED:
                theseKeys = event.getKeys(keyList=['y', 'n'])
                
                # check for quit:
                if "escape" in theseKeys:
                    endExpNow = True
                if len(theseKeys) > 0:  # at least one key was pressed
                    response.keys = theseKeys[-1]  # just the last key pressed
                    response.rt = response.clock.getTime()
            if response.keys == 'y':
                continueRoutine = True
            elif response.keys == 'n':
                continueRoutine = False 
            
            # *Advice* updates
            if (response.keys=='y') and Advice.status == NOT_STARTED:
                # keep track of start time/frame for later
                Advice.tStart = t
                Advice.frameNStart = frameN  # exact frame index
                Advice.setAutoDraw(True)
            if Advice.status == STARTED and t >= (Advice.tStart + 3):
                Advice.setAutoDraw(False)
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in askAdComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # check for quit (the Esc key)
            if endExpNow or event.getKeys(keyList=["escape"]):
                core.quit()
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "askAd"-------
        for thisComponent in askAdComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # check responses
        if response.keys in ['', [], None]:  # No response was made
            response.keys=None
        trials.addData('response.keys',response.keys)
        if response.keys != None:  # we had a response
            trials.addData('response.rt', response.rt)
        if response.keys == 'y':
            continueRoutine = True
        elif response.keys == 'n':
            continueRoutine = False 
        # the Routine "askAd" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # ------Prepare to start Routine "Choice2Gain"-------
        t = 0
        Choice2GainClock.reset()  # clock
        frameN = -1
        continueRoutine = True
        # update component parameters for each repeat
        text1.setColor([-1.000,-1.000,-1.000], colorSpace='rgb')
        text1.setText('I')
        text1.setPos((0, 0))
        text1.setFont('Arial')
        text1.setHeight(0.01)
        image_5.setImage(Gain1)
        image_5.setPos((0, 0))
        image_5.setSize((1.3, 0.9))
        image_5.setOpacity(1)
        image_5.setOri(0)
        resp = event.BuilderKeyResponse()
        checkL1.setOpacity(1)
        checkL1.setColor([1,1,1], colorSpace='rgb')
        checkL1.setMask('None')
        checkL1.setPos((0, 0))
        checkL1.setOri(0)
        checkL1.setImage('check2.png')
        checkL1.setSize((2, 1))
        checkR1.setOpacity(1)
        checkR1.setColor([1,1,1], colorSpace='rgb')
        checkR1.setMask('None')
        checkR1.setPos((0, 0))
        checkR1.setOri(0)
        checkR1.setImage('check3.png')
        checkR1.setSize((2, 1))
        
        # keep track of which components have finished
        Choice2GainComponents = [text1, image_5, resp, checkL1, checkR1]
        for thisComponent in Choice2GainComponents:
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        
        # -------Start Routine "Choice2Gain"-------
        while continueRoutine:
            # get current time
            t = Choice2GainClock.getTime()
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *text1* updates
            if t >= 0.0 and text1.status == NOT_STARTED:
                # keep track of start time/frame for later
                text1.tStart = t
                text1.frameNStart = frameN  # exact frame index
                text1.setAutoDraw(True)
            frameRemains = 0.0 + 5- win.monitorFramePeriod * 0.75  # most of one frame period left
            if text1.status == STARTED and t >= frameRemains:
                text1.setAutoDraw(False)
            
            # *image_5* updates
            if t >= 0.0 and image_5.status == NOT_STARTED:
                # keep track of start time/frame for later
                image_5.tStart = t
                image_5.frameNStart = frameN  # exact frame index
                image_5.setAutoDraw(True)
            frameRemains = 0.0 + 4- win.monitorFramePeriod * 0.75  # most of one frame period left
            if image_5.status == STARTED and t >= frameRemains:
                image_5.setAutoDraw(False)
            
            # *resp* updates
            if t >= 0.0 and resp.status == NOT_STARTED:
                # keep track of start time/frame for later
                resp.tStart = t
                resp.frameNStart = frameN  # exact frame index
                resp.status = STARTED
                # keyboard checking is just starting
                win.callOnFlip(resp.clock.reset)  # t=0 on next screen flip
                event.clearEvents(eventType='keyboard')
            frameRemains = 0.0 + 4- win.monitorFramePeriod * 0.75  # most of one frame period left
            if resp.status == STARTED and t >= frameRemains:
                resp.status = STOPPED
            if resp.status == STARTED:
                theseKeys = event.getKeys(keyList=['left', 'right'])
                
                # check for quit:
                if "escape" in theseKeys:
                    endExpNow = True
                if len(theseKeys) > 0:  # at least one key was pressed
                    resp.keys = theseKeys[-1]  # just the last key pressed
                    resp.rt = resp.clock.getTime()
            
            # *checkL1* updates
            if (resp.keys == 'left') and checkL1.status == NOT_STARTED:
                # keep track of start time/frame for later
                checkL1.tStart = t
                checkL1.frameNStart = frameN  # exact frame index
                checkL1.setAutoDraw(True)
            if checkL1.status == STARTED and t >= (checkL1.tStart + 2):
                checkL1.setAutoDraw(False)
            
            # *checkR1* updates
            if (resp.keys == 'right') and checkR1.status == NOT_STARTED:
                # keep track of start time/frame for later
                checkR1.tStart = t
                checkR1.frameNStart = frameN  # exact frame index
                checkR1.setAutoDraw(True)
            if checkR1.status == STARTED and t >= (checkR1.tStart + 2):
                checkR1.setAutoDraw(False)
            checkL1.autoLog=False
            checkR1.autoLog=False
            
            
            if resp.keys == 'left':
                checkL1.autoDraw=True
            #elif resp.keys == 'right':
             #   checkR1.autoDraw=False
            
            if resp.keys == 'right':
                checkR1.autoDraw=True
            
            if text1.status == FINISHED:
                checkR1.autoDraw=False
                checkL1.autoDraw=False
                continueRoutine=False
                #win.flip()
            
            
                #elif resp.keys == 'left':
             #   checkL1.autoDraw=False
            
            #clock = core.Clock()
            #while clock.getTime() < 2.0:
            #    if 0.5 <= clock.getTime() < 1.0:
             #       if checkL1.autoDraw==True:
              #          checkL1.setPhase(0.1, '+') 
               #     elif checkR1.autoDraw==True:
                #        checkR1.setPhase(0.1, '+')
                #win.flip()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in Choice2GainComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # check for quit (the Esc key)
            if endExpNow or event.getKeys(keyList=["escape"]):
                core.quit()
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "Choice2Gain"-------
        for thisComponent in Choice2GainComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # check responses
        if resp.keys in ['', [], None]:  # No response was made
            resp.keys=None
        trials.addData('resp.keys',resp.keys)
        if resp.keys != None:  # we had a response
            trials.addData('resp.rt', resp.rt)
        checkL1.autoLog=False
        checkR1.autoLog=False
        
        
        
        if resp.keys == 'left':
            checkL1.autoDraw=True
        #elif resp.keys == 'right':
         #   checkR1.autoDraw=False
        
        if resp.keys =='right':
            checkR1.autoDraw=True
        
        if text1.status == FINISHED:
            checkR1.autoDraw=False
            checkL1.autoDraw=False
            #win.flip()
        #elif resp.keys == 'left':
         #   checkL1.autoDraw=False
        
        
        #clock = core.Clock()
        #while clock.getTime() < 2.0:
         #   if 0.5 <= clock.getTime() < 1.0:
          #      if checkL1.autoDraw==True:
           #         checkL1.setPhase (0.1, '+')
            #    elif checkR1.autoDraw==True:
             #       checkR1.setPhase(0.1, '+')
            #win.flip()
        # the Routine "Choice2Gain" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        thisExp.nextEntry()
        
    # completed nRepsblock1 repeats of 'trials'
    
    
    # set up handler to look after randomisation of conditions etc
    trials_2 = data.TrialHandler(nReps=nRepsblock2, method='random', 
        extraInfo=expInfo, originPath=-1,
        trialList=data.importConditions(u'Conditions.csv'),
        seed=None, name='trials_2')
    thisExp.addLoop(trials_2)  # add the loop to the experiment
    thisTrial_2 = trials_2.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisTrial_2.rgb)
    if thisTrial_2 != None:
        for paramName in thisTrial_2.keys():
            exec(paramName + '= thisTrial_2.' + paramName)
    
    for thisTrial_2 in trials_2:
        currentLoop = trials_2
        # abbreviate parameter names if possible (e.g. rgb = thisTrial_2.rgb)
        if thisTrial_2 != None:
            for paramName in thisTrial_2.keys():
                exec(paramName + '= thisTrial_2.' + paramName)
        
        # ------Prepare to start Routine "isi"-------
        t = 0
        isiClock.reset()  # clock
        frameN = -1
        continueRoutine = True
        routineTimer.add(5.000000)
        # update component parameters for each repeat
        ISI.setColor(u'white', colorSpace='rgb')
        ISI.setText(u'+')
        ISI.setPos((0, 0))
        ISI.setFont(u'Arial')
        ISI.setHeight(0.08)
        text_2.setColor(u'white', colorSpace='rgb')
        text_2.setText(u'RECEIVE    $')
        text_2.setPos((-0.05, 0))
        text_2.setFont(u'Arial')
        text_2.setHeight(0.1)
        text_4.setColor(u'white', colorSpace='rgb')
        text_4.setText(Amount)
        text_4.setPos((0.05, 0))
        text_4.setFont(u'Arial')
        text_4.setHeight(0.1)
        # keep track of which components have finished
        isiComponents = [ISI, text_2, text_4]
        for thisComponent in isiComponents:
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        
        # -------Start Routine "isi"-------
        while continueRoutine and routineTimer.getTime() > 0:
            # get current time
            t = isiClock.getTime()
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *ISI* updates
            if t >= 0.0 and ISI.status == NOT_STARTED:
                # keep track of start time/frame for later
                ISI.tStart = t
                ISI.frameNStart = frameN  # exact frame index
                ISI.setAutoDraw(True)
            frameRemains = 0.0 + 3- win.monitorFramePeriod * 0.75  # most of one frame period left
            if ISI.status == STARTED and t >= frameRemains:
                ISI.setAutoDraw(False)
            
            # *text_2* updates
            if t >= 3 and text_2.status == NOT_STARTED:
                # keep track of start time/frame for later
                text_2.tStart = t
                text_2.frameNStart = frameN  # exact frame index
                text_2.setAutoDraw(True)
            frameRemains = 3 + 2- win.monitorFramePeriod * 0.75  # most of one frame period left
            if text_2.status == STARTED and t >= frameRemains:
                text_2.setAutoDraw(False)
            
            # *text_4* updates
            if t >= 3 and text_4.status == NOT_STARTED:
                # keep track of start time/frame for later
                text_4.tStart = t
                text_4.frameNStart = frameN  # exact frame index
                text_4.setAutoDraw(True)
            frameRemains = 3 + 2- win.monitorFramePeriod * 0.75  # most of one frame period left
            if text_4.status == STARTED and t >= frameRemains:
                text_4.setAutoDraw(False)
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in isiComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # check for quit (the Esc key)
            if endExpNow or event.getKeys(keyList=["escape"]):
                core.quit()
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "isi"-------
        for thisComponent in isiComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        
        # ------Prepare to start Routine "loseTrial"-------
        t = 0
        loseTrialClock.reset()  # clock
        frameN = -1
        continueRoutine = True
        routineTimer.add(4.000000)
        # update component parameters for each repeat
        image_2.setImage(Loss)
        image_2.setPos((0, 0))
        image_2.setSize((1.3, 0.9))
        image_2.setOpacity(1)
        image_2.setOri(0)
        # keep track of which components have finished
        loseTrialComponents = [image_2]
        for thisComponent in loseTrialComponents:
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
                image_2.tStart = t
                image_2.frameNStart = frameN  # exact frame index
                image_2.setAutoDraw(True)
            frameRemains = 0.0 + 4- win.monitorFramePeriod * 0.75  # most of one frame period left
            if image_2.status == STARTED and t >= frameRemains:
                image_2.setAutoDraw(False)
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in loseTrialComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # check for quit (the Esc key)
            if endExpNow or event.getKeys(keyList=["escape"]):
                core.quit()
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "loseTrial"-------
        for thisComponent in loseTrialComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        
        # ------Prepare to start Routine "askAd"-------
        t = 0
        askAdClock.reset()  # clock
        frameN = -1
        continueRoutine = True
        # update component parameters for each repeat
        response = event.BuilderKeyResponse()
        
        Advice.setColor('white', colorSpace='rgb')
        Advice.setPos((0, 0))
        Advice.setHeight(0.08)
        Advice.setFont('Arial')
        Advice.setText('Advisor 1 says\n\n"Go with the safe option here!"')
        # keep track of which components have finished
        askAdComponents = [text_3, ask, response, Advice]
        for thisComponent in askAdComponents:
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
                text_3.tStart = t
                text_3.frameNStart = frameN  # exact frame index
                text_3.setAutoDraw(True)
            if text_3.status == STARTED and bool(Advice.status==STARTED):
                text_3.setAutoDraw(False)
            
            # *ask* updates
            if t >= 0.0 and ask.status == NOT_STARTED:
                # keep track of start time/frame for later
                ask.tStart = t
                ask.frameNStart = frameN  # exact frame index
                ask.setAutoDraw(True)
            if ask.status == STARTED and bool(Advice.status==STARTED):
                ask.setAutoDraw(False)
            
            # *response* updates
            if t >= 0 and response.status == NOT_STARTED:
                # keep track of start time/frame for later
                response.tStart = t
                response.frameNStart = frameN  # exact frame index
                response.status = STARTED
                # keyboard checking is just starting
                win.callOnFlip(response.clock.reset)  # t=0 on next screen flip
                event.clearEvents(eventType='keyboard')
            frameRemains = 0 + 4- win.monitorFramePeriod * 0.75  # most of one frame period left
            if response.status == STARTED and t >= frameRemains:
                response.status = STOPPED
            if response.status == STARTED:
                theseKeys = event.getKeys(keyList=['y', 'n'])
                
                # check for quit:
                if "escape" in theseKeys:
                    endExpNow = True
                if len(theseKeys) > 0:  # at least one key was pressed
                    response.keys = theseKeys[-1]  # just the last key pressed
                    response.rt = response.clock.getTime()
            if response.keys == 'y':
                continueRoutine = True
            elif response.keys == 'n':
                continueRoutine = False 
            
            # *Advice* updates
            if (response.keys=='y') and Advice.status == NOT_STARTED:
                # keep track of start time/frame for later
                Advice.tStart = t
                Advice.frameNStart = frameN  # exact frame index
                Advice.setAutoDraw(True)
            if Advice.status == STARTED and t >= (Advice.tStart + 3):
                Advice.setAutoDraw(False)
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in askAdComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # check for quit (the Esc key)
            if endExpNow or event.getKeys(keyList=["escape"]):
                core.quit()
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "askAd"-------
        for thisComponent in askAdComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # check responses
        if response.keys in ['', [], None]:  # No response was made
            response.keys=None
        trials_2.addData('response.keys',response.keys)
        if response.keys != None:  # we had a response
            trials_2.addData('response.rt', response.rt)
        if response.keys == 'y':
            continueRoutine = True
        elif response.keys == 'n':
            continueRoutine = False 
        # the Routine "askAd" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # ------Prepare to start Routine "Choice2Loss"-------
        t = 0
        Choice2LossClock.reset()  # clock
        frameN = -1
        continueRoutine = True
        # update component parameters for each repeat
        text2.setColor([-1.000,-1.000,-1.000], colorSpace='rgb')
        text2.setText('I')
        text2.setPos((0, 0))
        text2.setFont('Arial')
        text2.setHeight(0.01)
        image_3.setImage(Loss2)
        image_3.setPos((0, 0))
        image_3.setSize((1.3, 0.9))
        image_3.setOpacity(1)
        image_3.setOri(0)
        resp2 = event.BuilderKeyResponse()
        checkR.setImage('check2.png')
        checkR.setPos((0, 0))
        checkR.setSize((2, 1))
        checkR.setOpacity(1)
        checkR.setOri(0)
        checkL.setImage('check3.png')
        checkL.setPos((0, 0))
        checkL.setSize((2, 1))
        checkL.setOpacity(1)
        checkL.setOri(0)
        
        # keep track of which components have finished
        Choice2LossComponents = [text2, image_3, resp2, checkR, checkL]
        for thisComponent in Choice2LossComponents:
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        
        # -------Start Routine "Choice2Loss"-------
        while continueRoutine:
            # get current time
            t = Choice2LossClock.getTime()
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *text2* updates
            if t >= 0.0 and text2.status == NOT_STARTED:
                # keep track of start time/frame for later
                text2.tStart = t
                text2.frameNStart = frameN  # exact frame index
                text2.setAutoDraw(True)
            frameRemains = 0.0 + 5- win.monitorFramePeriod * 0.75  # most of one frame period left
            if text2.status == STARTED and t >= frameRemains:
                text2.setAutoDraw(False)
            
            # *image_3* updates
            if t >= 0.0 and image_3.status == NOT_STARTED:
                # keep track of start time/frame for later
                image_3.tStart = t
                image_3.frameNStart = frameN  # exact frame index
                image_3.setAutoDraw(True)
            if image_3.status == STARTED and bool(resp2.status == FINISHED):
                image_3.setAutoDraw(False)
            
            # *resp2* updates
            if t >= 0.0 and resp2.status == NOT_STARTED:
                # keep track of start time/frame for later
                resp2.tStart = t
                resp2.frameNStart = frameN  # exact frame index
                resp2.status = STARTED
                # keyboard checking is just starting
                win.callOnFlip(resp2.clock.reset)  # t=0 on next screen flip
                event.clearEvents(eventType='keyboard')
            frameRemains = 0.0 + 4- win.monitorFramePeriod * 0.75  # most of one frame period left
            if resp2.status == STARTED and t >= frameRemains:
                resp2.status = STOPPED
            if resp2.status == STARTED:
                theseKeys = event.getKeys(keyList=['left', 'right'])
                
                # check for quit:
                if "escape" in theseKeys:
                    endExpNow = True
                if len(theseKeys) > 0:  # at least one key was pressed
                    resp2.keys = theseKeys[-1]  # just the last key pressed
                    resp2.rt = resp2.clock.getTime()
            
            # *checkR* updates
            if (resp2.keys == 'right') and checkR.status == NOT_STARTED:
                # keep track of start time/frame for later
                checkR.tStart = t
                checkR.frameNStart = frameN  # exact frame index
                checkR.setAutoDraw(True)
            if checkR.status == STARTED and t >= (checkR.tStart + 3):
                checkR.setAutoDraw(False)
            
            # *checkL* updates
            if (resp2.keys == 'left') and checkL.status == NOT_STARTED:
                # keep track of start time/frame for later
                checkL.tStart = t
                checkL.frameNStart = frameN  # exact frame index
                checkL.setAutoDraw(True)
            if checkL.status == STARTED and t >= (checkL.tStart + 3):
                checkL.setAutoDraw(False)
            
            checkL.autoLog=False
            checkR.autoLog=False
            
            
            if resp2.keys == 'left':
                checkL.autoDraw=True
            #elif resp.keys == 'right':
             #   checkR1.autoDraw=False
            
            if resp2.keys == 'right':
                checkR.autoDraw=True
            
            if text2.status == FINISHED:
                checkR.autoDraw=False
                checkL.autoDraw=False
                continueRoutine=False 
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in Choice2LossComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # check for quit (the Esc key)
            if endExpNow or event.getKeys(keyList=["escape"]):
                core.quit()
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "Choice2Loss"-------
        for thisComponent in Choice2LossComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # check responses
        if resp2.keys in ['', [], None]:  # No response was made
            resp2.keys=None
        trials_2.addData('resp2.keys',resp2.keys)
        if resp2.keys != None:  # we had a response
            trials_2.addData('resp2.rt', resp2.rt)
        checkL.autoLog=False
        checkR.autoLog=False
        
        
        
        if resp2.keys == 'left':
            checkL.autoDraw=True
        #elif resp.keys == 'right':
         #   checkR1.autoDraw=False
        
        if resp2.keys =='right':
            checkR.autoDraw=True
        
        if text2.status == FINISHED:
            checkR.autoDraw=False
            checkL.autoDraw=False 
        # the Routine "Choice2Loss" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        thisExp.nextEntry()
        
    # completed nRepsblock2 repeats of 'trials_2'
    
    thisExp.nextEntry()
    
# completed 1 repeats of 'trials_3'






# these shouldn't be strictly necessary (should auto-save)
thisExp.saveAsWideText(filename+'.csv')
thisExp.saveAsPickle(filename)
logging.flush()
# make sure everything is closed down
thisExp.abort()  # or data files will save again on exit
win.close()
core.quit()
