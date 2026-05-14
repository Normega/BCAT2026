#!/usr/bin/env python2
from psychopy import visual, event, core, logging, data, gui, sound, event
from random import shuffle, sample
from psychopy.tools.filetools import fromFile, toFile
from datetime import datetime
import os
import sys
import time, numpy

ExpName = 'Misattribution of Arousal'
#time for the breath entraining block, in seconds
entraintime = 60

#ExpName = 'Sense Task Series'

RespiratoryRate=12                #float(expInfo['Respiratory rate']) #THE RESPIRATORY RATE IN BREATHS PER MINUTE
firsttime = float(60/RespiratoryRate) #THE ANCHOR/REFERENCE TIME FOR THE FIRST PULSE
firstinterval = .4 * firsttime



# #################################################################################
# PROBABLY DON'T EDIT BELOW
# #################################################################################
#Arbitrary animation step size, might need to adjust on different size screens
step =.0005
minwait = .2
# ################################################################################


#Define pause       
pause=0.2*(firsttime/2)

#should we run the training?
setruntraining = 1

#should we run the complete experiment or skip the visual baseline period (for people who have done the task before)?
setrunvisual = 1

#Staircase variables
steps = [.4, .2, .1, .05] #changing steps
bsteps = [4, 2, 1, .5] #changing steps
nR = 4 #number of reversals

#define minimum # of trials- not sure why the staircase makes us do this now...
NT = 1

#Time intervals for heartbeat and timeestimation tasks
time=([25,30,35,40,45,50])
#time=([2,3,4,5,6,7])
#time=([2,3])
refPitch = 440
targetSound = sound.Sound(refPitch,secs = .5)
vol=0.40
targetSound.setVolume(vol)

# ---------------------------------
# Set Up Log File
# ---------------------------------
_thisDir = os.path.dirname(os.path.abspath(__file__)).decode(sys.getfilesystemencoding())
os.chdir(_thisDir)
#expInfo = {'Participant':''}
expInfo = {'Participant':'', 'Respiratory rate':''}
dlg = gui.DlgFromDict(dictionary=expInfo, title=ExpName)
if dlg.OK == False: core.quit()  #
expInfo['date'] = data.getDateStr() 

if os.path.exists('./data/'):
    os.chdir(_thisDir+ os.sep + 'data')
else:
    os.mkdir(_thisDir+ os.sep + 'data')
    os.chdir(_thisDir+ os.sep + 'data')

fileName = '%s_circletask_%s' %(expInfo['Participant'], expInfo['date'])
dataFile = open(fileName+'.csv', 'w')


Pnum = expInfo['Participant']

#------------------------------------
#create window and stimuli
#------------------------------------
win = visual.Window(allowGUI=True, fullscr=True, units='height',  rgb=(-1,-1,-1)) #, screen = 1
#qwin = visual.Window((800.0, 800.0), allowGUI=True)
screenwidth,screenheight= win.size # for converting norm units to pix
myMouse = event.Mouse()  #  will use win by default
win.setMouseVisible(False)


def beep():
    targetSound.play()
    core.wait(0.5)
    targetSound.stop()
    core.wait(0.5)
#-----------------------------------------------------
# SET UP STIMULUS OBJECTS
#-----------------------------------------------------
ww = 1.8
message1 = visual.TextStim(win, height = .08, units='norm', wrapWidth=ww, pos=[0,+.8], alignHoriz='center', alignVert='top', text='')

minwait = .2

stim1 = visual.Circle(win, 
                 radius = .1,
                 edges = 100,
                 lineColor='red',
                 lineWidth=2.0, #in pixels
                 fillColor='red', #beware, with convex shapes fill colors don't work
                 pos= [0,0], #the anchor (rotation and vertices are position with respect to this)
                 interpolate=True,
                 opacity=0.9,
                 autoLog=False)#this stim changes too much for autologging to be useful

#-----------------------------------------------------------------
# STIMULI
#-------------------------------------------------------------------
def pulse(pulsetime, pause, step):	
    #PULSE 1: first interval that radius is increasing
    timer = core.Clock()
    timer.add(pulsetime/2)
    while timer.getTime()<0:
        stim1.radius += step 
        stim1.draw()
        win.flip()
        if event.getKeys(keyList=['escape', 'q']):
            core.quit()
    print "increasing:"
    print stim1.radius
    #PULSE 1: second interval - pause
    timer = core.Clock()
    timer.add(pause)
    while timer.getTime()<0:
        stim1.radius += 0 
        stim1.draw()
        win.flip()
        if event.getKeys(keyList=['escape', 'q']):
            core.quit()

    #PULSE 1: third interval - radius is decreasing
    timer = core.Clock()
    timer.add(pulsetime/2)
    while timer.getTime()<0:
        stim1.radius -= step #adding something to the radius
        stim1.draw()
        win.flip()
        if event.getKeys(keyList=['escape', 'q']):
            core.quit()
    print "Decreasing:"
    print stim1.radius

    #PULSE 1: fourth interval - pause
    timer = core.Clock()
    timer.add(pause)
    while timer.getTime()<0:
        stim1.radius += 0 
        stim1.draw()
        win.flip()
        if event.getKeys(keyList=['escape', 'q']):
            core.quit()
    return

#SELF REPORT FUNCTIONS----------------------------------------------------------------------------------------------------------
#SELF REPORT   SELF REPORT  SELF REPORT   SELF REPORT   SELF REPORT   SELF REPORT   SELF REPORT   SELF REPORT   SELF REPORT
#SELF REPORT   SELF REPORT  SELF REPORT   SELF REPORT   SELF REPORT   SELF REPORT   SELF REPORT   SELF REPORT   SELF REPORT
#SELF REPORT   SELF REPORT  SELF REPORT   SELF REPORT   SELF REPORT   SELF REPORT   SELF REPORT   SELF REPORT   SELF REPORT
#--------------------------------------------------------------------------------------------------------------------------------

