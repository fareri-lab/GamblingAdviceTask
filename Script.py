from __future__ import absolute_import, division
from psychopy import locale_setup, sound, gui, visual, core, data, event, logging
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED, STOPPED, FINISHED, PRESSED, RELEASED, FOREVER)
import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average, sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle
import os  # handy system and path functions
import sys

_thisDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(_thisDir)

expName = 'Test' 
expInfo = {'participant': '', 'session': '001'}
dlg = gui.DlgFromDict(dictionary=expInfo, title=expName)
if dlg.OK == False:
    core.quit() 
expInfo['date'] = data.getDateStr()
expInfo['expName'] = expName

filename = _thisDir + os.sep + u'data/%s_%s_%s' % (expInfo['participant'], expName, expInfo['date'])


thisExp = data.ExperimentHandler(name=expName, version='', extraInfo=expInfo, runtimeInfo=None, originPath=u'C:\\Users\\farerilab\\Downloads\\GamblingAdviceTask\\Test1.psyexp', savePickle=True, saveWideText=True, dataFileName=filename)
logFile = logging.LogFile(filename+'.log', level=logging.EXP)
logging.console.setLevel(logging.WARNING)

# Create timers
globalClock = core.Clock()  
routineTimer = core.CountdownTimer() 

# set up handler to look after randomisation of conditions
trials_3 = data.TrialHandler(nReps=1, method='fullRandom', extraInfo=expInfo, originPath=-1, trialList=data.importConditions(u'Conditions.csv'), seed=None, name='trials_3')
thisExp.addLoop(trials_3)  # add the loop to the experiment
thisTrial_3 = trials_3.trialList[0] 

# Setup the Window
win = visual.Window( size=(1920, 1080), fullscr=True, screen=0, allowGUI=False, allowStencil=False, monitor='testMonitor', color=[-1,-1,-1], colorSpace='rgb', blendMode='avg', useFBO=True, units='height')
# store frame rate of monitor if we can measure it
expInfo['frameRate'] = win.getActualFrameRate()
if expInfo['frameRate'] != None:
    frameDur = 1.0 / round(expInfo['frameRate'])
else:
    frameDur = 1.0 / 60.0 

# Initialize components for Routine "code_2"
code_2Clock = core.Clock()
nRepsblock1=0
nRepsblock2=0


# Initialize components for Routine "ISI"
ISIClock = core.Clock()
iSi = visual.TextStim(win=win, name='iSi', text='+', font='Arial', pos=(0, 0), height=0.08, wrapWidth=None, ori=0, color='white', colorSpace='rgb', opacity=1, depth=0.0);

# Initialize components for Routine "Receive_money"
Receive_moneyClock = core.Clock()
receive = visual.TextStim(win=win, name='receive', text='$Amount', font='Arial', pos=[0,0], height=1.0, wrapWidth=None, ori=0, color=1.0, colorSpace='rgb', opacity=1, depth=0.0);

# Initialize components for Routine "trial"
trialClock = core.Clock()
image = visual.ImageStim( win=win, name='image', image='$Gain', mask=None, ori=1.0, pos=[0,0], size=(1.3, 0.9), color=[1,1,1], colorSpace='rgb', opacity=1.0, flipHoriz=False, flipVert=False, texRes=128, interpolate=True, depth=0.0)

# Initialize components for Routine "askAd"
askAdClock = core.Clock()
text_3 = visual.TextStim(win=win, name='text_3', text='Y                 N', font='Arial', pos=(0, -0.2), height=0.09, wrapWidth=None, color='white', colorSpace='rgb');
ask = visual.TextStim(win=win, name='ask', text='Would you like to hear advice from your financial advisor?', font='Arial', pos=(0, 0.11), height=0.05, wrapWidth=None, color='white', colorSpace='rgb');
Advice = visual.TextStim(win=win, name='Advice', text='$AdviceVar', font='Arial', pos=[0,0], height=1.0, wrapWidth=None, color=1.0, colorSpace='rgb');


# Initialize components for Routine "Choice2Gain"
Choice2GainClock = core.Clock()
text1 = visual.TextStim(win=win, name='text1', text='I', font='Arial', pos=[0,0], height=0.01, wrapWidth=None, ori=0, color=[-1.000,-1.000,-1.000], colorSpace='rgb', opacity=1, depth=0.0);
image_5 = visual.ImageStim( win=win, name='image_5', image=Gain1, mask=None, ori=1.0, pos=[0,0], size=(1.3, 0.9), color=[1,1,1], colorSpace='rgb', opacity=1.0, texRes=128, interpolate=True, depth=-1.0)
checkL1 = visual.ImageStim(win=win, name='checkL1', image='check2.png', mask=None, ori=1.0, pos=[0,0], size=(2, 1), color=1.0, colorSpace='rgb', opacity=1.0, texRes=128, interpolate=True, depth=-3.0)
checkR1 = visual.ImageStim( win=win, name='checkR1', image='check3.png', mask=None, ori=1.0, pos=[0,0], size=1.0, color=1.0, colorSpace='rgb', opacity=1.0, flipHoriz=False, flipVert=False, texRes=128, interpolate=True, depth=-4.0)

