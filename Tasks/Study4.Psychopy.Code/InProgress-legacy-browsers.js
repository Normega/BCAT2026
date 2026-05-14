/******************* 
 * Inprogress *
 *******************/


// store info about the experiment session:
let expName = 'InProgress';  // from the Builder filename that created this script
let expInfo = {
    'participant': '',
    'condition': '',
};

// Start code blocks for 'Before Experiment'
// Run 'Before Experiment' code from StartCode

var mean;
var squared_diff_sum;
var divisor;
var std_dev;
function std(numbers, is_sample = true) {
    /*
    Calculate the standard deviation of a list of numbers without using external libraries.

    Parameters:
    numbers: List of numbers to calculate standard deviation for
    is_sample: If True, calculates sample standard deviation (n-1),
    if False, calculates population standard deviation (n)

    Returns:
    float: The standard deviation of the numbers

    Raises:
    ValueError: If the input list is empty or has less than 2 items for sample std dev
    */
    var divisor, mean, squared_diff_sum, std_dev;
    if ((! numbers)) {
        throw new ValueError("Cannot calculate standard deviation of empty list");
    }
    if ((is_sample && (numbers.length < 2))) {
        throw new ValueError("Sample standard deviation requires at least 2 values");
    }
    mean = (util.sum(numbers) / numbers.length);
    squared_diff_sum = 0;
    for (var x, _pj_c = 0, _pj_a = numbers, _pj_b = _pj_a.length; (_pj_c < _pj_b); _pj_c += 1) {
        x = _pj_a[_pj_c];
        squared_diff_sum += Math.pow((x - mean), 2);
    }
    divisor = (is_sample ? (numbers.length - 1) : numbers.length);
    std_dev = Math.pow((squared_diff_sum / divisor), 0.5);
    return std_dev;
}

// init psychoJS:
const psychoJS = new PsychoJS({
  debug: true
});

// open window:
psychoJS.openWindow({
  fullscr: true,
  color: new util.Color([1.0, 1.0, 1.0]),
  units: 'height',
  waitBlanking: true,
  backgroundImage: '',
  backgroundFit: 'none',
});
// schedule the experiment:
psychoJS.schedule(psychoJS.gui.DlgFromDict({
  dictionary: expInfo,
  title: expName
}));

const flowScheduler = new Scheduler(psychoJS);
const dialogCancelScheduler = new Scheduler(psychoJS);
psychoJS.scheduleCondition(function() { return (psychoJS.gui.dialogComponent.button === 'OK'); }, flowScheduler, dialogCancelScheduler);

// flowScheduler gets run if the participants presses OK
flowScheduler.add(updateInfo); // add timeStamp
flowScheduler.add(experimentInit);
flowScheduler.add(StartRoutineBegin());
flowScheduler.add(StartRoutineEachFrame());
flowScheduler.add(StartRoutineEnd());
flowScheduler.add(Instruct2RoutineBegin());
flowScheduler.add(Instruct2RoutineEachFrame());
flowScheduler.add(Instruct2RoutineEnd());
const trials_2LoopScheduler = new Scheduler(psychoJS);
flowScheduler.add(trials_2LoopBegin(trials_2LoopScheduler));
flowScheduler.add(trials_2LoopScheduler);
flowScheduler.add(trials_2LoopEnd);








flowScheduler.add(CalcThresholdsRoutineBegin());
flowScheduler.add(CalcThresholdsRoutineEachFrame());
flowScheduler.add(CalcThresholdsRoutineEnd());
flowScheduler.add(TestTrialInstructRoutineBegin());
flowScheduler.add(TestTrialInstructRoutineEachFrame());
flowScheduler.add(TestTrialInstructRoutineEnd());
const testTrialsLoopScheduler = new Scheduler(psychoJS);
flowScheduler.add(testTrialsLoopBegin(testTrialsLoopScheduler));
flowScheduler.add(testTrialsLoopScheduler);
flowScheduler.add(testTrialsLoopEnd);





flowScheduler.add(CompleteInstructRoutineBegin());
flowScheduler.add(CompleteInstructRoutineEachFrame());
flowScheduler.add(CompleteInstructRoutineEnd());
flowScheduler.add(quitPsychoJS, '', true);

// quit if user presses Cancel in dialog box:
dialogCancelScheduler.add(quitPsychoJS, '', false);

psychoJS.start({
  expName: expName,
  expInfo: expInfo,
  resources: [
    // resources:
    {'name': 'justLabels.csv', 'path': 'justLabels.csv'},
    {'name': 'questDefinitionGeneral.csv', 'path': 'questDefinitionGeneral.csv'},
    {'name': 'justLabels.csv', 'path': 'justLabels.csv'},
    {'name': 'https://lib.pavlovia.org/vendors/jsQUEST.min.js', 'path': 'https://lib.pavlovia.org/vendors/jsQUEST.min.js'},
    {'name': 'images/SpeedImg.png', 'path': 'images/SpeedImg.png'},
    {'name': 'images/ConfidenceImg.png', 'path': 'images/ConfidenceImg.png'},
    {'name': 'images/ArousalImg.png', 'path': 'images/ArousalImg.png'},
  ]
});

psychoJS.experimentLogger.setLevel(core.Logger.ServerLevel.WARNING);


var currentLoop;
var frameDur;
async function updateInfo() {
  currentLoop = psychoJS.experiment;  // right now there are no loops
  expInfo['date'] = util.MonotonicClock.getDateStr();  // add a simple timestamp
  expInfo['expName'] = expName;
  expInfo['psychopyVersion'] = '2024.1.5';
  expInfo['OS'] = window.navigator.platform;


  // store frame rate of monitor if we can measure it successfully
  expInfo['frameRate'] = psychoJS.window.getActualFrameRate();
  if (typeof expInfo['frameRate'] !== 'undefined')
    frameDur = 1.0 / Math.round(expInfo['frameRate']);
  else
    frameDur = 1.0 / 60.0; // couldn't get a reliable measure so guess

  // add info from the URL:
  util.addInfoFromUrl(expInfo);
  

  
  psychoJS.experiment.dataFileName = (("." + "/") + `data/${expInfo["participant"]}_${expName}_${expInfo["date"]}`);
  psychoJS.experiment.field_separator = '\t';


  return Scheduler.Event.NEXT;
}