# Declare SelfReport Variables
# Declare SelfReport Variables   
# Declare SelfReport Variables

gender=-1
SexualOrientation=-1
# Misattribution of Arousal--------
blockNum= -1 #(misattribution)

Condition=' '
TotalChange=1. #(Percentage change across trial) 
fastORslow=-1


FoS_Response='none'
FoS_Accuracy=5
ConfidenceRating=-1
MoodRating=-1
ArousalRating=-1
#ATTRACTIVE PICTURES----------

PicturesDispayed='nope' #(which ones?)

N1=-1
N2=-1
A1=-1
A2=-1

Beep1Onset='NONE'
Beep2Onset='NONE'

#Staircase variables
steps = [.4, .2, .1, .05] #changing steps
bsteps = [4, 2, 1, .5] #changing steps
nR = 4 #number of reversals

#define minimum # of trials- not sure why the staircase makes us do this now...
NT = 1

#Time intervals for heartbeat and timeestimation tasks
time=([25,30,35,40,45,50])

PulseAOnset = 'NA'
PulseBOnset = 'NA'
PulseBOffset = 'NA'

#Second pulse time difference- these are logged as 0 before the trials begin
thisIncrement = 0
direction = 0
foil = 0
hitLimit = 0
JND = 0


trialNum=0

#Variables for Collecting Participant Response Data
Response = -1
Accuracy = -1

#SummaryData
OriRating = -1
TouchRating = -1
VisRating = -1
BreathRating = -1
HeartRating = -1
TimeRating = -1

HeartBeatEST=0

OriJND = -1
TouchJND = -1
VisJND = -1
BreathJND = -1
HeartCount = -1
TimeScore = -1



#Define pause     
#Write Data Function--------------------------------------------------------------------------------
#Write Data Function 
#Write Data Function 
#---------------------------------------------------------------------------------------------------


def writedata():
    dataFile.write('%s,%s,%s,%i,%i,%i, \
        %i,%i,%.3f,%s,%s,%i,%i, \
        %i,%i,%i,%i,%i,%i,%s,%s,%s, \
        %.3f,%.3f,%.3f,%.3f,%i,%s,%i,%.3f,%.3f\n' \
        %(Pnum,ExpName,Condition,gender,SexualOrientation,blockNum, \
        fastORslow,ConfidenceRating,TotalChange,FoS_Response,FoS_Accuracy,MoodRating,ArousalRating, \
        N1,N2,A1,A2,trialNum, hitLimit, PulseAOnset, PulseBOnset, PulseBOffset, \
        firsttime, thisIncrement, foil, pause,direction,Response,Accuracy,JND,BreathJND))
    return
    

#Initialize the log file

dataFile.write('Pnum,ExpName,Condition,gender,SexualOrientation,BlockNum, \
    fastORslow,ConfidenceRating,TotalChange,FoS_Response,FoS_Accuracy,MoodRating,ArousalRating, \
    N1,N2,A1,A2,trialNum, hitLimit, PulseAOnset, PulseBOnset, PulseBOffset, \
    firsttime, thisIncrement, foil, pause,direction,Response,Accuracy,JND,BreathJND\n')
writedata()



#Instructions-----------------------------------------
#
#-----------------------------------------------------
def Instruct():
    global InstructionList
    InstructVisual = visual.ImageStim(
        win=win, name='InstructVisual',
        image=InstructionList, mask=None,
        ori=0, pos=(0, 0), size=(1.5, 1),
        color=[1,1,1], colorSpace='rgb', opacity=1,
        flipHoriz=False, flipVert=False,
        texRes=128, interpolate=True, depth=0.0)
    InstructVisual.draw()
    win.flip()
    if event.getKeys(['escape']):
            core.quit()
    thisResp=None
    while thisResp is None:
        allKeys=event.waitKeys()           
        for thisKey in allKeys:
            if thisKey in ['q', 'escape']:
                core.quit()#abort experiment
            else:
                return 
                

def getresp(): #get a response, usually accuracy is involved
    global Accuracy
    global Response

    Response=None
    event.clearEvents()
    while Response is None:
        allKeys=event.waitKeys()           
        for thisKey in allKeys:
            if thisKey in ['q', 'escape']:
                core.quit()#abort experiment
            elif (thisKey=='1' and direction==1) or (thisKey=='2' and direction==-1):
                Accuracy = 1#correct
                Response = thisKey
                msg("Correct",1)
            elif (thisKey=='1') or (thisKey=='2'):
                Accuracy = 0#incorrect
                Response = thisKey
                msg("Incorrect",1)
        event.clearEvents()

def getkey(): #capture a 1 or 2 key response
    global Response

    Response=None
    event.clearEvents()
    while Response is None:
        allKeys=event.waitKeys()           
        for thisKey in allKeys:
            if thisKey in ['q', 'escape']:
                core.quit()#abort experiment
            elif (thisKey=='1') or (thisKey=='2'):
                Response = thisKey
                return Response