# Initialize components for Routine "loseTrial"
loseTrialClock = core.Clock()
image_2 = visual.ImageStim( win=win, name='image_2', image='$Loss', mask=None, ori=1.0, pos=[0,0], size=(1.3, 0.9), colorSpace='rgb', opacity=1.0, texRes=128, interpolate=True, depth=0.0)



# Initialize components for Routine "Choice2Loss"
Choice2LossClock = core.Clock()
text2 = visual.TextStim(win=win, name='text2', text='I', font='Arial', pos=[0,0], height=0.01, wrapWidth=None, ori=0, color=[-1.000,-1.000,-1.000], colorSpace='rgb', opacity=1, depth=0.0);
image_3 = visual.ImageStim( win=win, name='image_3', image='$Loss1', mask=None, ori=1.0, pos=[0,0], size=1.0, color=[1,1,1], colorSpace='rgb', opacity=1.0, flipHoriz=False, flipVert=False, texRes=128, interpolate=True, depth=-1.0)


if thisTrial_3 != None:
    for paramName in thisTrial_3.keys():
        exec(paramName + '= thisTrial_3.' + paramName)

for thisTrial_3 in trials_3:
    currentLoop = trials_3

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
        frameN = frameN + 1          
        
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
    trials = data.TrialHandler(nReps=nRepsblock1, method='sequential', extraInfo=expInfo, originPath=-1, trialList=data.importConditions(u'Conditions.csv'), seed=None, name='trials')
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
                iSi.tStart = t
                iSi.frameNStart = frameN  # exact frame index
                iSi.setAutoDraw(True)
            frameRemains = 0.0 + 3- win.monitorFramePeriod * 0.75  # most of one frame period left
            if iSi.status == STARTED and t >= frameRemains:
                iSi.setAutoDraw(False)
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in ISIComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # check for quit (the Esc key)
            if endExpNow or event.getKeys(keyList=["escape"]):
                core.quit()

        
        # -------Ending Routine "ISI"-------
        for thisComponent in ISIComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
                
        # ------Prepare to start Routine "Receive_money"-------
        t = 0
        Receive_moneyClock.reset()  # clock
        frameN = -1
        continueRoutine = True
        routineTimer.add(4.000000)

        # keep track of which components have finished
        Receive_moneyComponents = [receive, iSi]
        for thisComponent in Receive_moneyComponents:
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
                receive.tStart = t
                receive.frameNStart = frameN  # exact frame index
                receive.setAutoDraw(True)
            frameRemains = 0.0 + 2- win.monitorFramePeriod * 0.75  # most of one frame period left
            if receive.status == STARTED and t >= frameRemains:
                receive.setAutoDraw(False)
            
            # *ISI2* updates
            if t >= 2 and iSi.status == NOT_STARTED:
                # keep track of start time/frame for later
                iSi.tStart = t
                iSi.frameNStart = frameN  # exact frame index
                iSi.setAutoDraw(True)
            frameRemains = 2 + 2- win.monitorFramePeriod * 0.75  # most of one frame period left
            if iSi.status == STARTED and t >= frameRemains:
                iSi.setAutoDraw(False)
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in Receive_moneyComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # check for quit (the Esc key)
            if endExpNow or event.getKeys(keyList=["escape"]):
                core.quit()
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "Receive_money"-------
        for thisComponent in Receive_moneyComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        
        # ------Prepare to start Routine "trial"-------
        t = 0
        trialClock.reset()  # clock
        frameN = -1
        continueRoutine = True
        routineTimer.add(4.000000)

        # keep track of which components have finished
        trialComponents = [image]
        for thisComponent in trialComponents:
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        
        # -------Start Routine "trial"-------
        while continueRoutine and routineTimer.getTime() > 0:
            t = trialClock.getTime()
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            
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

        askAdComponents = [text_3, ask, response, Advice]
        for thisComponent in askAdComponents:
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        
        # -------Start Routine "askAd"-------
        while continueRoutine:
            # get current time
            t = askAdClock.getTime()
            frameN = frameN + 1  
            
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
            frameRemains = 0.0 + 4- win.monitorFramePeriod * 0.75  # most of one frame period left
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
            
            if resp.keys == 'right':
                checkR1.autoDraw=True
            
            if text1.status == FINISHED:
                checkR1.autoDraw=False
                checkL1.autoDraw=False
                continueRoutine=False

            
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
        
        if resp.keys =='right':
            checkR1.autoDraw=True
        
        if text1.status == FINISHED:
            checkR1.autoDraw=False
            checkL1.autoDraw=False

        routineTimer.reset()
        thisExp.nextEntry()
        
    
    # set up handler to look after randomisation of conditions etc
    trials_2 = data.TrialHandler(nReps=nRepsblock2, method='sequential', 
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
                
                # ------Prepare to start Routine "ISI"-------
        t = 0
        ISIClock.reset()  # clock
        frameN = -1
        continueRoutine = True
        routineTimer.add(3.000000)

        ISIComponents = [iSi]
        for thisComponent in ISIComponents:
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        
        # -------Start Routine "ISI"-------
        while continueRoutine and routineTimer.getTime() > 0:
            # get current time
            t = ISIClock.getTime()
            frameN = frameN + 1  
            
            # *iSi* updates
            if t >= 0.0 and iSi.status == NOT_STARTED:
                # keep track of start time/frame for later
                iSi.tStart = t
                iSi.frameNStart = frameN  # exact frame index
                iSi.setAutoDraw(True)
            frameRemains = 0.0 + 3- win.monitorFramePeriod * 0.75  # most of one frame period left
            if iSi.status == STARTED and t >= frameRemains:
                iSi.setAutoDraw(False)
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in ISIComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # check for quit (the Esc key)
            if endExpNow or event.getKeys(keyList=["escape"]):
                core.quit()
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "ISI"-------
        for thisComponent in ISIComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
                

        
        # ------Prepare to start Routine "Receive_money"-------
        t = 0
        Receive_moneyClock.reset()  # clock
        frameN = -1
        continueRoutine = True
        routineTimer.add(4.000000)

        # keep track of which components have finished
        Receive_moneyComponents = [receive, iSi]
        for thisComponent in Receive_moneyComponents:
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
                receive.tStart = t
                receive.frameNStart = frameN  # exact frame index
                receive.setAutoDraw(True)
            frameRemains = 0.0 + 2- win.monitorFramePeriod * 0.75  # most of one frame period left
            if receive.status == STARTED and t >= frameRemains:
                receive.setAutoDraw(False)
            
            # *ISI2* updates
            if t >= 2 and iSi.status == NOT_STARTED:
                # keep track of start time/frame for later
                iSi.tStart = t
                iSi.frameNStart = frameN  # exact frame index
                iSi.setAutoDraw(True)
            frameRemains = 2 + 2- win.monitorFramePeriod * 0.75  # most of one frame period left
            if iSi.status == STARTED and t >= frameRemains:
                iSi.setAutoDraw(False)
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in Receive_moneyComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # check for quit (the Esc key)
            if endExpNow or event.getKeys(keyList=["escape"]):
                core.quit()
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "Receive_money"-------
        for thisComponent in Receive_moneyComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        
        # ------Prepare to start Routine "loseTrial"-------
        t = 0
        loseTrialClock.reset()  # clock
        frameN = -1
        continueRoutine = True
        routineTimer.add(4.000000)

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
        resp2 = event.BuilderKeyResponse()

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
            frameRemains = 0.0 + 4- win.monitorFramePeriod * 0.75  # most of one frame period left
            if text2.status == STARTED and t >= frameRemains:
                text2.setAutoDraw(False)
            
            # *image_3* updates
            if t >= 0.0 and image_3.status == NOT_STARTED:
                # keep track of start time/frame for later
                image_3.tStart = t
                image_3.frameNStart = frameN  # exact frame index
                image_3.setAutoDraw(True)
            frameRemains = 0.0 + 4- win.monitorFramePeriod * 0.75  # most of one frame period left
            if image_3.status == STARTED and t >= frameRemains:
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

        
        if resp2.keys =='right':
            checkR.autoDraw=True
        
        if text2.status == FINISHED:
            checkR.autoDraw=False
            checkL.autoDraw=False 

        routineTimer.reset()
        thisExp.nextEntry()
        
    # completed nRepsblock2 repeats of 'trials_2'
    
    thisExp.nextEntry()
    
# completed 1 repeats of 'trials_3'



thisExp.saveAsWideText(filename+'.csv')
thisExp.saveAsPickle(filename)
logging.flush()
# make sure everything is closed down
thisExp.abort()  
win.close()
core.quit()
