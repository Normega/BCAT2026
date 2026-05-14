#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2024.1.4),
    on July 18, 2025, at 11:02
If you publish work using this script the most relevant publication is:

    Peirce J, Gray JR, Simpson S, MacAskill M, Höchenberger R, Sogo H, Kastman E, Lindeløv JK. (2019) 
        PsychoPy2: Experiments in behavior made easy Behav Res 51: 195. 
        https://doi.org/10.3758/s13428-018-01193-y

"""

# --- Import packages ---
from psychopy import locale_setup
from psychopy import prefs
from psychopy import plugins
plugins.activatePlugins()
prefs.hardware['audioLib'] = 'ptb'
prefs.hardware['audioLatencyMode'] = '3'
from psychopy import sound, gui, visual, core, data, event, logging, clock, colors, layout, hardware, parallel
from psychopy.tools import environmenttools
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER, priority)

import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle, choice as randchoice
import os  # handy system and path functions
import sys  # to get file system encoding

import psychopy.iohub as io
from psychopy.hardware import keyboard

# Run 'Before Experiment' code from StartupCode
def std(numbers, is_sample=True):
    # Calculate the standard deviation of a list of numbers without using external libraries.
    # Check for valid input
    if not numbers:
        raise ValueError("Cannot calculate standard deviation of empty list")
    if is_sample and len(numbers) < 2:
        raise ValueError("Sample standard deviation requires at least 2 values")
    
    # Calculate mean
    mean = sum(numbers) / len(numbers)
    
    # Calculate sum of squared differences from mean
    squared_diff_sum = 0
    for x in numbers:
        squared_diff_sum += (x - mean) ** 2
    
    # Determine divisor based on whether we're calculating sample or population std dev
    divisor = len(numbers) - 1 if is_sample else len(numbers)
    
    # Calculate standard deviation using exponentiation operator for square root
    std_dev = (squared_diff_sum / divisor) ** 0.5
    
    return std_dev

backcolor = [0.6549, 0.6549, 0.6549]
textColor = [-1.0000, -1.0000, -1.0000]
trialNum = 0

# Run 'Before Experiment' code from code
nLocalTrial = 0

# --- Setup global variables (available in all functions) ---
# create a device manager to handle hardware (keyboards, mice, mirophones, speakers, etc.)
deviceManager = hardware.DeviceManager()
# ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
# store info about the experiment session
psychopyVersion = '2024.1.4'
expName = 'Intero2025'  # from the Builder filename that created this script
# information about this experiment
expInfo = {
    'Participant': '0001',
    'Condition': 'breath',
    'date|hid': data.getDateStr(),
    'expName|hid': expName,
    'psychopyVersion|hid': psychopyVersion,
}

# --- Define some variables which will change depending on pilot mode ---
'''
To run in pilot mode, either use the run/pilot toggle in Builder, Coder and Runner, 
or run the experiment with `--pilot` as an argument. To change what pilot 
#mode does, check out the 'Pilot mode' tab in preferences.
'''
# work out from system args whether we are running in pilot mode
PILOTING = core.setPilotModeFromArgs()
# start off with values from experiment settings
_fullScr = True
_winSize = [1920, 1080]
_loggingLevel = logging.getLevel('warning')
# if in pilot mode, apply overrides according to preferences
if PILOTING:
    # force windowed mode
    if prefs.piloting['forceWindowed']:
        _fullScr = False
        # set window size
        _winSize = prefs.piloting['forcedWindowSize']
    # override logging level
    _loggingLevel = logging.getLevel(
        prefs.piloting['pilotLoggingLevel']
    )

def showExpInfoDlg(expInfo):
    """
    Show participant info dialog.
    Parameters
    ==========
    expInfo : dict
        Information about this experiment.
    
    Returns
    ==========
    dict
        Information about this experiment.
    """
    # show participant info dialog
    dlg = gui.DlgFromDict(
        dictionary=expInfo, sortKeys=False, title=expName, alwaysOnTop=True
    )
    if dlg.OK == False:
        core.quit()  # user pressed cancel
    # return expInfo
    return expInfo


def setupData(expInfo, dataDir=None):
    """
    Make an ExperimentHandler to handle trials and saving.
    
    Parameters
    ==========
    expInfo : dict
        Information about this experiment, created by the `setupExpInfo` function.
    dataDir : Path, str or None
        Folder to save the data to, leave as None to create a folder in the current directory.    
    Returns
    ==========
    psychopy.data.ExperimentHandler
        Handler object for this experiment, contains the data to save and information about 
        where to save it to.
    """
    # remove dialog-specific syntax from expInfo
    for key, val in expInfo.copy().items():
        newKey, _ = data.utils.parsePipeSyntax(key)
        expInfo[newKey] = expInfo.pop(key)
    
    # data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
    if dataDir is None:
        dataDir = _thisDir
    filename = u'data/%s_%s_%s' % (expInfo['Participant'], expName, expInfo['date'])
    # make sure filename is relative to dataDir
    if os.path.isabs(filename):
        dataDir = os.path.commonprefix([dataDir, filename])
        filename = os.path.relpath(filename, dataDir)
    
    # an ExperimentHandler isn't essential but helps with data saving
    thisExp = data.ExperimentHandler(
        name=expName, version='',
        extraInfo=expInfo, runtimeInfo=None,
        originPath='G:\\My Drive\\InteroSummer2025\\Task\\FirstRound_RightComputer_InteroSummer2025_lastrun.py',
        savePickle=True, saveWideText=True,
        dataFileName=dataDir + os.sep + filename, sortColumns='time'
    )
    thisExp.setPriority('thisRow.t', priority.CRITICAL)
    thisExp.setPriority('expName', priority.LOW)
    # return experiment handler
    return thisExp


def setupLogging(filename):
    """
    Setup a log file and tell it what level to log at.
    
    Parameters
    ==========
    filename : str or pathlib.Path
        Filename to save log file and data files as, doesn't need an extension.
    
    Returns
    ==========
    psychopy.logging.LogFile
        Text stream to receive inputs from the logging system.
    """
    # this outputs to the screen, not a file
    logging.console.setLevel(_loggingLevel)
    # save a log file for detail verbose info
    logFile = logging.LogFile(filename+'.log', level=_loggingLevel)
    
    return logFile


def setupWindow(expInfo=None, win=None):
    """
    Setup the Window
    
    Parameters
    ==========
    expInfo : dict
        Information about this experiment, created by the `setupExpInfo` function.
    win : psychopy.visual.Window
        Window to setup - leave as None to create a new window.
    
    Returns
    ==========
    psychopy.visual.Window
        Window in which to run this experiment.
    """
    if PILOTING:
        logging.debug('Fullscreen settings ignored as running in pilot mode.')
    
    if win is None:
        # if not given a window to setup, make one
        win = visual.Window(
            size=_winSize, fullscr=_fullScr, screen=0,
            winType='pyglet', allowStencil=True,
            monitor='testMonitor', color=backcolor, colorSpace='rgb',
            backgroundImage='', backgroundFit='none',
            blendMode='avg', useFBO=True,
            units='height', 
            checkTiming=False  # we're going to do this ourselves in a moment
        )
    else:
        # if we have a window, just set the attributes which are safe to set
        win.color = backcolor
        win.colorSpace = 'rgb'
        win.backgroundImage = ''
        win.backgroundFit = 'none'
        win.units = 'height'
    if expInfo is not None:
        # get/measure frame rate if not already in expInfo
        if win._monitorFrameRate is None:
            win.getActualFrameRate(infoMsg='Attempting to measure frame rate of screen, please wait...')
        expInfo['frameRate'] = win._monitorFrameRate
    win.mouseVisible = False
    win.hideMessage()
    # show a visual indicator if we're in piloting mode
    if PILOTING and prefs.piloting['showPilotingIndicator']:
        win.showPilotingIndicator()
    
    return win


def setupDevices(expInfo, thisExp, win):
    """
    Setup whatever devices are available (mouse, keyboard, speaker, eyetracker, etc.) and add them to 
    the device manager (deviceManager)
    
    Parameters
    ==========
    expInfo : dict
        Information about this experiment, created by the `setupExpInfo` function.
    thisExp : psychopy.data.ExperimentHandler
        Handler object for this experiment, contains the data to save and information about 
        where to save it to.
    win : psychopy.visual.Window
        Window in which to run this experiment.
    Returns
    ==========
    bool
        True if completed successfully.
    """
    # --- Setup input devices ---
    ioConfig = {}
    
    # Setup iohub keyboard
    ioConfig['Keyboard'] = dict(use_keymap='psychopy')
    
    ioSession = '1'
    if 'session' in expInfo:
        ioSession = str(expInfo['session'])
    ioServer = io.launchHubServer(window=win, **ioConfig)
    # store ioServer object in the device manager
    deviceManager.ioServer = ioServer
    
    # create a default keyboard (e.g. to check for escape)
    if deviceManager.getDevice('defaultKeyboard') is None:
        deviceManager.addDevice(
            deviceClass='keyboard', deviceName='defaultKeyboard', backend='iohub'
        )
    if deviceManager.getDevice('key_resp') is None:
        # initialise key_resp
        key_resp = deviceManager.addDevice(
            deviceClass='keyboard',
            deviceName='key_resp',
        )
    if deviceManager.getDevice('key_resp_4') is None:
        # initialise key_resp_4
        key_resp_4 = deviceManager.addDevice(
            deviceClass='keyboard',
            deviceName='key_resp_4',
        )
    if deviceManager.getDevice('key_resp_3') is None:
        # initialise key_resp_3
        key_resp_3 = deviceManager.addDevice(
            deviceClass='keyboard',
            deviceName='key_resp_3',
        )
    if deviceManager.getDevice('kbChange') is None:
        # initialise kbChange
        kbChange = deviceManager.addDevice(
            deviceClass='keyboard',
            deviceName='kbChange',
        )
    if deviceManager.getDevice('key_resp_2') is None:
        # initialise key_resp_2
        key_resp_2 = deviceManager.addDevice(
            deviceClass='keyboard',
            deviceName='key_resp_2',
        )
    if deviceManager.getDevice('key_space') is None:
        # initialise key_space
        key_space = deviceManager.addDevice(
            deviceClass='keyboard',
            deviceName='key_space',
        )
    if deviceManager.getDevice('key_space_2') is None:
        # initialise key_space_2
        key_space_2 = deviceManager.addDevice(
            deviceClass='keyboard',
            deviceName='key_space_2',
        )
    if deviceManager.getDevice('key_space_3') is None:
        # initialise key_space_3
        key_space_3 = deviceManager.addDevice(
            deviceClass='keyboard',
            deviceName='key_space_3',
        )
    # return True if completed successfully
    return True

def pauseExperiment(thisExp, win=None, timers=[], playbackComponents=[]):
    """
    Pause this experiment, preventing the flow from advancing to the next routine until resumed.
    
    Parameters
    ==========
    thisExp : psychopy.data.ExperimentHandler
        Handler object for this experiment, contains the data to save and information about 
        where to save it to.
    win : psychopy.visual.Window
        Window for this experiment.
    timers : list, tuple
        List of timers to reset once pausing is finished.
    playbackComponents : list, tuple
        List of any components with a `pause` method which need to be paused.
    """
    # if we are not paused, do nothing
    if thisExp.status != PAUSED:
        return
    
    # pause any playback components
    for comp in playbackComponents:
        comp.pause()
    # prevent components from auto-drawing
    win.stashAutoDraw()
    # make sure we have a keyboard
    defaultKeyboard = deviceManager.getDevice('defaultKeyboard')
    if defaultKeyboard is None:
        defaultKeyboard = deviceManager.addKeyboard(
            deviceClass='keyboard',
            deviceName='defaultKeyboard',
            backend='ioHub',
        )
    # run a while loop while we wait to unpause
    while thisExp.status == PAUSED:
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=['escape']):
            endExperiment(thisExp, win=win)
        # flip the screen
        win.flip()
    # if stop was requested while paused, quit
    if thisExp.status == FINISHED:
        endExperiment(thisExp, win=win)
    # resume any playback components
    for comp in playbackComponents:
        comp.play()
    # restore auto-drawn components
    win.retrieveAutoDraw()
    # reset any timers
    for timer in timers:
        timer.reset()


def run(expInfo, thisExp, win, globalClock=None, thisSession=None):
    """
    Run the experiment flow.
    
    Parameters
    ==========
    expInfo : dict
        Information about this experiment, created by the `setupExpInfo` function.
    thisExp : psychopy.data.ExperimentHandler
        Handler object for this experiment, contains the data to save and information about 
        where to save it to.
    psychopy.visual.Window
        Window in which to run this experiment.
    globalClock : psychopy.core.clock.Clock or None
        Clock to get global time from - supply None to make a new one.
    thisSession : psychopy.session.Session or None
        Handle of the Session object this experiment is being run from, if any.
    """
    # mark experiment as started
    thisExp.status = STARTED
    # make sure variables created by exec are available globally
    exec = environmenttools.setExecEnvironment(globals())
    # get device handles from dict of input devices
    ioServer = deviceManager.ioServer
    # get/create a default keyboard (e.g. to check for escape)
    defaultKeyboard = deviceManager.getDevice('defaultKeyboard')
    if defaultKeyboard is None:
        deviceManager.addDevice(
            deviceClass='keyboard', deviceName='defaultKeyboard', backend='ioHub'
        )
    eyetracker = deviceManager.getDevice('eyetracker')
    # make sure we're running in the directory for this experiment
    os.chdir(_thisDir)
    # get filename from ExperimentHandler for convenience
    filename = thisExp.dataFileName
    frameTolerance = 0.001  # how close to onset before 'same' frame
    endExpNow = False  # flag for 'escape' or other condition => quit the exp
    # get frame duration from frame rate in expInfo
    if 'frameRate' in expInfo and expInfo['frameRate'] is not None:
        frameDur = 1.0 / round(expInfo['frameRate'])
    else:
        frameDur = 1.0 / 60.0  # could not measure, so guess
    
    # Start Code - component code to be run after the window creation
    
    # --- Initialize components for Routine "StartupCode" ---
    # Run 'Begin Experiment' code from StartupCode
    Condition = expInfo['Condition']
    
    if (Condition == 'breath'):
        instructText = """Please breathe along with the circle.
        Breathe in as the circle gets larger,
        and breathe out as the circle gets smaller.
        
        Try to notice if your breathing speed is changing."""
    else:
        instructText = """Please watch the circle.
        Notice as the circle gets larger,
        and notice as the circle gets smaller.
        
        Try to notice if the circle speed is changing."""
    
    resetCycleDuration = 4 #starting breath length (in s)
    circleSize = .5
    numBreaths = 4
    freshBreath = True
    
    #changeVal = 1.2
    #changeSalience = 1
    midPoint = round(numBreaths / 2,0)
    
    n_highSalienceACC = 0
    n_lowSalienceACC = 0
    n_highSalienceDEC = 0
    n_lowSalienceDEC = 0
    
    highIntensitiesACC = []
    lowIntensitiesACC = []
    highIntensitiesDEC = []
    lowIntensitiesDEC = []
    
    highSEACC = ""
    lowSEACC = ""
    highSEDEC = ""
    lowSEDEC= ""
    
    highSalienceCIDEC = ""
    lowSalienceCIDEC = ""
    highSalienceCIACC = ""
    lowSalienceCIACC = ""
    
    highStopOKACC = False
    lowStopOKACC = False
    highStopOKDEC = False
    lowStopOKDEC = False
    
    highCIACC = ""
    lowCIACC = ""
    highCIDEC = ""
    lowCIDEC = ""
    
    highStepACC = ""
    lowStepACC = ""
    highStepDEC = ""
    lowStepDEC = ""
    
    lastHighLevelACC = .5
    lastLowLevelACC = .5
    lastHighLevelDEC = .5
    lastLowLevelDEC = .5
    
    #Eventually calculate the thresholds
    T_hiAc = ""
    T_loAc = ""
    T_hiDe = ""
    T_loDe = ""
    
    #Thresholds generate critical thresholds
    Crit_Ac = ""
    Crit_De = ""
    port_startexp = parallel.ParallelPort(address='0xD030')
    
    # --- Initialize components for Routine "judgeValence" ---
    valenceImage = visual.ImageStim(
        win=win,
        name='valenceImage', 
        image='images/ValenceImg.png', mask=None, anchor='center',
        ori=0.0, pos=(0, 0), size=(1.0, 0.307),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=0.0)
    valenceSlider = visual.Slider(win=win, name='valenceSlider',
        startValue=3, size=(.8, 0.1), pos=(0, -0.3), units=win.units,
        labels=(1, 2, 3, 4, 5, 6), ticks=(1, 2, 3, 4, 5, 6), granularity=1.0,
        style='rating', styleTweaks=('triangleMarker',), opacity=None,
        labelColor=[-1.0000, -1.0000, -1.0000], markerColor='Red', lineColor=[-1.0000, -1.0000, -1.0000], colorSpace='rgb',
        font='Open Sans', labelHeight=0.05,
        flip=False, ori=0.0, depth=-1, readOnly=False)
    
    # --- Initialize components for Routine "judgearousal_2" ---
    arousalImage = visual.ImageStim(
        win=win,
        name='arousalImage', 
        image='images/ArousalImg.png', mask=None, anchor='center',
        ori=0.0, pos=(0, 0), size=(1.0, 0.307),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=0.0)
    arousalSlider = visual.Slider(win=win, name='arousalSlider',
        startValue=3, size=(0.8, 0.1), pos=(0, -0.3), units=win.units,
        labels=(1, 2, 3, 4, 5, 6), ticks=(1, 2, 3, 4, 5, 6), granularity=1.0,
        style='rating', styleTweaks=('triangleMarker',), opacity=None,
        labelColor=[-1.0000, -1.0000, -1.0000], markerColor='Red', lineColor=[-1.0000, -1.0000, -1.0000], colorSpace='rgb',
        font='Open Sans', labelHeight=0.05,
        flip=False, ori=0.0, depth=-1, readOnly=False)
    
    # --- Initialize components for Routine "Start" ---
    text = visual.TextStim(win=win, name='text',
        text='Welcome to the Sensory Attention Task \n\nIn this task you will see a circle grow and shrink 4 times in a row.  You will be judging whether things are speeding up, slowing down, or staying the same.\n\nPress the <spacebar> to continue...',
        font='Arial',
        pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
        color=textColor, colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    key_resp = keyboard.Keyboard(deviceName='key_resp')
    
    # --- Initialize components for Routine "Instruct1" ---
    text_7 = visual.TextStim(win=win, name='text_7',
        text=instructText,
        font='Arial',
        pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
        color=textColor, colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    key_resp_4 = keyboard.Keyboard(deviceName='key_resp_4')
    
    # --- Initialize components for Routine "Instruct2" ---
    text_3 = visual.TextStim(win=win, name='text_3',
        text='After 4 pulses of the circle, you will be asked if things: slowed down (left arrow), stayed the same (up arrow), or sped up (right arrow). There will be a picture to remind you.\n\nYou will then be asked to rate your confidence in your judgment, and how energetic you feel. \n\nPress <spacebar> to begin...',
        font='Arial',
        pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
        color=textColor, colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    key_resp_3 = keyboard.Keyboard(deviceName='key_resp_3')
    
    # --- Initialize components for Routine "trial" ---
    Circle = visual.ShapeStim(
        win=win, name='Circle',
        size=circleSize, vertices='circle',
        ori=0.0, pos=(0, 0), anchor='center',
        lineWidth=1.0,     colorSpace='rgb',  lineColor=[-1.0000, -1.0000, 0.0902], fillColor=[-1.0000, -1.0000, 1.0000],
        opacity=None, depth=0.0, interpolate=True)
    port_starttrial = parallel.ParallelPort(address='0xD030')
    
    # --- Initialize components for Routine "judgebreath" ---
    kbChange = keyboard.Keyboard(deviceName='kbChange')
    speedImage = visual.ImageStim(
        win=win,
        name='speedImage', 
        image='images/SpeedImg.png', mask=None, anchor='center',
        ori=0.0, pos=(0, 0), size=(1,.483),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=-1.0)
    port_teststop = parallel.ParallelPort(address='0xD030')
    
    # --- Initialize components for Routine "judgeconfidence" ---
    confidenceImage = visual.ImageStim(
        win=win,
        name='confidenceImage', 
        image='images/ConfidenceImg.png', mask=None, anchor='center',
        ori=0.0, pos=(0, 0), size=(1.0, 0.307),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=0.0)
    confidenceSlider = visual.Slider(win=win, name='confidenceSlider',
        startValue=3, size=(.8, 0.1), pos=(0, -0.3), units=win.units,
        labels=(1, 2, 3, 4, 5, 6), ticks=(1, 2, 3, 4, 5, 6), granularity=1.0,
        style='rating', styleTweaks=('triangleMarker',), opacity=None,
        labelColor=[-1.0000, -1.0000, -1.0000], markerColor='Red', lineColor=[-1.0000, -1.0000, -1.0000], colorSpace='rgb',
        font='Open Sans', labelHeight=0.05,
        flip=False, ori=0.0, depth=-1, readOnly=False)
    
    # --- Initialize components for Routine "judgearousal_2" ---
    arousalImage = visual.ImageStim(
        win=win,
        name='arousalImage', 
        image='images/ArousalImg.png', mask=None, anchor='center',
        ori=0.0, pos=(0, 0), size=(1.0, 0.307),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=0.0)
    arousalSlider = visual.Slider(win=win, name='arousalSlider',
        startValue=3, size=(0.8, 0.1), pos=(0, -0.3), units=win.units,
        labels=(1, 2, 3, 4, 5, 6), ticks=(1, 2, 3, 4, 5, 6), granularity=1.0,
        style='rating', styleTweaks=('triangleMarker',), opacity=None,
        labelColor=[-1.0000, -1.0000, -1.0000], markerColor='Red', lineColor=[-1.0000, -1.0000, -1.0000], colorSpace='rgb',
        font='Open Sans', labelHeight=0.05,
        flip=False, ori=0.0, depth=-1, readOnly=False)
    
    # --- Initialize components for Routine "CalcThresholds" ---
    
    # --- Initialize components for Routine "TestTrialInstruct" ---
    text_2 = visual.TextStim(win=win, name='text_2',
        text="Great! Let's do just a few more rounds to see if we've measured correctly.\n\nPlease press <spacebar> to begin.",
        font='Arial',
        pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
        color=[-1.0000, -1.0000, -1.0000], colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    key_resp_2 = keyboard.Keyboard(deviceName='key_resp_2')
    
    # --- Initialize components for Routine "TestTrial" ---
    TestCircle = visual.ShapeStim(
        win=win, name='TestCircle',
        size=circleSize, vertices='circle',
        ori=0.0, pos=(0, 0), anchor='center',
        lineWidth=1.0,     colorSpace='rgb',  lineColor=[-1.0000, -1.0000, 0.0902], fillColor=[-1.0000, -1.0000, 1.0000],
        opacity=None, depth=0.0, interpolate=True)
    port_teststart = parallel.ParallelPort(address='0xD030')
    
    # --- Initialize components for Routine "judgebreath" ---
    kbChange = keyboard.Keyboard(deviceName='kbChange')
    speedImage = visual.ImageStim(
        win=win,
        name='speedImage', 
        image='images/SpeedImg.png', mask=None, anchor='center',
        ori=0.0, pos=(0, 0), size=(1,.483),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=-1.0)
    port_teststop = parallel.ParallelPort(address='0xD030')
    
    # --- Initialize components for Routine "judgeconfidence" ---
    confidenceImage = visual.ImageStim(
        win=win,
        name='confidenceImage', 
        image='images/ConfidenceImg.png', mask=None, anchor='center',
        ori=0.0, pos=(0, 0), size=(1.0, 0.307),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=0.0)
    confidenceSlider = visual.Slider(win=win, name='confidenceSlider',
        startValue=3, size=(.8, 0.1), pos=(0, -0.3), units=win.units,
        labels=(1, 2, 3, 4, 5, 6), ticks=(1, 2, 3, 4, 5, 6), granularity=1.0,
        style='rating', styleTweaks=('triangleMarker',), opacity=None,
        labelColor=[-1.0000, -1.0000, -1.0000], markerColor='Red', lineColor=[-1.0000, -1.0000, -1.0000], colorSpace='rgb',
        font='Open Sans', labelHeight=0.05,
        flip=False, ori=0.0, depth=-1, readOnly=False)
    
    # --- Initialize components for Routine "judgearousal_2" ---
    arousalImage = visual.ImageStim(
        win=win,
        name='arousalImage', 
        image='images/ArousalImg.png', mask=None, anchor='center',
        ori=0.0, pos=(0, 0), size=(1.0, 0.307),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=0.0)
    arousalSlider = visual.Slider(win=win, name='arousalSlider',
        startValue=3, size=(0.8, 0.1), pos=(0, -0.3), units=win.units,
        labels=(1, 2, 3, 4, 5, 6), ticks=(1, 2, 3, 4, 5, 6), granularity=1.0,
        style='rating', styleTweaks=('triangleMarker',), opacity=None,
        labelColor=[-1.0000, -1.0000, -1.0000], markerColor='Red', lineColor=[-1.0000, -1.0000, -1.0000], colorSpace='rgb',
        font='Open Sans', labelHeight=0.05,
        flip=False, ori=0.0, depth=-1, readOnly=False)
    
    # --- Initialize components for Routine "CompleteInstruct" ---
    key_space = keyboard.Keyboard(deviceName='key_space')
    text_4 = visual.TextStim(win=win, name='text_4',
        text="Great! You've completed the circle task.\n\nPress <spacebar> to continue.",
        font='Arial',
        pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
        color=textColor, colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-1.0);
    
    # --- Initialize components for Routine "HeartInstruct" ---
    key_space_2 = keyboard.Keyboard(deviceName='key_space_2')
    text_5 = visual.TextStim(win=win, name='text_5',
        text="Now we'd like you to try to focus on your heartbeat.\n\nWhen you see the word 'count' on the screen, please start counting the heartbeats that you can feel, without 'taking your pulse' with your fingers. \nJust count up from 0 for every hearbeat that you can sense until the word 'count' disappears.\n\nPress <spacebar> when you are ready to start.",
        font='Arial',
        pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
        color=textColor, colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-1.0);
    
    # --- Initialize components for Routine "HeartCount" ---
    readyScreen = visual.TextStim(win=win, name='readyScreen',
        text='Get ready to count your heartbeats...',
        font='Arial',
        pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
        color=textColor, colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    countScreen = visual.TextStim(win=win, name='countScreen',
        text='*******************************\n*** Count your Heartbeats ***\n*******************************',
        font='Arial',
        pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
        color=textColor, colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-1.0);
    port_HRstart = parallel.ParallelPort(address='0xD030')
    
    # --- Initialize components for Routine "HeartReport" ---
    beatReport = visual.TextStim(win=win, name='beatReport',
        text='Please type in the number of heartbeats that you counted and press <enter>',
        font='Arial',
        pos=(0, .3), height=0.05, wrapWidth=None, ori=0.0, 
        color=textColor, colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    HRenter_text = visual.TextBox2(
         win, text='', placeholder=None, font='Arial',
         pos=(0, -.1),     letterHeight=0.05,
         size=(0.5, 0.5), borderWidth=2.0,
         color=textColor, colorSpace='rgb',
         opacity=None,
         bold=False, italic=False,
         lineSpacing=1.0, speechPoint=None,
         padding=0.0, alignment='center',
         anchor='center', overflow='visible',
         fillColor=None, borderColor=None,
         flipHoriz=False, flipVert=False, languageStyle='LTR',
         editable=True,
         name='HRenter_text',
         depth=-1, autoLog=True,
    )
    # Run 'Begin Experiment' code from HRenter_code
    HRtext = ""
    lastKey = ""
    
    port_HRstop = parallel.ParallelPort(address='0xD030')
    
    # --- Initialize components for Routine "EndPart1" ---
    key_space_3 = keyboard.Keyboard(deviceName='key_space_3')
    text_6 = visual.TextStim(win=win, name='text_6',
        text="Great! Please let the researcher know that you've finished this section of the study.",
        font='Arial',
        pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
        color=textColor, colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-1.0);
    port_stopexp = parallel.ParallelPort(address='0xD030')
    
    # create some handy timers
    
    # global clock to track the time since experiment started
    if globalClock is None:
        # create a clock if not given one
        globalClock = core.Clock()
    if isinstance(globalClock, str):
        # if given a string, make a clock accoridng to it
        if globalClock == 'float':
            # get timestamps as a simple value
            globalClock = core.Clock(format='float')
        elif globalClock == 'iso':
            # get timestamps in ISO format
            globalClock = core.Clock(format='%Y-%m-%d_%H:%M:%S.%f%z')
        else:
            # get timestamps in a custom format
            globalClock = core.Clock(format=globalClock)
    if ioServer is not None:
        ioServer.syncClock(globalClock)
    logging.setDefaultClock(globalClock)
    # routine timer to track time remaining of each (possibly non-slip) routine
    routineTimer = core.Clock()
    win.flip()  # flip window to reset last flip timer
    # store the exact time the global clock started
    expInfo['expStart'] = data.getDateStr(
        format='%Y-%m-%d %Hh%M.%S.%f %z', fractionalSecondDigits=6
    )
    
    # --- Prepare to start Routine "StartupCode" ---
    continueRoutine = True
    # update component parameters for each repeat
    thisExp.addData('StartupCode.started', globalClock.getTime(format='float'))
    # keep track of which components have finished
    StartupCodeComponents = [port_startexp]
    for thisComponent in StartupCodeComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "StartupCode" ---
    routineForceEnded = not continueRoutine
    while continueRoutine and routineTimer.getTime() < 1.0:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        # *port_startexp* updates
        
        # if port_startexp is starting this frame...
        if port_startexp.status == NOT_STARTED and t >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            port_startexp.frameNStart = frameN  # exact frame index
            port_startexp.tStart = t  # local t and not account for scr refresh
            port_startexp.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(port_startexp, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.addData('port_startexp.started', t)
            # update status
            port_startexp.status = STARTED
            port_startexp.status = STARTED
            win.callOnFlip(port_startexp.setData, int(1))
        
        # if port_startexp is stopping this frame...
        if port_startexp.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > port_startexp.tStartRefresh + 1.0-frameTolerance:
                # keep track of stop time/frame for later
                port_startexp.tStop = t  # not accounting for scr refresh
                port_startexp.tStopRefresh = tThisFlipGlobal  # on global time
                port_startexp.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.addData('port_startexp.stopped', t)
                # update status
                port_startexp.status = FINISHED
                win.callOnFlip(port_startexp.setData, int(0))
        
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.status = FINISHED
        if thisExp.status == FINISHED or endExpNow:
            endExperiment(thisExp, win=win)
            return
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in StartupCodeComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "StartupCode" ---
    for thisComponent in StartupCodeComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    thisExp.addData('StartupCode.stopped', globalClock.getTime(format='float'))
    if port_startexp.status == STARTED:
        win.callOnFlip(port_startexp.setData, int(0))
    # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
    if routineForceEnded:
        routineTimer.reset()
    else:
        routineTimer.addTime(-1.000000)
    thisExp.nextEntry()
    
    # --- Prepare to start Routine "judgeValence" ---
    continueRoutine = True
    # update component parameters for each repeat
    thisExp.addData('judgeValence.started', globalClock.getTime(format='float'))
    valenceSlider.reset()
    # Run 'Begin Routine' code from code_7
    event.clearEvents('keyboard')
    valenceSlider.markerPos = 3
    # keep track of which components have finished
    judgeValenceComponents = [valenceImage, valenceSlider]
    for thisComponent in judgeValenceComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "judgeValence" ---
    routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *valenceImage* updates
        
        # if valenceImage is starting this frame...
        if valenceImage.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            valenceImage.frameNStart = frameN  # exact frame index
            valenceImage.tStart = t  # local t and not account for scr refresh
            valenceImage.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(valenceImage, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'valenceImage.started')
            # update status
            valenceImage.status = STARTED
            valenceImage.setAutoDraw(True)
        
        # if valenceImage is active this frame...
        if valenceImage.status == STARTED:
            # update params
            pass
        
        # *valenceSlider* updates
        
        # if valenceSlider is starting this frame...
        if valenceSlider.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            valenceSlider.frameNStart = frameN  # exact frame index
            valenceSlider.tStart = t  # local t and not account for scr refresh
            valenceSlider.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(valenceSlider, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'valenceSlider.started')
            # update status
            valenceSlider.status = STARTED
            valenceSlider.setAutoDraw(True)
        
        # if valenceSlider is active this frame...
        if valenceSlider.status == STARTED:
            # update params
            pass
        
        # Check valenceSlider for response to end Routine
        if valenceSlider.getRating() is not None and valenceSlider.status == STARTED:
            continueRoutine = False
        # Run 'Each Frame' code from code_7
        keys = event.getKeys()
        
        if len(keys):
            if 'left' in keys:
                valenceSlider.markerPos = valenceSlider.markerPos - 1
            elif 'right' in keys:
                valenceSlider.markerPos = valenceSlider.markerPos  + 1 
            elif 'return' in keys:
                # confirm rating by setting to current markerPos
                valenceSlider.rating= valenceSlider.markerPos
                continueRoutine=False
            elif 'enter' in keys:
                # confirm rating by setting to current markerPos
                valenceSlider.rating= valenceSlider.markerPos
                continueRoutine=False
            elif 'space' in keys:
                # confirm rating by setting to current markerPos
                valenceSlider.rating= valenceSlider.markerPos
                continueRoutine=False
        
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.status = FINISHED
        if thisExp.status == FINISHED or endExpNow:
            endExperiment(thisExp, win=win)
            return
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in judgeValenceComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "judgeValence" ---
    for thisComponent in judgeValenceComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    thisExp.addData('judgeValence.stopped', globalClock.getTime(format='float'))
    thisExp.addData('valenceSlider.response', valenceSlider.getRating())
    thisExp.addData('valenceSlider.rt', valenceSlider.getRT())
    # Run 'End Routine' code from code_7
    thisExp.addData("JudgeRating", confidenceSlider.markerPos)
    thisExp.nextEntry()
    # the Routine "judgeValence" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "judgearousal_2" ---
    continueRoutine = True
    # update component parameters for each repeat
    thisExp.addData('judgearousal_2.started', globalClock.getTime(format='float'))
    arousalSlider.reset()
    # Run 'Begin Routine' code from code_4
    event.clearEvents('keyboard')
    arousalSlider.markerPos = 3
    # keep track of which components have finished
    judgearousal_2Components = [arousalImage, arousalSlider]
    for thisComponent in judgearousal_2Components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "judgearousal_2" ---
    routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *arousalImage* updates
        
        # if arousalImage is starting this frame...
        if arousalImage.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            arousalImage.frameNStart = frameN  # exact frame index
            arousalImage.tStart = t  # local t and not account for scr refresh
            arousalImage.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(arousalImage, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'arousalImage.started')
            # update status
            arousalImage.status = STARTED
            arousalImage.setAutoDraw(True)
        
        # if arousalImage is active this frame...
        if arousalImage.status == STARTED:
            # update params
            pass
        
        # *arousalSlider* updates
        
        # if arousalSlider is starting this frame...
        if arousalSlider.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            arousalSlider.frameNStart = frameN  # exact frame index
            arousalSlider.tStart = t  # local t and not account for scr refresh
            arousalSlider.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(arousalSlider, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'arousalSlider.started')
            # update status
            arousalSlider.status = STARTED
            arousalSlider.setAutoDraw(True)
        
        # if arousalSlider is active this frame...
        if arousalSlider.status == STARTED:
            # update params
            pass
        
        # Check arousalSlider for response to end Routine
        if arousalSlider.getRating() is not None and arousalSlider.status == STARTED:
            continueRoutine = False
        # Run 'Each Frame' code from code_4
        keys = event.getKeys()
        
        if len(keys):
            if 'left' in keys:
                arousalSlider.markerPos = arousalSlider.markerPos - 1
            elif 'right' in keys:
                arousalSlider.markerPos = arousalSlider.markerPos  + 1
            elif 'return' in keys:
                # confirm rating by setting to current markerPos
                confidenceSlider.rating= confidenceSlider.markerPos
                continueRoutine=False
            elif 'enter' in keys:
                # confirm rating by setting to current markerPos
                confidenceSlider.rating= confidenceSlider.markerPos
                continueRoutine=False
            elif 'space' in keys:
                # confirm rating by setting to current markerPos
                confidenceSlider.rating= confidenceSlider.markerPos
                continueRoutine=False
        
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.status = FINISHED
        if thisExp.status == FINISHED or endExpNow:
            endExperiment(thisExp, win=win)
            return
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in judgearousal_2Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "judgearousal_2" ---
    for thisComponent in judgearousal_2Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    thisExp.addData('judgearousal_2.stopped', globalClock.getTime(format='float'))
    thisExp.addData('arousalSlider.response', arousalSlider.getRating())
    thisExp.addData('arousalSlider.rt', arousalSlider.getRT())
    # Run 'End Routine' code from code_4
    thisExp.addData("ArousalRating", arousalSlider.markerPos)
    thisExp.nextEntry()
    # the Routine "judgearousal_2" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "Start" ---
    continueRoutine = True
    # update component parameters for each repeat
    thisExp.addData('Start.started', globalClock.getTime(format='float'))
    key_resp.keys = []
    key_resp.rt = []
    _key_resp_allKeys = []
    # keep track of which components have finished
    StartComponents = [text, key_resp]
    for thisComponent in StartComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "Start" ---
    routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *text* updates
        
        # if text is starting this frame...
        if text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text.frameNStart = frameN  # exact frame index
            text.tStart = t  # local t and not account for scr refresh
            text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'text.started')
            # update status
            text.status = STARTED
            text.setAutoDraw(True)
        
        # if text is active this frame...
        if text.status == STARTED:
            # update params
            pass
        
        # *key_resp* updates
        waitOnFlip = False
        
        # if key_resp is starting this frame...
        if key_resp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            key_resp.frameNStart = frameN  # exact frame index
            key_resp.tStart = t  # local t and not account for scr refresh
            key_resp.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_resp, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'key_resp.started')
            # update status
            key_resp.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_resp.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(key_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if key_resp.status == STARTED and not waitOnFlip:
            theseKeys = key_resp.getKeys(keyList=['space'], ignoreKeys=["escape"], waitRelease=False)
            _key_resp_allKeys.extend(theseKeys)
            if len(_key_resp_allKeys):
                key_resp.keys = _key_resp_allKeys[-1].name  # just the last key pressed
                key_resp.rt = _key_resp_allKeys[-1].rt
                key_resp.duration = _key_resp_allKeys[-1].duration
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.status = FINISHED
        if thisExp.status == FINISHED or endExpNow:
            endExperiment(thisExp, win=win)
            return
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in StartComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "Start" ---
    for thisComponent in StartComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    thisExp.addData('Start.stopped', globalClock.getTime(format='float'))
    # check responses
    if key_resp.keys in ['', [], None]:  # No response was made
        key_resp.keys = None
    thisExp.addData('key_resp.keys',key_resp.keys)
    if key_resp.keys != None:  # we had a response
        thisExp.addData('key_resp.rt', key_resp.rt)
        thisExp.addData('key_resp.duration', key_resp.duration)
    thisExp.nextEntry()
    # the Routine "Start" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "Instruct1" ---
    continueRoutine = True
    # update component parameters for each repeat
    thisExp.addData('Instruct1.started', globalClock.getTime(format='float'))
    key_resp_4.keys = []
    key_resp_4.rt = []
    _key_resp_4_allKeys = []
    # keep track of which components have finished
    Instruct1Components = [text_7, key_resp_4]
    for thisComponent in Instruct1Components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "Instruct1" ---
    routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *text_7* updates
        
        # if text_7 is starting this frame...
        if text_7.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_7.frameNStart = frameN  # exact frame index
            text_7.tStart = t  # local t and not account for scr refresh
            text_7.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_7, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'text_7.started')
            # update status
            text_7.status = STARTED
            text_7.setAutoDraw(True)
        
        # if text_7 is active this frame...
        if text_7.status == STARTED:
            # update params
            pass
        
        # *key_resp_4* updates
        waitOnFlip = False
        
        # if key_resp_4 is starting this frame...
        if key_resp_4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            key_resp_4.frameNStart = frameN  # exact frame index
            key_resp_4.tStart = t  # local t and not account for scr refresh
            key_resp_4.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_resp_4, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'key_resp_4.started')
            # update status
            key_resp_4.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_resp_4.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(key_resp_4.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if key_resp_4.status == STARTED and not waitOnFlip:
            theseKeys = key_resp_4.getKeys(keyList=['space'], ignoreKeys=["escape"], waitRelease=False)
            _key_resp_4_allKeys.extend(theseKeys)
            if len(_key_resp_4_allKeys):
                key_resp_4.keys = _key_resp_4_allKeys[-1].name  # just the last key pressed
                key_resp_4.rt = _key_resp_4_allKeys[-1].rt
                key_resp_4.duration = _key_resp_4_allKeys[-1].duration
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.status = FINISHED
        if thisExp.status == FINISHED or endExpNow:
            endExperiment(thisExp, win=win)
            return
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in Instruct1Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "Instruct1" ---
    for thisComponent in Instruct1Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    thisExp.addData('Instruct1.stopped', globalClock.getTime(format='float'))
    # check responses
    if key_resp_4.keys in ['', [], None]:  # No response was made
        key_resp_4.keys = None
    thisExp.addData('key_resp_4.keys',key_resp_4.keys)
    if key_resp_4.keys != None:  # we had a response
        thisExp.addData('key_resp_4.rt', key_resp_4.rt)
        thisExp.addData('key_resp_4.duration', key_resp_4.duration)
    thisExp.nextEntry()
    # the Routine "Instruct1" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "Instruct2" ---
    continueRoutine = True
    # update component parameters for each repeat
    thisExp.addData('Instruct2.started', globalClock.getTime(format='float'))
    key_resp_3.keys = []
    key_resp_3.rt = []
    _key_resp_3_allKeys = []
    # keep track of which components have finished
    Instruct2Components = [text_3, key_resp_3]
    for thisComponent in Instruct2Components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "Instruct2" ---
    routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *text_3* updates
        
        # if text_3 is starting this frame...
        if text_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_3.frameNStart = frameN  # exact frame index
            text_3.tStart = t  # local t and not account for scr refresh
            text_3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_3, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'text_3.started')
            # update status
            text_3.status = STARTED
            text_3.setAutoDraw(True)
        
        # if text_3 is active this frame...
        if text_3.status == STARTED:
            # update params
            pass
        
        # *key_resp_3* updates
        waitOnFlip = False
        
        # if key_resp_3 is starting this frame...
        if key_resp_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            key_resp_3.frameNStart = frameN  # exact frame index
            key_resp_3.tStart = t  # local t and not account for scr refresh
            key_resp_3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_resp_3, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'key_resp_3.started')
            # update status
            key_resp_3.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_resp_3.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(key_resp_3.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if key_resp_3.status == STARTED and not waitOnFlip:
            theseKeys = key_resp_3.getKeys(keyList=['space'], ignoreKeys=["escape"], waitRelease=False)
            _key_resp_3_allKeys.extend(theseKeys)
            if len(_key_resp_3_allKeys):
                key_resp_3.keys = _key_resp_3_allKeys[-1].name  # just the last key pressed
                key_resp_3.rt = _key_resp_3_allKeys[-1].rt
                key_resp_3.duration = _key_resp_3_allKeys[-1].duration
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.status = FINISHED
        if thisExp.status == FINISHED or endExpNow:
            endExperiment(thisExp, win=win)
            return
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in Instruct2Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "Instruct2" ---
    for thisComponent in Instruct2Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    thisExp.addData('Instruct2.stopped', globalClock.getTime(format='float'))
    # check responses
    if key_resp_3.keys in ['', [], None]:  # No response was made
        key_resp_3.keys = None
    thisExp.addData('key_resp_3.keys',key_resp_3.keys)
    if key_resp_3.keys != None:  # we had a response
        thisExp.addData('key_resp_3.rt', key_resp_3.rt)
        thisExp.addData('key_resp_3.duration', key_resp_3.duration)
    thisExp.nextEntry()
    # the Routine "Instruct2" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # set up handler to look after randomisation of trials etc
    conditions = data.importConditions('questDefinitionRullRandom.csv')
    trials = data.MultiStairHandler(stairType='QUEST', name='trials',
        nTrials=10.0,
        conditions=conditions,
        method='random',
        originPath=-1)
    thisExp.addLoop(trials)  # add the loop to the experiment
    # initialise values for first condition
    level = trials._nextIntensity  # initialise some vals
    condition = trials.currentStaircase.condition
    
    for level, condition in trials:
        currentLoop = trials
        thisExp.timestampOnFlip(win, 'thisRow.t', format=globalClock.format)
        # abbreviate parameter names if possible (e.g. rgb=condition.rgb)
        for paramName in condition:
            globals()[paramName] = condition[paramName]
        
        # --- Prepare to start Routine "trial" ---
        continueRoutine = True
        # update component parameters for each repeat
        thisExp.addData('trial.started', globalClock.getTime(format='float'))
        # Run 'Begin Routine' code from code
        #For onine only:
        #thisCondition = trials.conditions[0]['label']
        #print(trials.conditions)
        
        #For local (where interleaved staircase works):
        thisCondition = condition['label']
        changeDirection = condition['changeDirection']
        changeSalience = condition['changeSalience']
        
        #print(thisCondition)
        #print(changeDirection)
        #print(changeSalience)
        #print(trials.currentStaircase.condition['label'])
        
        randomChange = random()
        
        cycleDuration = resetCycleDuration  #starting breath length (in s)
        #check for acceleration or deceleration
        if (changeDirection == 'Acc'):
            if randomChange <= .8:
                direction = -1
                correctAns = 'right'
            else:
                direction = 0
                correctAns = 'up'
        else:
            if randomChange <= .8:
                direction = 1
                correctAns = 'left'
            else:
                direction = 0
                correctAns = 'up'
        
        changeVal = 1 + (direction * level)
        breathCount = 0
        freshBreath = True
        
        #only applies to low salience trials
        changeAmount = changeVal ** (1/(numBreaths -1))
        trialClock = core.Clock()
        # keep track of which components have finished
        trialComponents = [Circle, port_starttrial]
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
        frameN = -1
        
        # --- Run Routine "trial" ---
        routineForceEnded = not continueRoutine
        while continueRoutine:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *Circle* updates
            
            # if Circle is starting this frame...
            if Circle.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                Circle.frameNStart = frameN  # exact frame index
                Circle.tStart = t  # local t and not account for scr refresh
                Circle.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(Circle, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'Circle.started')
                # update status
                Circle.status = STARTED
                Circle.setAutoDraw(True)
            
            # if Circle is active this frame...
            if Circle.status == STARTED:
                # update params
                pass
            # Run 'Each Frame' code from code
            t = trialClock.getTime()
            
            phase = (t % cycleDuration) / cycleDuration
            
            if phase <= 0.5:
                circleSize = 0.1 + (0.2 * phase * 2)  # Inhale
                if freshBreath == False:
                    breathCount += 1
                    if changeSalience == 0:
                        cycleDuration *= changeAmount
                    if changeSalience == 1:
                        if breathCount == midPoint:
                            cycleDuration *= changeVal
                    trialClock = core.Clock()
                    freshBreath = True
                    #print(breathCount)
                    #print(cycleDuration)
                    if breathCount >= numBreaths:
                        continueRoutine = False
            else:
                circleSize  = 0.1 + (0.2 * (1 - (phase - 0.5) * 2))  # Exhale
                if freshBreath == True:
                    freshBreath = False
                
            Circle.size = circleSize
            # *port_starttrial* updates
            
            # if port_starttrial is starting this frame...
            if port_starttrial.status == NOT_STARTED and t >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                port_starttrial.frameNStart = frameN  # exact frame index
                port_starttrial.tStart = t  # local t and not account for scr refresh
                port_starttrial.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(port_starttrial, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.addData('port_starttrial.started', t)
                # update status
                port_starttrial.status = STARTED
                port_starttrial.status = STARTED
                win.callOnFlip(port_starttrial.setData, int(3))
            
            # if port_starttrial is stopping this frame...
            if port_starttrial.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > port_starttrial.tStartRefresh + 1.0-frameTolerance:
                    # keep track of stop time/frame for later
                    port_starttrial.tStop = t  # not accounting for scr refresh
                    port_starttrial.tStopRefresh = tThisFlipGlobal  # on global time
                    port_starttrial.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.addData('port_starttrial.stopped', t)
                    # update status
                    port_starttrial.status = FINISHED
                    win.callOnFlip(port_starttrial.setData, int(0))
            
            # check for quit (typically the Esc key)
            if defaultKeyboard.getKeys(keyList=["escape"]):
                thisExp.status = FINISHED
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, win=win)
                return
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in trialComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "trial" ---
        for thisComponent in trialComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        thisExp.addData('trial.stopped', globalClock.getTime(format='float'))
        # Run 'End Routine' code from code
        #print("Trial: " + trials.thisTrialN)
        #print(trials)
        #print(trials.conditions)
        #print(trials.conditions[0])
        #print(trialNum)
        
        thisExp.addData('Condition', thisCondition)
        thisExp.addData('Salience', changeSalience)
        thisExp.addData('level', level)
        thisExp.addData('Direction',direction)
        thisExp.addData('DirectionLabel',changeDirection)
        thisExp.addData('Correct',correctAns)
        
        if thisCondition == "highSalienceAcc":
            n_highSalienceACC += 1
            thisExp.addData('n_highSalienceACC',n_highSalienceACC)
            highIntensitiesACC.append(level)
            if n_highSalienceACC > 2:
                highSEACC = std(highIntensitiesACC) / (n_highSalienceACC ** 0.5)
                #print(highSEACC)
                highSalienceCIACC = 1.645 * highSEACC
                highStepACC = abs(level - lastHighLevelACC)
                lastHighLevelACC = level
                highStopOKACC = highSalienceCIACC < (highStepACC / 2)
        elif thisCondition == "lowSalienceAcc":
            n_lowSalienceACC += 1
            thisExp.addData('n_lowSalienceACC',n_lowSalienceACC)
            lowIntensitiesACC.append(level)
            if n_lowSalienceACC > 2:
                lowSEACC = std(lowIntensitiesACC) / (n_lowSalienceACC ** 0.5)
                #print(lowSEACC)
                lowSalienceCIACC = 1.645 * lowSEACC
                lowStepACC = abs(level - lastLowLevelACC)
                lastLowLevelACC = level
                lowStopOKACC = lowSalienceCIACC < (lowStepACC / 2)
        elif thisCondition == "highSalienceDec":
            n_highSalienceDEC += 1
            thisExp.addData('n_highSalienceDEC',n_highSalienceDEC)
            highIntensitiesDEC.append(level)
            if n_highSalienceDEC > 2:
                highSEDEC = std(highIntensitiesDEC) / (n_highSalienceDEC ** 0.5)
                #print(highSEDEC)
                highSalienceCIDEC = 1.645 * highSEDEC
                highStepDEC = abs(level - lastHighLevelDEC)
                lastHighLevelDEC = level
                highStopOKDEC = highSalienceCIDEC < (highStepDEC / 2)
        else:
            n_lowSalienceDEC += 1
            thisExp.addData('n_lowSalienceDEC',n_lowSalienceDEC)
            lowIntensitiesDEC.append(level)
            if n_lowSalienceDEC > 2:
                lowSEDEC = std(lowIntensitiesDEC) / (n_lowSalienceDEC ** 0.5)
                #print(lowSEDEC)
                lowSalienceCIDEC = 1.645 * lowSEDEC
                lowStepDEC = abs(level - lastLowLevelDEC)
                lastLowLevelDEC = level
                lowStopOKDEC = lowSalienceCIDEC < (lowStepDEC / 2)
        
        thisExp.addData('highCIACC',highSalienceCIACC)
        thisExp.addData('lowCIACC',lowSalienceCIACC)
        thisExp.addData('highCIDEC',highSalienceCIDEC)
        thisExp.addData('lowCIDEC',lowSalienceCIDEC)
        
        thisExp.addData('highStepACC',highStepACC)
        thisExp.addData('lowStepACC',lowStepACC)
        thisExp.addData('highStepDEC',highStepDEC)
        thisExp.addData('lowStepDEC',lowStepDEC)
        
        thisExp.addData('highStopOKACC',highStopOKACC)
        thisExp.addData('lowStopOKACC',lowStopOKACC)
        thisExp.addData('highStopOKDEC',highStopOKDEC)
        thisExp.addData('lowStopOKDEC',lowStopOKDEC)
        
        #if trialNum == 10:
        #    trials.finished = True
        if port_starttrial.status == STARTED:
            win.callOnFlip(port_starttrial.setData, int(0))
        # the Routine "trial" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # --- Prepare to start Routine "judgebreath" ---
        continueRoutine = True
        # update component parameters for each repeat
        thisExp.addData('judgebreath.started', globalClock.getTime(format='float'))
        kbChange.keys = []
        kbChange.rt = []
        _kbChange_allKeys = []
        # Run 'Begin Routine' code from code_5
        event.clearEvents('keyboard')
        # keep track of which components have finished
        judgebreathComponents = [kbChange, speedImage, port_teststop]
        for thisComponent in judgebreathComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "judgebreath" ---
        routineForceEnded = not continueRoutine
        while continueRoutine:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *kbChange* updates
            waitOnFlip = False
            
            # if kbChange is starting this frame...
            if kbChange.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                kbChange.frameNStart = frameN  # exact frame index
                kbChange.tStart = t  # local t and not account for scr refresh
                kbChange.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(kbChange, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'kbChange.started')
                # update status
                kbChange.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(kbChange.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(kbChange.clearEvents, eventType='keyboard')  # clear events on next screen flip
            if kbChange.status == STARTED and not waitOnFlip:
                theseKeys = kbChange.getKeys(keyList=['left','up','right'], ignoreKeys=["escape"], waitRelease=False)
                _kbChange_allKeys.extend(theseKeys)
                if len(_kbChange_allKeys):
                    kbChange.keys = _kbChange_allKeys[-1].name  # just the last key pressed
                    kbChange.rt = _kbChange_allKeys[-1].rt
                    kbChange.duration = _kbChange_allKeys[-1].duration
                    # was this correct?
                    if (kbChange.keys == str(correctAns)) or (kbChange.keys == correctAns):
                        kbChange.corr = 1
                    else:
                        kbChange.corr = 0
                    # a response ends the routine
                    continueRoutine = False
            
            # *speedImage* updates
            
            # if speedImage is starting this frame...
            if speedImage.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                speedImage.frameNStart = frameN  # exact frame index
                speedImage.tStart = t  # local t and not account for scr refresh
                speedImage.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(speedImage, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'speedImage.started')
                # update status
                speedImage.status = STARTED
                speedImage.setAutoDraw(True)
            
            # if speedImage is active this frame...
            if speedImage.status == STARTED:
                # update params
                pass
            # Run 'Each Frame' code from code_5
            keys = event.getKeys()
            
            if len(keys):
                if 'left' in keys:
                    response = 'left'
                elif 'right' in keys:
                    response = 'right'
                elif 'up' in keys:
                    response = 'up'
            # *port_teststop* updates
            
            # if port_teststop is starting this frame...
            if port_teststop.status == NOT_STARTED and t >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                port_teststop.frameNStart = frameN  # exact frame index
                port_teststop.tStart = t  # local t and not account for scr refresh
                port_teststop.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(port_teststop, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.addData('port_teststop.started', t)
                # update status
                port_teststop.status = STARTED
                port_teststop.status = STARTED
                win.callOnFlip(port_teststop.setData, int(4))
            
            # if port_teststop is stopping this frame...
            if port_teststop.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > port_teststop.tStartRefresh + 1.0-frameTolerance:
                    # keep track of stop time/frame for later
                    port_teststop.tStop = t  # not accounting for scr refresh
                    port_teststop.tStopRefresh = tThisFlipGlobal  # on global time
                    port_teststop.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.addData('port_teststop.stopped', t)
                    # update status
                    port_teststop.status = FINISHED
                    win.callOnFlip(port_teststop.setData, int(0))
            
            # check for quit (typically the Esc key)
            if defaultKeyboard.getKeys(keyList=["escape"]):
                thisExp.status = FINISHED
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, win=win)
                return
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in judgebreathComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "judgebreath" ---
        for thisComponent in judgebreathComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        thisExp.addData('judgebreath.stopped', globalClock.getTime(format='float'))
        # check responses
        if kbChange.keys in ['', [], None]:  # No response was made
            kbChange.keys = None
            # was no response the correct answer?!
            if str(correctAns).lower() == 'none':
               kbChange.corr = 1;  # correct non-response
            else:
               kbChange.corr = 0;  # failed to respond (incorrectly)
        # store data for trials (MultiStairHandler)
        trials.addResponse(kbChange.corr, level)
        trials.addOtherData('kbChange.rt', kbChange.rt)
        # Run 'End Routine' code from code_5
        thisExp.addData('Response', response)
        
        if correctAns == response:
            thisExp.addData('Accuracy', 1)
        else:
            thisExp.addData('Accuracy', 0)
        if port_teststop.status == STARTED:
            win.callOnFlip(port_teststop.setData, int(0))
        # the Routine "judgebreath" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # --- Prepare to start Routine "judgeconfidence" ---
        continueRoutine = True
        # update component parameters for each repeat
        thisExp.addData('judgeconfidence.started', globalClock.getTime(format='float'))
        confidenceSlider.reset()
        # Run 'Begin Routine' code from code_3
        event.clearEvents('keyboard')
        confidenceSlider.markerPos = 3
        # keep track of which components have finished
        judgeconfidenceComponents = [confidenceImage, confidenceSlider]
        for thisComponent in judgeconfidenceComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "judgeconfidence" ---
        routineForceEnded = not continueRoutine
        while continueRoutine:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *confidenceImage* updates
            
            # if confidenceImage is starting this frame...
            if confidenceImage.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                confidenceImage.frameNStart = frameN  # exact frame index
                confidenceImage.tStart = t  # local t and not account for scr refresh
                confidenceImage.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(confidenceImage, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'confidenceImage.started')
                # update status
                confidenceImage.status = STARTED
                confidenceImage.setAutoDraw(True)
            
            # if confidenceImage is active this frame...
            if confidenceImage.status == STARTED:
                # update params
                pass
            
            # *confidenceSlider* updates
            
            # if confidenceSlider is starting this frame...
            if confidenceSlider.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                confidenceSlider.frameNStart = frameN  # exact frame index
                confidenceSlider.tStart = t  # local t and not account for scr refresh
                confidenceSlider.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(confidenceSlider, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'confidenceSlider.started')
                # update status
                confidenceSlider.status = STARTED
                confidenceSlider.setAutoDraw(True)
            
            # if confidenceSlider is active this frame...
            if confidenceSlider.status == STARTED:
                # update params
                pass
            
            # Check confidenceSlider for response to end Routine
            if confidenceSlider.getRating() is not None and confidenceSlider.status == STARTED:
                continueRoutine = False
            # Run 'Each Frame' code from code_3
            keys = event.getKeys()
            
            if len(keys):
                if 'left' in keys:
                    confidenceSlider.markerPos = confidenceSlider.markerPos - 1
                elif 'right' in keys:
                    confidenceSlider.markerPos = confidenceSlider.markerPos  + 1 
                elif 'return' in keys:
                    # confirm rating by setting to current markerPos
                    confidenceSlider.rating= confidenceSlider.markerPos
                    continueRoutine=False
                elif 'enter' in keys:
                    # confirm rating by setting to current markerPos
                    confidenceSlider.rating= confidenceSlider.markerPos
                    continueRoutine=False
                elif 'space' in keys:
                    # confirm rating by setting to current markerPos
                    confidenceSlider.rating= confidenceSlider.markerPos
                    continueRoutine=False
            
            # check for quit (typically the Esc key)
            if defaultKeyboard.getKeys(keyList=["escape"]):
                thisExp.status = FINISHED
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, win=win)
                return
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in judgeconfidenceComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "judgeconfidence" ---
        for thisComponent in judgeconfidenceComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        thisExp.addData('judgeconfidence.stopped', globalClock.getTime(format='float'))
        thisExp.addData('confidenceSlider.response', confidenceSlider.getRating())
        thisExp.addData('confidenceSlider.rt', confidenceSlider.getRT())
        # Run 'End Routine' code from code_3
        thisExp.addData("JudgeRating", confidenceSlider.markerPos)
        # the Routine "judgeconfidence" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # --- Prepare to start Routine "judgearousal_2" ---
        continueRoutine = True
        # update component parameters for each repeat
        thisExp.addData('judgearousal_2.started', globalClock.getTime(format='float'))
        arousalSlider.reset()
        # Run 'Begin Routine' code from code_4
        event.clearEvents('keyboard')
        arousalSlider.markerPos = 3
        # keep track of which components have finished
        judgearousal_2Components = [arousalImage, arousalSlider]
        for thisComponent in judgearousal_2Components:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "judgearousal_2" ---
        routineForceEnded = not continueRoutine
        while continueRoutine:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *arousalImage* updates
            
            # if arousalImage is starting this frame...
            if arousalImage.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                arousalImage.frameNStart = frameN  # exact frame index
                arousalImage.tStart = t  # local t and not account for scr refresh
                arousalImage.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(arousalImage, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'arousalImage.started')
                # update status
                arousalImage.status = STARTED
                arousalImage.setAutoDraw(True)
            
            # if arousalImage is active this frame...
            if arousalImage.status == STARTED:
                # update params
                pass
            
            # *arousalSlider* updates
            
            # if arousalSlider is starting this frame...
            if arousalSlider.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                arousalSlider.frameNStart = frameN  # exact frame index
                arousalSlider.tStart = t  # local t and not account for scr refresh
                arousalSlider.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(arousalSlider, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'arousalSlider.started')
                # update status
                arousalSlider.status = STARTED
                arousalSlider.setAutoDraw(True)
            
            # if arousalSlider is active this frame...
            if arousalSlider.status == STARTED:
                # update params
                pass
            
            # Check arousalSlider for response to end Routine
            if arousalSlider.getRating() is not None and arousalSlider.status == STARTED:
                continueRoutine = False
            # Run 'Each Frame' code from code_4
            keys = event.getKeys()
            
            if len(keys):
                if 'left' in keys:
                    arousalSlider.markerPos = arousalSlider.markerPos - 1
                elif 'right' in keys:
                    arousalSlider.markerPos = arousalSlider.markerPos  + 1
                elif 'return' in keys:
                    # confirm rating by setting to current markerPos
                    confidenceSlider.rating= confidenceSlider.markerPos
                    continueRoutine=False
                elif 'enter' in keys:
                    # confirm rating by setting to current markerPos
                    confidenceSlider.rating= confidenceSlider.markerPos
                    continueRoutine=False
                elif 'space' in keys:
                    # confirm rating by setting to current markerPos
                    confidenceSlider.rating= confidenceSlider.markerPos
                    continueRoutine=False
            
            # check for quit (typically the Esc key)
            if defaultKeyboard.getKeys(keyList=["escape"]):
                thisExp.status = FINISHED
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, win=win)
                return
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in judgearousal_2Components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "judgearousal_2" ---
        for thisComponent in judgearousal_2Components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        thisExp.addData('judgearousal_2.stopped', globalClock.getTime(format='float'))
        thisExp.addData('arousalSlider.response', arousalSlider.getRating())
        thisExp.addData('arousalSlider.rt', arousalSlider.getRT())
        # Run 'End Routine' code from code_4
        thisExp.addData("ArousalRating", arousalSlider.markerPos)
        # the Routine "judgearousal_2" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        thisExp.nextEntry()
        
        if thisSession is not None:
            # if running in a Session with a Liaison client, send data up to now
            thisSession.sendExperimentData()
    # all staircases completed
    
    
    # --- Prepare to start Routine "CalcThresholds" ---
    continueRoutine = True
    # update component parameters for each repeat
    thisExp.addData('CalcThresholds.started', globalClock.getTime(format='float'))
    # keep track of which components have finished
    CalcThresholdsComponents = []
    for thisComponent in CalcThresholdsComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "CalcThresholds" ---
    routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.status = FINISHED
        if thisExp.status == FINISHED or endExpNow:
            endExperiment(thisExp, win=win)
            return
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in CalcThresholdsComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "CalcThresholds" ---
    for thisComponent in CalcThresholdsComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    thisExp.addData('CalcThresholds.stopped', globalClock.getTime(format='float'))
    # Run 'End Routine' code from CalcThresholds
    T_hiAc = (highIntensitiesACC[-2] + highIntensitiesACC[-1])/2
    T_loAc = (lowIntensitiesACC[-2] + lowIntensitiesACC[-1])/2
    T_hiDe = (highIntensitiesDEC[-2] + highIntensitiesDEC[-1])/2
    T_loDe = (lowIntensitiesDEC[-2] + lowIntensitiesDEC[-1])/2
    
    #print(T_hiAc)
    #print(T_loAc)
    #print(T_hiDe)
    #print(T_loDe)
    
    #Thresholds generate critical thresholds
    Crit_Ac = (T_hiAc + T_loAc) / 2
    Crit_De = (T_hiDe + T_loDe) / 2
    
    print(Crit_Ac)
    print(Crit_De)
    thisExp.nextEntry()
    # the Routine "CalcThresholds" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "TestTrialInstruct" ---
    continueRoutine = True
    # update component parameters for each repeat
    thisExp.addData('TestTrialInstruct.started', globalClock.getTime(format='float'))
    key_resp_2.keys = []
    key_resp_2.rt = []
    _key_resp_2_allKeys = []
    # keep track of which components have finished
    TestTrialInstructComponents = [text_2, key_resp_2]
    for thisComponent in TestTrialInstructComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "TestTrialInstruct" ---
    routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *text_2* updates
        
        # if text_2 is starting this frame...
        if text_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_2.frameNStart = frameN  # exact frame index
            text_2.tStart = t  # local t and not account for scr refresh
            text_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_2, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'text_2.started')
            # update status
            text_2.status = STARTED
            text_2.setAutoDraw(True)
        
        # if text_2 is active this frame...
        if text_2.status == STARTED:
            # update params
            pass
        
        # *key_resp_2* updates
        waitOnFlip = False
        
        # if key_resp_2 is starting this frame...
        if key_resp_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            key_resp_2.frameNStart = frameN  # exact frame index
            key_resp_2.tStart = t  # local t and not account for scr refresh
            key_resp_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_resp_2, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'key_resp_2.started')
            # update status
            key_resp_2.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_resp_2.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(key_resp_2.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if key_resp_2.status == STARTED and not waitOnFlip:
            theseKeys = key_resp_2.getKeys(keyList=['space'], ignoreKeys=["escape"], waitRelease=False)
            _key_resp_2_allKeys.extend(theseKeys)
            if len(_key_resp_2_allKeys):
                key_resp_2.keys = _key_resp_2_allKeys[-1].name  # just the last key pressed
                key_resp_2.rt = _key_resp_2_allKeys[-1].rt
                key_resp_2.duration = _key_resp_2_allKeys[-1].duration
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.status = FINISHED
        if thisExp.status == FINISHED or endExpNow:
            endExperiment(thisExp, win=win)
            return
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in TestTrialInstructComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "TestTrialInstruct" ---
    for thisComponent in TestTrialInstructComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    thisExp.addData('TestTrialInstruct.stopped', globalClock.getTime(format='float'))
    # check responses
    if key_resp_2.keys in ['', [], None]:  # No response was made
        key_resp_2.keys = None
    thisExp.addData('key_resp_2.keys',key_resp_2.keys)
    if key_resp_2.keys != None:  # we had a response
        thisExp.addData('key_resp_2.rt', key_resp_2.rt)
        thisExp.addData('key_resp_2.duration', key_resp_2.duration)
    thisExp.nextEntry()
    # the Routine "TestTrialInstruct" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # set up handler to look after randomisation of conditions etc
    testTrials = data.TrialHandler(nReps=2.0, method='fullRandom', 
        extraInfo=expInfo, originPath=-1,
        trialList=data.importConditions('justLabels.csv'),
        seed=None, name='testTrials')
    thisExp.addLoop(testTrials)  # add the loop to the experiment
    thisTestTrial = testTrials.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisTestTrial.rgb)
    if thisTestTrial != None:
        for paramName in thisTestTrial:
            globals()[paramName] = thisTestTrial[paramName]
    
    for thisTestTrial in testTrials:
        currentLoop = testTrials
        thisExp.timestampOnFlip(win, 'thisRow.t', format=globalClock.format)
        # pause experiment here if requested
        if thisExp.status == PAUSED:
            pauseExperiment(
                thisExp=thisExp, 
                win=win, 
                timers=[routineTimer], 
                playbackComponents=[]
        )
        # abbreviate parameter names if possible (e.g. rgb = thisTestTrial.rgb)
        if thisTestTrial != None:
            for paramName in thisTestTrial:
                globals()[paramName] = thisTestTrial[paramName]
        
        # --- Prepare to start Routine "TestTrial" ---
        continueRoutine = True
        # update component parameters for each repeat
        thisExp.addData('TestTrial.started', globalClock.getTime(format='float'))
        # Run 'Begin Routine' code from testTrialCode
        #Same as training but now set level to critical val
        #thisCondition = condition['label']
        #changeDirection = condition['changeDirection']
        #changeSalience = condition['changeSalience']
        
        thisCondition = testLabel #condition['label']
        changeDirection = testChangeDirection #condition['changeDirection']
        changeSalience = testChangeSalience #condition['changeSalience']
        
        print(thisCondition)
        print(changeDirection)
        print(changeSalience)
        
        cycleDuration = resetCycleDuration  #starting breath length (in s)
        #check for acceleration or deceleration
        if (changeDirection == 'Acc'):
            level = Crit_Ac
            direction = -1
            correctAns = 'right'
        else:
            level = Crit_De
            direction = 1
            correctAns = 'left'
        
        changeVal = 1 + (direction * level)
        breathCount = 0
        freshBreath = True
        
        changeAmount = changeVal ** (1/(numBreaths -1))
        
        trialClock = core.Clock() 
        
        # keep track of which components have finished
        TestTrialComponents = [TestCircle, port_teststart]
        for thisComponent in TestTrialComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "TestTrial" ---
        routineForceEnded = not continueRoutine
        while continueRoutine:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *TestCircle* updates
            
            # if TestCircle is starting this frame...
            if TestCircle.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                TestCircle.frameNStart = frameN  # exact frame index
                TestCircle.tStart = t  # local t and not account for scr refresh
                TestCircle.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(TestCircle, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'TestCircle.started')
                # update status
                TestCircle.status = STARTED
                TestCircle.setAutoDraw(True)
            
            # if TestCircle is active this frame...
            if TestCircle.status == STARTED:
                # update params
                pass
            # Run 'Each Frame' code from testTrialCode
            t = trialClock.getTime()
            
            phase = (t % cycleDuration) / cycleDuration
            
            if phase <= 0.5:
                circleSize = 0.1 + (0.2 * phase * 2)  # Inhale
                if freshBreath == False:
                    breathCount += 1
                    if changeSalience == 0:
                        cycleDuration *= changeAmount
                    if changeSalience == 1:
                        if breathCount == midPoint:
                            cycleDuration *= changeVal
                    trialClock = core.Clock()
                    freshBreath = True
                    #print(breathCount)
                    #print(cycleDuration)
                    if breathCount >= numBreaths:
                        continueRoutine = False
            else:
                circleSize  = 0.1 + (0.2 * (1 - (phase - 0.5) * 2))  # Exhale
                if freshBreath == True:
                    freshBreath = False
            
            TestCircle.size = circleSize
            
            # *port_teststart* updates
            
            # if port_teststart is starting this frame...
            if port_teststart.status == NOT_STARTED and t >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                port_teststart.frameNStart = frameN  # exact frame index
                port_teststart.tStart = t  # local t and not account for scr refresh
                port_teststart.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(port_teststart, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.addData('port_teststart.started', t)
                # update status
                port_teststart.status = STARTED
                port_teststart.status = STARTED
                win.callOnFlip(port_teststart.setData, int(5))
            
            # if port_teststart is stopping this frame...
            if port_teststart.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > port_teststart.tStartRefresh + 1.0-frameTolerance:
                    # keep track of stop time/frame for later
                    port_teststart.tStop = t  # not accounting for scr refresh
                    port_teststart.tStopRefresh = tThisFlipGlobal  # on global time
                    port_teststart.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.addData('port_teststart.stopped', t)
                    # update status
                    port_teststart.status = FINISHED
                    win.callOnFlip(port_teststart.setData, int(0))
            
            # check for quit (typically the Esc key)
            if defaultKeyboard.getKeys(keyList=["escape"]):
                thisExp.status = FINISHED
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, win=win)
                return
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in TestTrialComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "TestTrial" ---
        for thisComponent in TestTrialComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        thisExp.addData('TestTrial.stopped', globalClock.getTime(format='float'))
        # Run 'End Routine' code from testTrialCode
        thisExp.addData('Condition', thisCondition)
        thisExp.addData('Salience', changeSalience)
        thisExp.addData('level', level)
        thisExp.addData('Direction',direction)
        thisExp.addData('DirectionLabel',changeDirection)
        thisExp.addData('Correct',correctAns)
        thisExp.addData('Crit_Ac',Crit_Ac)
        thisExp.addData('Crit_De',Crit_De)
        
        if thisCondition == "highSalienceAcc":
            n_highSalienceACC += 1
            highIntensitiesACC.append(level)
            if n_highSalienceACC > 2:
                highSEACC = std(highIntensitiesACC) / (n_highSalienceACC ** 0.5)
                #print(highSEACC)
                highSalienceCIACC = 1.645 * highSEACC
                highStepACC = abs(level - lastHighLevelACC)
                lastHighLevelACC = level
                highStopOKACC = highSalienceCIACC < (highStepACC / 2)
        elif thisCondition == "lowSalienceAcc":
            n_lowSalienceACC += 1
            lowIntensitiesACC.append(level)
            if n_lowSalienceACC > 2:
                lowSEACC = std(lowIntensitiesACC) / (n_lowSalienceACC ** 0.5)
                #print(lowSEACC)
                lowSalienceCIACC = 1.645 * lowSEACC
                lowStepACC = abs(level - lastLowLevelACC)
                lastLowLevelACC = level
                lowStopOKACC = lowSalienceCIACC < (lowStepACC / 2)
        elif thisCondition == "highSalienceDec":
            n_highSalienceDEC += 1
            highIntensitiesDEC.append(level)
            if n_highSalienceDEC > 2:
                highSEDEC = std(highIntensitiesDEC) / (n_highSalienceDEC ** 0.5)
                #print(highSEDEC)
                highSalienceCIDEC = 1.645 * highSEDEC
                highStepDEC = abs(level - lastHighLevelDEC)
                lastHighLevelDEC = level
                highStopOKDEC = highSalienceCIDEC < (highStepDEC / 2)
        else:
            n_lowSalienceDEC += 1
            lowIntensitiesDEC.append(level)
            if n_lowSalienceDEC > 2:
                lowSEDEC = std(lowIntensitiesDEC) / (n_lowSalienceDEC ** 0.5)
                #print(lowSEDEC)
                lowSalienceCIDEC = 1.645 * lowSEDEC
                lowStepDEC = abs(level - lastLowLevelDEC)
                lastLowLevelDEC = level
                lowStopOKDEC = lowSalienceCIDEC < (lowStepDEC / 2)
        
        thisExp.addData('highCIACC',highSalienceCIACC)
        thisExp.addData('lowCIACC',lowSalienceCIACC)
        thisExp.addData('highCIDEC',highSalienceCIDEC)
        thisExp.addData('lowCIDEC',lowSalienceCIDEC)
        
        thisExp.addData('highStepACC',highStepACC)
        thisExp.addData('lowStepACC',lowStepACC)
        thisExp.addData('highStepDEC',highStepDEC)
        thisExp.addData('lowStepDEC',lowStepDEC)
        
        thisExp.addData('highStopOKACC',highStopOKACC)
        thisExp.addData('lowStopOKACC',lowStopOKACC)
        thisExp.addData('highStopOKDEC',highStopOKDEC)
        thisExp.addData('lowStopOKDEC',lowStopOKDEC)
        if port_teststart.status == STARTED:
            win.callOnFlip(port_teststart.setData, int(0))
        # the Routine "TestTrial" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # --- Prepare to start Routine "judgebreath" ---
        continueRoutine = True
        # update component parameters for each repeat
        thisExp.addData('judgebreath.started', globalClock.getTime(format='float'))
        kbChange.keys = []
        kbChange.rt = []
        _kbChange_allKeys = []
        # Run 'Begin Routine' code from code_5
        event.clearEvents('keyboard')
        # keep track of which components have finished
        judgebreathComponents = [kbChange, speedImage, port_teststop]
        for thisComponent in judgebreathComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "judgebreath" ---
        routineForceEnded = not continueRoutine
        while continueRoutine:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *kbChange* updates
            waitOnFlip = False
            
            # if kbChange is starting this frame...
            if kbChange.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                kbChange.frameNStart = frameN  # exact frame index
                kbChange.tStart = t  # local t and not account for scr refresh
                kbChange.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(kbChange, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'kbChange.started')
                # update status
                kbChange.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(kbChange.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(kbChange.clearEvents, eventType='keyboard')  # clear events on next screen flip
            if kbChange.status == STARTED and not waitOnFlip:
                theseKeys = kbChange.getKeys(keyList=['left','up','right'], ignoreKeys=["escape"], waitRelease=False)
                _kbChange_allKeys.extend(theseKeys)
                if len(_kbChange_allKeys):
                    kbChange.keys = _kbChange_allKeys[-1].name  # just the last key pressed
                    kbChange.rt = _kbChange_allKeys[-1].rt
                    kbChange.duration = _kbChange_allKeys[-1].duration
                    # was this correct?
                    if (kbChange.keys == str(correctAns)) or (kbChange.keys == correctAns):
                        kbChange.corr = 1
                    else:
                        kbChange.corr = 0
                    # a response ends the routine
                    continueRoutine = False
            
            # *speedImage* updates
            
            # if speedImage is starting this frame...
            if speedImage.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                speedImage.frameNStart = frameN  # exact frame index
                speedImage.tStart = t  # local t and not account for scr refresh
                speedImage.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(speedImage, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'speedImage.started')
                # update status
                speedImage.status = STARTED
                speedImage.setAutoDraw(True)
            
            # if speedImage is active this frame...
            if speedImage.status == STARTED:
                # update params
                pass
            # Run 'Each Frame' code from code_5
            keys = event.getKeys()
            
            if len(keys):
                if 'left' in keys:
                    response = 'left'
                elif 'right' in keys:
                    response = 'right'
                elif 'up' in keys:
                    response = 'up'
            # *port_teststop* updates
            
            # if port_teststop is starting this frame...
            if port_teststop.status == NOT_STARTED and t >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                port_teststop.frameNStart = frameN  # exact frame index
                port_teststop.tStart = t  # local t and not account for scr refresh
                port_teststop.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(port_teststop, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.addData('port_teststop.started', t)
                # update status
                port_teststop.status = STARTED
                port_teststop.status = STARTED
                win.callOnFlip(port_teststop.setData, int(4))
            
            # if port_teststop is stopping this frame...
            if port_teststop.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > port_teststop.tStartRefresh + 1.0-frameTolerance:
                    # keep track of stop time/frame for later
                    port_teststop.tStop = t  # not accounting for scr refresh
                    port_teststop.tStopRefresh = tThisFlipGlobal  # on global time
                    port_teststop.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.addData('port_teststop.stopped', t)
                    # update status
                    port_teststop.status = FINISHED
                    win.callOnFlip(port_teststop.setData, int(0))
            
            # check for quit (typically the Esc key)
            if defaultKeyboard.getKeys(keyList=["escape"]):
                thisExp.status = FINISHED
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, win=win)
                return
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in judgebreathComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "judgebreath" ---
        for thisComponent in judgebreathComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        thisExp.addData('judgebreath.stopped', globalClock.getTime(format='float'))
        # check responses
        if kbChange.keys in ['', [], None]:  # No response was made
            kbChange.keys = None
            # was no response the correct answer?!
            if str(correctAns).lower() == 'none':
               kbChange.corr = 1;  # correct non-response
            else:
               kbChange.corr = 0;  # failed to respond (incorrectly)
        # store data for testTrials (TrialHandler)
        testTrials.addData('kbChange.keys',kbChange.keys)
        testTrials.addData('kbChange.corr', kbChange.corr)
        if kbChange.keys != None:  # we had a response
            testTrials.addData('kbChange.rt', kbChange.rt)
            testTrials.addData('kbChange.duration', kbChange.duration)
        # Run 'End Routine' code from code_5
        thisExp.addData('Response', response)
        
        if correctAns == response:
            thisExp.addData('Accuracy', 1)
        else:
            thisExp.addData('Accuracy', 0)
        if port_teststop.status == STARTED:
            win.callOnFlip(port_teststop.setData, int(0))
        # the Routine "judgebreath" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # --- Prepare to start Routine "judgeconfidence" ---
        continueRoutine = True
        # update component parameters for each repeat
        thisExp.addData('judgeconfidence.started', globalClock.getTime(format='float'))
        confidenceSlider.reset()
        # Run 'Begin Routine' code from code_3
        event.clearEvents('keyboard')
        confidenceSlider.markerPos = 3
        # keep track of which components have finished
        judgeconfidenceComponents = [confidenceImage, confidenceSlider]
        for thisComponent in judgeconfidenceComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "judgeconfidence" ---
        routineForceEnded = not continueRoutine
        while continueRoutine:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *confidenceImage* updates
            
            # if confidenceImage is starting this frame...
            if confidenceImage.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                confidenceImage.frameNStart = frameN  # exact frame index
                confidenceImage.tStart = t  # local t and not account for scr refresh
                confidenceImage.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(confidenceImage, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'confidenceImage.started')
                # update status
                confidenceImage.status = STARTED
                confidenceImage.setAutoDraw(True)
            
            # if confidenceImage is active this frame...
            if confidenceImage.status == STARTED:
                # update params
                pass
            
            # *confidenceSlider* updates
            
            # if confidenceSlider is starting this frame...
            if confidenceSlider.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                confidenceSlider.frameNStart = frameN  # exact frame index
                confidenceSlider.tStart = t  # local t and not account for scr refresh
                confidenceSlider.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(confidenceSlider, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'confidenceSlider.started')
                # update status
                confidenceSlider.status = STARTED
                confidenceSlider.setAutoDraw(True)
            
            # if confidenceSlider is active this frame...
            if confidenceSlider.status == STARTED:
                # update params
                pass
            
            # Check confidenceSlider for response to end Routine
            if confidenceSlider.getRating() is not None and confidenceSlider.status == STARTED:
                continueRoutine = False
            # Run 'Each Frame' code from code_3
            keys = event.getKeys()
            
            if len(keys):
                if 'left' in keys:
                    confidenceSlider.markerPos = confidenceSlider.markerPos - 1
                elif 'right' in keys:
                    confidenceSlider.markerPos = confidenceSlider.markerPos  + 1 
                elif 'return' in keys:
                    # confirm rating by setting to current markerPos
                    confidenceSlider.rating= confidenceSlider.markerPos
                    continueRoutine=False
                elif 'enter' in keys:
                    # confirm rating by setting to current markerPos
                    confidenceSlider.rating= confidenceSlider.markerPos
                    continueRoutine=False
                elif 'space' in keys:
                    # confirm rating by setting to current markerPos
                    confidenceSlider.rating= confidenceSlider.markerPos
                    continueRoutine=False
            
            # check for quit (typically the Esc key)
            if defaultKeyboard.getKeys(keyList=["escape"]):
                thisExp.status = FINISHED
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, win=win)
                return
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in judgeconfidenceComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "judgeconfidence" ---
        for thisComponent in judgeconfidenceComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        thisExp.addData('judgeconfidence.stopped', globalClock.getTime(format='float'))
        testTrials.addData('confidenceSlider.response', confidenceSlider.getRating())
        testTrials.addData('confidenceSlider.rt', confidenceSlider.getRT())
        # Run 'End Routine' code from code_3
        thisExp.addData("JudgeRating", confidenceSlider.markerPos)
        # the Routine "judgeconfidence" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # --- Prepare to start Routine "judgearousal_2" ---
        continueRoutine = True
        # update component parameters for each repeat
        thisExp.addData('judgearousal_2.started', globalClock.getTime(format='float'))
        arousalSlider.reset()
        # Run 'Begin Routine' code from code_4
        event.clearEvents('keyboard')
        arousalSlider.markerPos = 3
        # keep track of which components have finished
        judgearousal_2Components = [arousalImage, arousalSlider]
        for thisComponent in judgearousal_2Components:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "judgearousal_2" ---
        routineForceEnded = not continueRoutine
        while continueRoutine:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *arousalImage* updates
            
            # if arousalImage is starting this frame...
            if arousalImage.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                arousalImage.frameNStart = frameN  # exact frame index
                arousalImage.tStart = t  # local t and not account for scr refresh
                arousalImage.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(arousalImage, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'arousalImage.started')
                # update status
                arousalImage.status = STARTED
                arousalImage.setAutoDraw(True)
            
            # if arousalImage is active this frame...
            if arousalImage.status == STARTED:
                # update params
                pass
            
            # *arousalSlider* updates
            
            # if arousalSlider is starting this frame...
            if arousalSlider.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                arousalSlider.frameNStart = frameN  # exact frame index
                arousalSlider.tStart = t  # local t and not account for scr refresh
                arousalSlider.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(arousalSlider, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'arousalSlider.started')
                # update status
                arousalSlider.status = STARTED
                arousalSlider.setAutoDraw(True)
            
            # if arousalSlider is active this frame...
            if arousalSlider.status == STARTED:
                # update params
                pass
            
            # Check arousalSlider for response to end Routine
            if arousalSlider.getRating() is not None and arousalSlider.status == STARTED:
                continueRoutine = False
            # Run 'Each Frame' code from code_4
            keys = event.getKeys()
            
            if len(keys):
                if 'left' in keys:
                    arousalSlider.markerPos = arousalSlider.markerPos - 1
                elif 'right' in keys:
                    arousalSlider.markerPos = arousalSlider.markerPos  + 1
                elif 'return' in keys:
                    # confirm rating by setting to current markerPos
                    confidenceSlider.rating= confidenceSlider.markerPos
                    continueRoutine=False
                elif 'enter' in keys:
                    # confirm rating by setting to current markerPos
                    confidenceSlider.rating= confidenceSlider.markerPos
                    continueRoutine=False
                elif 'space' in keys:
                    # confirm rating by setting to current markerPos
                    confidenceSlider.rating= confidenceSlider.markerPos
                    continueRoutine=False
            
            # check for quit (typically the Esc key)
            if defaultKeyboard.getKeys(keyList=["escape"]):
                thisExp.status = FINISHED
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, win=win)
                return
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in judgearousal_2Components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "judgearousal_2" ---
        for thisComponent in judgearousal_2Components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        thisExp.addData('judgearousal_2.stopped', globalClock.getTime(format='float'))
        testTrials.addData('arousalSlider.response', arousalSlider.getRating())
        testTrials.addData('arousalSlider.rt', arousalSlider.getRT())
        # Run 'End Routine' code from code_4
        thisExp.addData("ArousalRating", arousalSlider.markerPos)
        # the Routine "judgearousal_2" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        thisExp.nextEntry()
        
        if thisSession is not None:
            # if running in a Session with a Liaison client, send data up to now
            thisSession.sendExperimentData()
    # completed 2.0 repeats of 'testTrials'
    
    
    # --- Prepare to start Routine "CompleteInstruct" ---
    continueRoutine = True
    # update component parameters for each repeat
    thisExp.addData('CompleteInstruct.started', globalClock.getTime(format='float'))
    key_space.keys = []
    key_space.rt = []
    _key_space_allKeys = []
    # keep track of which components have finished
    CompleteInstructComponents = [key_space, text_4]
    for thisComponent in CompleteInstructComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "CompleteInstruct" ---
    routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *key_space* updates
        waitOnFlip = False
        
        # if key_space is starting this frame...
        if key_space.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            key_space.frameNStart = frameN  # exact frame index
            key_space.tStart = t  # local t and not account for scr refresh
            key_space.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_space, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'key_space.started')
            # update status
            key_space.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_space.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(key_space.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if key_space.status == STARTED and not waitOnFlip:
            theseKeys = key_space.getKeys(keyList=['space'], ignoreKeys=["escape"], waitRelease=False)
            _key_space_allKeys.extend(theseKeys)
            if len(_key_space_allKeys):
                key_space.keys = _key_space_allKeys[-1].name  # just the last key pressed
                key_space.rt = _key_space_allKeys[-1].rt
                key_space.duration = _key_space_allKeys[-1].duration
                # a response ends the routine
                continueRoutine = False
        
        # *text_4* updates
        
        # if text_4 is starting this frame...
        if text_4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_4.frameNStart = frameN  # exact frame index
            text_4.tStart = t  # local t and not account for scr refresh
            text_4.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_4, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'text_4.started')
            # update status
            text_4.status = STARTED
            text_4.setAutoDraw(True)
        
        # if text_4 is active this frame...
        if text_4.status == STARTED:
            # update params
            pass
        
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.status = FINISHED
        if thisExp.status == FINISHED or endExpNow:
            endExperiment(thisExp, win=win)
            return
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in CompleteInstructComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "CompleteInstruct" ---
    for thisComponent in CompleteInstructComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    thisExp.addData('CompleteInstruct.stopped', globalClock.getTime(format='float'))
    # check responses
    if key_space.keys in ['', [], None]:  # No response was made
        key_space.keys = None
    thisExp.addData('key_space.keys',key_space.keys)
    if key_space.keys != None:  # we had a response
        thisExp.addData('key_space.rt', key_space.rt)
        thisExp.addData('key_space.duration', key_space.duration)
    thisExp.nextEntry()
    # the Routine "CompleteInstruct" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "HeartInstruct" ---
    continueRoutine = True
    # update component parameters for each repeat
    thisExp.addData('HeartInstruct.started', globalClock.getTime(format='float'))
    key_space_2.keys = []
    key_space_2.rt = []
    _key_space_2_allKeys = []
    # keep track of which components have finished
    HeartInstructComponents = [key_space_2, text_5]
    for thisComponent in HeartInstructComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "HeartInstruct" ---
    routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *key_space_2* updates
        waitOnFlip = False
        
        # if key_space_2 is starting this frame...
        if key_space_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            key_space_2.frameNStart = frameN  # exact frame index
            key_space_2.tStart = t  # local t and not account for scr refresh
            key_space_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_space_2, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'key_space_2.started')
            # update status
            key_space_2.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_space_2.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(key_space_2.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if key_space_2.status == STARTED and not waitOnFlip:
            theseKeys = key_space_2.getKeys(keyList=['space'], ignoreKeys=["escape"], waitRelease=False)
            _key_space_2_allKeys.extend(theseKeys)
            if len(_key_space_2_allKeys):
                key_space_2.keys = _key_space_2_allKeys[-1].name  # just the last key pressed
                key_space_2.rt = _key_space_2_allKeys[-1].rt
                key_space_2.duration = _key_space_2_allKeys[-1].duration
                # a response ends the routine
                continueRoutine = False
        
        # *text_5* updates
        
        # if text_5 is starting this frame...
        if text_5.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_5.frameNStart = frameN  # exact frame index
            text_5.tStart = t  # local t and not account for scr refresh
            text_5.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_5, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'text_5.started')
            # update status
            text_5.status = STARTED
            text_5.setAutoDraw(True)
        
        # if text_5 is active this frame...
        if text_5.status == STARTED:
            # update params
            pass
        
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.status = FINISHED
        if thisExp.status == FINISHED or endExpNow:
            endExperiment(thisExp, win=win)
            return
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in HeartInstructComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "HeartInstruct" ---
    for thisComponent in HeartInstructComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    thisExp.addData('HeartInstruct.stopped', globalClock.getTime(format='float'))
    # check responses
    if key_space_2.keys in ['', [], None]:  # No response was made
        key_space_2.keys = None
    thisExp.addData('key_space_2.keys',key_space_2.keys)
    if key_space_2.keys != None:  # we had a response
        thisExp.addData('key_space_2.rt', key_space_2.rt)
        thisExp.addData('key_space_2.duration', key_space_2.duration)
    thisExp.nextEntry()
    # the Routine "HeartInstruct" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # set up handler to look after randomisation of conditions etc
    HeartbeatLoop = data.TrialHandler(nReps=1.0, method='random', 
        extraInfo=expInfo, originPath=-1,
        trialList=data.importConditions('heartConditions.csv'),
        seed=None, name='HeartbeatLoop')
    thisExp.addLoop(HeartbeatLoop)  # add the loop to the experiment
    thisHeartbeatLoop = HeartbeatLoop.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisHeartbeatLoop.rgb)
    if thisHeartbeatLoop != None:
        for paramName in thisHeartbeatLoop:
            globals()[paramName] = thisHeartbeatLoop[paramName]
    
    for thisHeartbeatLoop in HeartbeatLoop:
        currentLoop = HeartbeatLoop
        thisExp.timestampOnFlip(win, 'thisRow.t', format=globalClock.format)
        # pause experiment here if requested
        if thisExp.status == PAUSED:
            pauseExperiment(
                thisExp=thisExp, 
                win=win, 
                timers=[routineTimer], 
                playbackComponents=[]
        )
        # abbreviate parameter names if possible (e.g. rgb = thisHeartbeatLoop.rgb)
        if thisHeartbeatLoop != None:
            for paramName in thisHeartbeatLoop:
                globals()[paramName] = thisHeartbeatLoop[paramName]
        
        # --- Prepare to start Routine "HeartCount" ---
        continueRoutine = True
        # update component parameters for each repeat
        thisExp.addData('HeartCount.started', globalClock.getTime(format='float'))
        # keep track of which components have finished
        HeartCountComponents = [readyScreen, countScreen, port_HRstart]
        for thisComponent in HeartCountComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "HeartCount" ---
        routineForceEnded = not continueRoutine
        while continueRoutine:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *readyScreen* updates
            
            # if readyScreen is starting this frame...
            if readyScreen.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                readyScreen.frameNStart = frameN  # exact frame index
                readyScreen.tStart = t  # local t and not account for scr refresh
                readyScreen.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(readyScreen, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'readyScreen.started')
                # update status
                readyScreen.status = STARTED
                readyScreen.setAutoDraw(True)
            
            # if readyScreen is active this frame...
            if readyScreen.status == STARTED:
                # update params
                pass
            
            # if readyScreen is stopping this frame...
            if readyScreen.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > readyScreen.tStartRefresh + 5-frameTolerance:
                    # keep track of stop time/frame for later
                    readyScreen.tStop = t  # not accounting for scr refresh
                    readyScreen.tStopRefresh = tThisFlipGlobal  # on global time
                    readyScreen.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'readyScreen.stopped')
                    # update status
                    readyScreen.status = FINISHED
                    readyScreen.setAutoDraw(False)
            
            # *countScreen* updates
            
            # if countScreen is starting this frame...
            if countScreen.status == NOT_STARTED and tThisFlip >= 5-frameTolerance:
                # keep track of start time/frame for later
                countScreen.frameNStart = frameN  # exact frame index
                countScreen.tStart = t  # local t and not account for scr refresh
                countScreen.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(countScreen, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'countScreen.started')
                # update status
                countScreen.status = STARTED
                countScreen.setAutoDraw(True)
            
            # if countScreen is active this frame...
            if countScreen.status == STARTED:
                # update params
                pass
            
            # if countScreen is stopping this frame...
            if countScreen.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > countScreen.tStartRefresh + countDuration-frameTolerance:
                    # keep track of stop time/frame for later
                    countScreen.tStop = t  # not accounting for scr refresh
                    countScreen.tStopRefresh = tThisFlipGlobal  # on global time
                    countScreen.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'countScreen.stopped')
                    # update status
                    countScreen.status = FINISHED
                    countScreen.setAutoDraw(False)
            # *port_HRstart* updates
            
            # if port_HRstart is starting this frame...
            if port_HRstart.status == NOT_STARTED and t >= 5-frameTolerance:
                # keep track of start time/frame for later
                port_HRstart.frameNStart = frameN  # exact frame index
                port_HRstart.tStart = t  # local t and not account for scr refresh
                port_HRstart.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(port_HRstart, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.addData('port_HRstart.started', t)
                # update status
                port_HRstart.status = STARTED
                port_HRstart.status = STARTED
                win.callOnFlip(port_HRstart.setData, int(7))
            
            # if port_HRstart is stopping this frame...
            if port_HRstart.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > port_HRstart.tStartRefresh + 1.0-frameTolerance:
                    # keep track of stop time/frame for later
                    port_HRstart.tStop = t  # not accounting for scr refresh
                    port_HRstart.tStopRefresh = tThisFlipGlobal  # on global time
                    port_HRstart.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.addData('port_HRstart.stopped', t)
                    # update status
                    port_HRstart.status = FINISHED
                    win.callOnFlip(port_HRstart.setData, int(0))
            
            # check for quit (typically the Esc key)
            if defaultKeyboard.getKeys(keyList=["escape"]):
                thisExp.status = FINISHED
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, win=win)
                return
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in HeartCountComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "HeartCount" ---
        for thisComponent in HeartCountComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        thisExp.addData('HeartCount.stopped', globalClock.getTime(format='float'))
        if port_HRstart.status == STARTED:
            win.callOnFlip(port_HRstart.setData, int(0))
        # the Routine "HeartCount" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # --- Prepare to start Routine "HeartReport" ---
        continueRoutine = True
        # update component parameters for each repeat
        thisExp.addData('HeartReport.started', globalClock.getTime(format='float'))
        HRenter_text.reset()
        # Run 'Begin Routine' code from HRenter_code
        HRtext = ""
        lastKey = ""
        #allowedKeys = ['1','2','3','4','5','6','7','8','9','0', 'return', 'backspace', 'num_1', 'num_2', 'num_3','num_4','num_5','num_6','num_7','num_8','num_9','num_0']
        allowedKeys = ['1','2','3','4','5','6','7','8','9','0', 'return', 'backspace']
        # keep track of which components have finished
        HeartReportComponents = [beatReport, HRenter_text, port_HRstop]
        for thisComponent in HeartReportComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "HeartReport" ---
        routineForceEnded = not continueRoutine
        while continueRoutine:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *beatReport* updates
            
            # if beatReport is starting this frame...
            if beatReport.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                beatReport.frameNStart = frameN  # exact frame index
                beatReport.tStart = t  # local t and not account for scr refresh
                beatReport.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(beatReport, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'beatReport.started')
                # update status
                beatReport.status = STARTED
                beatReport.setAutoDraw(True)
            
            # if beatReport is active this frame...
            if beatReport.status == STARTED:
                # update params
                pass
            
            # *HRenter_text* updates
            
            # if HRenter_text is starting this frame...
            if HRenter_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                HRenter_text.frameNStart = frameN  # exact frame index
                HRenter_text.tStart = t  # local t and not account for scr refresh
                HRenter_text.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(HRenter_text, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'HRenter_text.started')
                # update status
                HRenter_text.status = STARTED
                HRenter_text.setAutoDraw(True)
            
            # if HRenter_text is active this frame...
            if HRenter_text.status == STARTED:
                # update params
                HRenter_text.setText(HRtext, log=False)
            # Run 'Each Frame' code from HRenter_code
            # Get currently pressed key
            currentKey = event.getKeys()
            # If it is not nothing, update last pressed
            if currentKey:
                lastKey= currentKey[-1]
            # This key checking will override the usual listener for ESCAPE, so add it back in manually
            #if lastKey == "escape":
            #    continueRoutine = False
            if lastKey in allowedKeys:
                if lastKey == "backspace":
                    HRtext = HRtext[:-1]
                    lastKey = ""
                elif lastKey == "return":
                    lastKey = ""
                    continueRoutine = False
                else:
                    HRtext = HRtext + lastKey
                    lastKey = ""
            
            # *port_HRstop* updates
            
            # if port_HRstop is starting this frame...
            if port_HRstop.status == NOT_STARTED and t >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                port_HRstop.frameNStart = frameN  # exact frame index
                port_HRstop.tStart = t  # local t and not account for scr refresh
                port_HRstop.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(port_HRstop, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.addData('port_HRstop.started', t)
                # update status
                port_HRstop.status = STARTED
                port_HRstop.status = STARTED
                win.callOnFlip(port_HRstop.setData, int(8))
            
            # if port_HRstop is stopping this frame...
            if port_HRstop.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > port_HRstop.tStartRefresh + 1.0-frameTolerance:
                    # keep track of stop time/frame for later
                    port_HRstop.tStop = t  # not accounting for scr refresh
                    port_HRstop.tStopRefresh = tThisFlipGlobal  # on global time
                    port_HRstop.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.addData('port_HRstop.stopped', t)
                    # update status
                    port_HRstop.status = FINISHED
                    win.callOnFlip(port_HRstop.setData, int(0))
            
            # check for quit (typically the Esc key)
            if defaultKeyboard.getKeys(keyList=["escape"]):
                thisExp.status = FINISHED
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, win=win)
                return
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in HeartReportComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "HeartReport" ---
        for thisComponent in HeartReportComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        thisExp.addData('HeartReport.stopped', globalClock.getTime(format='float'))
        HeartbeatLoop.addData('HRenter_text.text',HRenter_text.text)
        # Run 'End Routine' code from HRenter_code
        thisExp.addData('HRreport', HRtext)
        if port_HRstop.status == STARTED:
            win.callOnFlip(port_HRstop.setData, int(0))
        # the Routine "HeartReport" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        thisExp.nextEntry()
        
        if thisSession is not None:
            # if running in a Session with a Liaison client, send data up to now
            thisSession.sendExperimentData()
    # completed 1.0 repeats of 'HeartbeatLoop'
    
    
    # --- Prepare to start Routine "EndPart1" ---
    continueRoutine = True
    # update component parameters for each repeat
    thisExp.addData('EndPart1.started', globalClock.getTime(format='float'))
    key_space_3.keys = []
    key_space_3.rt = []
    _key_space_3_allKeys = []
    # keep track of which components have finished
    EndPart1Components = [key_space_3, text_6, port_stopexp]
    for thisComponent in EndPart1Components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "EndPart1" ---
    routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *key_space_3* updates
        waitOnFlip = False
        
        # if key_space_3 is starting this frame...
        if key_space_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            key_space_3.frameNStart = frameN  # exact frame index
            key_space_3.tStart = t  # local t and not account for scr refresh
            key_space_3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_space_3, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'key_space_3.started')
            # update status
            key_space_3.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_space_3.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(key_space_3.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if key_space_3.status == STARTED and not waitOnFlip:
            theseKeys = key_space_3.getKeys(keyList=['space'], ignoreKeys=["escape"], waitRelease=False)
            _key_space_3_allKeys.extend(theseKeys)
            if len(_key_space_3_allKeys):
                key_space_3.keys = _key_space_3_allKeys[-1].name  # just the last key pressed
                key_space_3.rt = _key_space_3_allKeys[-1].rt
                key_space_3.duration = _key_space_3_allKeys[-1].duration
                # a response ends the routine
                continueRoutine = False
        
        # *text_6* updates
        
        # if text_6 is starting this frame...
        if text_6.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_6.frameNStart = frameN  # exact frame index
            text_6.tStart = t  # local t and not account for scr refresh
            text_6.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_6, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'text_6.started')
            # update status
            text_6.status = STARTED
            text_6.setAutoDraw(True)
        
        # if text_6 is active this frame...
        if text_6.status == STARTED:
            # update params
            pass
        # *port_stopexp* updates
        
        # if port_stopexp is starting this frame...
        if port_stopexp.status == NOT_STARTED and t >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            port_stopexp.frameNStart = frameN  # exact frame index
            port_stopexp.tStart = t  # local t and not account for scr refresh
            port_stopexp.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(port_stopexp, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.addData('port_stopexp.started', t)
            # update status
            port_stopexp.status = STARTED
            port_stopexp.status = STARTED
            win.callOnFlip(port_stopexp.setData, int(2))
        
        # if port_stopexp is stopping this frame...
        if port_stopexp.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > port_stopexp.tStartRefresh + 1.0-frameTolerance:
                # keep track of stop time/frame for later
                port_stopexp.tStop = t  # not accounting for scr refresh
                port_stopexp.tStopRefresh = tThisFlipGlobal  # on global time
                port_stopexp.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.addData('port_stopexp.stopped', t)
                # update status
                port_stopexp.status = FINISHED
                win.callOnFlip(port_stopexp.setData, int(0))
        
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.status = FINISHED
        if thisExp.status == FINISHED or endExpNow:
            endExperiment(thisExp, win=win)
            return
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in EndPart1Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "EndPart1" ---
    for thisComponent in EndPart1Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    thisExp.addData('EndPart1.stopped', globalClock.getTime(format='float'))
    # check responses
    if key_space_3.keys in ['', [], None]:  # No response was made
        key_space_3.keys = None
    thisExp.addData('key_space_3.keys',key_space_3.keys)
    if key_space_3.keys != None:  # we had a response
        thisExp.addData('key_space_3.rt', key_space_3.rt)
        thisExp.addData('key_space_3.duration', key_space_3.duration)
    if port_stopexp.status == STARTED:
        win.callOnFlip(port_stopexp.setData, int(0))
    thisExp.nextEntry()
    # the Routine "EndPart1" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # mark experiment as finished
    endExperiment(thisExp, win=win)


def saveData(thisExp):
    """
    Save data from this experiment
    
    Parameters
    ==========
    thisExp : psychopy.data.ExperimentHandler
        Handler object for this experiment, contains the data to save and information about 
        where to save it to.
    """
    filename = thisExp.dataFileName
    # these shouldn't be strictly necessary (should auto-save)
    thisExp.saveAsWideText(filename + '.csv', delim='auto')
    thisExp.saveAsPickle(filename)


def endExperiment(thisExp, win=None):
    """
    End this experiment, performing final shut down operations.
    
    This function does NOT close the window or end the Python process - use `quit` for this.
    
    Parameters
    ==========
    thisExp : psychopy.data.ExperimentHandler
        Handler object for this experiment, contains the data to save and information about 
        where to save it to.
    win : psychopy.visual.Window
        Window for this experiment.
    """
    if win is not None:
        # remove autodraw from all current components
        win.clearAutoDraw()
        # Flip one final time so any remaining win.callOnFlip() 
        # and win.timeOnFlip() tasks get executed
        win.flip()
    # mark experiment handler as finished
    thisExp.status = FINISHED
    # shut down eyetracker, if there is one
    if deviceManager.getDevice('eyetracker') is not None:
        deviceManager.removeDevice('eyetracker')
    logging.flush()


def quit(thisExp, win=None, thisSession=None):
    """
    Fully quit, closing the window and ending the Python process.
    
    Parameters
    ==========
    win : psychopy.visual.Window
        Window to close.
    thisSession : psychopy.session.Session or None
        Handle of the Session object this experiment is being run from, if any.
    """
    thisExp.abort()  # or data files will save again on exit
    # make sure everything is closed down
    if win is not None:
        # Flip one final time so any remaining win.callOnFlip() 
        # and win.timeOnFlip() tasks get executed before quitting
        win.flip()
        win.close()
    # shut down eyetracker, if there is one
    if deviceManager.getDevice('eyetracker') is not None:
        deviceManager.removeDevice('eyetracker')
    logging.flush()
    if thisSession is not None:
        thisSession.stop()
    # terminate Python process
    core.quit()


# if running this experiment as a script...
if __name__ == '__main__':
    # call all functions in order
    expInfo = showExpInfoDlg(expInfo=expInfo)
    thisExp = setupData(expInfo=expInfo)
    logFile = setupLogging(filename=thisExp.dataFileName)
    win = setupWindow(expInfo=expInfo)
    setupDevices(expInfo=expInfo, thisExp=thisExp, win=win)
    run(
        expInfo=expInfo, 
        thisExp=thisExp, 
        win=win,
        globalClock='float'
    )
    saveData(thisExp=thisExp)
    quit(thisExp=thisExp, win=win)