#MESSAGE FUNCTION------------------------------------
#
#----------------------------------------------------
def msg(text, pause=None):
    global message1
    message1.setText(text)
    message1.draw()    
    if pause is None:
        win.flip()
        core.wait(minwait)
        allKeys = event.waitKeys()
        for thisKey in allKeys:
            if thisKey in ['escape', 'q']:
                core.quit()
    elif pause == "getresp":
        win.flip()
        core.wait(minwait)
        getresp() #get response
    elif pause == "extresp":
        core.wait(.001)
    elif pause == "trainresp":
        win.flip()
        core.wait(minwait)
        getkey()
    elif pause == "final":
        #wait only for exit command
        win.flip()
        thisResp=None
        while thisResp is None:
            allKeys=event.waitKeys()
            for thisKey in allKeys:
                if thisKey=='q':
                    core.quit()
                else:
                    thisResp = None 
    else:
        win.flip()
        core.wait(pause)
        



#-------------------------------------------------------------------

def getresp(): #get a response, usually accuracy is involved
    global Accuracy
    global Response

    Response=None
    event.clearEvents()
    while Response is None:
        allKeys=event.waitKeys()           
        for thisKey in allKeys:
            if thisKey in ['q', 'escape']:
                core.quit()#abort experiment
            elif (thisKey=='1' and direction==1) or (thisKey=='2' and direction==-1):
                Accuracy = 1#correct
                Response = thisKey
                msg("Correct",1)
            elif (thisKey=='1') or (thisKey=='2'):
                Accuracy = 0#incorrect
                Response = thisKey
                msg("Incorrect",1)
        event.clearEvents()
        
def getkey(): #capture a 1 or 2 key response
    global Response

    Response=None
    event.clearEvents()
    while Response is None:
        allKeys=event.waitKeys()           
        for thisKey in allKeys:
            if thisKey in ['q', 'escape']:
                core.quit()#abort experiment
            elif (thisKey=='1') or (thisKey=='2'):
                Response = thisKey
                return Response


#Confidence FUNCTION-------------------------------
#
#--------------------------------------------------

def TestScale(): 
    TestRatingScale = visual.RatingScale(win,low=1, high=9, marker='slider',
            tickMarks=[ 1, 2, 3, 4, 5, 6, 7, 8, 9], stretch=1.8, tickHeight=-1.5, 
            labels=["1", "2", "3","4","5","6","7","8","9"], scale=None)
    # show & update until a response has been made
    while TestRatingScale.noResponse:
        msg("During the study you will be asked to respond by clicking on a rating scale similar to the one shown below\n\n To respond you need to click on the line and then click on the grey box below with the mouse \n\n Please practice this now to continue...", "extresp")
        TestRatingScale.draw()
        win.flip()
        if event.getKeys(['escape']):
            core.quit()
        TestRatingScale.getRating()
    return 

#Gender FUNCTION-----------------------------------
#
#--------------------------------------------------
def genderRating(): 
    global gender 
    GenderScale = visual.RatingScale(win,low=1, high=2, marker='slider',
            tickMarks=[1, 2], stretch=0.5, tickHeight=-1.5, 
            labels=["Male","Female"], scale=None)
    # show & update until a response has been made
    while GenderScale.noResponse:
        msg("Are you Male or Female?\nPlease click on the line and then press enter\n", "extresp")
        GenderScale.draw()
        picture = visual.ImageStim(
        win=win, name='picture',
        image=u'gender.jpg', mask=None,    
        ori=0, pos=(0, 0), size=(1, 0.35),
        color=[1,1,1], colorSpace='rgb', opacity=1,
        flipHoriz=False, flipVert=False,
        texRes=128, interpolate=True, depth=0.0)
        picture.draw()
        win.flip()
        if event.getKeys(['escape']):
            core.quit()
        GenderScale.getRating()
        gender = GenderScale.getRating()


#Sexual Orientation FUNCTION-----------------------
#
#--------------------------------------------------

def Orientation(): 
    global SexualOrientation
    SexualOrientationScale = visual.RatingScale(win,low=0, high=6, marker='slider',
            tickMarks=[ 0, 1, 2, 3, 4, 5, 6], stretch=1.6, tickHeight=-1.5, 
            labels=["0","1", "2", "3","4","5","6"], scale=None)
    # show & update until a response has been made
    while SexualOrientationScale.noResponse:
        msg("Please indicate your sexual orientation on the Kinsey scale\n", "extresp")
        SexualOrientationScale.draw()
        picture = visual.ImageStim(
        win=win, name='picture',
        image=u'kinsey.PNG', mask=None,    
        ori=0, pos=(0, 0), size=(1, 0.35),
        color=[1,1,1], colorSpace='rgb', opacity=1,
        flipHoriz=False, flipVert=False,
        texRes=128, interpolate=True, depth=0.0)
        picture.draw()
        win.flip()
        if event.getKeys(['escape']):
            core.quit()
        SexualOrientationScale.getRating()
        SexualOrientation = SexualOrientationScale.getRating()
    return SexualOrientation 
    writedata()

#Speed Response FUNCTION---------------------------
#
#--------------------------------------------------

def speedquery():
    global FoS_Response
    global FoS_Accuracy
    global Accuracy
    global fastORslow
    Speed = visual.ImageStim(
        win=win, name='Speed',
        image=u'22Speed.PNG', mask=None,
        ori=0, pos=(0, 0), size=(1.5, 1),
        color=[1,1,1], colorSpace='rgb', opacity=1,
        flipHoriz=False, flipVert=False,
        texRes=128, interpolate=True, depth=0.0)
    Speed.draw()
    win.flip()
    if event.getKeys(['escape']):
            core.quit()
    thisResp=None
    while thisResp is None:
        allKeys=event.waitKeys()           
        for thisKey in allKeys:
            FoS_Response = thisKey
            if thisKey in ['q', 'escape']:
                core.quit()#abort experiment
            elif (thisKey=='left'):
                if TotalChange >1:
                    FoS_Accuracy=1
                    return FoS_Response
                elif TotalChange <1:
                    FoS_Accuracy=0
                    return FoS_Response
            elif (thisKey=='up'):
                FoS_Accuracy=0
                return FoS_Response
            elif (thisKey=='right'):
                if TotalChange >1:
                    FoS_Accuracy=0
                    return FoS_Response
                elif TotalChange <1:
                    FoS_Accuracy=1
                    return FoS_Response


