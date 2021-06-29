#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2021.1.4),
    on Tue Jun 29 20:43:35 2021
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
expName = 'instrumental'  # from the Builder filename that created this script
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
    originPath='/Users/rich/Documents/Github/hunger-games/Instrumental_lastrun.py',
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

# Initialize components for Routine "rate_Teddies"
rate_TeddiesClock = core.Clock()
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

# Initialize components for Routine "rate_MMs"
rate_MMsClock = core.Clock()
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

# Initialize components for Routine "rate_BBQ"
rate_BBQClock = core.Clock()
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

# Initialize components for Routine "rate_Hunger"
rate_HungerClock = core.Clock()
Hunger_rating = visual.RatingScale(win=win, name='Hunger_rating', acceptPreText='key, enter')
Hunger_text = visual.TextStim(win=win, name='Hunger_text',
    text='How hungry are you right now?',
    font='Helvetica Bold',
    pos=[0, 0.5], height=0.075, wrapWidth=None, ori=0, 
    color='LightGray', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);

# Initialize components for Routine "instructions"
instructionsClock = core.Clock()
Instructions_text = visual.TextStim(win=win, name='Instructions_text',
    text='Someone has said you can get free\nsnacks from our vending machine.\n\nUse the button box to tilt the \nmachine to the left and right, and \nlearn how to steal different snacks!\n\n\n\n\n           Press space to begin',
    font='Helvetica Bold',
    pos=[0, 0.1], height=0.075, wrapWidth=2, ori=0, 
    color='LightGray', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
spacetobegin = keyboard.Keyboard()

# Initialize components for Routine "Trial"
TrialClock = core.Clock()
if expInfo['version'] == 'A':
   rewardA = 'images/M&M.png'
   rewardB = 'images/BBQ.png'
   logging.log(level=logging.DATA, msg = 'version A')
if expInfo['version'] == 'B':
   rewardA = 'images/BBQ.png'
   rewardB = 'images/M&M.png'
   logging.log(level=logging.DATA, msg = 'version B')
if expInfo['version'] == 'C':
   rewardA = 'images/teddy.png'
   rewardB = 'images/BBQ.png'
   logging.log(level=logging.DATA, msg = 'version C')
if expInfo['version'] == 'D':
   rewardA = 'images/BBQ.png'
   rewardB = 'images/teddy.png'
   logging.log(level=logging.DATA, msg = 'version D')
if expInfo['version'] == 'E':
   rewardA = 'images/M&M.png'
   rewardB = 'images/teddy.png'
   logging.log(level=logging.DATA, msg = 'version E')
if expInfo['version'] == 'F':
   rewardA = 'images/teddy.png'
   rewardB = 'images/M&M.png'
   logging.log(level=logging.DATA, msg = 'version F')

#initialise counters
pressL=0
pressR=0
tilt=0


vending_machine = visual.ImageStim(
    win=win,
    name='vending_machine', 
    image='images/vend.png', mask=None,
    ori=1.0, pos=[0, 0], size=[1.5, 2],
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=512, interpolate=True, depth=-2.0)

# Initialize components for Routine "A"
AClock = core.Clock()
vendingA_image = visual.ImageStim(
    win=win,
    name='vendingA_image', 
    image='images/vend.png', mask=None,
    ori=1.0, pos=[0, 0], size=[1.5, 2],
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=512, interpolate=True, depth=-1.0)
rewardA_image = visual.ImageStim(
    win=win,
    name='rewardA_image', 
    image=rewardA, mask=None,
    ori=0, pos=[0, -0.5], size=[0.4, 0.5],
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=512, interpolate=True, depth=-2.0)

# Initialize components for Routine "B"
BClock = core.Clock()
vendingB_image = visual.ImageStim(
    win=win,
    name='vendingB_image', 
    image='images/vend.png', mask=None,
    ori=1.0, pos=[0, 0], size=[1.5, 2],
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=512, interpolate=True, depth=-1.0)
rewardB_image = visual.ImageStim(
    win=win,
    name='rewardB_image', 
    image=rewardB, mask=None,
    ori=0, pos=[0, -0.5], size=[0.4, 0.5],
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=512, interpolate=True, depth=-2.0)

# Initialize components for Routine "test"
testClock = core.Clock()
test_question = visual.TextStim(win=win, name='test_question',
    text='Which direction did you tilt to get:',
    font='Helvetica Bold',
    pos=[0, 0.5], height=0.075, wrapWidth=None, ori=0, 
    color='LightGray', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
test_instructions = visual.TextStim(win=win, name='test_instructions',
    text='Press left or right button',
    font='Helvetica Bold',
    pos=[0, -0.5], height=0.075, wrapWidth=None, ori=0, 
    color='LightGray', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);
test_image = visual.ImageStim(
    win=win,
    name='test_image', 
    image='sin', mask=None,
    ori=0, pos=[0, 0], size=[0.4, 0.5],
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=512, interpolate=True, depth=-3.0)
test_response = keyboard.Keyboard()

# Initialize components for Routine "feedback"
feedbackClock = core.Clock()
nTest=25
Error=6
feedback_text = visual.TextStim(win=win, name='feedback_text',
    text='',
    font='Helvetica Bold',
    pos=[0, 0], height=0.1, wrapWidth=None, ori=0, 
    color='LightGray', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);

# Initialize components for Routine "finish"
finishClock = core.Clock()
finish_text = visual.TextStim(win=win, name='finish_text',
    text='  Thankyou!\n\nEnd of Stage 1',
    font='Helvetica Bold',
    pos=[0, 0], height=0.075, wrapWidth=None, ori=0, 
    color='LightGray', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

# ------Prepare to start Routine "rate_Teddies"-------
continueRoutine = True
# update component parameters for each repeat
teddy_rating.reset()
# keep track of which components have finished
rate_TeddiesComponents = [teddy_rating, teddy_ratingImage, teddy_ratingText]
for thisComponent in rate_TeddiesComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
rate_TeddiesClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "rate_Teddies"-------
while continueRoutine:
    # get current time
    t = rate_TeddiesClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=rate_TeddiesClock)
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
    for thisComponent in rate_TeddiesComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "rate_Teddies"-------
for thisComponent in rate_TeddiesComponents:
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
# the Routine "rate_Teddies" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "rate_MMs"-------
continueRoutine = True
# update component parameters for each repeat
MM_rating.reset()
# keep track of which components have finished
rate_MMsComponents = [MM_rating, MM_ratingImage, MM_ratingText]
for thisComponent in rate_MMsComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
rate_MMsClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "rate_MMs"-------
while continueRoutine:
    # get current time
    t = rate_MMsClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=rate_MMsClock)
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
    for thisComponent in rate_MMsComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "rate_MMs"-------
for thisComponent in rate_MMsComponents:
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
# the Routine "rate_MMs" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "rate_BBQ"-------
continueRoutine = True
# update component parameters for each repeat
BBQ_rating.reset()
# keep track of which components have finished
rate_BBQComponents = [BBQ_rating, BBQ_ratingImage, BBQ_ratingText]
for thisComponent in rate_BBQComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
rate_BBQClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "rate_BBQ"-------
while continueRoutine:
    # get current time
    t = rate_BBQClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=rate_BBQClock)
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
    for thisComponent in rate_BBQComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "rate_BBQ"-------
