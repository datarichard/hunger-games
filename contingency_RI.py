#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2021.1.4),
    on Wed Jun 30 13:10:35 2021
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
expName = 'contingency'  # from the Builder filename that created this script
expInfo = {'version': 'A', 'participant': 'CON'}
dlg = gui.DlgFromDict(dictionary=expInfo, sortKeys=False, title=expName)
if dlg.OK == False:
    core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName
expInfo['psychopyVersion'] = psychopyVersion

# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
filename = _thisDir + os.sep + 'data' + os.sep + '%s_%s_%s' % (expInfo['participant'], expName, expInfo['date'])

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath='/Users/rich/Documents/Github/hunger-games/contingency_RI.py',
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
    size=[1792, 1120], fullscr=True, screen=0, 
    winType='pyglet', allowGUI=False, allowStencil=False,
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

# Initialize components for Routine "Begin"
BeginClock = core.Clock()
press_space = keyboard.Keyboard()
Instruc_text = visual.TextStim(win=win, name='Instruc_text',
    text='You can steal snacks from our vending machines by tilting them to the left or to the right. Use the button pad to tilt left and right. Find out which direction releases the most snacks.',
    font='Arial',
    pos=[0, 0.3], height=0.1, wrapWidth=1.5, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
Begin_text = visual.TextStim(win=win, name='Begin_text',
    text='Press space to begin',
    font='Arial',
    pos=[0, -0.5], height=0.1, wrapWidth=1.5, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);

# Initialize components for Routine "Update"
UpdateClock = core.Clock()

# Initialize components for Routine "Trial"
TrialClock = core.Clock()
PressA = False
PressB = False
vending = visual.ImageStim(
    win=win,
    name='vending', 
    image='images/vend.png', mask=None,
    ori=1.0, pos=[0, 0], size=[2, 2],
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=512, interpolate=True, depth=-2.0)

# Initialize components for Routine "win_A"
win_AClock = core.Clock()
vendingA = visual.PatchStim(
    win=win, name='vendingA',
    tex='images/vend.png', mask=None,
    ori=1.0, pos=[0, 0], size=[2, 2], sf=None, phase=0.0,
    color=[1,1,1], colorSpace='rgb', opacity=1,
    texRes=512
, interpolate=True, depth=0.0)
snackA = visual.ImageStim(
    win=win,
    name='snackA', 
    image='sin', mask=None,
    ori=0, pos=[0, -0.5], size=[0.5, 0.5],
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=512, interpolate=True, depth=-1.0)

# Initialize components for Routine "win_B"
win_BClock = core.Clock()
vendingB = visual.ImageStim(
    win=win,
    name='vendingB', 
    image='images/vend.png', mask=None,
    ori=1.0, pos=[0, 0], size=[2, 2],
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=512, interpolate=True, depth=0.0)
snackB = visual.ImageStim(
    win=win,
    name='snackB', 
    image='sin', mask=None,
    ori=0, pos=[0, -0.5], size=[0.5, 0.5],
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=512, interpolate=True, depth=-1.0)

# Initialize components for Routine "Rate_A"
Rate_AClock = core.Clock()
testSnackA = visual.ImageStim(
    win=win,
    name='testSnackA', 
    image='sin', mask=None,
    ori=0, pos=[0, 0], size=[0.5, 0.5],
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=512, interpolate=True, depth=0.0)
rateA_text = visual.TextStim(win=win, name='rateA_text',
    text='',
    font='Arial',
    pos=[0, 0.5], height=0.1, wrapWidth=1.5, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
sliderA = visual.Slider(win=win, name='sliderA',
    size=(1.0, 0.1), pos=(0, -0.4), units=None,
    labels=(1, 2, 3, 4, 5), ticks=(1, 2, 3, 4, 5), granularity=0,
    style=['rating'], styleTweaks=(), opacity=1,
    color='LightGray', fillColor='Red', borderColor='White', colorSpace='rgb',
    font='HelveticaBold', labelHeight=0.05,
    flip=False, depth=-2, readOnly=False)

# Initialize components for Routine "Rate_B"
Rate_BClock = core.Clock()
testSnackB = visual.ImageStim(
    win=win,
    name='testSnackB', 
    image='sin', mask=None,
    ori=0, pos=[0, 0], size=[0.5, 0.5],
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=512, interpolate=True, depth=0.0)
rateB_text = visual.TextStim(win=win, name='rateB_text',
    text='',
    font='Arial',
    pos=[0, 0.5], height=0.1, wrapWidth=1.5, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
sliderB = visual.Slider(win=win, name='sliderB',
    size=(1.0, 0.1), pos=(0, -0.4), units=None,
    labels=(1, 2, 3, 4, 5), ticks=(1, 2, 3, 4, 5), granularity=0,
    style=['rating'], styleTweaks=(), opacity=1,
    color='LightGray', fillColor='Red', borderColor='White', colorSpace='rgb',
    font='HelveticaBold', labelHeight=0.05,
    flip=False, depth=-2, readOnly=False)

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

# ------Prepare to start Routine "Begin"-------
continueRoutine = True
# update component parameters for each repeat
press_space.keys = []
press_space.rt = []
_press_space_allKeys = []
if expInfo['version'] == 'A':
   rewardA = 'images/M&M.png'
   rewardB = 'images/BBQ.png'
   msgA = 'How effective was tilting the machine to get M&Ms?'
   msgB = 'How effective was tilting the machine to get BBQ shapes?'
   logging.log(level=logging.DATA, msg = 'version A')
if expInfo['version'] == 'B':
   rewardA = 'images/BBQ.png'
   rewardB = 'images/M&M.png'
   msgB = 'How effective was tilting the machine to get M&Ms?'
   msgA = 'How effective was tilting the machine to get BBQ shapes?'
   logging.log(level=logging.DATA, msg = 'version B')
if expInfo['version'] == 'C':
   rewardA = 'images/teddy.png'
   rewardB = 'images/BBQ.png'
   msgA = 'How effective was tilting the machine to get tiny teddys?'
   msgB = 'How effective was tilting the machine to get BBQ shapes?'
   logging.log(level=logging.DATA, msg = 'version C')
if expInfo['version'] == 'D':
   rewardA = 'images/BBQ.png'
   rewardB = 'images/teddy.png'
   msgB = 'How effective was tilting the machine to get tiny teddys?'
   msgA = 'How effective was tilting the machine to get BBQ shapes?'
   logging.log(level=logging.DATA, msg = 'version D')
if expInfo['version'] == 'E':
   rewardA = 'images/M&M.png'
   rewardB = 'images/teddy.png'
   msgA = 'How effective was tilting the machine to get M&Ms?'
   msgB = 'How effective was tilting the machine to get tiny teddys?'
   logging.log(level=logging.DATA, msg = 'version E')
if expInfo['version'] == 'F':
   rewardA = 'images/teddy.png'
   rewardB = 'images/M&M.png'
   msgB = 'How effective was tilting the machine to get M&Ms?'
   msgA = 'How effective was tilting the machine to get tiny teddys?'
   logging.log(level=logging.DATA, msg = 'version F')

# keep track of which components have finished
BeginComponents = [press_space, Instruc_text, Begin_text]
for thisComponent in BeginComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
BeginClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "Begin"-------
while continueRoutine:
    # get current time
    t = BeginClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=BeginClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *press_space* updates
    waitOnFlip = False
    if press_space.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        press_space.frameNStart = frameN  # exact frame index
        press_space.tStart = t  # local t and not account for scr refresh
        press_space.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(press_space, 'tStartRefresh')  # time at next scr refresh
        press_space.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(press_space.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(press_space.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if press_space.status == STARTED and not waitOnFlip:
        theseKeys = press_space.getKeys(keyList=['space'], waitRelease=False)
        _press_space_allKeys.extend(theseKeys)
        if len(_press_space_allKeys):
            press_space.keys = _press_space_allKeys[-1].name  # just the last key pressed
            press_space.rt = _press_space_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # *Instruc_text* updates
    if Instruc_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        Instruc_text.frameNStart = frameN  # exact frame index
        Instruc_text.tStart = t  # local t and not account for scr refresh
        Instruc_text.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Instruc_text, 'tStartRefresh')  # time at next scr refresh
        Instruc_text.setAutoDraw(True)
    
    # *Begin_text* updates
    if Begin_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        Begin_text.frameNStart = frameN  # exact frame index
        Begin_text.tStart = t  # local t and not account for scr refresh
        Begin_text.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Begin_text, 'tStartRefresh')  # time at next scr refresh
        Begin_text.setAutoDraw(True)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in BeginComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "Begin"-------
for thisComponent in BeginComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if press_space.keys in ['', [], None]:  # No response was made
    press_space.keys = None
thisExp.addData('press_space.keys',press_space.keys)
if press_space.keys != None:  # we had a response
    thisExp.addData('press_space.rt', press_space.rt)
thisExp.addData('press_space.started', press_space.tStartRefresh)
thisExp.addData('press_space.stopped', press_space.tStopRefresh)
thisExp.nextEntry()
thisExp.addData('Instruc_text.started', Instruc_text.tStartRefresh)
thisExp.addData('Instruc_text.stopped', Instruc_text.tStopRefresh)
thisExp.addData('Begin_text.started', Begin_text.tStartRefresh)
thisExp.addData('Begin_text.stopped', Begin_text.tStopRefresh)
# the Routine "Begin" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
conditions = data.TrialHandler(nReps=1, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('Conditions-ConRI.xlsx'),
    seed=None, name='conditions')
thisExp.addLoop(conditions)  # add the loop to the experiment
thisCondition = conditions.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisCondition.rgb)
if thisCondition != None:
    for paramName in thisCondition:
        exec('{} = thisCondition[paramName]'.format(paramName))

for thisCondition in conditions:
    currentLoop = conditions
    # abbreviate parameter names if possible (e.g. rgb = thisCondition.rgb)
    if thisCondition != None:
        for paramName in thisCondition:
            exec('{} = thisCondition[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "Update"-------
    continueRoutine = True
    # update component parameters for each repeat
    RRA=randint(lowerA,upperA)
    RRB=randint(lowerB,upperB)
    tilt=0
    # keep track of which components have finished
    UpdateComponents = []
    for thisComponent in UpdateComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    UpdateClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "Update"-------
    while continueRoutine:
        # get current time
        t = UpdateClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=UpdateClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in UpdateComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "Update"-------
    for thisComponent in UpdateComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    timer1=core.CountdownTimer()
    timer1.reset(60)
    # the Routine "Update" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # set up handler to look after randomisation of conditions etc
    repeat = data.TrialHandler(nReps=60, method='random', 
        extraInfo=expInfo, originPath=-1,
        trialList=[None],
        seed=None, name='repeat')
    thisExp.addLoop(repeat)  # add the loop to the experiment
    thisRepeat = repeat.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisRepeat.rgb)
    if thisRepeat != None:
        for paramName in thisRepeat:
            exec('{} = thisRepeat[paramName]'.format(paramName))
    
    for thisRepeat in repeat:
        currentLoop = repeat
        # abbreviate parameter names if possible (e.g. rgb = thisRepeat.rgb)
        if thisRepeat != None:
            for paramName in thisRepeat:
                exec('{} = thisRepeat[paramName]'.format(paramName))
        
        # ------Prepare to start Routine "Trial"-------
        continueRoutine = True
        # update component parameters for each repeat
        timer2=core.CountdownTimer()
        timer2.reset(1)
        # keep track of which components have finished
        TrialComponents = [vending]
        for thisComponent in TrialComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        TrialClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        
        # -------Run Routine "Trial"-------
        while continueRoutine:
            # get current time
            t = TrialClock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=TrialClock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            if timer2.getTime()<0 and PressA == True:
             timer2.reset(1)
             PressA = False
             RRA = randint(lowerA,upperA)
             if RRA == 1:
              logging.log(level=logging.DATA, msg = 'earnA')
              nRepA=1
              nRepB=0
              continueRoutine=False
            if timer2.getTime()<0 and PressB == True:
             timer2.reset(1)
             PressB = False
             RRB = randint(lowerB,upperB)
             if RRB == 1:
              logging.log(level=logging.DATA, msg = 'earnB')
              nRepA=0
              nRepB=1
              continueRoutine=False
            if event.getKeys(['t']) and tilt == 0: #tilt left
             tilt = -5
             PressA = True
            if event.getKeys(['v']) and tilt == 0: #tilt right
             tilt=5
             PressB = True
            
            # *vending* updates
            if vending.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                # keep track of start time/frame for later
                vending.frameNStart = frameN  # exact frame index
                vending.tStart = t  # local t and not account for scr refresh
                vending.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(vending, 'tStartRefresh')  # time at next scr refresh
                vending.setAutoDraw(True)
            if vending.status == STARTED:  # only update if drawing
                vending.setOri(tilt)
            if tilt > 0: #keep vending upright
             tilt  = tilt-0.5
            if tilt < 0:
             tilt = tilt+0.5
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in TrialComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "Trial"-------
        for thisComponent in TrialComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        #check end of trial
        if timer1.getTime()<0:
         repeat.finished=True
        repeat.addData('vending.started', vending.tStartRefresh)
        repeat.addData('vending.stopped', vending.tStopRefresh)
        # the Routine "Trial" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # set up handler to look after randomisation of conditions etc
        repA = data.TrialHandler(nReps=nRepA, method='random', 
            extraInfo=expInfo, originPath=-1,
            trialList=[None],
            seed=None, name='repA')
        thisExp.addLoop(repA)  # add the loop to the experiment
        thisRepA = repA.trialList[0]  # so we can initialise stimuli with some values
        # abbreviate parameter names if possible (e.g. rgb = thisRepA.rgb)
        if thisRepA != None:
            for paramName in thisRepA:
                exec('{} = thisRepA[paramName]'.format(paramName))
        
        for thisRepA in repA:
            currentLoop = repA
            # abbreviate parameter names if possible (e.g. rgb = thisRepA.rgb)
            if thisRepA != None:
                for paramName in thisRepA:
                    exec('{} = thisRepA[paramName]'.format(paramName))
            
            # ------Prepare to start Routine "win_A"-------
            continueRoutine = True
            routineTimer.add(1.000000)
            # update component parameters for each repeat
            snackA.setImage(rewardA)
            # keep track of which components have finished
            win_AComponents = [vendingA, snackA]
            for thisComponent in win_AComponents:
                thisComponent.tStart = None
                thisComponent.tStop = None
                thisComponent.tStartRefresh = None
                thisComponent.tStopRefresh = None
                if hasattr(thisComponent, 'status'):
                    thisComponent.status = NOT_STARTED
            # reset timers
            t = 0
            _timeToFirstFrame = win.getFutureFlipTime(clock="now")
            win_AClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
            frameN = -1
            
            # -------Run Routine "win_A"-------
            while continueRoutine and routineTimer.getTime() > 0:
                # get current time
                t = win_AClock.getTime()
                tThisFlip = win.getFutureFlipTime(clock=win_AClock)
                tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                
                # *vendingA* updates
                if vendingA.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    vendingA.frameNStart = frameN  # exact frame index
                    vendingA.tStart = t  # local t and not account for scr refresh
                    vendingA.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(vendingA, 'tStartRefresh')  # time at next scr refresh
                    vendingA.setAutoDraw(True)
                if vendingA.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > vendingA.tStartRefresh + 1.0-frameTolerance:
                        # keep track of stop time/frame for later
                        vendingA.tStop = t  # not accounting for scr refresh
                        vendingA.frameNStop = frameN  # exact frame index
                        win.timeOnFlip(vendingA, 'tStopRefresh')  # time at next scr refresh
                        vendingA.setAutoDraw(False)
                if vendingA.status == STARTED:  # only update if drawing
                    vendingA.setOri(tilt)
                
                # *snackA* updates
                if snackA.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    snackA.frameNStart = frameN  # exact frame index
                    snackA.tStart = t  # local t and not account for scr refresh
                    snackA.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(snackA, 'tStartRefresh')  # time at next scr refresh
                    snackA.setAutoDraw(True)
                if snackA.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > snackA.tStartRefresh + 1-frameTolerance:
                        # keep track of stop time/frame for later
                        snackA.tStop = t  # not accounting for scr refresh
                        snackA.frameNStop = frameN  # exact frame index
                        win.timeOnFlip(snackA, 'tStopRefresh')  # time at next scr refresh
                        snackA.setAutoDraw(False)
                if tilt > 0: #keep vending upright
                 tilt  = tilt-1
                if tilt < 0:
                 tilt = tilt+1
                if event.getKeys(['t']): #tilt left
                 tilt = -5
                if event.getKeys(['v']): #tilt right
                 tilt = 5
                
                # check for quit (typically the Esc key)
                if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                    core.quit()
                
                # check if all components have finished
                if not continueRoutine:  # a component has requested a forced-end of Routine
                    break
                continueRoutine = False  # will revert to True if at least one component still running
                for thisComponent in win_AComponents:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
            
            # -------Ending Routine "win_A"-------
            for thisComponent in win_AComponents:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            repA.addData('vendingA.started', vendingA.tStartRefresh)
            repA.addData('vendingA.stopped', vendingA.tStopRefresh)
            repA.addData('snackA.started', snackA.tStartRefresh)
            repA.addData('snackA.stopped', snackA.tStopRefresh)
            thisExp.nextEntry()
            
        # completed nRepA repeats of 'repA'
        
        
        # set up handler to look after randomisation of conditions etc
        repB = data.TrialHandler(nReps=nRepB, method='random', 
            extraInfo=expInfo, originPath=-1,
            trialList=[None],
            seed=None, name='repB')
        thisExp.addLoop(repB)  # add the loop to the experiment
        thisRepB = repB.trialList[0]  # so we can initialise stimuli with some values
        # abbreviate parameter names if possible (e.g. rgb = thisRepB.rgb)
        if thisRepB != None:
            for paramName in thisRepB:
                exec('{} = thisRepB[paramName]'.format(paramName))
        
        for thisRepB in repB:
            currentLoop = repB
            # abbreviate parameter names if possible (e.g. rgb = thisRepB.rgb)
            if thisRepB != None:
                for paramName in thisRepB:
                    exec('{} = thisRepB[paramName]'.format(paramName))
            
            # ------Prepare to start Routine "win_B"-------
            continueRoutine = True
            routineTimer.add(1.000000)
            # update component parameters for each repeat
            snackB.setImage(rewardB)
            # keep track of which components have finished
            win_BComponents = [vendingB, snackB]
            for thisComponent in win_BComponents:
                thisComponent.tStart = None
                thisComponent.tStop = None
                thisComponent.tStartRefresh = None
                thisComponent.tStopRefresh = None
                if hasattr(thisComponent, 'status'):
                    thisComponent.status = NOT_STARTED
            # reset timers
            t = 0
            _timeToFirstFrame = win.getFutureFlipTime(clock="now")
            win_BClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
            frameN = -1
            
            # -------Run Routine "win_B"-------
            while continueRoutine and routineTimer.getTime() > 0:
                # get current time
                t = win_BClock.getTime()
                tThisFlip = win.getFutureFlipTime(clock=win_BClock)
                tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                
                # *vendingB* updates
                if vendingB.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    vendingB.frameNStart = frameN  # exact frame index
                    vendingB.tStart = t  # local t and not account for scr refresh
                    vendingB.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(vendingB, 'tStartRefresh')  # time at next scr refresh
                    vendingB.setAutoDraw(True)
                if vendingB.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > vendingB.tStartRefresh + 1.0-frameTolerance:
                        # keep track of stop time/frame for later
                        vendingB.tStop = t  # not accounting for scr refresh
                        vendingB.frameNStop = frameN  # exact frame index
                        win.timeOnFlip(vendingB, 'tStopRefresh')  # time at next scr refresh
                        vendingB.setAutoDraw(False)
                if vendingB.status == STARTED:  # only update if drawing
                    vendingB.setOri(tilt)
                
                # *snackB* updates
                if snackB.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    snackB.frameNStart = frameN  # exact frame index
                    snackB.tStart = t  # local t and not account for scr refresh
                    snackB.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(snackB, 'tStartRefresh')  # time at next scr refresh
                    snackB.setAutoDraw(True)
                if snackB.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > snackB.tStartRefresh + 1-frameTolerance:
                        # keep track of stop time/frame for later
                        snackB.tStop = t  # not accounting for scr refresh
                        snackB.frameNStop = frameN  # exact frame index
                        win.timeOnFlip(snackB, 'tStopRefresh')  # time at next scr refresh
                        snackB.setAutoDraw(False)
                if tilt > 0: #keep vending upright
                 tilt  = tilt-1
                if tilt < 0:
                 tilt = tilt+1
                if event.getKeys(['t']): #tilt left
                 tilt = -5
                if event.getKeys(['v']): #tilt right
                 tilt=5
                
                # check for quit (typically the Esc key)
                if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                    core.quit()
                
                # check if all components have finished
                if not continueRoutine:  # a component has requested a forced-end of Routine
                    break
                continueRoutine = False  # will revert to True if at least one component still running
                for thisComponent in win_BComponents:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
            
            # -------Ending Routine "win_B"-------
            for thisComponent in win_BComponents:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            repB.addData('vendingB.started', vendingB.tStartRefresh)
            repB.addData('vendingB.stopped', vendingB.tStopRefresh)
            repB.addData('snackB.started', snackB.tStartRefresh)
            repB.addData('snackB.stopped', snackB.tStopRefresh)
            thisExp.nextEntry()
            
        # completed nRepB repeats of 'repB'
        
        thisExp.nextEntry()
        
    # completed 60 repeats of 'repeat'
    
    
    # ------Prepare to start Routine "Rate_A"-------
    continueRoutine = True
    # update component parameters for each repeat
    testSnackA.setImage(rewardA)
    rateA_text.setText(msgA)
    sliderA.reset()
    logging.log(level=logging.DATA, msg = 'start rating A')
    # keep track of which components have finished
    Rate_AComponents = [testSnackA, rateA_text, sliderA]
    for thisComponent in Rate_AComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    Rate_AClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "Rate_A"-------
    while continueRoutine:
        # get current time
        t = Rate_AClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=Rate_AClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *testSnackA* updates
        if testSnackA.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            testSnackA.frameNStart = frameN  # exact frame index
            testSnackA.tStart = t  # local t and not account for scr refresh
            testSnackA.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(testSnackA, 'tStartRefresh')  # time at next scr refresh
            testSnackA.setAutoDraw(True)
        if testSnackA.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > testSnackA.tStartRefresh + 20-frameTolerance:
                # keep track of stop time/frame for later
                testSnackA.tStop = t  # not accounting for scr refresh
                testSnackA.frameNStop = frameN  # exact frame index
                win.timeOnFlip(testSnackA, 'tStopRefresh')  # time at next scr refresh
                testSnackA.setAutoDraw(False)
        
        # *rateA_text* updates
        if rateA_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            rateA_text.frameNStart = frameN  # exact frame index
            rateA_text.tStart = t  # local t and not account for scr refresh
            rateA_text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(rateA_text, 'tStartRefresh')  # time at next scr refresh
            rateA_text.setAutoDraw(True)
        if rateA_text.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > rateA_text.tStartRefresh + 20-frameTolerance:
                # keep track of stop time/frame for later
                rateA_text.tStop = t  # not accounting for scr refresh
                rateA_text.frameNStop = frameN  # exact frame index
                win.timeOnFlip(rateA_text, 'tStopRefresh')  # time at next scr refresh
                rateA_text.setAutoDraw(False)
        
        # *sliderA* updates
        if sliderA.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            sliderA.frameNStart = frameN  # exact frame index
            sliderA.tStart = t  # local t and not account for scr refresh
            sliderA.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(sliderA, 'tStartRefresh')  # time at next scr refresh
            sliderA.setAutoDraw(True)
        
        # Check sliderA for response to end routine
        if sliderA.getRating() is not None and sliderA.status == STARTED:
            continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in Rate_AComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "Rate_A"-------
    for thisComponent in Rate_AComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    conditions.addData('testSnackA.started', testSnackA.tStartRefresh)
    conditions.addData('testSnackA.stopped', testSnackA.tStopRefresh)
    conditions.addData('rateA_text.started', rateA_text.tStartRefresh)
    conditions.addData('rateA_text.stopped', rateA_text.tStopRefresh)
    conditions.addData('sliderA.response', sliderA.getRating())
    conditions.addData('sliderA.started', sliderA.tStartRefresh)
    conditions.addData('sliderA.stopped', sliderA.tStopRefresh)
    #save rating
    rating = sliderA.getRating()
    logging.log(level=logging.DATA, msg = "rating A: " + rating.astype('str'))
    logging.log(level=logging.DATA, msg = 'end rating A')
    # the Routine "Rate_A" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "Rate_B"-------
    continueRoutine = True
    # update component parameters for each repeat
    testSnackB.setImage(rewardB)
    rateB_text.setText(msgB)
    sliderB.reset()
    logging.log(level=logging.DATA, msg = 'start rating B')
    # keep track of which components have finished
    Rate_BComponents = [testSnackB, rateB_text, sliderB]
    for thisComponent in Rate_BComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    Rate_BClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "Rate_B"-------
    while continueRoutine:
        # get current time
        t = Rate_BClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=Rate_BClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *testSnackB* updates
        if testSnackB.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            testSnackB.frameNStart = frameN  # exact frame index
            testSnackB.tStart = t  # local t and not account for scr refresh
            testSnackB.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(testSnackB, 'tStartRefresh')  # time at next scr refresh
            testSnackB.setAutoDraw(True)
        if testSnackB.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > testSnackB.tStartRefresh + 10-frameTolerance:
                # keep track of stop time/frame for later
                testSnackB.tStop = t  # not accounting for scr refresh
                testSnackB.frameNStop = frameN  # exact frame index
                win.timeOnFlip(testSnackB, 'tStopRefresh')  # time at next scr refresh
                testSnackB.setAutoDraw(False)
        
        # *rateB_text* updates
        if rateB_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            rateB_text.frameNStart = frameN  # exact frame index
            rateB_text.tStart = t  # local t and not account for scr refresh
            rateB_text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(rateB_text, 'tStartRefresh')  # time at next scr refresh
            rateB_text.setAutoDraw(True)
        if rateB_text.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > rateB_text.tStartRefresh + 10-frameTolerance:
                # keep track of stop time/frame for later
                rateB_text.tStop = t  # not accounting for scr refresh
                rateB_text.frameNStop = frameN  # exact frame index
                win.timeOnFlip(rateB_text, 'tStopRefresh')  # time at next scr refresh
                rateB_text.setAutoDraw(False)
        
        # *sliderB* updates
        if sliderB.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            sliderB.frameNStart = frameN  # exact frame index
            sliderB.tStart = t  # local t and not account for scr refresh
            sliderB.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(sliderB, 'tStartRefresh')  # time at next scr refresh
            sliderB.setAutoDraw(True)
        
        # Check sliderB for response to end routine
        if sliderB.getRating() is not None and sliderB.status == STARTED:
            continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in Rate_BComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "Rate_B"-------
    for thisComponent in Rate_BComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    conditions.addData('testSnackB.started', testSnackB.tStartRefresh)
    conditions.addData('testSnackB.stopped', testSnackB.tStopRefresh)
    conditions.addData('rateB_text.started', rateB_text.tStartRefresh)
    conditions.addData('rateB_text.stopped', rateB_text.tStopRefresh)
    conditions.addData('sliderB.response', sliderB.getRating())
    conditions.addData('sliderB.rt', sliderB.getRT())
    conditions.addData('sliderB.started', sliderB.tStartRefresh)
    conditions.addData('sliderB.stopped', sliderB.tStopRefresh)
    #save rating
    rating = sliderB.getRating()
    logging.log(level=logging.DATA, msg = "rating B: " + rating.astype('str'))
    logging.log(level=logging.DATA, msg = 'end rating B')
    # the Routine "Rate_B" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 1 repeats of 'conditions'


# Flip one final time so any remaining win.callOnFlip() 
# and win.timeOnFlip() tasks get executed before quitting
win.flip()

# these shouldn't be strictly necessary (should auto-save)
thisExp.saveAsPickle(filename)
logging.flush()
# make sure everything is closed down
thisExp.abort()  # or data files will save again on exit
win.close()
core.quit()