#Confidence FUNCTION-------------------------------
#
#--------------------------------------------------

def confidence(): 
    global ConfidenceRating
    ConfidenceRatingScale = visual.RatingScale(win,low=1, high=9, marker='slider',
            tickMarks=[ 1, 2, 3, 4, 5, 6, 7, 8, 9], stretch=1.8, tickHeight=-1.5, 
            labels=["1", "2", "3","4","5","6","7","8","9"], scale=None)
    # show & update until a response has been made
    while ConfidenceRatingScale.noResponse:
        msg("On a scale from 1-9...How confident are you in your previous response?\n", "extresp")
        ConfidenceRatingScale.draw()
        picture = visual.ImageStim(
        win=win, name='picture',
        image=u'2CONFIDENCE.PNG', mask=None,    
        ori=0, pos=(0, 0), size=(1.5, 0.35),
        color=[1,1,1], colorSpace='rgb', opacity=1,
        flipHoriz=False, flipVert=False,
        texRes=128, interpolate=True, depth=0.0)
        picture.draw()
        win.flip()
        if event.getKeys(['escape']):
            core.quit()
        ConfidenceRatingScale.getRating()
        ConfidenceRating = ConfidenceRatingScale.getRating()
    return ConfidenceRating

#MOOD Rating FUNCTION------------------------------
#
#--------------------------------------------------

def mood(): 
    global MoodRating
    MoodRatingScale = visual.RatingScale(win,low=1, high=9, marker='slider',
            tickMarks=[ 1, 2, 3, 4, 5, 6, 7, 8, 9], stretch=2, tickHeight=-1.5, 
            labels=["1", "2", "3","4","5","6","7","8","9"], scale=None)
    # show & update until a response has been made
    while MoodRatingScale.noResponse:
        msg("Please indicate your current mood on a scale from 1-9\n", "extresp")
        MoodRatingScale.draw()
        picture = visual.ImageStim(
        win=win, name='picture',
        image=u'2MOOD.PNG', mask=None,    
        ori=0, pos=(0, 0), size=(1.3, 0.35),
        color=[1,1,1], colorSpace='rgb', opacity=1,
        flipHoriz=False, flipVert=False,
        texRes=128, interpolate=True, depth=0.0)
        picture.draw()
        win.flip()
        if event.getKeys(['escape']):
            core.quit()
        MoodRatingScale.getRating()
        MoodRating = MoodRatingScale.getRating()
    return MoodRating

#Arousal Rating FUNCTION------------------------------
#
#-----------------------------------------------------

def arousal(): 
    global ArousalRating
    ArousalRatingScale = visual.RatingScale(win,low=1, high=9, marker='slider',
            tickMarks=[ 1, 2, 3, 4, 5, 6, 7, 8, 9], stretch=2, tickHeight=-1.5, 
            labels=["1", "2", "3","4","5","6","7","8","9"], scale=None)
    # show & update until a response has been made
    while ArousalRatingScale.noResponse:
        msg("Please indicate your current level of arousal on a scale from 1-9\n", "extresp")
        ArousalRatingScale.draw()
        picture = visual.ImageStim(
        win=win, name='picture',
        image=u'2AROUSAL.PNG', mask=None,    
        ori=0, pos=(0, 0), size=(1.3, 0.35),
        color=[1,1,1], colorSpace='rgb', opacity=1,
        flipHoriz=False, flipVert=False,
        texRes=128, interpolate=True, depth=0.0)
        picture.draw()
        win.flip()
        if event.getKeys(['escape']):
            core.quit()
        ArousalRatingScale.getRating()
        ArousalRating = ArousalRatingScale.getRating()
    return ArousalRating


def attractionRating():
    global AttractiveRandomized
    global NeutralRandomized
    global CurrentBlock
    global PicturesDispayed
    global trialOrderRandomized
    global displaycounter
    global A1
    global A2
    global N1
    global N2
    global AOutsidecounter
    global NOutsidecounter
    attANDneut=[['X1'],['X2'],['X3'],['X4']]
    #PrePrintDispay=[['Y1'],['Y2'],['Y3'],['Y4']]
    
#trial Holder To Pick Pictures 
#First create 1x4 Array, "attANDneut", that holds the four images (two attractive ones are positioned in columns 0 and 1 and two Neutral are in columns 2 and 3)
    AInsidecounter=0
    while AInsidecounter<2: 
        ArandNum=AttractiveRandomized[AOutsidecounter]        
        attANDneut[AInsidecounter]="A"+str(ArandNum)+".jpg"   
        #PrePrintDisplay[Acounter]="A"+str(ArandNum)    #Save a version that doesn't have the .PNG extension for clarity on the log file 
        AOutsidecounter=AOutsidecounter+1
        AInsidecounter=AInsidecounter+1
    NInsidecounter=2
    while NInsidecounter<4:
        NrandNum=NeutralRandomized[NOutsidecounter]
        attANDneut[NInsidecounter]="N"+str(NrandNum)+".jpg"
        #PrePrintDisplay[Ncounter]="N"+str(ArandNum)
        NOutsidecounter=NOutsidecounter+1
        NInsidecounter=NInsidecounter+1