for thisComponent in rate_BBQComponents:
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
# the Routine "rate_BBQ" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "rate_Hunger"-------
continueRoutine = True
# update component parameters for each repeat
Hunger_rating.reset()
# keep track of which components have finished
rate_HungerComponents = [Hunger_rating, Hunger_text]
for thisComponent in rate_HungerComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
rate_HungerClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "rate_Hunger"-------
while continueRoutine:
    # get current time
    t = rate_HungerClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=rate_HungerClock)
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
    for thisComponent in rate_HungerComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "rate_Hunger"-------
for thisComponent in rate_HungerComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# store data for thisExp (ExperimentHandler)
thisExp.addData('Hunger_rating.response', Hunger_rating.getRating())
thisExp.nextEntry()
thisExp.addData('Hunger_rating.started', Hunger_rating.tStart)
thisExp.addData('Hunger_rating.stopped', Hunger_rating.tStop)
thisExp.addData('Hunger_text.started', Hunger_text.tStartRefresh)
thisExp.addData('Hunger_text.stopped', Hunger_text.tStopRefresh)
# the Routine "rate_Hunger" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "instructions"-------
continueRoutine = True
# update component parameters for each repeat
spacetobegin.keys = []
spacetobegin.rt = []
_spacetobegin_allKeys = []
# keep track of which components have finished
instructionsComponents = [Instructions_text, spacetobegin]
for thisComponent in instructionsComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
instructionsClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "instructions"-------
while continueRoutine:
    # get current time
    t = instructionsClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=instructionsClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *Instructions_text* updates
    if Instructions_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        Instructions_text.frameNStart = frameN  # exact frame index
        Instructions_text.tStart = t  # local t and not account for scr refresh
        Instructions_text.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Instructions_text, 'tStartRefresh')  # time at next scr refresh
        Instructions_text.setAutoDraw(True)
    
    # *spacetobegin* updates
    waitOnFlip = False
    if spacetobegin.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        spacetobegin.frameNStart = frameN  # exact frame index
        spacetobegin.tStart = t  # local t and not account for scr refresh
        spacetobegin.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(spacetobegin, 'tStartRefresh')  # time at next scr refresh
        spacetobegin.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(spacetobegin.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(spacetobegin.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if spacetobegin.status == STARTED and not waitOnFlip:
        theseKeys = spacetobegin.getKeys(keyList=['space'], waitRelease=False)
        _spacetobegin_allKeys.extend(theseKeys)
        if len(_spacetobegin_allKeys):
            spacetobegin.keys = _spacetobegin_allKeys[-1].name  # just the last key pressed
            spacetobegin.rt = _spacetobegin_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in instructionsComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "instructions"-------
for thisComponent in instructionsComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('Instructions_text.started', Instructions_text.tStartRefresh)
thisExp.addData('Instructions_text.stopped', Instructions_text.tStopRefresh)
# the Routine "instructions" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
tests = data.TrialHandler(nReps=nTest, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=[None],
    seed=None, name='tests')
thisExp.addLoop(tests)  # add the loop to the experiment
thisTest = tests.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisTest.rgb)
if thisTest != None:
    for paramName in thisTest:
        exec('{} = thisTest[paramName]'.format(paramName))

for thisTest in tests:
    currentLoop = tests
    # abbreviate parameter names if possible (e.g. rgb = thisTest.rgb)
    if thisTest != None:
        for paramName in thisTest:
            exec('{} = thisTest[paramName]'.format(paramName))
    
    # set up handler to look after randomisation of conditions etc
    trials = data.TrialHandler(nReps=3, method='random', 
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
        
        # ------Prepare to start Routine "Trial"-------
        continueRoutine = True
        # update component parameters for each repeat
        VR=randint(5,10)
        
        # keep track of which components have finished
        TrialComponents = [vending_machine]
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
            if tilt > 0: #keep vending upright
             tilt  = tilt-1
            if tilt < 0:
             tilt = tilt+1
             
            if event.getKeys(['t']): #tilt left
             pressL = pressL+1
             pressR = 0
             tilt = -15
            
            if pressL>VR: #win A
             logging.log(level=logging.DATA, msg = 'win A')
             nRepA=1
             nRepB=0
             continueRoutine=False
             
            if event.getKeys(['v']): #tilt right
             pressR=pressR+1
             pressL=0
             tilt=15
            
            if pressR>VR: #win B
             logging.log(level=logging.DATA, msg = 'win B')
             nRepA=0
             nRepB=1
             continueRoutine=False
            
            
            # *vending_machine* updates
            if vending_machine.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                vending_machine.frameNStart = frameN  # exact frame index
                vending_machine.tStart = t  # local t and not account for scr refresh
                vending_machine.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(vending_machine, 'tStartRefresh')  # time at next scr refresh
                vending_machine.setAutoDraw(True)
            if vending_machine.status == STARTED:  # only update if drawing
                vending_machine.setOri(tilt)
            
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
        trials.addData('vending_machine.started', vending_machine.tStartRefresh)
        trials.addData('vending_machine.stopped', vending_machine.tStopRefresh)
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
            
            # ------Prepare to start Routine "A"-------
            continueRoutine = True
            routineTimer.add(1.000000)
            # update component parameters for each repeat
            # keep track of which components have finished
            AComponents = [vendingA_image, rewardA_image]
            for thisComponent in AComponents:
                thisComponent.tStart = None
                thisComponent.tStop = None
                thisComponent.tStartRefresh = None
                thisComponent.tStopRefresh = None
                if hasattr(thisComponent, 'status'):
                    thisComponent.status = NOT_STARTED
            # reset timers
            t = 0
            _timeToFirstFrame = win.getFutureFlipTime(clock="now")
            AClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
            frameN = -1
            
            # -------Run Routine "A"-------
            while continueRoutine and routineTimer.getTime() > 0:
                # get current time
                t = AClock.getTime()
                tThisFlip = win.getFutureFlipTime(clock=AClock)
                tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                if tilt > 0: #keep vending upright
                 tilt = tilt-1
                if tilt < 0:
                 tilt = tilt+1
                
                if event.getKeys(['t']): #tilt left
                 tilt = -15
                
                if event.getKeys(['v']): #tilt right
                 tilt=15
                
                # *vendingA_image* updates
                if vendingA_image.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    vendingA_image.frameNStart = frameN  # exact frame index
                    vendingA_image.tStart = t  # local t and not account for scr refresh
                    vendingA_image.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(vendingA_image, 'tStartRefresh')  # time at next scr refresh
                    vendingA_image.setAutoDraw(True)
                if vendingA_image.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > vendingA_image.tStartRefresh + 1.0-frameTolerance:
                        # keep track of stop time/frame for later
                        vendingA_image.tStop = t  # not accounting for scr refresh
                        vendingA_image.frameNStop = frameN  # exact frame index
                        win.timeOnFlip(vendingA_image, 'tStopRefresh')  # time at next scr refresh
                        vendingA_image.setAutoDraw(False)
                if vendingA_image.status == STARTED:  # only update if drawing
                    vendingA_image.setOri(tilt)
                
                # *rewardA_image* updates
                if rewardA_image.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    rewardA_image.frameNStart = frameN  # exact frame index
                    rewardA_image.tStart = t  # local t and not account for scr refresh
                    rewardA_image.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(rewardA_image, 'tStartRefresh')  # time at next scr refresh
                    rewardA_image.setAutoDraw(True)
                if rewardA_image.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > rewardA_image.tStartRefresh + 1.0-frameTolerance:
                        # keep track of stop time/frame for later
                        rewardA_image.tStop = t  # not accounting for scr refresh
                        rewardA_image.frameNStop = frameN  # exact frame index
                        win.timeOnFlip(rewardA_image, 'tStopRefresh')  # time at next scr refresh
                        rewardA_image.setAutoDraw(False)
                
                # check for quit (typically the Esc key)
                if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                    core.quit()
                
                # check if all components have finished
                if not continueRoutine:  # a component has requested a forced-end of Routine
                    break
                continueRoutine = False  # will revert to True if at least one component still running
                for thisComponent in AComponents:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
            
            # -------Ending Routine "A"-------
            for thisComponent in AComponents:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            pressL=0 #reset left button count
            pressR=0 #reset right button count
            repA.addData('vendingA_image.started', vendingA_image.tStartRefresh)
            repA.addData('vendingA_image.stopped', vendingA_image.tStopRefresh)
            repA.addData('rewardA_image.started', rewardA_image.tStartRefresh)
            repA.addData('rewardA_image.stopped', rewardA_image.tStopRefresh)
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
            
            # ------Prepare to start Routine "B"-------
            continueRoutine = True
            routineTimer.add(1.000000)
            # update component parameters for each repeat
            # keep track of which components have finished
            BComponents = [vendingB_image, rewardB_image]
            for thisComponent in BComponents:
                thisComponent.tStart = None
                thisComponent.tStop = None
                thisComponent.tStartRefresh = None
                thisComponent.tStopRefresh = None
                if hasattr(thisComponent, 'status'):
                    thisComponent.status = NOT_STARTED
            # reset timers
            t = 0
            _timeToFirstFrame = win.getFutureFlipTime(clock="now")
            BClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
            frameN = -1
            
            # -------Run Routine "B"-------
            while continueRoutine and routineTimer.getTime() > 0:
                # get current time
                t = BClock.getTime()
                tThisFlip = win.getFutureFlipTime(clock=BClock)
                tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                if tilt > 0: #keep vending upright
                 tilt = tilt-1
                if tilt < 0:
                 tilt = tilt+1
                
                if event.getKeys(['t']): #tilt left
                 tilt = -15
                
                if event.getKeys(['v']): #tilt right
                 tilt=15
                
                # *vendingB_image* updates
                if vendingB_image.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    vendingB_image.frameNStart = frameN  # exact frame index
                    vendingB_image.tStart = t  # local t and not account for scr refresh
                    vendingB_image.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(vendingB_image, 'tStartRefresh')  # time at next scr refresh
                    vendingB_image.setAutoDraw(True)
                if vendingB_image.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > vendingB_image.tStartRefresh + 1.0-frameTolerance:
                        # keep track of stop time/frame for later
                        vendingB_image.tStop = t  # not accounting for scr refresh
                        vendingB_image.frameNStop = frameN  # exact frame index
                        win.timeOnFlip(vendingB_image, 'tStopRefresh')  # time at next scr refresh
                        vendingB_image.setAutoDraw(False)
                if vendingB_image.status == STARTED:  # only update if drawing
                    vendingB_image.setOri(tilt)
                
                # *rewardB_image* updates
                if rewardB_image.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    rewardB_image.frameNStart = frameN  # exact frame index
                    rewardB_image.tStart = t  # local t and not account for scr refresh
                    rewardB_image.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(rewardB_image, 'tStartRefresh')  # time at next scr refresh
                    rewardB_image.setAutoDraw(True)
                if rewardB_image.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > rewardB_image.tStartRefresh + 1.0-frameTolerance:
                        # keep track of stop time/frame for later
                        rewardB_image.tStop = t  # not accounting for scr refresh
                        rewardB_image.frameNStop = frameN  # exact frame index
                        win.timeOnFlip(rewardB_image, 'tStopRefresh')  # time at next scr refresh
                        rewardB_image.setAutoDraw(False)
                
                # check for quit (typically the Esc key)
                if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                    core.quit()
                
                # check if all components have finished
                if not continueRoutine:  # a component has requested a forced-end of Routine
                    break
                continueRoutine = False  # will revert to True if at least one component still running
                for thisComponent in BComponents:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
            
            # -------Ending Routine "B"-------
            for thisComponent in BComponents:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            pressL=0 #reset left button count
            pressR=0 #reset right button count
            repB.addData('vendingB_image.started', vendingB_image.tStartRefresh)
            repB.addData('vendingB_image.stopped', vendingB_image.tStopRefresh)
            repB.addData('rewardB_image.started', rewardB_image.tStartRefresh)
            repB.addData('rewardB_image.stopped', rewardB_image.tStopRefresh)
            thisExp.nextEntry()
            
        # completed nRepB repeats of 'repB'
        
        thisExp.nextEntry()
        
    # completed 3 repeats of 'trials'
    
    
    # ------Prepare to start Routine "test"-------
    continueRoutine = True
    # update component parameters for each repeat
    if nRepB == 1:
      testImage=rewardB
      correctAns='v'
    if nRepA == 1:
      testImage=rewardA
      correctAns='t'
    
    test_image.setImage(testImage)
    test_response.keys = []
    test_response.rt = []
    _test_response_allKeys = []
    # keep track of which components have finished
    testComponents = [test_question, test_instructions, test_image, test_response]
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
    while continueRoutine:
        # get current time
        t = testClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=testClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *test_question* updates
        if test_question.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            test_question.frameNStart = frameN  # exact frame index
            test_question.tStart = t  # local t and not account for scr refresh
            test_question.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(test_question, 'tStartRefresh')  # time at next scr refresh
            test_question.setAutoDraw(True)
        
        # *test_instructions* updates
        if test_instructions.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            test_instructions.frameNStart = frameN  # exact frame index
            test_instructions.tStart = t  # local t and not account for scr refresh
            test_instructions.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(test_instructions, 'tStartRefresh')  # time at next scr refresh
            test_instructions.setAutoDraw(True)
        
        # *test_image* updates
        if test_image.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            test_image.frameNStart = frameN  # exact frame index
            test_image.tStart = t  # local t and not account for scr refresh
            test_image.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(test_image, 'tStartRefresh')  # time at next scr refresh
            test_image.setAutoDraw(True)
        
        # *test_response* updates
        waitOnFlip = False
        if test_response.status == NOT_STARTED and tThisFlip >= 3-frameTolerance:
            # keep track of start time/frame for later
            test_response.frameNStart = frameN  # exact frame index
            test_response.tStart = t  # local t and not account for scr refresh
            test_response.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(test_response, 'tStartRefresh')  # time at next scr refresh
            test_response.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(test_response.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(test_response.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if test_response.status == STARTED and not waitOnFlip:
            theseKeys = test_response.getKeys(keyList=['t', 'v'], waitRelease=False)
            _test_response_allKeys.extend(theseKeys)
            if len(_test_response_allKeys):
                test_response.keys = _test_response_allKeys[0].name  # just the first key pressed
                test_response.rt = _test_response_allKeys[0].rt
                # was this correct?
                if (test_response.keys == str(correctAns)) or (test_response.keys == correctAns):
                    test_response.corr = 1
                else:
                    test_response.corr = 0
                # a response ends the routine
                continueRoutine = False
        
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
    tests.addData('test_question.started', test_question.tStartRefresh)
    tests.addData('test_question.stopped', test_question.tStopRefresh)
    tests.addData('test_instructions.started', test_instructions.tStartRefresh)
    tests.addData('test_instructions.stopped', test_instructions.tStopRefresh)
    tests.addData('test_image.started', test_image.tStartRefresh)
    tests.addData('test_image.stopped', test_image.tStopRefresh)
    # check responses
    if test_response.keys in ['', [], None]:  # No response was made
        test_response.keys = None
        # was no response the correct answer?!
        if str(correctAns).lower() == 'none':
           test_response.corr = 1;  # correct non-response
        else:
           test_response.corr = 0;  # failed to respond (incorrectly)
    # store data for tests (TrialHandler)
    tests.addData('test_response.keys',test_response.keys)
    tests.addData('test_response.corr', test_response.corr)
    if test_response.keys != None:  # we had a response
        tests.addData('test_response.rt', test_response.rt)
    tests.addData('test_response.started', test_response.tStartRefresh)
    tests.addData('test_response.stopped', test_response.tStopRefresh)
    # the Routine "test" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "feedback"-------
    continueRoutine = True
    routineTimer.add(1.000000)
    # update component parameters for each repeat
    if test_response.corr:
      msg1="correct!"
      logging.log(level=logging.DATA, msg = 'correct')
      Error=Error-1
    else:
      msg1="Oops! That was wrong"
      logging.log(level=logging.DATA, msg = 'Oops!')
      Error=6
    feedback_text.setText(msg1)
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
    logging.flush()
    if Error<1:
     tests.finished=True
    
    
    tests.addData('feedback_text.started', feedback_text.tStartRefresh)
    tests.addData('feedback_text.stopped', feedback_text.tStopRefresh)
    thisExp.nextEntry()
    
# completed nTest repeats of 'tests'


# ------Prepare to start Routine "finish"-------
continueRoutine = True
routineTimer.add(3.000000)
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
while continueRoutine and routineTimer.getTime() > 0:
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
    if finish_text.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > finish_text.tStartRefresh + 3.0-frameTolerance:
            # keep track of stop time/frame for later
            finish_text.tStop = t  # not accounting for scr refresh
            finish_text.frameNStop = frameN  # exact frame index
            win.timeOnFlip(finish_text, 'tStopRefresh')  # time at next scr refresh
            finish_text.setAutoDraw(False)
    
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

# Flip one final time so any remaining win.callOnFlip() 
# and win.timeOnFlip() tasks get executed before quitting
win.flip()

# these shouldn't be strictly necessary (should auto-save)
logging.flush()
# make sure everything is closed down
thisExp.abort()  # or data files will save again on exit
win.close()
core.quit()
