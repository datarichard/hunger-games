#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2021.1.4),
    on Tue Jun 29 20:55:19 2021
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
expName = 'pavlov'  # from the Builder filename that created this script
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
    originPath='/Users/rich/Documents/Github/hunger-games/Pavlovian_lastrun.py',
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
    monitor='testMonitor', color=[-1.0,-1.0,-1.0], colorSpace='rgb',
    blendMode='avg', useFBO=True)
# store frame rate of monitor if we can measure it
expInfo['frameRate'] = win.getActualFrameRate()
if expInfo['frameRate'] != None:
    frameDur = 1.0 / round(expInfo['frameRate'])
else:
    frameDur = 1.0 / 60.0  # could not measure, so guess

# create a default keyboard (e.g. to check for escape)
defaultKeyboard = keyboard.Keyboard()

# Initialize components for Routine "Instr"
InstrClock = core.Clock()
Ready = visual.TextStim(win=win, name='Ready',
    text='We have discovered that people\nwere stealing from the vending\nmachines! We have upgraded the\nmachine to make them harder to\nsteal from. However, when the\nmachine is overstocked a free snack \nwill fall out. \n\nThe lights on the front panel\nindicate whether the machine is\noverstocked. Watch the lights and\nlearn which snacks fall out. A\nmultiple choice question will test\nwhat you have learnt. Use the\nkeyboard [a b c d] to indicate the\ncorrect answer.\n\n\n\n\n         press space to begin',
    font='Helvetica Bold',
    pos=[0, 0], height=0.075, wrapWidth=None, ori=0, 
    color='LightGray', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
Begin_resp = keyboard.Keyboard()
yellowSize = 0
blueSize = 0
logging.log(level=logging.DATA, msg = "version " + expInfo['version'])

# Initialize components for Routine "ITI"
ITIClock = core.Clock()
vend = visual.PatchStim(
    win=win, name='vend',
    tex='images/vend.png', mask=None,
    ori=0, pos=[0, 0], size=[1.5, 2], sf=None, phase=0.0,
    color=[1,1,1], colorSpace='rgb', opacity=1,
    texRes=512
, interpolate=True, depth=-1.0)

# Initialize components for Routine "trial"
trialClock = core.Clock()
vend_CS = visual.PatchStim(
    win=win, name='vend_CS',
    tex='sin', mask=None,
    ori=0, pos=[0, 0], size=[1.5, 2], sf=None, phase=0,
    color='white', colorSpace='rgb', opacity=1,
    texRes=512
, interpolate=True, depth=0.0)
Outcome = visual.PatchStim(
    win=win, name='Outcome',
    tex='sin', mask=None,
    ori=0, pos=[0, -0.4], size=[0.4, 0.5], sf=None, phase=0.0,
    color=[1,1,1], colorSpace='rgb', opacity=1,
    texRes=512
, interpolate=True, depth=-1.0)

# Initialize components for Routine "ITI"
ITIClock = core.Clock()
vend = visual.PatchStim(
    win=win, name='vend',
    tex='images/vend.png', mask=None,
    ori=0, pos=[0, 0], size=[1.5, 2], sf=None, phase=0.0,
    color=[1,1,1], colorSpace='rgb', opacity=1,
    texRes=512
, interpolate=True, depth=-1.0)

# Initialize components for Routine "Choice"
ChoiceClock = core.Clock()
vend_testy = visual.PatchStim(
    win=win, name='vend_testy',
    tex='sin', mask=None,
    ori=0, pos=[0, 0], size=[1.5, 2], sf=None, phase=0.0,
    color=[1,1,1], colorSpace='rgb', opacity=1,
    texRes=512
, interpolate=True, depth=0.0)
choice_text = visual.TextStim(win=win, name='choice_text',
    text='Which snack is overstocked?\n\na) M&Ms\nb) BBQ\nc) tiny teddy\nd) empty',
    font='Helvetica Bold',
    pos=[0, -0.4], height=0.075, wrapWidth=None, ori=0, 
    color='LightGray', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
key_resp_2 = keyboard.Keyboard()

# Initialize components for Routine "feedback"
feedbackClock = core.Clock()
msg="msg not updated!"
feedback_text = visual.TextStim(win=win, name='feedback_text',
    text='',
    font='Helvetica Bold',
    pos=[0, 0], height=0.075, wrapWidth=None, ori=0, 
    color='LightGray', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);

# Initialize components for Routine "Thankyou"
ThankyouClock = core.Clock()
Thankyou_text = visual.TextStim(win=win, name='Thankyou_text',
    text='     Thankyou!\n\nStage 2 completed',
    font='Helvetica Bold',
    pos=[0, 0], height=0.075, wrapWidth=None, ori=0, 
    color='LightGray', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

# ------Prepare to start Routine "Instr"-------
continueRoutine = True
# update component parameters for each repeat
Begin_resp.keys = []
Begin_resp.rt = []
_Begin_resp_allKeys = []
# keep track of which components have finished
InstrComponents = [Ready, Begin_resp]
for thisComponent in InstrComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
InstrClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "Instr"-------
while continueRoutine:
    # get current time
    t = InstrClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=InstrClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *Ready* updates
    if Ready.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        Ready.frameNStart = frameN  # exact frame index
        Ready.tStart = t  # local t and not account for scr refresh
        Ready.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Ready, 'tStartRefresh')  # time at next scr refresh
        Ready.setAutoDraw(True)
    
    # *Begin_resp* updates
    waitOnFlip = False
    if Begin_resp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        Begin_resp.frameNStart = frameN  # exact frame index
        Begin_resp.tStart = t  # local t and not account for scr refresh
        Begin_resp.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Begin_resp, 'tStartRefresh')  # time at next scr refresh
        Begin_resp.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(Begin_resp.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(Begin_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if Begin_resp.status == STARTED and not waitOnFlip:
        theseKeys = Begin_resp.getKeys(keyList=['space'], waitRelease=False)
        _Begin_resp_allKeys.extend(theseKeys)
        if len(_Begin_resp_allKeys):
            Begin_resp.keys = _Begin_resp_allKeys[-1].name  # just the last key pressed
            Begin_resp.rt = _Begin_resp_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in InstrComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "Instr"-------
for thisComponent in InstrComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('Ready.started', Ready.tStartRefresh)
thisExp.addData('Ready.stopped', Ready.tStopRefresh)
# the Routine "Instr" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
blocks = data.TrialHandler(nReps=3, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('Pavlov_blocks.xlsx'),
    seed=None, name='blocks')
thisExp.addLoop(blocks)  # add the loop to the experiment
thisBlock = blocks.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisBlock.rgb)
if thisBlock != None:
    for paramName in thisBlock:
        exec('{} = thisBlock[paramName]'.format(paramName))

for thisBlock in blocks:
    currentLoop = blocks
    # abbreviate parameter names if possible (e.g. rgb = thisBlock.rgb)
    if thisBlock != None:
        for paramName in thisBlock:
            exec('{} = thisBlock[paramName]'.format(paramName))
    
    # set up handler to look after randomisation of conditions etc
    trials = data.TrialHandler(nReps=1, method='random', 
        extraInfo=expInfo, originPath=-1,
        trialList=data.importConditions('Pavlov_trials.xlsx'),
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
        
        # ------Prepare to start Routine "ITI"-------
        continueRoutine = True
        routineTimer.add(3.000000)
        # update component parameters for each repeat
        delta = randint(-5,5)
        ITIdur = 3
        # keep track of which components have finished
        ITIComponents = [vend]
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
        while continueRoutine and routineTimer.getTime() > 0:
            # get current time
            t = ITIClock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=ITIClock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *vend* updates
            if vend.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                vend.frameNStart = frameN  # exact frame index
                vend.tStart = t  # local t and not account for scr refresh
                vend.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(vend, 'tStartRefresh')  # time at next scr refresh
                vend.setAutoDraw(True)
            if vend.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > vend.tStartRefresh + 3-frameTolerance:
                    # keep track of stop time/frame for later
                    vend.tStop = t  # not accounting for scr refresh
                    vend.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(vend, 'tStopRefresh')  # time at next scr refresh
                    vend.setAutoDraw(False)
            
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
        trials.addData('vend.started', vend.tStartRefresh)
        trials.addData('vend.stopped', vend.tStopRefresh)
        
        # ------Prepare to start Routine "trial"-------
        continueRoutine = True
        routineTimer.add(3.000000)
        # update component parameters for each repeat
        vend_CS.setColor([1,1,1], colorSpace='rgb')
        vend_CS.setTex(CS)
        Outcome.setTex(US)
        # keep track of which components have finished
        trialComponents = [vend_CS, Outcome]
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
        
        # -------Run Routine "trial"-------
        while continueRoutine and routineTimer.getTime() > 0:
            # get current time
            t = trialClock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=trialClock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *vend_CS* updates
            if vend_CS.status == NOT_STARTED and frameN >= 0:
                # keep track of start time/frame for later
                vend_CS.frameNStart = frameN  # exact frame index
                vend_CS.tStart = t  # local t and not account for scr refresh
                vend_CS.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(vend_CS, 'tStartRefresh')  # time at next scr refresh
                vend_CS.setAutoDraw(True)
            if vend_CS.status == STARTED:
                if frameN >= 180:
                    # keep track of stop time/frame for later
                    vend_CS.tStop = t  # not accounting for scr refresh
                    vend_CS.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(vend_CS, 'tStopRefresh')  # time at next scr refresh
                    vend_CS.setAutoDraw(False)
            
            # *Outcome* updates
            if Outcome.status == NOT_STARTED and frameN >= 60:
                # keep track of start time/frame for later
                Outcome.frameNStart = frameN  # exact frame index
                Outcome.tStart = t  # local t and not account for scr refresh
                Outcome.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(Outcome, 'tStartRefresh')  # time at next scr refresh
                Outcome.setAutoDraw(True)
            if Outcome.status == STARTED:
                if frameN >= (Outcome.frameNStart + 120):
                    # keep track of stop time/frame for later
                    Outcome.tStop = t  # not accounting for scr refresh
                    Outcome.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(Outcome, 'tStopRefresh')  # time at next scr refresh
                    Outcome.setAutoDraw(False)
            
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
        trials.addData('vend_CS.started', vend_CS.tStartRefresh)
        trials.addData('vend_CS.stopped', vend_CS.tStopRefresh)
        trials.addData('Outcome.started', Outcome.tStartRefresh)
        trials.addData('Outcome.stopped', Outcome.tStopRefresh)
        thisExp.nextEntry()
        
    # completed 1 repeats of 'trials'
    
    
    # ------Prepare to start Routine "ITI"-------
    continueRoutine = True
    routineTimer.add(3.000000)
    # update component parameters for each repeat
    delta = randint(-5,5)
    ITIdur = 3
    # keep track of which components have finished
    ITIComponents = [vend]
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
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = ITIClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=ITIClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *vend* updates
        if vend.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            vend.frameNStart = frameN  # exact frame index
            vend.tStart = t  # local t and not account for scr refresh
            vend.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(vend, 'tStartRefresh')  # time at next scr refresh
            vend.setAutoDraw(True)
        if vend.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > vend.tStartRefresh + 3-frameTolerance:
                # keep track of stop time/frame for later
                vend.tStop = t  # not accounting for scr refresh
                vend.frameNStop = frameN  # exact frame index
                win.timeOnFlip(vend, 'tStopRefresh')  # time at next scr refresh
                vend.setAutoDraw(False)
        
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
    blocks.addData('vend.started', vend.tStartRefresh)
    blocks.addData('vend.stopped', vend.tStopRefresh)
    
    # ------Prepare to start Routine "Choice"-------
    continueRoutine = True
    # update component parameters for each repeat
    vend_testy.setTex(testCS)
    key_resp_2.keys = []
    key_resp_2.rt = []
    _key_resp_2_allKeys = []
    # keep track of which components have finished
    ChoiceComponents = [vend_testy, choice_text, key_resp_2]
    for thisComponent in ChoiceComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    ChoiceClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "Choice"-------
    while continueRoutine:
        # get current time
        t = ChoiceClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=ChoiceClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *vend_testy* updates
        if vend_testy.status == NOT_STARTED and frameN >= 0:
            # keep track of start time/frame for later
            vend_testy.frameNStart = frameN  # exact frame index
            vend_testy.tStart = t  # local t and not account for scr refresh
            vend_testy.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(vend_testy, 'tStartRefresh')  # time at next scr refresh
            vend_testy.setAutoDraw(True)
        
        # *choice_text* updates
        if choice_text.status == NOT_STARTED and frameN >= 60:
            # keep track of start time/frame for later
            choice_text.frameNStart = frameN  # exact frame index
            choice_text.tStart = t  # local t and not account for scr refresh
            choice_text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(choice_text, 'tStartRefresh')  # time at next scr refresh
            choice_text.setAutoDraw(True)
        
        # *key_resp_2* updates
        waitOnFlip = False
        if key_resp_2.status == NOT_STARTED and frameN >= 60:
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
            theseKeys = key_resp_2.getKeys(keyList=['a', 'b', 'c', 'd'], waitRelease=False)
            _key_resp_2_allKeys.extend(theseKeys)
            if len(_key_resp_2_allKeys):
                key_resp_2.keys = _key_resp_2_allKeys[0].name  # just the first key pressed
                key_resp_2.rt = _key_resp_2_allKeys[0].rt
                # was this correct?
                if (key_resp_2.keys == str(correctAns)) or (key_resp_2.keys == correctAns):
                    key_resp_2.corr = 1
                else:
                    key_resp_2.corr = 0
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in ChoiceComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "Choice"-------
    for thisComponent in ChoiceComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    blocks.addData('vend_testy.started', vend_testy.tStartRefresh)
    blocks.addData('vend_testy.stopped', vend_testy.tStopRefresh)
    blocks.addData('choice_text.started', choice_text.tStartRefresh)
    blocks.addData('choice_text.stopped', choice_text.tStopRefresh)
    # check responses
    if key_resp_2.keys in ['', [], None]:  # No response was made
        key_resp_2.keys = None
        # was no response the correct answer?!
        if str(correctAns).lower() == 'none':
           key_resp_2.corr = 1;  # correct non-response
        else:
           key_resp_2.corr = 0;  # failed to respond (incorrectly)
    # store data for blocks (TrialHandler)
    blocks.addData('key_resp_2.keys',key_resp_2.keys)
    blocks.addData('key_resp_2.corr', key_resp_2.corr)
    if key_resp_2.keys != None:  # we had a response
        blocks.addData('key_resp_2.rt', key_resp_2.rt)
    blocks.addData('key_resp_2.started', key_resp_2.tStartRefresh)
    blocks.addData('key_resp_2.stopped', key_resp_2.tStopRefresh)
    # the Routine "Choice" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "feedback"-------
    continueRoutine = True
    routineTimer.add(1.000000)
    # update component parameters for each repeat
    logging.log(level=logging.DATA, msg = 'test_' + thisBlock["testCS"])
    if len(key_resp_2.keys)<1:
      msg="Failed to respond"
    elif key_resp_2.corr:
      msg="correct!"
      logging.log(level=logging.DATA, msg = 'correct')
    else:
      msg="Oops! That was wrong"
      logging.log(level=logging.DATA, msg = 'Oops!')
    feedback_text.setText(msg)
    # keep track of which components have finished
    feedbackComponents = [feedback_text]
    for thisComponent in feedbackComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    feedbackClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "feedback"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = feedbackClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=feedbackClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *feedback_text* updates
        if feedback_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            feedback_text.frameNStart = frameN  # exact frame index
            feedback_text.tStart = t  # local t and not account for scr refresh
            feedback_text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(feedback_text, 'tStartRefresh')  # time at next scr refresh
            feedback_text.setAutoDraw(True)
        if feedback_text.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > feedback_text.tStartRefresh + 1.0-frameTolerance:
                # keep track of stop time/frame for later
                feedback_text.tStop = t  # not accounting for scr refresh
                feedback_text.frameNStop = frameN  # exact frame index
                win.timeOnFlip(feedback_text, 'tStopRefresh')  # time at next scr refresh
                feedback_text.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in feedbackComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "feedback"-------
    for thisComponent in feedbackComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    blocks.addData('feedback_text.started', feedback_text.tStartRefresh)
    blocks.addData('feedback_text.stopped', feedback_text.tStopRefresh)
    thisExp.nextEntry()
    
# completed 3 repeats of 'blocks'


# ------Prepare to start Routine "Thankyou"-------
continueRoutine = True
routineTimer.add(1.000000)
# update component parameters for each repeat
# keep track of which components have finished
ThankyouComponents = [Thankyou_text]
for thisComponent in ThankyouComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
ThankyouClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "Thankyou"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = ThankyouClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=ThankyouClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *Thankyou_text* updates
    if Thankyou_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        Thankyou_text.frameNStart = frameN  # exact frame index
        Thankyou_text.tStart = t  # local t and not account for scr refresh
        Thankyou_text.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Thankyou_text, 'tStartRefresh')  # time at next scr refresh
        Thankyou_text.setAutoDraw(True)
    if Thankyou_text.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > Thankyou_text.tStartRefresh + 1.0-frameTolerance:
            # keep track of stop time/frame for later
            Thankyou_text.tStop = t  # not accounting for scr refresh
            Thankyou_text.frameNStop = frameN  # exact frame index
            win.timeOnFlip(Thankyou_text, 'tStopRefresh')  # time at next scr refresh
            Thankyou_text.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in ThankyouComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "Thankyou"-------
for thisComponent in ThankyouComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('Thankyou_text.started', Thankyou_text.tStartRefresh)
thisExp.addData('Thankyou_text.stopped', Thankyou_text.tStopRefresh)

# Flip one final time so any remaining win.callOnFlip() 
# and win.timeOnFlip() tasks get executed before quitting
win.flip()

# these shouldn't be strictly necessary (should auto-save)
logging.flush()
# make sure everything is closed down
thisExp.abort()  # or data files will save again on exit
win.close()
core.quit()