#Randomize the Order for this Trial 
    print attANDneut
    trialOrder = [0,1,2,3]
    trialOrderRandomized = numpy.random.choice (trialOrder,4,replace=False)

    displaycounter=0
    while displaycounter<4: 
        Current=trialOrderRandomized[displaycounter]
        print Current
        
        AttractionRatingScale = visual.RatingScale(win,low=0, high=10, marker='slider',
            tickMarks=[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10], stretch=1, tickHeight=-1.5, 
            labels=["0", "1", "2", "3","4","5","6","7","8","9","10"], scale=None)
    # show & update until a response has been made
    
        picture = visual.ImageStim(win=win, name='picture',
            image=(attANDneut[Current]), mask=None,    # Randomly Pulling image Name from the 1x4 Array 
            ori=0, pos=(0, 0), size=(0.5, 0.35),
            color=[1,1,1], colorSpace='rgb', opacity=1,
            flipHoriz=False, flipVert=False,
            texRes=128, interpolate=True, depth=0.0)
            
        while AttractionRatingScale.noResponse:
            msg("On a scale from 0-10...How attractive do you find this individual?\nChoose a value by clicking on the line and press enter.", "extresp")
            AttractionRatingScale.draw()
            picture.draw()
            win.flip()
            #core.wait(3)
            if event.getKeys(['escape']):
                core.quit()
        AttractionRatingScale.getRating()
        ThisRating = AttractionRatingScale.getRating()
        if Current==0:                                          #Current variable is randomized # from 0-3... The initial 1x4 array is organized with first two columns holding Att pics, and columns 2-3 holding neutral
            A1=ThisRating
        if Current==1:
            A2=ThisRating
        if Current==2:
            N1=ThisRating
        if Current==3:
            N2=ThisRating
        win.flip()
        AttractionRatingScale.reset()
        displaycounter=displaycounter+1




#------------------------------------------------------------------------------------------
# BREATH MISATTRIBUTION
#------------------------------------------------------------------------------------------
def runmisattribution():
    global Condition
    global blockNum
    global trialNum
    global step
    global pulsetime 
    global percentChange 
    global fastORslow
    global TotalChange
    global CurrentBlock
    global AttractiveRandomize
    
    Condition = 'Breath Misattribution' #For Logging

    step=0.0005
    firsttime=5
    pulsetime = firsttime
    pause=0.2*(firsttime/2)
    TotalPulses= 8.
    StudyDesignArray = [[0,1.2],[0,1.35],[0,1.5],[0,1.65],[1,1.2],[1,1.35],[1,1.5],[1,1.65],[0,0.8],[0,0.65],[0,0.5],[0,0.35],[1,0.8],[1,0.65],[1,0.5],[1,0.35]]   
    #StudyDesignArray ChangeRate (Gradual-0 vs. Quick-1) as well as overall change in pulse rate increasing (1.2, 1.35, 1.5), decreasing (0.8,0.65,0.5)

    #RandomizeBlocks 
    MyArray = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
    RandBlock =numpy.random.choice (MyArray,16,replace=False)   # Randomizing the order of the "Blocks"
    blockNum=0
    while blockNum<16: 
        CurrentBlock=RandBlock[blockNum]
        ThisBlock=StudyDesignArray[CurrentBlock]   #"ThisBlock" is 1 by 2 vector [gradual or fast, TotalChange] 
        print "ThisBlock"
        print (ThisBlock)
        fastORslow = ThisBlock[0]
        msg("\n Please continue to match your breath to the circle. You will do this for a short duration, and then will be asked a series of self-report questions. \n \n Remember... Breath in as the circle expands, pause as it does not change, breathe out as it contracts.\n \n Press any key to continue")
        if fastORslow == 0:                                #0 = gradual change
            pulsetime=5                                    #Pulsetime set to 5 seconds 
            count=0
            step=0.0005
            
            while (count< 8):
                pulse(pulsetime, pause, step)
                TotalChange=ThisBlock[1]                    # Overall change accross all Pulses (if 150% than 1.5...) 
                PulseChange=TotalChange**(1/(TotalPulses))  # calculate the change per Pulse
                oldpulsetime = pulsetime
                pulsetime=pulsetime*(PulseChange)           # calculate new pulsetime
                step=step*oldpulsetime/pulsetime
                count=count+1
            pulse(pulsetime, pause, step)

            speedquery()                                    #Awareness Check....Did you notice a change in speed?
            confidence()                                    #Confidence rating... 
            arousal()
            mood()
            attractionRating()
            writedata()
        if fastORslow == 1:                                #quick change
            TotalPulses=8
            HalfPulse = TotalPulses/2                      #First half at initial pulse length, second half at increase/decrease
            TotalChange=ThisBlock[1]
            pulsetime=5
            step=0.0005
            count=0
            while (count< HalfPulse):
                pulse(pulsetime, pause, step)
                count=count+1
            oldpulsetime = pulsetime
            pulsetime=pulsetime*TotalChange           # calculate new pulsetime
            step=step*oldpulsetime/pulsetime 
            while (count<TotalPulses):
                pulse(pulsetime, pause, step)
                count=count+1

            speedquery()                                         #Awareness Check....Did you notice a change in speed?
            confidence()                                         #Confidence rating... 
            arousal()
            mood()
            attractionRating()
            writedata()
        blockNum=blockNum+1