var StartClock;
var text;
var key_resp;
var circleSize;
var numBreaths;
var freshBreath;
var midPoint;
var n_highSalienceACC;
var n_lowSalienceACC;
var n_highSalienceDEC;
var n_lowSalienceDEC;
var highIntensitiesACC;
var lowIntensitiesACC;
var highIntensitiesDEC;
var lowIntensitiesDEC;
var highSEACC;
var lowSEACC;
var highSEDEC;
var lowSEDEC;
var highSalienceCIDEC;
var lowSalienceCIDEC;
var highSalienceCIACC;
var lowSalienceCIACC;
var highStopOKACC;
var lowStopOKACC;
var highStopOKDEC;
var lowStopOKDEC;
var highCIACC;
var lowCIACC;
var highCIDEC;
var lowCIDEC;
var highStepACC;
var lowStepACC;
var highStepDEC;
var lowStepDEC;
var lastHighLevelACC;
var lastLowLevelACC;
var lastHighLevelDEC;
var lastLowLevelDEC;
var T_hiAc;
var T_loAc;
var T_hiDe;
var T_loDe;
var Crit_Ac;
var Crit_De;
var Instruct2Clock;
var text_3;
var key_resp_3;
var CounterCodeClock;
var trialClock;
var Circle;
var judgebreathClock;
var kbChange;
var speedImage;
var judgeconfidenceClock;
var confidenceImage;
var confidenceSlider;
var judgearousal_2Clock;
var arousalImage;
var arousalSlider;
var CalcThresholdsClock;
var TestTrialInstructClock;
var text_2;
var key_resp_2;
var TestTrialClock;
var TestCircle;
var CompleteInstructClock;
var key_resp_4;
var text_4;
var globalClock;
var routineTimer;
async function experimentInit() {
  // Initialize components for Routine "Start"
  StartClock = new util.Clock();
  text = new visual.TextStim({
    win: psychoJS.window,
    name: 'text',
    text: 'Welcome to the Sensory Attention Task \n\nIn this task you will see a circle grow and shrink 4 times in a row. \n\nPlease try to sense if things are getting faster, slower, or staying the same speed.\n\nPress the <spacebar> to continue...',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.05,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color([(- 1.0), (- 1.0), (- 1.0)]),  opacity: undefined,
    depth: 0.0 
  });
  
  key_resp = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Run 'Begin Experiment' code from StartCode
  circleSize = 0.5;
  numBreaths = 4;
  freshBreath = true;
  midPoint = util.round((numBreaths / 2), 0);
  n_highSalienceACC = 0;
  n_lowSalienceACC = 0;
  n_highSalienceDEC = 0;
  n_lowSalienceDEC = 0;
  highIntensitiesACC = [];
  lowIntensitiesACC = [];
  highIntensitiesDEC = [];
  lowIntensitiesDEC = [];
  highSEACC = "";
  lowSEACC = "";
  highSEDEC = "";
  lowSEDEC = "";
  highSalienceCIDEC = "";
  lowSalienceCIDEC = "";
  highSalienceCIACC = "";
  lowSalienceCIACC = "";
  highStopOKACC = false;
  lowStopOKACC = false;
  highStopOKDEC = false;
  lowStopOKDEC = false;
  highCIACC = "";
  lowCIACC = "";
  highCIDEC = "";
  lowCIDEC = "";
  highStepACC = "";
  lowStepACC = "";
  highStepDEC = "";
  lowStepDEC = "";
  lastHighLevelACC = 0.5;
  lastLowLevelACC = 0.5;
  lastHighLevelDEC = 0.5;
  lastLowLevelDEC = 0.5;
  T_hiAc = "";
  T_loAc = "";
  T_hiDe = "";
  T_loDe = "";
  Crit_Ac = "";
  Crit_De = "";
  
  // Initialize components for Routine "Instruct2"
  Instruct2Clock = new util.Clock();
  text_3 = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_3',
    text: 'After each set of circles, you will be asked if things: slowed down (left arrow), stayed the same (up arrow), or sped up (right arrow). There will be a picture to remind you.\n\nYou will then be asked to rate your confidence in your judgment, and how energetic you feel. \n\nPress <spacebar> to begin...',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.05,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color([(- 1.0), (- 1.0), (- 1.0)]),  opacity: undefined,
    depth: 0.0 
  });
  
  key_resp_3 = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "CounterCode"
  CounterCodeClock = new util.Clock();
  // Initialize components for Routine "trial"
  trialClock = new util.Clock();
  Circle = new visual.Polygon({
    win: psychoJS.window, name: 'Circle', 
    edges: 100, size:circleSize,
    ori: 0.0, pos: [0, 0],
    anchor: 'center',
    lineWidth: 1.0, 
    colorSpace: 'rgb',
    lineColor: new util.Color([(- 1.0), (- 1.0), 0.0902]),
    fillColor: new util.Color([(- 1.0), (- 1.0), 1.0]),
    fillColor: [(- 1.0), (- 1.0), 1.0],
    opacity: undefined, depth: 0, interpolate: true,
  });
  
  // Initialize components for Routine "judgebreath"
  judgebreathClock = new util.Clock();
  kbChange = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  speedImage = new visual.ImageStim({
    win : psychoJS.window,
    name : 'speedImage', units : undefined, 
    image : 'images/SpeedImg.png', mask : undefined,
    anchor : 'center',
    ori : 0.0, pos : [0, 0], size : [1, 0.5],
    color : new util.Color([1,1,1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : -1.0 
  });
  // Initialize components for Routine "judgeconfidence"
  judgeconfidenceClock = new util.Clock();
  confidenceImage = new visual.ImageStim({
    win : psychoJS.window,
    name : 'confidenceImage', units : undefined, 
    image : 'images/ConfidenceImg.png', mask : undefined,
    anchor : 'center',
    ori : 0.0, pos : [0, 0], size : [1.0, 0.2],
    color : new util.Color([1,1,1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : 0.0 
  });
  confidenceSlider = new visual.Slider({
    win: psychoJS.window, name: 'confidenceSlider',
    startValue: 3,
    size: [0.8, 0.1], pos: [0, (- 0.3)], ori: 0.0, units: psychoJS.window.units,
    labels: [1, 2, 3, 4, 5, 6], fontSize: 0.05, ticks: [1, 2, 3, 4, 5, 6],
    granularity: 1.0, style: ["RATING", "TRIANGLE_MARKER"],
    color: new util.Color([(- 1.0), (- 1.0), (- 1.0)]), markerColor: new util.Color('Red'), lineColor: new util.Color([(- 1.0), (- 1.0), (- 1.0)]), 
    opacity: undefined, fontFamily: 'Open Sans', bold: true, italic: false, depth: -1, 
    flip: false,
  });
  
  // Initialize components for Routine "judgearousal_2"
  judgearousal_2Clock = new util.Clock();
  arousalImage = new visual.ImageStim({
    win : psychoJS.window,
    name : 'arousalImage', units : undefined, 
    image : 'images/ArousalImg.png', mask : undefined,
    anchor : 'center',
    ori : 0.0, pos : [0, 0], size : [1.0, 0.2],
    color : new util.Color([1,1,1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : 0.0 
  });
  arousalSlider = new visual.Slider({
    win: psychoJS.window, name: 'arousalSlider',
    startValue: 3,
    size: [0.8, 0.1], pos: [0, (- 0.3)], ori: 0.0, units: psychoJS.window.units,
    labels: [1, 2, 3, 4, 5, 6], fontSize: 0.05, ticks: [1, 2, 3, 4, 5, 6],
    granularity: 1.0, style: ["RATING", "TRIANGLE_MARKER"],
    color: new util.Color([(- 1.0), (- 1.0), (- 1.0)]), markerColor: new util.Color('Red'), lineColor: new util.Color([(- 1.0), (- 1.0), (- 1.0)]), 
    opacity: undefined, fontFamily: 'Open Sans', bold: true, italic: false, depth: -1, 
    flip: false,
  });
  
  // Initialize components for Routine "CalcThresholds"
  CalcThresholdsClock = new util.Clock();
  // Initialize components for Routine "TestTrialInstruct"
  TestTrialInstructClock = new util.Clock();
  text_2 = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_2',
    text: "Great! Let's do a few more rounds to see if we've measured correctly.\n\nPlease press <spacebar> to begin breathing along with the circle again.",
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.05,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color([(- 1.0), (- 1.0), (- 1.0)]),  opacity: undefined,
    depth: 0.0 
  });
  
  key_resp_2 = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "TestTrial"
  TestTrialClock = new util.Clock();
  TestCircle = new visual.Polygon({
    win: psychoJS.window, name: 'TestCircle', 
    edges: 100, size:circleSize,
    ori: 0.0, pos: [0, 0],
    anchor: 'center',
    lineWidth: 1.0, 
    colorSpace: 'rgb',
    lineColor: new util.Color([(- 1.0), (- 1.0), 0.0902]),
    fillColor: new util.Color([(- 1.0), (- 1.0), 1.0]),
    fillColor: [(- 1.0), (- 1.0), 1.0],
    opacity: undefined, depth: 0, interpolate: true,
  });
  
  // Initialize components for Routine "CompleteInstruct"
  CompleteInstructClock = new util.Clock();
  key_resp_4 = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  text_4 = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_4',
    text: "Great! You've completed the study.\n\nThe purpose of the study was to see whether your mood and wellbeing are related to how finely you can detect change in your senses. Some people focused on the visual circle, others focused on breathing along with the circle to see if that sense modality makes a diffference.\n\nThanks for your participation. You are done!\nPress <spacebar> to exit.",
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.05,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color([(- 1.0), (- 1.0), (- 1.0)]),  opacity: undefined,
    depth: -1.0 
  });
  
  // Create some handy timers
  globalClock = new util.Clock();  // to track the time since experiment started
  routineTimer = new util.CountdownTimer();  // to track time remaining of each (non-slip) routine
  
  return Scheduler.Event.NEXT;
}


var t;
var frameN;
var continueRoutine;
var _key_resp_allKeys;
var StartComponents;
function StartRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'Start' ---
    t = 0;
    StartClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    psychoJS.experiment.addData('Start.started', globalClock.getTime());
    key_resp.keys = undefined;
    key_resp.rt = undefined;
    _key_resp_allKeys = [];
    // keep track of which components have finished
    StartComponents = [];
    StartComponents.push(text);
    StartComponents.push(key_resp);
    
    StartComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}


function StartRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'Start' ---
    // get current time
    t = StartClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *text* updates
    if (t >= 0.0 && text.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text.tStart = t;  // (not accounting for frame time here)
      text.frameNStart = frameN;  // exact frame index
      
      text.setAutoDraw(true);
    }
    
    
    // *key_resp* updates
    if (t >= 0.0 && key_resp.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      key_resp.tStart = t;  // (not accounting for frame time here)
      key_resp.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { key_resp.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { key_resp.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { key_resp.clearEvents(); });
    }
    
    if (key_resp.status === PsychoJS.Status.STARTED) {
      let theseKeys = key_resp.getKeys({keyList: ['space'], waitRelease: false});
      _key_resp_allKeys = _key_resp_allKeys.concat(theseKeys);
      if (_key_resp_allKeys.length > 0) {
        key_resp.keys = _key_resp_allKeys[_key_resp_allKeys.length - 1].name;  // just the last key pressed
        key_resp.rt = _key_resp_allKeys[_key_resp_allKeys.length - 1].rt;
        key_resp.duration = _key_resp_allKeys[_key_resp_allKeys.length - 1].duration;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    StartComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function StartRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'Start' ---
    StartComponents.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    psychoJS.experiment.addData('Start.stopped', globalClock.getTime());
    // update the trial handler
    if (currentLoop instanceof MultiStairHandler) {
      currentLoop.addResponse(key_resp.corr, level);
    }
    psychoJS.experiment.addData('key_resp.keys', key_resp.keys);
    if (typeof key_resp.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('key_resp.rt', key_resp.rt);
        psychoJS.experiment.addData('key_resp.duration', key_resp.duration);
        routineTimer.reset();
        }
    
    key_resp.stop();
    // the Routine "Start" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var _key_resp_3_allKeys;
var Instruct2Components;
function Instruct2RoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'Instruct2' ---
    t = 0;
    Instruct2Clock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    psychoJS.experiment.addData('Instruct2.started', globalClock.getTime());
    key_resp_3.keys = undefined;
    key_resp_3.rt = undefined;
    _key_resp_3_allKeys = [];
    // keep track of which components have finished
    Instruct2Components = [];
    Instruct2Components.push(text_3);
    Instruct2Components.push(key_resp_3);
    
    Instruct2Components.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}


function Instruct2RoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'Instruct2' ---
    // get current time
    t = Instruct2Clock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *text_3* updates
    if (t >= 0.0 && text_3.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text_3.tStart = t;  // (not accounting for frame time here)
      text_3.frameNStart = frameN;  // exact frame index
      
      text_3.setAutoDraw(true);
    }
    
    
    // *key_resp_3* updates
    if (t >= 0.0 && key_resp_3.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      key_resp_3.tStart = t;  // (not accounting for frame time here)
      key_resp_3.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { key_resp_3.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { key_resp_3.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { key_resp_3.clearEvents(); });
    }
    
    if (key_resp_3.status === PsychoJS.Status.STARTED) {
      let theseKeys = key_resp_3.getKeys({keyList: ['space'], waitRelease: false});
      _key_resp_3_allKeys = _key_resp_3_allKeys.concat(theseKeys);
      if (_key_resp_3_allKeys.length > 0) {
        key_resp_3.keys = _key_resp_3_allKeys[_key_resp_3_allKeys.length - 1].name;  // just the last key pressed
        key_resp_3.rt = _key_resp_3_allKeys[_key_resp_3_allKeys.length - 1].rt;
        key_resp_3.duration = _key_resp_3_allKeys[_key_resp_3_allKeys.length - 1].duration;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    Instruct2Components.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function Instruct2RoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'Instruct2' ---
    Instruct2Components.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    psychoJS.experiment.addData('Instruct2.stopped', globalClock.getTime());
    // update the trial handler
    if (currentLoop instanceof MultiStairHandler) {
      currentLoop.addResponse(key_resp_3.corr, level);
    }
    psychoJS.experiment.addData('key_resp_3.keys', key_resp_3.keys);
    if (typeof key_resp_3.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('key_resp_3.rt', key_resp_3.rt);
        psychoJS.experiment.addData('key_resp_3.duration', key_resp_3.duration);
        routineTimer.reset();
        }
    
    key_resp_3.stop();
    // the Routine "Instruct2" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var trials_2;
function trials_2LoopBegin(trials_2LoopScheduler, snapshot) {
  return async function() {
    TrialHandler.fromSnapshot(snapshot); // update internal variables (.thisN etc) of the loop
    
    // set up handler to look after randomisation of conditions etc
    trials_2 = new TrialHandler({
      psychoJS: psychoJS,
      nReps: 1, method: TrialHandler.Method.RANDOM,
      extraInfo: expInfo, originPath: undefined,
      trialList: 'justLabels.csv',
      seed: undefined, name: 'trials_2'
    });
    psychoJS.experiment.addLoop(trials_2); // add the loop to the experiment
    currentLoop = trials_2;  // we're now the current loop
    
    // Schedule all the trials in the trialList:
    trials_2.forEach(function() {
      snapshot = trials_2.getSnapshot();
    
      trials_2LoopScheduler.add(importConditions(snapshot));
      trials_2LoopScheduler.add(CounterCodeRoutineBegin(snapshot));
      trials_2LoopScheduler.add(CounterCodeRoutineEachFrame());
      trials_2LoopScheduler.add(CounterCodeRoutineEnd(snapshot));
      const trialsLoopScheduler = new Scheduler(psychoJS);
      trials_2LoopScheduler.add(trialsLoopBegin(trialsLoopScheduler, snapshot));
      trials_2LoopScheduler.add(trialsLoopScheduler);
      trials_2LoopScheduler.add(trialsLoopEnd);
      trials_2LoopScheduler.add(trials_2LoopEndIteration(trials_2LoopScheduler, snapshot));
    });
    
    return Scheduler.Event.NEXT;
  }
}


var trialsConditions;
var trials;
function trialsLoopBegin(trialsLoopScheduler, snapshot) {
  return async function() {
    // setup a MultiStairTrialHandler
    trialsConditions = TrialHandler.importConditions(psychoJS.serverManager, 'questDefinitionGeneral.csv');
    trials = new data.MultiStairHandler({stairType:MultiStairHandler.StaircaseType.QUEST, 
      psychoJS: psychoJS,
      name: 'trials',
      varName: 'intensity',
      nTrials: 10.0,
      conditions: trialsConditions,
      method: TrialHandler.Method.RANDOM
    });
    psychoJS.experiment.addLoop(trials); // add the loop to the experiment
    currentLoop = trials;  // we're now the current loop
    // Schedule all the trials in the trialList:
    for (const thisQuestLoop of trials) {
      trialsLoopScheduler.add(trialsLoopBeginIteration(snapshot));
      snapshot = trials.getSnapshot();
      trialsLoopScheduler.add(importConditions(snapshot));
      trialsLoopScheduler.add(trialRoutineBegin(snapshot));
      trialsLoopScheduler.add(trialRoutineEachFrame());
      trialsLoopScheduler.add(trialRoutineEnd());
      snapshot = trials.getSnapshot();
      trialsLoopScheduler.add(importConditions(snapshot));
      trialsLoopScheduler.add(judgebreathRoutineBegin(snapshot));
      trialsLoopScheduler.add(judgebreathRoutineEachFrame());
      trialsLoopScheduler.add(judgebreathRoutineEnd());
      snapshot = trials.getSnapshot();
      trialsLoopScheduler.add(importConditions(snapshot));
      trialsLoopScheduler.add(judgeconfidenceRoutineBegin(snapshot));
      trialsLoopScheduler.add(judgeconfidenceRoutineEachFrame());
      trialsLoopScheduler.add(judgeconfidenceRoutineEnd());
      snapshot = trials.getSnapshot();
      trialsLoopScheduler.add(importConditions(snapshot));
      trialsLoopScheduler.add(judgearousal_2RoutineBegin(snapshot));
      trialsLoopScheduler.add(judgearousal_2RoutineEachFrame());
      trialsLoopScheduler.add(judgearousal_2RoutineEnd());
    // then iterate over this loop (trials)
    trialsLoopScheduler.add(trialsLoopEndIteration(trialsLoopScheduler, snapshot));
    }
    
    return Scheduler.Event.NEXT;
  }
}


var level;
function trialsLoopBeginIteration(snapshot) {
  return async function() {
    // ------Prepare for next entry------
    level = trials.intensity;

    return Scheduler.Event.NEXT;
  }
}


async function trialsLoopEnd() {
  // terminate loop
  psychoJS.experiment.removeLoop(trials);
  // update the current loop from the ExperimentHandler
  if (psychoJS.experiment._unfinishedLoops.length>0)
    currentLoop = psychoJS.experiment._unfinishedLoops.at(-1);
  else
    currentLoop = psychoJS.experiment;  // so we use addData from the experiment
  return Scheduler.Event.NEXT;
}


function trialsLoopEndIteration(scheduler, snapshot) {
  // ------Prepare for next entry------
  return async function () {
    if (typeof snapshot !== 'undefined') {
      // ------Check if user ended loop early------
      if (snapshot.finished) {
        // Check for and save orphaned data
        if (psychoJS.experiment.isEntryEmpty()) {
          psychoJS.experiment.nextEntry(snapshot);
        }
        scheduler.stop();
      } else {
        psychoJS.experiment.nextEntry(snapshot);
      }
    return Scheduler.Event.NEXT;
    }
  };
}


async function trials_2LoopEnd() {
  // terminate loop
  psychoJS.experiment.removeLoop(trials_2);
  // update the current loop from the ExperimentHandler
  if (psychoJS.experiment._unfinishedLoops.length>0)
    currentLoop = psychoJS.experiment._unfinishedLoops.at(-1);
  else
    currentLoop = psychoJS.experiment;  // so we use addData from the experiment
  return Scheduler.Event.NEXT;
}


function trials_2LoopEndIteration(scheduler, snapshot) {
  // ------Prepare for next entry------
  return async function () {
    if (typeof snapshot !== 'undefined') {
      // ------Check if user ended loop early------
      if (snapshot.finished) {
        // Check for and save orphaned data
        if (psychoJS.experiment.isEntryEmpty()) {
          psychoJS.experiment.nextEntry(snapshot);
        }
        scheduler.stop();
      } else {
        psychoJS.experiment.nextEntry(snapshot);
      }
    return Scheduler.Event.NEXT;
    }
  };
}


var testTrials;
function testTrialsLoopBegin(testTrialsLoopScheduler, snapshot) {
  return async function() {
    TrialHandler.fromSnapshot(snapshot); // update internal variables (.thisN etc) of the loop
    
    // set up handler to look after randomisation of conditions etc
    testTrials = new TrialHandler({
      psychoJS: psychoJS,
      nReps: 2, method: TrialHandler.Method.FULLRANDOM,
      extraInfo: expInfo, originPath: undefined,
      trialList: 'justLabels.csv',
      seed: undefined, name: 'testTrials'
    });
    psychoJS.experiment.addLoop(testTrials); // add the loop to the experiment
    currentLoop = testTrials;  // we're now the current loop
    
    // Schedule all the trials in the trialList:
    testTrials.forEach(function() {
      snapshot = testTrials.getSnapshot();
    
      testTrialsLoopScheduler.add(importConditions(snapshot));
      testTrialsLoopScheduler.add(TestTrialRoutineBegin(snapshot));
      testTrialsLoopScheduler.add(TestTrialRoutineEachFrame());
      testTrialsLoopScheduler.add(TestTrialRoutineEnd(snapshot));
      testTrialsLoopScheduler.add(judgebreathRoutineBegin(snapshot));
      testTrialsLoopScheduler.add(judgebreathRoutineEachFrame());
      testTrialsLoopScheduler.add(judgebreathRoutineEnd(snapshot));
      testTrialsLoopScheduler.add(judgeconfidenceRoutineBegin(snapshot));
      testTrialsLoopScheduler.add(judgeconfidenceRoutineEachFrame());
      testTrialsLoopScheduler.add(judgeconfidenceRoutineEnd(snapshot));
      testTrialsLoopScheduler.add(judgearousal_2RoutineBegin(snapshot));
      testTrialsLoopScheduler.add(judgearousal_2RoutineEachFrame());
      testTrialsLoopScheduler.add(judgearousal_2RoutineEnd(snapshot));
      testTrialsLoopScheduler.add(testTrialsLoopEndIteration(testTrialsLoopScheduler, snapshot));
    });
    
    return Scheduler.Event.NEXT;
  }
}


async function testTrialsLoopEnd() {
  // terminate loop
  psychoJS.experiment.removeLoop(testTrials);
  // update the current loop from the ExperimentHandler
  if (psychoJS.experiment._unfinishedLoops.length>0)
    currentLoop = psychoJS.experiment._unfinishedLoops.at(-1);
  else
    currentLoop = psychoJS.experiment;  // so we use addData from the experiment
  return Scheduler.Event.NEXT;
}


function testTrialsLoopEndIteration(scheduler, snapshot) {
  // ------Prepare for next entry------
  return async function () {
    if (typeof snapshot !== 'undefined') {
      // ------Check if user ended loop early------
      if (snapshot.finished) {
        // Check for and save orphaned data
        if (psychoJS.experiment.isEntryEmpty()) {
          psychoJS.experiment.nextEntry(snapshot);
        }
        scheduler.stop();
      } else {
        psychoJS.experiment.nextEntry(snapshot);
      }
    return Scheduler.Event.NEXT;
    }
  };
}


var trialNum;
var CounterCodeComponents;
function CounterCodeRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'CounterCode' ---
    t = 0;
    CounterCodeClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    psychoJS.experiment.addData('CounterCode.started', globalClock.getTime());
    // Run 'Begin Routine' code from code_6
    trialNum = 0;
    
    // keep track of which components have finished
    CounterCodeComponents = [];
    
    CounterCodeComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}


function CounterCodeRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'CounterCode' ---
    // get current time
    t = CounterCodeClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    CounterCodeComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function CounterCodeRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'CounterCode' ---
    CounterCodeComponents.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    psychoJS.experiment.addData('CounterCode.stopped', globalClock.getTime());
    // the Routine "CounterCode" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var cycleDuration;
var randomChange;
var direction;
var correctAns;
var changeVal;
var breathCount;
var changeAmount;
var trialComponents;
function trialRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'trial' ---
    t = 0;
    trialClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    psychoJS.experiment.addData('trial.started', globalClock.getTime());
    // Run 'Begin Routine' code from code
    cycleDuration = 4;
    randomChange = Math.random();
    trialNum += 1;
    if ((changeDirection === "Acc")) {
        if ((randomChange <= 0.8)) {
            direction = (- 1);
            correctAns = "right";
        } else {
            direction = 0;
            correctAns = "up";
        }
    } else {
        if ((randomChange <= 0.8)) {
            direction = 1;
            correctAns = "left";
        } else {
            direction = 0;
            correctAns = "up";
        }
    }
    changeVal = (1 + (direction * level));
    breathCount = 0;
    freshBreath = true;
    changeAmount = Math.pow(changeVal, (1 / (numBreaths - 1)));
    trialClock = new util.Clock();
    
    // keep track of which components have finished
    trialComponents = [];
    trialComponents.push(Circle);
    
    trialComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}


var phase;
function trialRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'trial' ---
    // get current time
    t = trialClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *Circle* updates
    if (t >= 0.0 && Circle.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      Circle.tStart = t;  // (not accounting for frame time here)
      Circle.frameNStart = frameN;  // exact frame index
      
      Circle.setAutoDraw(true);
    }
    
    // Run 'Each Frame' code from code
    t = trialClock.getTime();
    phase = ((t % cycleDuration) / cycleDuration);
    if ((phase <= 0.5)) {
        circleSize = (0.1 + ((0.2 * phase) * 2));
        if ((freshBreath === false)) {
            breathCount += 1;
            if ((changeSalience === 0)) {
                cycleDuration *= changeAmount;
            }
            if ((changeSalience === 1)) {
                if ((breathCount === midPoint)) {
                    cycleDuration *= changeVal;
                }
            }
            trialClock = new util.Clock();
            freshBreath = true;
            if ((breathCount >= numBreaths)) {
                continueRoutine = false;
            }
        }
    } else {
        circleSize = (0.1 + (0.2 * (1 - ((phase - 0.5) * 2))));
        if ((freshBreath === true)) {
            freshBreath = false;
        }
    }
    Circle.size = circleSize;
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    trialComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function trialRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'trial' ---
    trialComponents.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    psychoJS.experiment.addData('trial.stopped', globalClock.getTime());
    // Run 'End Routine' code from code
    console.log(trialNum);
    psychoJS.experiment.addData("Condition", thisCondition);
    psychoJS.experiment.addData("Salience", changeSalience);
    psychoJS.experiment.addData("Level", level);
    psychoJS.experiment.addData("Direction", direction);
    psychoJS.experiment.addData("DirectionLabel", changeDirection);
    psychoJS.experiment.addData("Correct", correctAns);
    if ((thisCondition === "highSalienceAcc")) {
        n_highSalienceACC += 1;
        highIntensitiesACC.push(level);
        if ((n_highSalienceACC > 2)) {
            highSEACC = (std(highIntensitiesACC) / Math.pow(n_highSalienceACC, 0.5));
            highSalienceCIACC = (1.645 * highSEACC);
            highStepACC = Math.abs((level - lastHighLevelACC));
            lastHighLevelACC = level;
            highStopOKACC = (highSalienceCIACC < (highStepACC / 2));
        }
    } else {
        if ((thisCondition === "lowSalienceAcc")) {
            n_lowSalienceACC += 1;
            lowIntensitiesACC.push(level);
            if ((n_lowSalienceACC > 2)) {
                lowSEACC = (std(lowIntensitiesACC) / Math.pow(n_lowSalienceACC, 0.5));
                lowSalienceCIACC = (1.645 * lowSEACC);
                lowStepACC = Math.abs((level - lastLowLevelACC));
                lastLowLevelACC = level;
                lowStopOKACC = (lowSalienceCIACC < (lowStepACC / 2));
            }
        } else {
            if ((thisCondition === "highSalienceDec")) {
                n_highSalienceDEC += 1;
                highIntensitiesDEC.push(level);
                if ((n_highSalienceDEC > 2)) {
                    highSEDEC = (std(highIntensitiesDEC) / Math.pow(n_highSalienceDEC, 0.5));
                    highSalienceCIDEC = (1.645 * highSEDEC);
                    highStepDEC = Math.abs((level - lastHighLevelDEC));
                    lastHighLevelDEC = level;
                    highStopOKDEC = (highSalienceCIDEC < (highStepDEC / 2));
                }
            } else {
                n_lowSalienceDEC += 1;
                lowIntensitiesDEC.push(level);
                if ((n_lowSalienceDEC > 2)) {
                    lowSEDEC = (std(lowIntensitiesDEC) / Math.pow(n_lowSalienceDEC, 0.5));
                    lowSalienceCIDEC = (1.645 * lowSEDEC);
                    lowStepDEC = Math.abs((level - lastLowLevelDEC));
                    lastLowLevelDEC = level;
                    lowStopOKDEC = (lowSalienceCIDEC < (lowStepDEC / 2));
                }
            }
        }
    }
    psychoJS.experiment.addData("highCIACC", highSalienceCIACC);
    psychoJS.experiment.addData("lowCIACC", lowSalienceCIACC);
    psychoJS.experiment.addData("highCIDEC", highSalienceCIDEC);
    psychoJS.experiment.addData("lowCIDEC", lowSalienceCIDEC);
    psychoJS.experiment.addData("highStepACC", highStepACC);
    psychoJS.experiment.addData("lowStepACC", lowStepACC);
    psychoJS.experiment.addData("highStepDEC", highStepDEC);
    psychoJS.experiment.addData("lowStepDEC", lowStepDEC);
    psychoJS.experiment.addData("highStopOKACC", highStopOKACC);
    psychoJS.experiment.addData("lowStopOKACC", lowStopOKACC);
    psychoJS.experiment.addData("highStopOKDEC", highStopOKDEC);
    psychoJS.experiment.addData("lowStopOKDEC", lowStopOKDEC);
    if ((trialNum === 10)) {
        trials.finished = true;
    }
    
    // the Routine "trial" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var _kbChange_allKeys;
var judgebreathComponents;
function judgebreathRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'judgebreath' ---
    t = 0;
    judgebreathClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    psychoJS.experiment.addData('judgebreath.started', globalClock.getTime());
    kbChange.keys = undefined;
    kbChange.rt = undefined;
    _kbChange_allKeys = [];
    // Run 'Begin Routine' code from code_5
    psychoJS.eventManager.clearEvents("keyboard");
    
    // keep track of which components have finished
    judgebreathComponents = [];
    judgebreathComponents.push(kbChange);
    judgebreathComponents.push(speedImage);
    
    judgebreathComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}


var _pj;
var keys;
var response;
function judgebreathRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'judgebreath' ---
    // get current time
    t = judgebreathClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *kbChange* updates
    if (t >= 0.0 && kbChange.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      kbChange.tStart = t;  // (not accounting for frame time here)
      kbChange.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { kbChange.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { kbChange.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { kbChange.clearEvents(); });
    }
    
    if (kbChange.status === PsychoJS.Status.STARTED) {
      let theseKeys = kbChange.getKeys({keyList: ['left', 'up', 'right'], waitRelease: false});
      _kbChange_allKeys = _kbChange_allKeys.concat(theseKeys);
      if (_kbChange_allKeys.length > 0) {
        kbChange.keys = _kbChange_allKeys[_kbChange_allKeys.length - 1].name;  // just the last key pressed
        kbChange.rt = _kbChange_allKeys[_kbChange_allKeys.length - 1].rt;
        kbChange.duration = _kbChange_allKeys[_kbChange_allKeys.length - 1].duration;
        // was this correct?
        if (kbChange.keys == correctAns) {
            kbChange.corr = 1;
        } else {
            kbChange.corr = 0;
        }
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    
    // *speedImage* updates
    if (t >= 0.0 && speedImage.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      speedImage.tStart = t;  // (not accounting for frame time here)
      speedImage.frameNStart = frameN;  // exact frame index
      
      speedImage.setAutoDraw(true);
    }
    
    // Run 'Each Frame' code from code_5
    var _pj;
    function _pj_snippets(container) {
        function in_es6(left, right) {
            if (((right instanceof Array) || ((typeof right) === "string"))) {
                return (right.indexOf(left) > (- 1));
            } else {
                if (((right instanceof Map) || (right instanceof Set) || (right instanceof WeakMap) || (right instanceof WeakSet))) {
                    return right.has(left);
                } else {
                    return (left in right);
                }
            }
        }
        container["in_es6"] = in_es6;
        return container;
    }
    _pj = {};
    _pj_snippets(_pj);
    keys = psychoJS.eventManager.getKeys();
    if (keys.length) {
        if (_pj.in_es6("left", keys)) {
            response = "left";
        } else {
            if (_pj.in_es6("right", keys)) {
                response = "right";
            } else {
                if (_pj.in_es6("up", keys)) {
                    response = "up";
                }
            }
        }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    judgebreathComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function judgebreathRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'judgebreath' ---
    judgebreathComponents.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    psychoJS.experiment.addData('judgebreath.stopped', globalClock.getTime());
    // was no response the correct answer?!
    if (kbChange.keys === undefined) {
      if (['None','none',undefined].includes(correctAns)) {
         kbChange.corr = 1;  // correct non-response
      } else {
         kbChange.corr = 0;  // failed to respond (incorrectly)
      }
    }
    // store data for current loop
    // update the trial handler
    if (currentLoop instanceof MultiStairHandler) {
      currentLoop.addResponse(kbChange.corr, level);
    }
    psychoJS.experiment.addData('kbChange.keys', kbChange.keys);
    psychoJS.experiment.addData('kbChange.corr', kbChange.corr);
    if (typeof kbChange.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('kbChange.rt', kbChange.rt);
        psychoJS.experiment.addData('kbChange.duration', kbChange.duration);
        routineTimer.reset();
        }
    
    kbChange.stop();
    // Run 'End Routine' code from code_5
    psychoJS.experiment.addData("Response", response);
    if ((correctAns === response)) {
        psychoJS.experiment.addData("Accuracy", 1);
    } else {
        psychoJS.experiment.addData("Accuracy", 0);
    }
    
    // the Routine "judgebreath" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var judgeconfidenceComponents;
function judgeconfidenceRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'judgeconfidence' ---
    t = 0;
    judgeconfidenceClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    psychoJS.experiment.addData('judgeconfidence.started', globalClock.getTime());
    confidenceSlider.reset()
    // Run 'Begin Routine' code from code_3
    psychoJS.eventManager.clearEvents("keyboard");
    confidenceSlider.markerPos = 3;
    
    // keep track of which components have finished
    judgeconfidenceComponents = [];
    judgeconfidenceComponents.push(confidenceImage);
    judgeconfidenceComponents.push(confidenceSlider);
    
    judgeconfidenceComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}


function judgeconfidenceRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'judgeconfidence' ---
    // get current time
    t = judgeconfidenceClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *confidenceImage* updates
    if (t >= 0.0 && confidenceImage.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      confidenceImage.tStart = t;  // (not accounting for frame time here)
      confidenceImage.frameNStart = frameN;  // exact frame index
      
      confidenceImage.setAutoDraw(true);
    }
    
    
    // *confidenceSlider* updates
    if (t >= 0.0 && confidenceSlider.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      confidenceSlider.tStart = t;  // (not accounting for frame time here)
      confidenceSlider.frameNStart = frameN;  // exact frame index
      
      confidenceSlider.setAutoDraw(true);
    }
    
    
    // Check confidenceSlider for response to end Routine
    if (confidenceSlider.getRating() !== undefined && confidenceSlider.status === PsychoJS.Status.STARTED) {
      continueRoutine = false; }
    // Run 'Each Frame' code from code_3
    var _pj;
    function _pj_snippets(container) {
        function in_es6(left, right) {
            if (((right instanceof Array) || ((typeof right) === "string"))) {
                return (right.indexOf(left) > (- 1));
            } else {
                if (((right instanceof Map) || (right instanceof Set) || (right instanceof WeakMap) || (right instanceof WeakSet))) {
                    return right.has(left);
                } else {
                    return (left in right);
                }
            }
        }
        container["in_es6"] = in_es6;
        return container;
    }
    _pj = {};
    _pj_snippets(_pj);
    keys = psychoJS.eventManager.getKeys();
    if (keys.length) {
        if (_pj.in_es6("left", keys)) {
            confidenceSlider.markerPos = (confidenceSlider.markerPos - 1);
        } else {
            if (_pj.in_es6("right", keys)) {
                confidenceSlider.markerPos = (confidenceSlider.markerPos + 1);
            } else {
                if (_pj.in_es6("return", keys)) {
                    confidenceSlider.rating = confidenceSlider.markerPos;
                    continueRoutine = false;
                } else {
                    if (_pj.in_es6("enter", keys)) {
                        confidenceSlider.rating = confidenceSlider.markerPos;
                        continueRoutine = false;
                    } else {
                        if (_pj.in_es6("space", keys)) {
                            confidenceSlider.rating = confidenceSlider.markerPos;
                            continueRoutine = false;
                        }
                    }
                }
            }
        }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    judgeconfidenceComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function judgeconfidenceRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'judgeconfidence' ---
    judgeconfidenceComponents.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    psychoJS.experiment.addData('judgeconfidence.stopped', globalClock.getTime());
    psychoJS.experiment.addData('confidenceSlider.response', confidenceSlider.getRating());
    psychoJS.experiment.addData('confidenceSlider.rt', confidenceSlider.getRT());
    // Run 'End Routine' code from code_3
    psychoJS.experiment.addData("JudgeRating", confidenceSlider.markerPos);
    
    // the Routine "judgeconfidence" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var judgearousal_2Components;
function judgearousal_2RoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'judgearousal_2' ---
    t = 0;
    judgearousal_2Clock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    psychoJS.experiment.addData('judgearousal_2.started', globalClock.getTime());
    arousalSlider.reset()
    // Run 'Begin Routine' code from code_4
    psychoJS.eventManager.clearEvents("keyboard");
    arousalSlider.markerPos = 3;
    
    // keep track of which components have finished
    judgearousal_2Components = [];
    judgearousal_2Components.push(arousalImage);
    judgearousal_2Components.push(arousalSlider);
    
    judgearousal_2Components.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}


function judgearousal_2RoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'judgearousal_2' ---
    // get current time
    t = judgearousal_2Clock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *arousalImage* updates
    if (t >= 0.0 && arousalImage.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      arousalImage.tStart = t;  // (not accounting for frame time here)
      arousalImage.frameNStart = frameN;  // exact frame index
      
      arousalImage.setAutoDraw(true);
    }
    
    
    // *arousalSlider* updates
    if (t >= 0.0 && arousalSlider.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      arousalSlider.tStart = t;  // (not accounting for frame time here)
      arousalSlider.frameNStart = frameN;  // exact frame index
      
      arousalSlider.setAutoDraw(true);
    }
    
    
    // Check arousalSlider for response to end Routine
    if (arousalSlider.getRating() !== undefined && arousalSlider.status === PsychoJS.Status.STARTED) {
      continueRoutine = false; }
    // Run 'Each Frame' code from code_4
    var _pj;
    function _pj_snippets(container) {
        function in_es6(left, right) {
            if (((right instanceof Array) || ((typeof right) === "string"))) {
                return (right.indexOf(left) > (- 1));
            } else {
                if (((right instanceof Map) || (right instanceof Set) || (right instanceof WeakMap) || (right instanceof WeakSet))) {
                    return right.has(left);
                } else {
                    return (left in right);
                }
            }
        }
        container["in_es6"] = in_es6;
        return container;
    }
    _pj = {};
    _pj_snippets(_pj);
    keys = psychoJS.eventManager.getKeys();
    if (keys.length) {
        if (_pj.in_es6("left", keys)) {
            arousalSlider.markerPos = (arousalSlider.markerPos - 1);
        } else {
            if (_pj.in_es6("right", keys)) {
                arousalSlider.markerPos = (arousalSlider.markerPos + 1);
            } else {
                if (_pj.in_es6("return", keys)) {
                    confidenceSlider.rating = confidenceSlider.markerPos;
                    continueRoutine = false;
                } else {
                    if (_pj.in_es6("enter", keys)) {
                        confidenceSlider.rating = confidenceSlider.markerPos;
                        continueRoutine = false;
                    } else {
                        if (_pj.in_es6("space", keys)) {
                            confidenceSlider.rating = confidenceSlider.markerPos;
                            continueRoutine = false;
                        }
                    }
                }
            }
        }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    judgearousal_2Components.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function judgearousal_2RoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'judgearousal_2' ---
    judgearousal_2Components.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    psychoJS.experiment.addData('judgearousal_2.stopped', globalClock.getTime());
    psychoJS.experiment.addData('arousalSlider.response', arousalSlider.getRating());
    psychoJS.experiment.addData('arousalSlider.rt', arousalSlider.getRT());
    // Run 'End Routine' code from code_4
    psychoJS.experiment.addData("ArousalRating", arousalSlider.markerPos);
    
    // the Routine "judgearousal_2" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var CalcThresholdsComponents;
function CalcThresholdsRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'CalcThresholds' ---
    t = 0;
    CalcThresholdsClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    psychoJS.experiment.addData('CalcThresholds.started', globalClock.getTime());
    // keep track of which components have finished
    CalcThresholdsComponents = [];
    
    CalcThresholdsComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}


function CalcThresholdsRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'CalcThresholds' ---
    // get current time
    t = CalcThresholdsClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    CalcThresholdsComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function CalcThresholdsRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'CalcThresholds' ---
    CalcThresholdsComponents.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    psychoJS.experiment.addData('CalcThresholds.stopped', globalClock.getTime());
    // Run 'End Routine' code from code_2
    T_hiAc = ((highIntensitiesACC.slice((- 2))[0] + highIntensitiesACC.slice((- 1))[0]) / 2);
    T_loAc = ((lowIntensitiesACC.slice((- 2))[0] + lowIntensitiesACC.slice((- 1))[0]) / 2);
    T_hiDe = ((highIntensitiesDEC.slice((- 2))[0] + highIntensitiesDEC.slice((- 1))[0]) / 2);
    T_loDe = ((lowIntensitiesDEC.slice((- 2))[0] + lowIntensitiesDEC.slice((- 1))[0]) / 2);
    console.log(T_hiAc);
    console.log(T_loAc);
    console.log(T_hiDe);
    console.log(T_loDe);
    Crit_Ac = ((T_hiAc + T_loAc) / 2);
    Crit_De = ((T_hiDe + T_loDe) / 2);
    
    // the Routine "CalcThresholds" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var _key_resp_2_allKeys;
var TestTrialInstructComponents;
function TestTrialInstructRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'TestTrialInstruct' ---
    t = 0;
    TestTrialInstructClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    psychoJS.experiment.addData('TestTrialInstruct.started', globalClock.getTime());
    key_resp_2.keys = undefined;
    key_resp_2.rt = undefined;
    _key_resp_2_allKeys = [];
    // keep track of which components have finished
    TestTrialInstructComponents = [];
    TestTrialInstructComponents.push(text_2);
    TestTrialInstructComponents.push(key_resp_2);
    
    TestTrialInstructComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}


function TestTrialInstructRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'TestTrialInstruct' ---
    // get current time
    t = TestTrialInstructClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *text_2* updates
    if (t >= 0.0 && text_2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text_2.tStart = t;  // (not accounting for frame time here)
      text_2.frameNStart = frameN;  // exact frame index
      
      text_2.setAutoDraw(true);
    }
    
    
    // *key_resp_2* updates
    if (t >= 0.0 && key_resp_2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      key_resp_2.tStart = t;  // (not accounting for frame time here)
      key_resp_2.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { key_resp_2.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { key_resp_2.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { key_resp_2.clearEvents(); });
    }
    
    if (key_resp_2.status === PsychoJS.Status.STARTED) {
      let theseKeys = key_resp_2.getKeys({keyList: ['space'], waitRelease: false});
      _key_resp_2_allKeys = _key_resp_2_allKeys.concat(theseKeys);
      if (_key_resp_2_allKeys.length > 0) {
        key_resp_2.keys = _key_resp_2_allKeys[_key_resp_2_allKeys.length - 1].name;  // just the last key pressed
        key_resp_2.rt = _key_resp_2_allKeys[_key_resp_2_allKeys.length - 1].rt;
        key_resp_2.duration = _key_resp_2_allKeys[_key_resp_2_allKeys.length - 1].duration;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    TestTrialInstructComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function TestTrialInstructRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'TestTrialInstruct' ---
    TestTrialInstructComponents.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    psychoJS.experiment.addData('TestTrialInstruct.stopped', globalClock.getTime());
    // update the trial handler
    if (currentLoop instanceof MultiStairHandler) {
      currentLoop.addResponse(key_resp_2.corr, level);
    }
    psychoJS.experiment.addData('key_resp_2.keys', key_resp_2.keys);
    if (typeof key_resp_2.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('key_resp_2.rt', key_resp_2.rt);
        psychoJS.experiment.addData('key_resp_2.duration', key_resp_2.duration);
        routineTimer.reset();
        }
    
    key_resp_2.stop();
    // the Routine "TestTrialInstruct" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var TestTrialComponents;
function TestTrialRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'TestTrial' ---
    t = 0;
    TestTrialClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    psychoJS.experiment.addData('TestTrial.started', globalClock.getTime());
    // Run 'Begin Routine' code from testTrialCode
    cycleDuration = 4;
    if ((changeDirection === "Acc")) {
        level = Crit_Ac;
        direction = (- 1);
        correctAns = "right";
    } else {
        level = Crit_De;
        direction = 1;
        correctAns = "left";
    }
    changeVal = (1 + (direction * level));
    breathCount = 0;
    freshBreath = true;
    changeAmount = Math.pow(changeVal, (1 / (numBreaths - 1)));
    trialClock = new util.Clock();
    
    // keep track of which components have finished
    TestTrialComponents = [];
    TestTrialComponents.push(TestCircle);
    
    TestTrialComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}


function TestTrialRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'TestTrial' ---
    // get current time
    t = TestTrialClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *TestCircle* updates
    if (t >= 0.0 && TestCircle.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      TestCircle.tStart = t;  // (not accounting for frame time here)
      TestCircle.frameNStart = frameN;  // exact frame index
      
      TestCircle.setAutoDraw(true);
    }
    
    // Run 'Each Frame' code from testTrialCode
    t = trialClock.getTime();
    phase = ((t % cycleDuration) / cycleDuration);
    if ((phase <= 0.5)) {
        circleSize = (0.1 + ((0.2 * phase) * 2));
        if ((freshBreath === false)) {
            breathCount += 1;
            if ((changeSalience === 0)) {
                cycleDuration *= changeAmount;
            }
            if ((changeSalience === 1)) {
                if ((breathCount === midPoint)) {
                    cycleDuration *= changeVal;
                }
            }
            trialClock = new util.Clock();
            freshBreath = true;
            if ((breathCount >= numBreaths)) {
                continueRoutine = false;
            }
        }
    } else {
        circleSize = (0.1 + (0.2 * (1 - ((phase - 0.5) * 2))));
        if ((freshBreath === true)) {
            freshBreath = false;
        }
    }
    TestCircle.size = circleSize;
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    TestTrialComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function TestTrialRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'TestTrial' ---
    TestTrialComponents.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    psychoJS.experiment.addData('TestTrial.stopped', globalClock.getTime());
    // Run 'End Routine' code from testTrialCode
    psychoJS.experiment.addData("Condition", thisCondition);
    psychoJS.experiment.addData("Salience", changeSalience);
    psychoJS.experiment.addData("Level", level);
    psychoJS.experiment.addData("Direction", direction);
    psychoJS.experiment.addData("DirectionLabel", changeDirection);
    psychoJS.experiment.addData("Correct", correctAns);
    psychoJS.experiment.addData("Crit_Ac", Crit_Ac);
    psychoJS.experiment.addData("Crit_De", Crit_De);
    if ((thisCondition === "highSalienceAcc")) {
        n_highSalienceACC += 1;
        highIntensitiesACC.push(level);
        if ((n_highSalienceACC > 2)) {
            highSEACC = (std(highIntensitiesACC) / Math.pow(n_highSalienceACC, 0.5));
            highSalienceCIACC = (1.645 * highSEACC);
            highStepACC = Math.abs((level - lastHighLevelACC));
            lastHighLevelACC = level;
            highStopOKACC = (highSalienceCIACC < (highStepACC / 2));
        }
    } else {
        if ((thisCondition === "lowSalienceAcc")) {
            n_lowSalienceACC += 1;
            lowIntensitiesACC.push(level);
            if ((n_lowSalienceACC > 2)) {
                lowSEACC = (std(lowIntensitiesACC) / Math.pow(n_lowSalienceACC, 0.5));
                lowSalienceCIACC = (1.645 * lowSEACC);
                lowStepACC = Math.abs((level - lastLowLevelACC));
                lastLowLevelACC = level;
                lowStopOKACC = (lowSalienceCIACC < (lowStepACC / 2));
            }
        } else {
            if ((thisCondition === "highSalienceDec")) {
                n_highSalienceDEC += 1;
                highIntensitiesDEC.push(level);
                if ((n_highSalienceDEC > 2)) {
                    highSEDEC = (std(highIntensitiesDEC) / Math.pow(n_highSalienceDEC, 0.5));
                    highSalienceCIDEC = (1.645 * highSEDEC);
                    highStepDEC = Math.abs((level - lastHighLevelDEC));
                    lastHighLevelDEC = level;
                    highStopOKDEC = (highSalienceCIDEC < (highStepDEC / 2));
                }
            } else {
                n_lowSalienceDEC += 1;
                lowIntensitiesDEC.push(level);
                if ((n_lowSalienceDEC > 2)) {
                    lowSEDEC = (std(lowIntensitiesDEC) / Math.pow(n_lowSalienceDEC, 0.5));
                    lowSalienceCIDEC = (1.645 * lowSEDEC);
                    lowStepDEC = Math.abs((level - lastLowLevelDEC));
                    lastLowLevelDEC = level;
                    lowStopOKDEC = (lowSalienceCIDEC < (lowStepDEC / 2));
                }
            }
        }
    }
    psychoJS.experiment.addData("highCIACC", highSalienceCIACC);
    psychoJS.experiment.addData("lowCIACC", lowSalienceCIACC);
    psychoJS.experiment.addData("highCIDEC", highSalienceCIDEC);
    psychoJS.experiment.addData("lowCIDEC", lowSalienceCIDEC);
    psychoJS.experiment.addData("highStepACC", highStepACC);
    psychoJS.experiment.addData("lowStepACC", lowStepACC);
    psychoJS.experiment.addData("highStepDEC", highStepDEC);
    psychoJS.experiment.addData("lowStepDEC", lowStepDEC);
    psychoJS.experiment.addData("highStopOKACC", highStopOKACC);
    psychoJS.experiment.addData("lowStopOKACC", lowStopOKACC);
    psychoJS.experiment.addData("highStopOKDEC", highStopOKDEC);
    psychoJS.experiment.addData("lowStopOKDEC", lowStopOKDEC);
    
    // the Routine "TestTrial" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var _key_resp_4_allKeys;
var CompleteInstructComponents;
function CompleteInstructRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'CompleteInstruct' ---
    t = 0;
    CompleteInstructClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    psychoJS.experiment.addData('CompleteInstruct.started', globalClock.getTime());
    key_resp_4.keys = undefined;
    key_resp_4.rt = undefined;
    _key_resp_4_allKeys = [];
    // keep track of which components have finished
    CompleteInstructComponents = [];
    CompleteInstructComponents.push(key_resp_4);
    CompleteInstructComponents.push(text_4);
    
    CompleteInstructComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}


function CompleteInstructRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'CompleteInstruct' ---
    // get current time
    t = CompleteInstructClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *key_resp_4* updates
    if (t >= 0.0 && key_resp_4.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      key_resp_4.tStart = t;  // (not accounting for frame time here)
      key_resp_4.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { key_resp_4.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { key_resp_4.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { key_resp_4.clearEvents(); });
    }
    
    if (key_resp_4.status === PsychoJS.Status.STARTED) {
      let theseKeys = key_resp_4.getKeys({keyList: ['space'], waitRelease: false});
      _key_resp_4_allKeys = _key_resp_4_allKeys.concat(theseKeys);
      if (_key_resp_4_allKeys.length > 0) {
        key_resp_4.keys = _key_resp_4_allKeys[_key_resp_4_allKeys.length - 1].name;  // just the last key pressed
        key_resp_4.rt = _key_resp_4_allKeys[_key_resp_4_allKeys.length - 1].rt;
        key_resp_4.duration = _key_resp_4_allKeys[_key_resp_4_allKeys.length - 1].duration;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    
    // *text_4* updates
    if (t >= 0.0 && text_4.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text_4.tStart = t;  // (not accounting for frame time here)
      text_4.frameNStart = frameN;  // exact frame index
      
      text_4.setAutoDraw(true);
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    CompleteInstructComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function CompleteInstructRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'CompleteInstruct' ---
    CompleteInstructComponents.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    psychoJS.experiment.addData('CompleteInstruct.stopped', globalClock.getTime());
    // update the trial handler
    if (currentLoop instanceof MultiStairHandler) {
      currentLoop.addResponse(key_resp_4.corr, level);
    }
    psychoJS.experiment.addData('key_resp_4.keys', key_resp_4.keys);
    if (typeof key_resp_4.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('key_resp_4.rt', key_resp_4.rt);
        psychoJS.experiment.addData('key_resp_4.duration', key_resp_4.duration);
        routineTimer.reset();
        }
    
    key_resp_4.stop();
    // the Routine "CompleteInstruct" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


function importConditions(currentLoop) {
  return async function () {
    psychoJS.importAttributes(currentLoop.getCurrentTrial());
    return Scheduler.Event.NEXT;
    };
}


async function quitPsychoJS(message, isCompleted) {
  // Check for and save orphaned data
  if (psychoJS.experiment.isEntryEmpty()) {
    psychoJS.experiment.nextEntry();
  }
  psychoJS.window.close();
  psychoJS.quit({message: message, isCompleted: isCompleted});
  
  return Scheduler.Event.QUIT;
}
