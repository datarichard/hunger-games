#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2021.1.4),
    on Tue Jun 29 21:01:38 2021
If you publish work using this script the most relevant publication is:

    Peirce J, Gray JR, Simpson S, MacAskill M, Höchenberger R, Sogo H, Kastman E, Lindeløv JK. (2019) 
        PsychoPy2: Experiments in behavior made easy Behav Res 51: 195. 
        https://doi.org/10.3758/s13428-018-01193-y

"""

from __future__ import absolute_import, division

from psychopy import locale_setup
from psychopy import prefs
from psychopy import sound, gui, visual, core, data, event, logging, clock, colors
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER)

import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle, choice as randchoice
import os  # handy system and path functions
import sys  # to get file system encoding

from psychopy.hardware import keyboard



# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(_thisDir)

# Store info about the experiment session
psychopyVersion = '2021.1.4'
expName = 'devaluation'  # from the Builder filename that created this script
expInfo = {'version': 'A', 'participant': ''}
dlg = gui.DlgFromDict(dictionary=expInfo, sortKeys=False, title=expName)
if dlg.OK == False:
    core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName
expInfo['psychopyVersion'] = psychopyVersion

# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
filename = _thisDir + os.sep + u"/data/" + os.sep + '%s_%s_%s' % (expInfo['participant'], expName, expInfo['date'])

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath='/Users/rich/Documents/Github/hunger-games/Devaluation_lastrun.py',
    savePickle=False, saveWideText=False,
    dataFileName=filename)
# save a log file for detail verbose info
logFile = logging.LogFile(filename+'.log', level=logging.DATA)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp
frameTolerance = 0.001  # how close to onset before 'same' frame

# Start Code - component code to be run after the window creation

# Setup the Window
win = visual.Window(
    size=[1440, 900], fullscr=False, screen=0, 
    winType='pyglet', allowGUI=True, allowStencil=False,
    monitor='testMonitor', color=[-1,-1,-1], colorSpace='rgb',
    blendMode='avg', useFBO=True)
# store frame rate of monitor if we can measure it
expInfo['frameRate'] = win.getActualFrameRate()
if expInfo['frameRate'] != None:
    frameDur = 1.0 / round(expInfo['frameRate'])
else:
    frameDur = 1.0 / 60.0  # could not measure, so guess

# create a default keyboard (e.g. to check for escape)
defaultKeyboard = keyboard.Keyboard()

# Initialize components for Routine "instr"
instrClock = core.Clock()
tilt=0
pressL = 0.0
pressR = 0.0
logging.log(level=logging.DATA, msg = "version " + expInfo['version'])
test_trigger = visual.TextStim(win=win, name='test_trigger',
    text="You have found one of the original\nvending machines. As before you\nwon't be shown any snacks on\nscreen. Use your memory to tilt it\nfor the snack you want. \n\nTry to steal as much as you can, as\nthis will determine what you will eat\nafterwards!\n\n           Press space to begin",
    font='Helvetica Bold',
    pos=[0, 0], height=0.075, wrapWidth=None, ori=0, 
    color='LightGray', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
trigger_resp = keyboard.Keyboard()

# Initialize components for Routine "test"
testClock = core.Clock()
CStest = visual.PatchStim(
    win=win, name='CStest',
    tex='images/vend.png', mask=None,
    ori=1.0, pos=[0, 0], size=[1.5, 2], sf=None, phase=0,
    color=[1,1,1], colorSpace='rgb', opacity=1,
    texRes=512
, interpolate=True, depth=-1.0)

# Initialize components for Routine "ITI"
ITIClock = core.Clock()
fixation = visual.TextStim(win=win, name='fixation',
    text='+',
    font='Arial',
    pos=[0, 0], height=.5, wrapWidth=None, ori=0, 
    color='LightGray', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);

# Initialize components for Routine "Teddies"
TeddiesClock = core.Clock()
teddy_rating = visual.RatingScale(win=win, name='teddy_rating', acceptPreText='key, enter')
teddy_ratingImage = visual.ImageStim(
    win=win,
    name='teddy_ratingImage', 
    image='images/teddy.png', mask=None,
    ori=0, pos=[0, 0.1], size=[0.4, 0.5],
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=512, interpolate=True, depth=-1.0)
teddy_ratingText = visual.TextStim(win=win, name='teddy_ratingText',
    text='How much do you like tiny teddies?',
    font='Helvetica Bold',
    pos=[0, 0.5], height=.075, wrapWidth=None, ori=0, 
    color='LightGray', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);

# Initialize components for Routine "MMs"
MMsClock = core.Clock()
MM_rating = visual.RatingScale(win=win, name='MM_rating', acceptPreText='key, enter')
MM_ratingImage = visual.ImageStim(
    win=win,
    name='MM_ratingImage', 
    image='images/M&M.png', mask=None,
    ori=0, pos=[0, 0.1], size=[0.4, 0.5],
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=512, interpolate=True, depth=-1.0)
MM_ratingText = visual.TextStim(win=win, name='MM_ratingText',
    text='How much do you like M&Ms?',
    font='Helvetica Bold',
    pos=[0, 0.5], height=0.075, wrapWidth=None, ori=0, 
    color='LightGray', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);

# Initialize components for Routine "BBQ"
BBQClock = core.Clock()
BBQ_rating = visual.RatingScale(win=win, name='BBQ_rating', acceptPreText='key, enter')
BBQ_ratingImage = visual.ImageStim(
    win=win,
    name='BBQ_ratingImage', 
    image='images/BBQ.png', mask=None,
    ori=0, pos=[0, 0.1], size=[0.4, 0.5],
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=512, interpolate=True, depth=-1.0)
BBQ_ratingText = visual.TextStim(win=win, name='BBQ_ratingText',
    text='How much do you like BBQ shapes?',
    font='Helvetica Bold',
    pos=[0, 0.5], height=0.075, wrapWidth=None, ori=0, 
    color='LightGray', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);

# Initialize components for Routine "hunger"
hungerClock = core.Clock()
Hunger_rating = visual.RatingScale(win=win, name='Hunger_rating', acceptPreText='key, enter')
Hunger_text = visual.TextStim(win=win, name='Hunger_text',
    text='How hungry are you right now?',
    font='Helvetica Bold',
    pos=[0, 0.5], height=0.075, wrapWidth=None, ori=0, 
    color='LightGray', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);

# Initialize components for Routine "finish"
finishClock = core.Clock()
finish_text = visual.TextStim(win=win, name='finish_text',
    text='Thankyou!',
    font='Helvetica Bold',
    pos=[0, 0.5], height=0.075, wrapWidth=None, ori=0, 
    color='LightGray', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

# ------Prepare to start Routine "instr"-------
continueRoutine = True
# update component parameters for each repeat
trigger_resp.keys = []
trigger_resp.rt = []
_trigger_resp_allKeys = []
# keep track of which components have finished
instrComponents = [test_trigger, trigger_resp]
for thisComponent in instrComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
instrClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "instr"-------
while continueRoutine:
    # get current time
    t = instrClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=instrClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    
    
    # *test_trigger* updates
    if test_trigger.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        test_trigger.frameNStart = frameN  # exact frame index
        test_trigger.tStart = t  # local t and not account for scr refresh
        test_trigger.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(test_trigger, 'tStartRefresh')  # time at next scr refresh
        test_trigger.setAutoDraw(True)
    
    # *trigger_resp* updates
    waitOnFlip = False
    if trigger_resp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        trigger_resp.frameNStart = frameN  # exact frame index
        trigger_resp.tStart = t  # local t and not account for scr refresh
        trigger_resp.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(trigger_resp, 'tStartRefresh')  # time at next scr refresh
        trigger_resp.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(trigger_resp.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(trigger_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if trigger_resp.status == STARTED and not waitOnFlip:
        theseKeys = trigger_resp.getKeys(keyList=['space'], waitRelease=False)
        _trigger_resp_allKeys.extend(theseKeys)
        if len(_trigger_resp_allKeys):
            trigger_resp.keys = _trigger_resp_allKeys[-1].name  # just the last key pressed
            trigger_resp.rt = _trigger_resp_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in instrComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "instr"-------
for thisComponent in instrComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('test_trigger.started', test_trigger.tStartRefresh)
thisExp.addData('test_trigger.stopped', test_trigger.tStopRefresh)
# the Routine "instr" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
trials = data.TrialHandler(nReps=4, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=[None],
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
    
    # ------Prepare to start Routine "test"-------
    continueRoutine = True
    routineTimer.add(6.000000)
    # update component parameters for each repeat
    tilt = 0
    pressL = 0.0
    pressR = 0.0
    logging.log(level=logging.DATA, msg = 'start')
    # keep track of which components have finished
    testComponents = [CStest]
    for thisComponent in testComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    testClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "test"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = testClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=testClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        if tilt > 0:
         tilt  = tilt-1
        if tilt < 0:
         tilt = tilt+1
        
        if event.getKeys(['t']):
         pressL = pressL+1
         tilt = -15
        
        if event.getKeys(['v']):
         pressR=pressR+1
         tilt = 15
        
        
        
        # *CStest* updates
        if CStest.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            CStest.frameNStart = frameN  # exact frame index
            CStest.tStart = t  # local t and not account for scr refresh
            CStest.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(CStest, 'tStartRefresh')  # time at next scr refresh
            CStest.setAutoDraw(True)
        if CStest.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > CStest.tStartRefresh + 6-frameTolerance:
                # keep track of stop time/frame for later
                CStest.tStop = t  # not accounting for scr refresh
                CStest.frameNStop = frameN  # exact frame index
                win.timeOnFlip(CStest, 'tStopRefresh')  # time at next scr refresh
                CStest.setAutoDraw(False)
        if CStest.status == STARTED:  # only update if drawing
            CStest.setOri(tilt)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in testComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "test"-------
    for thisComponent in testComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    logging.log(level=logging.DATA, msg = 'end')
    trials.addData('CStest.started', CStest.tStartRefresh)
    trials.addData('CStest.stopped', CStest.tStopRefresh)
    
    # ------Prepare to start Routine "ITI"-------
    continueRoutine = True
    # update component parameters for each repeat
    dur = randint(5,10)
    tilt = 0
    # keep track of which components have finished
    ITIComponents = [fixation]
    for thisComponent in ITIComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    ITIClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "ITI"-------
    while continueRoutine:
        # get current time
        t = ITIClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=ITIClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *fixation* updates
        if fixation.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            fixation.frameNStart = frameN  # exact frame index
            fixation.tStart = t  # local t and not account for scr refresh
            fixation.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(fixation, 'tStartRefresh')  # time at next scr refresh
            fixation.setAutoDraw(True)
        if fixation.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > fixation.tStartRefresh + dur-frameTolerance:
                # keep track of stop time/frame for later
                fixation.tStop = t  # not accounting for scr refresh
                fixation.frameNStop = frameN  # exact frame index
                win.timeOnFlip(fixation, 'tStopRefresh')  # time at next scr refresh
                fixation.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in ITIComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "ITI"-------
    for thisComponent in ITIComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    trials.addData('fixation.started', fixation.tStartRefresh)
    trials.addData('fixation.stopped', fixation.tStopRefresh)
    # the Routine "ITI" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 4 repeats of 'trials'


# ------Prepare to start Routine "Teddies"-------
continueRoutine = True
# update component parameters for each repeat
teddy_rating.reset()
# keep track of which components have finished
TeddiesComponents = [teddy_rating, teddy_ratingImage, teddy_ratingText]
for thisComponent in TeddiesComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
TeddiesClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "Teddies"-------
while continueRoutine:
    # get current time
    t = TeddiesClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=TeddiesClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    # *teddy_rating* updates
    if teddy_rating.status == NOT_STARTED and t >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        teddy_rating.frameNStart = frameN  # exact frame index
        teddy_rating.tStart = t  # local t and not account for scr refresh
        teddy_rating.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(teddy_rating, 'tStartRefresh')  # time at next scr refresh
        teddy_rating.setAutoDraw(True)
    continueRoutine &= teddy_rating.noResponse  # a response ends the trial
    
    # *teddy_ratingImage* updates
    if teddy_ratingImage.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        teddy_ratingImage.frameNStart = frameN  # exact frame index
        teddy_ratingImage.tStart = t  # local t and not account for scr refresh
        teddy_ratingImage.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(teddy_ratingImage, 'tStartRefresh')  # time at next scr refresh
        teddy_ratingImage.setAutoDraw(True)
    
    # *teddy_ratingText* updates
    if teddy_ratingText.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        teddy_ratingText.frameNStart = frameN  # exact frame index
        teddy_ratingText.tStart = t  # local t and not account for scr refresh
        teddy_ratingText.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(teddy_ratingText, 'tStartRefresh')  # time at next scr refresh
        teddy_ratingText.setAutoDraw(True)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in TeddiesComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "Teddies"-------
for thisComponent in TeddiesComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# store data for thisExp (ExperimentHandler)
thisExp.addData('teddy_rating.response', teddy_rating.getRating())
thisExp.nextEntry()
thisExp.addData('teddy_rating.started', teddy_rating.tStart)
thisExp.addData('teddy_rating.stopped', teddy_rating.tStop)
thisExp.addData('teddy_ratingImage.started', teddy_ratingImage.tStartRefresh)
thisExp.addData('teddy_ratingImage.stopped', teddy_ratingImage.tStopRefresh)
thisExp.addData('teddy_ratingText.started', teddy_ratingText.tStartRefresh)
thisExp.addData('teddy_ratingText.stopped', teddy_ratingText.tStopRefresh)
# the Routine "Teddies" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "MMs"-------
continueRoutine = True
# update component parameters for each repeat
MM_rating.reset()
# keep track of which components have finished
MMsComponents = [MM_rating, MM_ratingImage, MM_ratingText]
for thisComponent in MMsComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
MMsClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "MMs"-------
while continueRoutine:
    # get current time
    t = MMsClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=MMsClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    # *MM_rating* updates
    if MM_rating.status == NOT_STARTED and t >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        MM_rating.frameNStart = frameN  # exact frame index
        MM_rating.tStart = t  # local t and not account for scr refresh
        MM_rating.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(MM_rating, 'tStartRefresh')  # time at next scr refresh
        MM_rating.setAutoDraw(True)
    continueRoutine &= MM_rating.noResponse  # a response ends the trial
    
    # *MM_ratingImage* updates
    if MM_ratingImage.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        MM_ratingImage.frameNStart = frameN  # exact frame index
        MM_ratingImage.tStart = t  # local t and not account for scr refresh
        MM_ratingImage.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(MM_ratingImage, 'tStartRefresh')  # time at next scr refresh
        MM_ratingImage.setAutoDraw(True)
    
    # *MM_ratingText* updates
    if MM_ratingText.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        MM_ratingText.frameNStart = frameN  # exact frame index
        MM_ratingText.tStart = t  # local t and not account for scr refresh
        MM_ratingText.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(MM_ratingText, 'tStartRefresh')  # time at next scr refresh
        MM_ratingText.setAutoDraw(True)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in MMsComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "MMs"-------
for thisComponent in MMsComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# store data for thisExp (ExperimentHandler)
thisExp.addData('MM_rating.response', MM_rating.getRating())
thisExp.nextEntry()
thisExp.addData('MM_rating.started', MM_rating.tStart)
thisExp.addData('MM_rating.stopped', MM_rating.tStop)
thisExp.addData('MM_ratingImage.started', MM_ratingImage.tStartRefresh)
thisExp.addData('MM_ratingImage.stopped', MM_ratingImage.tStopRefresh)
thisExp.addData('MM_ratingText.started', MM_ratingText.tStartRefresh)
thisExp.addData('MM_ratingText.stopped', MM_ratingText.tStopRefresh)
# the Routine "MMs" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "BBQ"-------
continueRoutine = True
# update component parameters for each repeat
BBQ_rating.reset()
# keep track of which components have finished
BBQComponents = [BBQ_rating, BBQ_ratingImage, BBQ_ratingText]
for thisComponent in BBQComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
BBQClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "BBQ"-------
while continueRoutine:
    # get current time
    t = BBQClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=BBQClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    # *BBQ_rating* updates
    if BBQ_rating.status == NOT_STARTED and t >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        BBQ_rating.frameNStart = frameN  # exact frame index
        BBQ_rating.tStart = t  # local t and not account for scr refresh
        BBQ_rating.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(BBQ_rating, 'tStartRefresh')  # time at next scr refresh
        BBQ_rating.setAutoDraw(True)
    continueRoutine &= BBQ_rating.noResponse  # a response ends the trial
    
    # *BBQ_ratingImage* updates
    if BBQ_ratingImage.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        BBQ_ratingImage.frameNStart = frameN  # exact frame index
        BBQ_ratingImage.tStart = t  # local t and not account for scr refresh
        BBQ_ratingImage.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(BBQ_ratingImage, 'tStartRefresh')  # time at next scr refresh
        BBQ_ratingImage.setAutoDraw(True)
    
    # *BBQ_ratingText* updates
    if BBQ_ratingText.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        BBQ_ratingText.frameNStart = frameN  # exact frame index
        BBQ_ratingText.tStart = t  # local t and not account for scr refresh
        BBQ_ratingText.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(BBQ_ratingText, 'tStartRefresh')  # time at next scr refresh
        BBQ_ratingText.setAutoDraw(True)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in BBQComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "BBQ"-------
for thisComponent in BBQComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# store data for thisExp (ExperimentHandler)
thisExp.addData('BBQ_rating.response', BBQ_rating.getRating())
thisExp.nextEntry()
thisExp.addData('BBQ_rating.started', BBQ_rating.tStart)
thisExp.addData('BBQ_rating.stopped', BBQ_rating.tStop)
thisExp.addData('BBQ_ratingImage.started', BBQ_ratingImage.tStartRefresh)
thisExp.addData('BBQ_ratingImage.stopped', BBQ_ratingImage.tStopRefresh)
thisExp.addData('BBQ_ratingText.started', BBQ_ratingText.tStartRefresh)
thisExp.addData('BBQ_ratingText.stopped', BBQ_ratingText.tStopRefresh)
# the Routine "BBQ" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "hunger"-------
continueRoutine = True
# update component parameters for each repeat
Hunger_rating.reset()
# keep track of which components have finished
hungerComponents = [Hunger_rating, Hunger_text]
for thisComponent in hungerComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
hungerClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "hunger"-------
while continueRoutine:
    # get current time
    t = hungerClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=hungerClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    # *Hunger_rating* updates
    if Hunger_rating.status == NOT_STARTED and t >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        Hunger_rating.frameNStart = frameN  # exact frame index
        Hunger_rating.tStart = t  # local t and not account for scr refresh
        Hunger_rating.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Hunger_rating, 'tStartRefresh')  # time at next scr refresh
        Hunger_rating.setAutoDraw(True)
    continueRoutine &= Hunger_rating.noResponse  # a response ends the trial
    
    # *Hunger_text* updates
    if Hunger_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        Hunger_text.frameNStart = frameN  # exact frame index
        Hunger_text.tStart = t  # local t and not account for scr refresh
        Hunger_text.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Hunger_text, 'tStartRefresh')  # time at next scr refresh
        Hunger_text.setAutoDraw(True)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in hungerComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "hunger"-------
for thisComponent in hungerComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# store data for thisExp (ExperimentHandler)
thisExp.addData('Hunger_rating.response', Hunger_rating.getRating())
thisExp.nextEntry()
thisExp.addData('Hunger_rating.started', Hunger_rating.tStart)
thisExp.addData('Hunger_rating.stopped', Hunger_rating.tStop)
thisExp.addData('Hunger_text.started', Hunger_text.tStartRefresh)
thisExp.addData('Hunger_text.stopped', Hunger_text.tStopRefresh)
# the Routine "hunger" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "finish"-------
continueRoutine = True
# update component parameters for each repeat
# keep track of which components have finished
finishComponents = [finish_text]
for thisComponent in finishComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
finishClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "finish"-------
while continueRoutine:
    # get current time
    t = finishClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=finishClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *finish_text* updates
    if finish_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        finish_text.frameNStart = frameN  # exact frame index
        finish_text.tStart = t  # local t and not account for scr refresh
        finish_text.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(finish_text, 'tStartRefresh')  # time at next scr refresh
        finish_text.setAutoDraw(True)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in finishComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "finish"-------
for thisComponent in finishComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('finish_text.started', finish_text.tStartRefresh)
thisExp.addData('finish_text.stopped', finish_text.tStopRefresh)
# the Routine "finish" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# Flip one final time so any remaining win.callOnFlip() 
# and win.timeOnFlip() tasks get executed before quitting
win.flip()

# these shouldn't be strictly necessary (should auto-save)
logging.flush()
# make sure everything is closed down
thisExp.abort()  # or data files will save again on exit
win.close()
core.quit()