#------------------------------------------------------------------------------------------
# BREATH MISATTRIBUTION
#------------------------------------------------------------------------------------------
def runmisattribution2():
    global Condition
    global blockNum
    global trialNum
    global step
    global pulsetime 
    global percentChange 
    global fastORslow
    global TotalChange
    global CurrentBlock
    global AttractiveRandomize

    Condition = 'Second Breath Misattribution' #For Logging
    
    step=0.0005
    firsttime=5
    pulsetime = firsttime
    pause=0.2*(firsttime/2)
    TotalPulses= 8.
    StudyDesignArray = [[0,1.2],[0,1.35],[0,1.5],[0,1.65],[1,1.2],[1,1.35],[1,1.5],[1,1.65],[0,0.8],[0,0.65],[0,0.5],[0,0.35],[1,0.8],[1,0.65],[1,0.5],[1,0.35]]   
    #StudyDesignArray ChangeRate (Gradual-0 vs. Quick-1) as well as overall change in pulse rate increasing (1.2, 1.35, 1.5), decreasing (0.8,0.65,0.5)

    #RandomizeBlocks 
    MyArray = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
    RandBlock =numpy.random.choice (MyArray,16,replace=False)   # Randomizing the order of the "Blocks"
    blockNum=0
    while blockNum<16: 
        CurrentBlock=RandBlock[blockNum]
        ThisBlock=StudyDesignArray[CurrentBlock]   #"ThisBlock" is 1 by 2 vector [gradual or fast, TotalChange] 
        print "ThisBlock"
        print (ThisBlock)
        fastORslow = ThisBlock[0]
        msg("\n Please continue to match your breath to the circle. You will do this for a short duration, and then will be asked a series of self-report questions. \n \n Remember... Breath in as the circle expands, pause as it does not change, breathe out as it contracts.\n \n Press any key to continue")
        if fastORslow == 0:                                #0 = gradual change
            pulsetime=5                                    #Pulsetime set to 5 seconds 
            count=0
            step=0.0005
            
            while (count< 8):
                pulse(pulsetime, pause, step)
                TotalChange=ThisBlock[1]                    # Overall change accross all Pulses (if 150% than 1.5...) 
                PulseChange=TotalChange**(1/(TotalPulses))  # calculate the change per Pulse
                oldpulsetime = pulsetime
                pulsetime=pulsetime*(PulseChange)           # calculate new pulsetime
                step=step*oldpulsetime/pulsetime
                count=count+1
            pulse(pulsetime, pause, step)

            speedquery()                                    #Awareness Check....Did you notice a change in speed?
            confidence()                                    #Confidence rating... 
            arousal()
            mood()
            attractionRating()
            writedata()
        if fastORslow == 1:                                #quick change
            TotalPulses=8
            HalfPulse = TotalPulses/2                      #First half at initial pulse length, second half at increase/decrease
            TotalChange=ThisBlock[1]
            pulsetime=5
            step=0.0005
            count=0
            while (count< HalfPulse):
                pulse(pulsetime, pause, step)
                count=count+1
            oldpulsetime = pulsetime
            pulsetime=pulsetime*TotalChange           # calculate new pulsetime
            step=step*oldpulsetime/pulsetime 
            while (count<TotalPulses):
                pulse(pulsetime, pause, step)
                count=count+1

            speedquery()                                         #Awareness Check....Did you notice a change in speed?
            confidence()                                         #Confidence rating... 
            arousal()
            mood()
            attractionRating()
            writedata()
        blockNum=blockNum+1

#------------------------------------------------------------------------------------------
# BREATH ENTRAINING
#------------------------------------------------------------------------------------------
def runentraining():
    global Condition
    global trialNum
    global PulseAOnset
    global PulseBOnset
    global PulseBOffset

    RespiratoryRate=12.                #float(expInfo['Respiratory rate']) #THE RESPIRATORY RATE IN BREATHS PER MINUTE
    firsttime = float(60/RespiratoryRate)
    Condition = 'Breath Entraining' #For Logging
    trialNum = 0
    entraintime=60
    
    step=0.0005
    firsttime=5
    pause=0.2*(firsttime/2)
    
    #msg("For this next part of the study you will be asked to match your breath to a pulsating circle.\n Press any key to continue.")
    #msg("Please spend the next minute matching your breath to the circle. Breath in as it expands, pause as it does not change, breathe out as it contracts. \n \n It is important that you do you best to sychronize your breath to the circle... Please ask the researcher if you have any questions about this part of the study. \n Press any key to begin.")
    #if event.getKeys(['escape']):
        #core.quit()
    #count=0
    #while count<4:
        #pulse(firsttime, pause, step)
        #count=count+1
        #return
        
    bigtimer = core.Clock()
    bigtimer.add(entraintime)
    while bigtimer.getTime() < 0:
        trialNum += 1
            #First Pulse
            #PulseAOnset = datetime.now().strftime('%d/%m/%Y %H:%M:%S.%f')[:-3]
            
        pulse(firsttime, pause, step)
            
            #PulseBOnset=datetime.now().strftime('%d/%m/%Y %H:%M:%S.%f')[:-3]
            #PulseBOffset='NA' #There is no secondpulse to model in a 'trial'
            #writedata()


#-------------------------------------------------------------------------------------------------------------------------------------------------
#STAIRCASE  STAIRCASE   STAIRCASE   STAIRCASE   STAIRCASE  STAIRCASE   STAIRCASE   STAIRCASE    STAIRCASE  STAIRCASE   STAIRCASE   STAIRCASE
#STAIRCASE  STAIRCASE   STAIRCASE   STAIRCASE   STAIRCASE  STAIRCASE   STAIRCASE   STAIRCASE    STAIRCASE  STAIRCASE   STAIRCASE   STAIRCASE
#STAIRCASE  STAIRCASE   STAIRCASE   STAIRCASE   STAIRCASE  STAIRCASE   STAIRCASE   STAIRCASE    STAIRCASE  STAIRCASE   STAIRCASE   STAIRCASE
#STAIRCASE  STAIRCASE   STAIRCASE   STAIRCASE   STAIRCASE  STAIRCASE   STAIRCASE   STAIRCASE    STAIRCASE  STAIRCASE   STAIRCASE   STAIRCASE
#STAIRCASE  STAIRCASE   STAIRCASE   STAIRCASE   STAIRCASE  STAIRCASE   STAIRCASE   STAIRCASE    STAIRCASE  STAIRCASE   STAIRCASE   STAIRCASE
#-------------------------------------------------------------------------------------------------------------------------------------------------

def confrating():
    #Confidence judgment

    myRatingScale = visual.RatingScale(win,low=0, high=100, marker='slider',
        tickMarks=[0, 25, 50, 75, 100], stretch=2.5, tickHeight=-1.5, 
        labels=["very poor", "poor", "average", "well", "very well"], scale=None)

    # show & update until a response has been made
    while myRatingScale.noResponse:
        msg("How well do you think you did?\nChoose a value by clicking at the scale and press enter.", "extresp")
        myRatingScale.draw()
        win.flip()
        if event.getKeys(['escape']):
            core.quit()
    print 'Confidence judgment =', myRatingScale.getRating()
    Rating = myRatingScale.getRating()
    return Rating



#------------------------------------------------------------------------------------------
# BREATH INTEGRATION STAIRCASE
#------------------------------------------------------------------------------------------
def runintegration():
    global Condition
    global trialNum
    global foil
    global thisIncrement
    global PulseAOnset
    global PulseBOnset
    global PulseBOffset
    global direction
    global hitLimit
    global BreathRating

    global JND
    global BreathJND
    
    global Accuracy
    global Response
    Condition = 'BreathStaircase'
    trialNum = 0
    hitLimit = 0 #to count if particpants hit the upper/lower limit
    
    stim1.draw()
    msg("We would like you to sychronize your breathing to the circle again. This time the circle will pulse twice and you will be asked to decide which pulse was faster. \nPress any key to begin.")
    
    #runs twice: x=0 and x=1
    for x in range(0, 2):
        #(re)create the staircase
        bstaircase = data.StairHandler(startVal = firstinterval,
        stepType = 'lin', stepSizes=steps, #reduce step size every reversals
        minVal=0.001, maxVal = 5,
        nUp=1, nDown=3,  #will home in on the 80% threshold
        nTrials=NT, nReversals = nR)
        
        #See if it is safe to exist the loop
        if (x > 0):
            #this is the second time through the loop, which means it either completed successfully or the person hit the limits too many times
            if (hitLimit >3):
                #looping again if the person hit the limits too many times
                Condition = 'Breath_Hit_Limit'
                writedata()
                hitLimit = 0 #reset hitLimit counter

                #display instructions and wait
                msg("Let's Review:\n\nBreath along with a circle as it pulses (grows and shrinks) twice.nHit any key to Continue.")
                msg("Compared to the first pulse, press '1' if you think the second pulse was slower or '2' if you think it was faster.\nHit a key to continue")
            else:
                #the staircase completed successfully
                #so break out of the loop
                break;

        for thisIncrement in bstaircase: #will step through the staircase
            trialNum += 1
            #Randomly pick the trial type
            direction= round(numpy.random.random())*2-1 #will be either +1(slower) or -1(faster)

            #Keep the second stim (foil) in bounds!
            if (firsttime + (thisIncrement * direction)) < (firsttime-2):
                foil = minVal
                hitLimit += 1
    #            print 'lower bound: 0'
            elif (firsttime + (thisIncrement * direction)) > (firsttime+2):
                foil = firsttime + 2
                hitLimit += 1
            else:
                foil = firsttime + (thisIncrement * direction)

         # define step2 as the radius growth step of second ball
            step2=step*firsttime*(foil)**(-1)

            #First Pulse
            PulseAOnset = datetime.now().strftime('%d/%m/%Y %H:%M:%S.%f')[:-3]
            pulse(firsttime, pause, step)
            PulseBOnset=datetime.now().strftime('%d/%m/%Y %H:%M:%S.%f')[:-3]
            
            #Second Pulse
            pulse(foil, pause, step2)
            PulseBOffset=datetime.now().strftime('%d/%m/%Y %H:%M:%S.%f')[:-3]

            #blank screen
            stim1.draw()
            msg("1 = Second Pulse Slower\n2 = Second Pulse Faster","getresp")

            #add the data to the staircase so it can calculate the next level
            bstaircase.addResponse(Accuracy)
            if not bstaircase.reversalIntensities:
                JND = -1
            else:
                JND = bstaircase.reversalIntensities[-1]
                BreathJND = JND
            writedata()

            #if the participant keeps hitting the upper/lower limit restart the task
            if (hitLimit > 3):
                break;

            win.flip()
            core.wait(1)
            #end of inner loop
        #end of outer loop
        BreathJND =  numpy.average(bstaircase.reversalIntensities[-2:])
    #staircase has ended
    if (hitLimit >3):
        #the reason we are here is because the person hit the limits too many times and failed on their second chance
        #so the staircase was not completed, but this person does not get it
        #write to the file: that we are skipping that staircase
        Condition = 'Breathing_staircase_failed'
        writedata()    
    else:
        #write the JND to the file: participant,expName,mean of final reversals
        Condition = 'BreathComplete'
    writedata()

    #bstaircase.saveAsExcel(fileName + 'breath', sheetName='data', matrixOnly=False, appendFile=True, fileCollisionMethod='rename')
    #__________________________________________________________________________
    #Rating
    #__________________________________________________________________________
    Condition = 'Breath Confidence Rating'
    BreathRating = confrating()
    writedata()
    
    

    #___________________________________________
    #Confidence judgment
    #___________________________________________
    HeartRating = confrating()
    writedata()
    win.setMouseVisible(False)

    msg("Thanks, you've completed this task.You can now remove the headphones.\n\nPress any key to continue to the next task.")
# -----------------------
# START THE STUDY
# -----------------------
#msg("Hi, welcome to the study.\n\nFor this experiment you will be asked to complete several body-awareness related tasks. \n\nHit any key to continue.")

InstructionList='Instructions.png'
Instruct()
InstructionList='Instructions2.png'
Instruct()
InstructionList='Instructions3.png'
Instruct()
InstructionList='Instructions4.png'
Instruct()
InstructionList='Instructions5.png'
Instruct()
InstructionList='Instructions6.png'
Instruct()
InstructionList='Instructions7.png'
Instruct()
InstructionList='Instructions8.png'
Instruct()
InstructionList='Instructions9.png'
Instruct()
InstructionList='Instructions10.png'
Instruct()
InstructionList='Instructions11.png'
Instruct()
InstructionList='Instructions12.png'
Instruct()


#CALL FUNCTIONS----------------------------------------------------------------------------------------------------------
#
#------------------------------------------------------------------------------------------------------------------------


TestScale()
msg("Great...let's try that one more time \nPress any key to continue...")
TestScale()
msg("Great, let's start the experiment....As previously mentioned, for part of this study you will be asked to rate human faces for attractiveness.\n\nIn order to show faces of the appropriate gender you will be asked about your sexual orientation.\nAll of your responses will remain confidential.\n \n\n\n\n\n\n\n\n\n\n\n\n\nPress any key to continue...", "extresp")
win.flip()
thisResp=None
while thisResp is None:
    allKeys=event.waitKeys()
    for thisKey in allKeys:
        if thisKey in ['q','escape']:
            core.quit()
        else:
            thisResp = 1

genderRating()
Orientation()

#----------------------------------------------------------------------------------------------
# SET UP FOR ATTRACTIVENESS RATINGS 
#----------------------------------------------------------------------------------------------
MenAArray=[33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64]
MenNArray=[33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64]
WomenAArray=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32]
WomenNArray=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32]

AArray=[33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64]
NArray=[33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64]
#global AArray
#global NArray
#global MenAArray
#global MenNArray
#global WomenAArray
#global WomenNArray


if (gender==1 and SexualOrientation==0) or (gender==1 and SexualOrientation==1) or (gender==1 and SexualOrientation==2) or (gender==1 and SexualOrientation==3):
    AArray=WomenAArray
    NArray=WomenNArray
elif (gender==1 and SexualOrientation==4) or (gender==1 and SexualOrientation==5) or (gender==1 and SexualOrientation==6):
    AArray=MenAArray
    NArray=MenNArray
elif (gender==2 and SexualOrientation==0) or (gender==2 and SexualOrientation==1) or (gender==2 and SexualOrientation==2) or (gender==2 and SexualOrientation==3):
    AArray=MenAArray
    NArray=MenNArray
elif (gender==2 and SexualOrientation==4) or (gender==2 and SexualOrientation==5) or (gender==2 and SexualOrientation==6):
    AArray=WomenAArray
    NArray=WomenNArray

print AArray
print NArray

AttractiveRandomized = numpy.random.choice (AArray,32,replace=False)
NeutralRandomized = numpy.random.choice (NArray,32,replace=False)
AOutsidecounter=0
NOutsidecounter=0

#----------------------------------------------------------------------------------------------
# 
#----------------------------------------------------------------------------------------------



InstructionList='PracticeCircleTask.png'
Instruct()
runentraining()

InstructionList='MisattributionOfArousal.png'
Instruct()
runmisattribution()


AttractiveRandomized = numpy.random.choice (AArray,32,replace=False)
NeutralRandomized = numpy.random.choice (NArray,32,replace=False)
AOutsidecounter=0
NOutsidecounter=0


InstructionList='MisattributionOfArousal2.png'
Instruct()
runmisattribution2()

#------------------------------------------------------------------------------------------
#RESET FOR LOG  RESET FOR LOG   RESET FOR LOG
#RESET FOR LOG  RESET FOR LOG   RESET FOR LOG
#RESET FOR LOG  RESET FOR LOG   RESET FOR LOG
#------------------------------------------------------------------------------------------

Pulse_1='NONE'
Pulse_2='NONE'
Pulse_3='NONE'
Pulse_4='NONE'
Pulse_5='NONE'
Pulse_6='NONE'
Pulse_7='NONE'
Pulse_8='NONE'
blockNum =-1 


FoS_Response='none'
FoS_Accuracy=5
ConfidenceRating=-1
MoodRating=-1
ArousalRating=-1
#ATTRACTIVE PICTURES----------

PicturesDispayed='nope' #(which ones?)

N1=-1
N2=-1
A1=-1
A2=-1

Beep1Onset='NONE'
Beep2Onset='NONE'

#------------------------------------------------------------------------------------------
#
#------------------------------------------------------------------------------------------
InstructionList='Staircase.png'
Instruct()
runintegration()

#runheartbeat()
#experiment has ended
Condition = "End of Study"
dataFile.close()

msg("Thanks, you've completed this part of the study. Please alert the researcher.")



