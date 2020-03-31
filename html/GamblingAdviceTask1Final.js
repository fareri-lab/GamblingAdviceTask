/********************************* 
 * Gamblingadvicetask1Final Test *
 *********************************/

import { PsychoJS } from './lib/core-2020.1.js';
import * as core from './lib/core-2020.1.js';
import { TrialHandler } from './lib/data-2020.1.js';
import { Scheduler } from './lib/util-2020.1.js';
import * as util from './lib/util-2020.1.js';
import * as visual from './lib/visual-2020.1.js';
import * as sound from './lib/sound-2020.1.js';

// init psychoJS:
const psychoJS = new PsychoJS({
  debug: true
});

// open window:
psychoJS.openWindow({
  fullscr: true,
  color: new util.Color([(- 1), (- 1), (- 1)]),
  units: 'height',
  waitBlanking: true
});

// store info about the experiment session:
let expName = 'GamblingAdviceTask1Final';  // from the Builder filename that created this script
let expInfo = {'participant': '', 'session': '001', 'age': '', 'gender (0=male, 1 = female, 2 = other)': ''};

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
flowScheduler.add(welcomeRoutineBegin());
flowScheduler.add(welcomeRoutineEachFrame());
flowScheduler.add(welcomeRoutineEnd());
flowScheduler.add(instRoutineBegin());
flowScheduler.add(instRoutineEachFrame());
flowScheduler.add(instRoutineEnd());
flowScheduler.add(preBlockRoutineBegin());
flowScheduler.add(preBlockRoutineEachFrame());
flowScheduler.add(preBlockRoutineEnd());
const practiceLoopScheduler = new Scheduler(psychoJS);
flowScheduler.add(practiceLoopBegin, practiceLoopScheduler);
flowScheduler.add(practiceLoopScheduler);
flowScheduler.add(practiceLoopEnd);
flowScheduler.add(endpracRoutineBegin());
flowScheduler.add(endpracRoutineEachFrame());
flowScheduler.add(endpracRoutineEnd());
const trials_2LoopScheduler = new Scheduler(psychoJS);
flowScheduler.add(trials_2LoopBegin, trials_2LoopScheduler);
flowScheduler.add(trials_2LoopScheduler);
flowScheduler.add(trials_2LoopEnd);
flowScheduler.add(EndingRoutineBegin());
flowScheduler.add(EndingRoutineEachFrame());
flowScheduler.add(EndingRoutineEnd());
flowScheduler.add(quitPsychoJS, '', true);

// quit if user presses Cancel in dialog box:
dialogCancelScheduler.add(quitPsychoJS, '', false);

psychoJS.start({
  expName: expName,
  expInfo: expInfo,
  });


var frameDur;
function updateInfo() {
  expInfo['date'] = util.MonotonicClock.getDateStr();  // add a simple timestamp
  expInfo['expName'] = expName;
  expInfo['psychopyVersion'] = '2020.1.2';
  expInfo['OS'] = window.navigator.platform;

  // store frame rate of monitor if we can measure it successfully
  expInfo['frameRate'] = psychoJS.window.getActualFrameRate();
  if (typeof expInfo['frameRate'] !== 'undefined')
    frameDur = 1.0 / Math.round(expInfo['frameRate']);
  else
    frameDur = 1.0 / 60.0; // couldn't get a reliable measure so guess

  // add info from the URL:
  util.addInfoFromUrl(expInfo);
  
  return Scheduler.Event.NEXT;
}


var welcomeClock;
var text;
var key_resp_4;
var instClock;
var instructions;
var space;
var preBlockClock;
var chooseInst;
var Ad1;
var Ad2;
var key_resp_3;
var Ad1pic;
var Ad2pic;
var enter;
var ISIClock;
var iSi;
var Receive_moneyClock;
var receiveMoneyPicture;
var ISI2;
var trialClock;
var ChoicePic;
var askAdClock;
var response;
var yesNo;
var ask;
var getAdClock;
var getAdv;
var textForCode;
var Choice2GainClock;
var blank;
var ChoicePic2;
var resp;
var checkL1;
var checkR1;
var endpracClock;
var EndPrac;
var key_resp;
var FeedbackClock;
var endText;
var key_resp_2;
var EndingClock;
var Ending_;
var globalClock;
var routineTimer;
function experimentInit() {
  // Initialize components for Routine "welcome"
  welcomeClock = new util.Clock();
  text = new visual.TextStim({
    win: psychoJS.window,
    name: 'text',
    text: 'Welcome to the gambling advice task. Here you will make a series of choices between accepting a monetary gamble or accepting a guaranteed monetary outcome. \n\nOn each trial, you can choose whether you want to recieve advice from your chosen advisor.\n\nPress the spacebar to move on to the practice trials.',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.05,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: 0.0 
  });
  
  key_resp_4 = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "inst"
  instClock = new util.Clock();
  instructions = new visual.TextStim({
    win: psychoJS.window,
    name: 'instructions',
    text: '\nWelcome to the study! \n\nOn the following page you will be instructed to choose an advisor. \n\nPress the space bar when you are ready to proceed.',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.05,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: 0.0 
  });
  
  space = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "preBlock"
  preBlockClock = new util.Clock();
  chooseInst = new visual.TextStim({
    win: psychoJS.window,
    name: 'chooseInst',
    text: 'default text',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 1.0,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: 0.0 
  });
  
  Ad1 = new visual.TextStim({
    win: psychoJS.window,
    name: 'Ad1',
    text: 'default text',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 1.0,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: -1.0 
  });
  
  Ad2 = new visual.TextStim({
    win: psychoJS.window,
    name: 'Ad2',
    text: 'default text',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 1.0,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: -2.0 
  });
  
  key_resp_3 = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  Ad1pic = new visual.ImageStim({
    win : psychoJS.window,
    name : 'Ad1pic', units : undefined, 
    image : undefined, mask : undefined,
    ori : 1.0, pos : [0, 0], size : 1.0,
    color : new util.Color([1, 1, 1]), opacity : 1.0,
    flipHoriz : false, flipVert : false,
    texRes : 128, interpolate : true, depth : -4.0 
  });
  Ad2pic = new visual.ImageStim({
    win : psychoJS.window,
    name : 'Ad2pic', units : undefined, 
    image : 'avatar_2.png', mask : undefined,
    ori : 0, pos : [0.4, (- 0.06)], size : [0.3, 0.3],
    color : new util.Color([1, 1, 1]), opacity : 1,
    flipHoriz : false, flipVert : false,
    texRes : 128, interpolate : true, depth : -5.0 
  });
  enter = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "ISI"
  ISIClock = new util.Clock();
  iSi = new visual.TextStim({
    win: psychoJS.window,
    name: 'iSi',
    text: '+',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.08,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: 0.0 
  });
  
  // Initialize components for Routine "Receive_money"
  Receive_moneyClock = new util.Clock();
  receiveMoneyPicture = new visual.ImageStim({
    win : psychoJS.window,
    name : 'receiveMoneyPicture', units : undefined, 
    image : undefined, mask : undefined,
    ori : 1.0, pos : [0, 0], size : 1.0,
    color : new util.Color([1, 1, 1]), opacity : 1.0,
    flipHoriz : false, flipVert : false,
    texRes : 128, interpolate : true, depth : 0.0 
  });
  ISI2 = new visual.TextStim({
    win: psychoJS.window,
    name: 'ISI2',
    text: 'default text',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 1.0,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: -1.0 
  });
  
  // Initialize components for Routine "trial"
  trialClock = new util.Clock();
  ChoicePic = new visual.ImageStim({
    win : psychoJS.window,
    name : 'ChoicePic', units : undefined, 
    image : undefined, mask : undefined,
    ori : 1.0, pos : [0, 0], size : 1.0,
    color : new util.Color([1, 1, 1]), opacity : 1.0,
    flipHoriz : false, flipVert : false,
    texRes : 128, interpolate : true, depth : 0.0 
  });
  // Initialize components for Routine "askAd"
  askAdClock = new util.Clock();
  response = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  yesNo = new visual.TextStim({
    win: psychoJS.window,
    name: 'yesNo',
    text: 'default text',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 1.0,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: -1.0 
  });
  
  ask = new visual.TextStim({
    win: psychoJS.window,
    name: 'ask',
    text: 'default text',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 1.0,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: -2.0 
  });
  
  // Initialize components for Routine "getAd"
  getAdClock = new util.Clock();
  getAdv = new visual.TextStim({
    win: psychoJS.window,
    name: 'getAdv',
    text: 'default text',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 1.0,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: -1.0 
  });
  
  textForCode = new visual.TextStim({
    win: psychoJS.window,
    name: 'textForCode',
    text: 'default text',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 1.0,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: -2.0 
  });
  
  // Initialize components for Routine "Choice2Gain"
  Choice2GainClock = new util.Clock();
  blank = new visual.TextStim({
    win: psychoJS.window,
    name: 'blank',
    text: 'default text',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 1.0,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: 0.0 
  });
  
  ChoicePic2 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'ChoicePic2', units : undefined, 
    image : undefined, mask : undefined,
    ori : 1.0, pos : [0, 0], size : 1.0,
    color : new util.Color([1, 1, 1]), opacity : 1.0,
    flipHoriz : false, flipVert : false,
    texRes : 128, interpolate : true, depth : -1.0 
  });
  resp = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  checkL1 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'checkL1', units : undefined, 
    image : undefined, mask : undefined,
    ori : 1.0, pos : [0, 0], size : 1.0,
    color : new util.Color('white'), opacity : 1.0,
    flipHoriz : false, flipVert : false,
    texRes : 128, interpolate : true, depth : -3.0 
  });
  checkR1 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'checkR1', units : undefined, 
    image : undefined, mask : undefined,
    ori : 1.0, pos : [0, 0], size : 1.0,
    color : new util.Color('white'), opacity : 1.0,
    flipHoriz : false, flipVert : false,
    texRes : 128, interpolate : true, depth : -4.0 
  });
  // Initialize components for Routine "endprac"
  endpracClock = new util.Clock();
  EndPrac = new visual.TextStim({
    win: psychoJS.window,
    name: 'EndPrac',
    text: 'You have reached the end of the practice round.  \n\nIf you have any questions, please let the experimenter know now.\n\nOtherwise, please press the spacebar to begin.',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.05,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: 0.0 
  });
  
  key_resp = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "preBlock"
  preBlockClock = new util.Clock();
  chooseInst = new visual.TextStim({
    win: psychoJS.window,
    name: 'chooseInst',
    text: 'default text',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 1.0,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: 0.0 
  });
  
  Ad1 = new visual.TextStim({
    win: psychoJS.window,
    name: 'Ad1',
    text: 'default text',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 1.0,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: -1.0 
  });
  
  Ad2 = new visual.TextStim({
    win: psychoJS.window,
    name: 'Ad2',
    text: 'default text',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 1.0,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: -2.0 
  });
  
  key_resp_3 = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  Ad1pic = new visual.ImageStim({
    win : psychoJS.window,
    name : 'Ad1pic', units : undefined, 
    image : undefined, mask : undefined,
    ori : 1.0, pos : [0, 0], size : 1.0,
    color : new util.Color([1, 1, 1]), opacity : 1.0,
    flipHoriz : false, flipVert : false,
    texRes : 128, interpolate : true, depth : -4.0 
  });
  Ad2pic = new visual.ImageStim({
    win : psychoJS.window,
    name : 'Ad2pic', units : undefined, 
    image : 'avatar_2.png', mask : undefined,
    ori : 0, pos : [0.4, (- 0.06)], size : [0.3, 0.3],
    color : new util.Color([1, 1, 1]), opacity : 1,
    flipHoriz : false, flipVert : false,
    texRes : 128, interpolate : true, depth : -5.0 
  });
  enter = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "ISI"
  ISIClock = new util.Clock();
  iSi = new visual.TextStim({
    win: psychoJS.window,
    name: 'iSi',
    text: '+',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.08,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: 0.0 
  });
  
  // Initialize components for Routine "Receive_money"
  Receive_moneyClock = new util.Clock();
  receiveMoneyPicture = new visual.ImageStim({
    win : psychoJS.window,
    name : 'receiveMoneyPicture', units : undefined, 
    image : undefined, mask : undefined,
    ori : 1.0, pos : [0, 0], size : 1.0,
    color : new util.Color([1, 1, 1]), opacity : 1.0,
    flipHoriz : false, flipVert : false,
    texRes : 128, interpolate : true, depth : 0.0 
  });
  ISI2 = new visual.TextStim({
    win: psychoJS.window,
    name: 'ISI2',
    text: 'default text',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 1.0,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: -1.0 
  });
  
  // Initialize components for Routine "trial"
  trialClock = new util.Clock();
  ChoicePic = new visual.ImageStim({
    win : psychoJS.window,
    name : 'ChoicePic', units : undefined, 
    image : undefined, mask : undefined,
    ori : 1.0, pos : [0, 0], size : 1.0,
    color : new util.Color([1, 1, 1]), opacity : 1.0,
    flipHoriz : false, flipVert : false,
    texRes : 128, interpolate : true, depth : 0.0 
  });
  // Initialize components for Routine "askAd"
  askAdClock = new util.Clock();
  response = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  yesNo = new visual.TextStim({
    win: psychoJS.window,
    name: 'yesNo',
    text: 'default text',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 1.0,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: -1.0 
  });
  
  ask = new visual.TextStim({
    win: psychoJS.window,
    name: 'ask',
    text: 'default text',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 1.0,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: -2.0 
  });
  
  // Initialize components for Routine "getAd"
  getAdClock = new util.Clock();
  getAdv = new visual.TextStim({
    win: psychoJS.window,
    name: 'getAdv',
    text: 'default text',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 1.0,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: -1.0 
  });
  
  textForCode = new visual.TextStim({
    win: psychoJS.window,
    name: 'textForCode',
    text: 'default text',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 1.0,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: -2.0 
  });
  
  // Initialize components for Routine "Choice2Gain"
  Choice2GainClock = new util.Clock();
  blank = new visual.TextStim({
    win: psychoJS.window,
    name: 'blank',
    text: 'default text',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 1.0,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: 0.0 
  });
  
  ChoicePic2 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'ChoicePic2', units : undefined, 
    image : undefined, mask : undefined,
    ori : 1.0, pos : [0, 0], size : 1.0,
    color : new util.Color([1, 1, 1]), opacity : 1.0,
    flipHoriz : false, flipVert : false,
    texRes : 128, interpolate : true, depth : -1.0 
  });
  resp = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  checkL1 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'checkL1', units : undefined, 
    image : undefined, mask : undefined,
    ori : 1.0, pos : [0, 0], size : 1.0,
    color : new util.Color('white'), opacity : 1.0,
    flipHoriz : false, flipVert : false,
    texRes : 128, interpolate : true, depth : -3.0 
  });
  checkR1 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'checkR1', units : undefined, 
    image : undefined, mask : undefined,
    ori : 1.0, pos : [0, 0], size : 1.0,
    color : new util.Color('white'), opacity : 1.0,
    flipHoriz : false, flipVert : false,
    texRes : 128, interpolate : true, depth : -4.0 
  });
  // Initialize components for Routine "Feedback"
  FeedbackClock = new util.Clock();
  endText = new visual.TextStim({
    win: psychoJS.window,
    name: 'endText',
    text: 'default text',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 1.0,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: -1.0 
  });
  
  key_resp_2 = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "Ending"
  EndingClock = new util.Clock();
  Ending_ = new visual.TextStim({
    win: psychoJS.window,
    name: 'Ending_',
    text: 'You have reached the end of the experiment. Thank you for participating :)',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.1,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: 0.0 
  });
  
  // Create some handy timers
  globalClock = new util.Clock();  // to track the time since experiment started
  routineTimer = new util.CountdownTimer();  // to track time remaining of each (non-slip) routine
  
  return Scheduler.Event.NEXT;
}


var t;
var frameN;
var _key_resp_4_allKeys;
var welcomeComponents;
function welcomeRoutineBegin(trials) {
  return function () {
    //------Prepare to start Routine 'welcome'-------
    t = 0;
    welcomeClock.reset(); // clock
    frameN = -1;
    // update component parameters for each repeat
    key_resp_4.keys = undefined;
    key_resp_4.rt = undefined;
    _key_resp_4_allKeys = [];
    // keep track of which components have finished
    welcomeComponents = [];
    welcomeComponents.push(text);
    welcomeComponents.push(key_resp_4);
    
    for (const thisComponent of welcomeComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    
    return Scheduler.Event.NEXT;
  };
}


var continueRoutine;
function welcomeRoutineEachFrame(trials) {
  return function () {
    //------Loop for each frame of Routine 'welcome'-------
    let continueRoutine = true; // until we're told otherwise
    // get current time
    t = welcomeClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *text* updates
    if (t >= 0.0 && text.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text.tStart = t;  // (not accounting for frame time here)
      text.frameNStart = frameN;  // exact frame index
      
      text.setAutoDraw(true);
    }

    
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
    for (const thisComponent of welcomeComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function welcomeRoutineEnd(trials) {
  return function () {
    //------Ending Routine 'welcome'-------
    for (const thisComponent of welcomeComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    psychoJS.experiment.addData('key_resp_4.keys', key_resp_4.keys);
    if (typeof key_resp_4.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('key_resp_4.rt', key_resp_4.rt);
        routineTimer.reset();
        }
    
    key_resp_4.stop();
    // the Routine "welcome" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    return Scheduler.Event.NEXT;
  };
}


var _space_allKeys;
var instComponents;
function instRoutineBegin(trials) {
  return function () {
    //------Prepare to start Routine 'inst'-------
    t = 0;
    instClock.reset(); // clock
    frameN = -1;
    // update component parameters for each repeat
    space.keys = undefined;
    space.rt = undefined;
    _space_allKeys = [];
    // keep track of which components have finished
    instComponents = [];
    instComponents.push(instructions);
    instComponents.push(space);
    
    for (const thisComponent of instComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    
    return Scheduler.Event.NEXT;
  };
}


function instRoutineEachFrame(trials) {
  return function () {
    //------Loop for each frame of Routine 'inst'-------
    let continueRoutine = true; // until we're told otherwise
    // get current time
    t = instClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *instructions* updates
    if (t >= 0.0 && instructions.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      instructions.tStart = t;  // (not accounting for frame time here)
      instructions.frameNStart = frameN;  // exact frame index
      
      instructions.setAutoDraw(true);
    }

    
    // *space* updates
    if (t >= 0.0 && space.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      space.tStart = t;  // (not accounting for frame time here)
      space.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { space.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { space.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { space.clearEvents(); });
    }

    if (space.status === PsychoJS.Status.STARTED) {
      let theseKeys = space.getKeys({keyList: ['space'], waitRelease: false});
      _space_allKeys = _space_allKeys.concat(theseKeys);
      if (_space_allKeys.length > 0) {
        space.keys = _space_allKeys[_space_allKeys.length - 1].name;  // just the last key pressed
        space.rt = _space_allKeys[_space_allKeys.length - 1].rt;
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
    for (const thisComponent of instComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function instRoutineEnd(trials) {
  return function () {
    //------Ending Routine 'inst'-------
    for (const thisComponent of instComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    psychoJS.experiment.addData('space.keys', space.keys);
    if (typeof space.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('space.rt', space.rt);
        routineTimer.reset();
        }
    
    space.stop();
    // the Routine "inst" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    return Scheduler.Event.NEXT;
  };
}


var _key_resp_3_allKeys;
var _enter_allKeys;
var preBlockComponents;
function preBlockRoutineBegin(trials) {
  return function () {
    //------Prepare to start Routine 'preBlock'-------
    t = 0;
    preBlockClock.reset(); // clock
    frameN = -1;
    // update component parameters for each repeat
    chooseInst.setColor(new util.Color('white'));
    chooseInst.setPos([0, 0.4]);
    chooseInst.setText('Please choose which person you would want to receive financial advice from, and then press enter.');
    chooseInst.setFont('Arial');
    chooseInst.setHeight(0.04);
    Ad1.setColor(new util.Color('white'));
    Ad1.setPos([(- 0.4), (- 0.05)]);
    Ad1.setText('\n  Advisor 1: (Left Arrow)\n\n\n\n\n\n\n\n\nAdelphi University MBA student,\ninterning at Chase Bank ');
    Ad1.setFont('Arial');
    Ad1.setHeight(0.04);
    Ad2.setColor(new util.Color('white'));
    Ad2.setPos([0.4, (- 0.05)]);
    Ad2.setText('\nAdvisor 2: (Right arrow)\n\n\n\n\n\n\n\n \nAdelphi University\nundergraduate biology major');
    Ad2.setFont('Arial');
    Ad2.setHeight(0.04);
    key_resp_3.keys = undefined;
    key_resp_3.rt = undefined;
    _key_resp_3_allKeys = [];
    Ad1pic.setOpacity(1);
    Ad1pic.setPos([(- 0.4), (- 0.06)]);
    Ad1pic.setSize([0.3, 0.3]);
    Ad1pic.setOri(0);
    Ad1pic.setImage('avatar_1.png');
    enter.keys = undefined;
    enter.rt = undefined;
    _enter_allKeys = [];
    // keep track of which components have finished
    preBlockComponents = [];
    preBlockComponents.push(chooseInst);
    preBlockComponents.push(Ad1);
    preBlockComponents.push(Ad2);
    preBlockComponents.push(key_resp_3);
    preBlockComponents.push(Ad1pic);
    preBlockComponents.push(Ad2pic);
    preBlockComponents.push(enter);
    
    for (const thisComponent of preBlockComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    
    return Scheduler.Event.NEXT;
  };
}


function preBlockRoutineEachFrame(trials) {
  return function () {
    //------Loop for each frame of Routine 'preBlock'-------
    let continueRoutine = true; // until we're told otherwise
    // get current time
    t = preBlockClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *chooseInst* updates
    if (t >= 0.0 && chooseInst.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      chooseInst.tStart = t;  // (not accounting for frame time here)
      chooseInst.frameNStart = frameN;  // exact frame index
      
      chooseInst.setAutoDraw(true);
    }

    
    // *Ad1* updates
    if (t >= 0.0 && Ad1.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      Ad1.tStart = t;  // (not accounting for frame time here)
      Ad1.frameNStart = frameN;  // exact frame index
      
      Ad1.setAutoDraw(true);
    }

    
    // *Ad2* updates
    if (t >= 0.0 && Ad2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      Ad2.tStart = t;  // (not accounting for frame time here)
      Ad2.frameNStart = frameN;  // exact frame index
      
      Ad2.setAutoDraw(true);
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
      let theseKeys = key_resp_3.getKeys({keyList: ['left', 'right'], waitRelease: false});
      _key_resp_3_allKeys = _key_resp_3_allKeys.concat(theseKeys);
      if (_key_resp_3_allKeys.length > 0) {
        key_resp_3.keys = _key_resp_3_allKeys[_key_resp_3_allKeys.length - 1].name;  // just the last key pressed
        key_resp_3.rt = _key_resp_3_allKeys[_key_resp_3_allKeys.length - 1].rt;
      }
    }
    
    
    // *Ad1pic* updates
    if (t >= 0.0 && Ad1pic.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      Ad1pic.tStart = t;  // (not accounting for frame time here)
      Ad1pic.frameNStart = frameN;  // exact frame index
      
      Ad1pic.setAutoDraw(true);
    }

    
    // *Ad2pic* updates
    if (t >= 0.0 && Ad2pic.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      Ad2pic.tStart = t;  // (not accounting for frame time here)
      Ad2pic.frameNStart = frameN;  // exact frame index
      
      Ad2pic.setAutoDraw(true);
    }

    
    // *enter* updates
    if (t >= 0.0 && enter.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      enter.tStart = t;  // (not accounting for frame time here)
      enter.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { enter.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { enter.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { enter.clearEvents(); });
    }

    if (enter.status === PsychoJS.Status.STARTED) {
      let theseKeys = enter.getKeys({keyList: ['return'], waitRelease: false});
      _enter_allKeys = _enter_allKeys.concat(theseKeys);
      if (_enter_allKeys.length > 0) {
        enter.keys = _enter_allKeys[_enter_allKeys.length - 1].name;  // just the last key pressed
        enter.rt = _enter_allKeys[_enter_allKeys.length - 1].rt;
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
    for (const thisComponent of preBlockComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function preBlockRoutineEnd(trials) {
  return function () {
    //------Ending Routine 'preBlock'-------
    for (const thisComponent of preBlockComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    psychoJS.experiment.addData('key_resp_3.keys', key_resp_3.keys);
    if (typeof key_resp_3.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('key_resp_3.rt', key_resp_3.rt);
        }
    
    key_resp_3.stop();
    psychoJS.experiment.addData('enter.keys', enter.keys);
    if (typeof enter.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('enter.rt', enter.rt);
        routineTimer.reset();
        }
    
    enter.stop();
    // the Routine "preBlock" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    return Scheduler.Event.NEXT;
  };
}


var practice;
var currentLoop;
function practiceLoopBegin(thisScheduler) {
  // set up handler to look after randomisation of conditions etc
  practice = new TrialHandler({
    psychoJS: psychoJS,
    nReps: 1, method: TrialHandler.Method.RANDOM,
    extraInfo: expInfo, originPath: undefined,
    trialList: 'practice.xlsx',
    seed: undefined, name: 'practice'
  });
  psychoJS.experiment.addLoop(practice); // add the loop to the experiment
  currentLoop = practice;  // we're now the current loop

  // Schedule all the trials in the trialList:
  for (const thisPractice of practice) {
    const snapshot = practice.getSnapshot();
    thisScheduler.add(importConditions(snapshot));
    thisScheduler.add(ISIRoutineBegin(snapshot));
    thisScheduler.add(ISIRoutineEachFrame(snapshot));
    thisScheduler.add(ISIRoutineEnd(snapshot));
    thisScheduler.add(Receive_moneyRoutineBegin(snapshot));
    thisScheduler.add(Receive_moneyRoutineEachFrame(snapshot));
    thisScheduler.add(Receive_moneyRoutineEnd(snapshot));
    thisScheduler.add(trialRoutineBegin(snapshot));
    thisScheduler.add(trialRoutineEachFrame(snapshot));
    thisScheduler.add(trialRoutineEnd(snapshot));
    thisScheduler.add(askAdRoutineBegin(snapshot));
    thisScheduler.add(askAdRoutineEachFrame(snapshot));
    thisScheduler.add(askAdRoutineEnd(snapshot));
    thisScheduler.add(getAdRoutineBegin(snapshot));
    thisScheduler.add(getAdRoutineEachFrame(snapshot));
    thisScheduler.add(getAdRoutineEnd(snapshot));
    thisScheduler.add(Choice2GainRoutineBegin(snapshot));
    thisScheduler.add(Choice2GainRoutineEachFrame(snapshot));
    thisScheduler.add(Choice2GainRoutineEnd(snapshot));
    thisScheduler.add(endLoopIteration(thisScheduler, snapshot));
  }

  return Scheduler.Event.NEXT;
}


function practiceLoopEnd() {
  psychoJS.experiment.removeLoop(practice);

  return Scheduler.Event.NEXT;
}


var trials_2;
function trials_2LoopBegin(thisScheduler) {
  // set up handler to look after randomisation of conditions etc
  trials_2 = new TrialHandler({
    psychoJS: psychoJS,
    nReps: 10, method: TrialHandler.Method.RANDOM,
    extraInfo: expInfo, originPath: undefined,
    trialList: undefined,
    seed: undefined, name: 'trials_2'
  });
  psychoJS.experiment.addLoop(trials_2); // add the loop to the experiment
  currentLoop = trials_2;  // we're now the current loop

  // Schedule all the trials in the trialList:
  for (const thisTrial_2 of trials_2) {
    const snapshot = trials_2.getSnapshot();
    thisScheduler.add(importConditions(snapshot));
    thisScheduler.add(preBlockRoutineBegin(snapshot));
    thisScheduler.add(preBlockRoutineEachFrame(snapshot));
    thisScheduler.add(preBlockRoutineEnd(snapshot));
    const trialsLoopScheduler = new Scheduler(psychoJS);
    thisScheduler.add(trialsLoopBegin, trialsLoopScheduler);
    thisScheduler.add(trialsLoopScheduler);
    thisScheduler.add(trialsLoopEnd);
    thisScheduler.add(FeedbackRoutineBegin(snapshot));
    thisScheduler.add(FeedbackRoutineEachFrame(snapshot));
    thisScheduler.add(FeedbackRoutineEnd(snapshot));
    thisScheduler.add(endLoopIteration(thisScheduler, snapshot));
  }

  return Scheduler.Event.NEXT;
}


var trials;
function trialsLoopBegin(thisScheduler) {
  // set up handler to look after randomisation of conditions etc
  trials = new TrialHandler({
    psychoJS: psychoJS,
    nReps: 1, method: TrialHandler.Method.RANDOM,
    extraInfo: expInfo, originPath: undefined,
    trialList: TrialHandler.importConditions(psychoJS.serverManager, 'Book1.xlsx', choice(40, size=20, replace=False)),
    seed: undefined, name: 'trials'
  });
  psychoJS.experiment.addLoop(trials); // add the loop to the experiment
  currentLoop = trials;  // we're now the current loop

  // Schedule all the trials in the trialList:
  for (const thisTrial of trials) {
    const snapshot = trials.getSnapshot();
    thisScheduler.add(importConditions(snapshot));
    thisScheduler.add(ISIRoutineBegin(snapshot));
    thisScheduler.add(ISIRoutineEachFrame(snapshot));
    thisScheduler.add(ISIRoutineEnd(snapshot));
    thisScheduler.add(Receive_moneyRoutineBegin(snapshot));
    thisScheduler.add(Receive_moneyRoutineEachFrame(snapshot));
    thisScheduler.add(Receive_moneyRoutineEnd(snapshot));
    thisScheduler.add(trialRoutineBegin(snapshot));
    thisScheduler.add(trialRoutineEachFrame(snapshot));
    thisScheduler.add(trialRoutineEnd(snapshot));
    thisScheduler.add(askAdRoutineBegin(snapshot));
    thisScheduler.add(askAdRoutineEachFrame(snapshot));
    thisScheduler.add(askAdRoutineEnd(snapshot));
    thisScheduler.add(getAdRoutineBegin(snapshot));
    thisScheduler.add(getAdRoutineEachFrame(snapshot));
    thisScheduler.add(getAdRoutineEnd(snapshot));
    thisScheduler.add(Choice2GainRoutineBegin(snapshot));
    thisScheduler.add(Choice2GainRoutineEachFrame(snapshot));
    thisScheduler.add(Choice2GainRoutineEnd(snapshot));
    thisScheduler.add(endLoopIteration(thisScheduler, snapshot));
  }

  return Scheduler.Event.NEXT;
}


function trialsLoopEnd() {
  psychoJS.experiment.removeLoop(trials);

  return Scheduler.Event.NEXT;
}


function trials_2LoopEnd() {
  psychoJS.experiment.removeLoop(trials_2);

  return Scheduler.Event.NEXT;
}


var ISIComponents;
function ISIRoutineBegin(trials) {
  return function () {
    //------Prepare to start Routine 'ISI'-------
    t = 0;
    ISIClock.reset(); // clock
    frameN = -1;
    routineTimer.add(2.000000);
    // update component parameters for each repeat
    // keep track of which components have finished
    ISIComponents = [];
    ISIComponents.push(iSi);
    
    for (const thisComponent of ISIComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    
    return Scheduler.Event.NEXT;
  };
}


var frameRemains;
function ISIRoutineEachFrame(trials) {
  return function () {
    //------Loop for each frame of Routine 'ISI'-------
    let continueRoutine = true; // until we're told otherwise
    // get current time
    t = ISIClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *iSi* updates
    if (t >= 0.0 && iSi.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      iSi.tStart = t;  // (not accounting for frame time here)
      iSi.frameNStart = frameN;  // exact frame index
      
      iSi.setAutoDraw(true);
    }

    frameRemains = 0.0 + 2 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (iSi.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      iSi.setAutoDraw(false);
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
    for (const thisComponent of ISIComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine && routineTimer.getTime() > 0) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function ISIRoutineEnd(trials) {
  return function () {
    //------Ending Routine 'ISI'-------
    for (const thisComponent of ISIComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    return Scheduler.Event.NEXT;
  };
}


var Receive_moneyComponents;
function Receive_moneyRoutineBegin(trials) {
  return function () {
    //------Prepare to start Routine 'Receive_money'-------
    t = 0;
    Receive_moneyClock.reset(); // clock
    frameN = -1;
    routineTimer.add(3.000000);
    // update component parameters for each repeat
    receiveMoneyPicture.setOpacity(1);
    receiveMoneyPicture.setPos([0, (- 0.05)]);
    receiveMoneyPicture.setSize([1.5, 1.1]);
    receiveMoneyPicture.setOri(0);
    receiveMoneyPicture.setImage(Amount);
    ISI2.setColor(new util.Color('white'));
    ISI2.setPos([0, 0]);
    ISI2.setText('+');
    ISI2.setFont('Arial');
    ISI2.setHeight(0.08);
    // keep track of which components have finished
    Receive_moneyComponents = [];
    Receive_moneyComponents.push(receiveMoneyPicture);
    Receive_moneyComponents.push(ISI2);
    
    for (const thisComponent of Receive_moneyComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    
    return Scheduler.Event.NEXT;
  };
}


function Receive_moneyRoutineEachFrame(trials) {
  return function () {
    //------Loop for each frame of Routine 'Receive_money'-------
    let continueRoutine = true; // until we're told otherwise
    // get current time
    t = Receive_moneyClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *receiveMoneyPicture* updates
    if (t >= 0.0 && receiveMoneyPicture.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      receiveMoneyPicture.tStart = t;  // (not accounting for frame time here)
      receiveMoneyPicture.frameNStart = frameN;  // exact frame index
      
      receiveMoneyPicture.setAutoDraw(true);
    }

    frameRemains = 0.0 + 1.5 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (receiveMoneyPicture.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      receiveMoneyPicture.setAutoDraw(false);
    }
    
    // *ISI2* updates
    if (t >= 1.5 && ISI2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      ISI2.tStart = t;  // (not accounting for frame time here)
      ISI2.frameNStart = frameN;  // exact frame index
      
      ISI2.setAutoDraw(true);
    }

    frameRemains = 1.5 + 1.5 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (ISI2.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      ISI2.setAutoDraw(false);
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
    for (const thisComponent of Receive_moneyComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine && routineTimer.getTime() > 0) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function Receive_moneyRoutineEnd(trials) {
  return function () {
    //------Ending Routine 'Receive_money'-------
    for (const thisComponent of Receive_moneyComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    return Scheduler.Event.NEXT;
  };
}


var trialComponents;
function trialRoutineBegin(trials) {
  return function () {
    //------Prepare to start Routine 'trial'-------
    t = 0;
    trialClock.reset(); // clock
    frameN = -1;
    routineTimer.add(2.000000);
    // update component parameters for each repeat
    ChoicePic.setOpacity(1);
    ChoicePic.setPos([0, 0]);
    ChoicePic.setSize([1.3, 0.9]);
    ChoicePic.setOri(0);
    ChoicePic.setImage(Choice);
    // keep track of which components have finished
    trialComponents = [];
    trialComponents.push(ChoicePic);
    
    for (const thisComponent of trialComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    
    return Scheduler.Event.NEXT;
  };
}


function trialRoutineEachFrame(trials) {
  return function () {
    //------Loop for each frame of Routine 'trial'-------
    let continueRoutine = true; // until we're told otherwise
    // get current time
    t = trialClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *ChoicePic* updates
    if (t >= 0.0 && ChoicePic.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      ChoicePic.tStart = t;  // (not accounting for frame time here)
      ChoicePic.frameNStart = frameN;  // exact frame index
      
      ChoicePic.setAutoDraw(true);
    }

    frameRemains = 0.0 + 2 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (ChoicePic.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      ChoicePic.setAutoDraw(false);
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
    for (const thisComponent of trialComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine && routineTimer.getTime() > 0) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function trialRoutineEnd(trials) {
  return function () {
    //------Ending Routine 'trial'-------
    for (const thisComponent of trialComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    return Scheduler.Event.NEXT;
  };
}


var _response_allKeys;
var askAdComponents;
function askAdRoutineBegin(trials) {
  return function () {
    //------Prepare to start Routine 'askAd'-------
    t = 0;
    askAdClock.reset(); // clock
    frameN = -1;
    routineTimer.add(3.000000);
    // update component parameters for each repeat
    response.keys = undefined;
    response.rt = undefined;
    _response_allKeys = [];
    yesNo.setColor(new util.Color('white'));
    yesNo.setPos([0, (- 0.2)]);
    yesNo.setText('Y=1                 N=2');
    yesNo.setFont('Arial');
    yesNo.setHeight(0.09);
    ask.setColor(new util.Color('white'));
    ask.setPos([0, 0.11]);
    ask.setText('Would you like to hear advice from your financial advisor? \n');
    ask.setFont('Arial');
    ask.setHeight(0.06);
    // keep track of which components have finished
    askAdComponents = [];
    askAdComponents.push(response);
    askAdComponents.push(yesNo);
    askAdComponents.push(ask);
    
    for (const thisComponent of askAdComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    
    return Scheduler.Event.NEXT;
  };
}


function askAdRoutineEachFrame(trials) {
  return function () {
    //------Loop for each frame of Routine 'askAd'-------
    let continueRoutine = true; // until we're told otherwise
    // get current time
    t = askAdClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *response* updates
    if (t >= 0 && response.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      response.tStart = t;  // (not accounting for frame time here)
      response.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { response.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { response.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { response.clearEvents(); });
    }

    frameRemains = 0 + 3 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (response.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      response.status = PsychoJS.Status.FINISHED;
  }

    if (response.status === PsychoJS.Status.STARTED) {
      let theseKeys = response.getKeys({keyList: ['1', '2'], waitRelease: false});
      _response_allKeys = _response_allKeys.concat(theseKeys);
      if (_response_allKeys.length > 0) {
        response.keys = _response_allKeys[_response_allKeys.length - 1].name;  // just the last key pressed
        response.rt = _response_allKeys[_response_allKeys.length - 1].rt;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    
    // *yesNo* updates
    if (t >= 0.0 && yesNo.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      yesNo.tStart = t;  // (not accounting for frame time here)
      yesNo.frameNStart = frameN;  // exact frame index
      
      yesNo.setAutoDraw(true);
    }

    frameRemains = 0.0 + 3 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (yesNo.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      yesNo.setAutoDraw(false);
    }
    
    // *ask* updates
    if (t >= 0.0 && ask.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      ask.tStart = t;  // (not accounting for frame time here)
      ask.frameNStart = frameN;  // exact frame index
      
      ask.setAutoDraw(true);
    }

    frameRemains = 0.0 + 3 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (ask.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      ask.setAutoDraw(false);
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
    for (const thisComponent of askAdComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine && routineTimer.getTime() > 0) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function askAdRoutineEnd(trials) {
  return function () {
    //------Ending Routine 'askAd'-------
    for (const thisComponent of askAdComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    psychoJS.experiment.addData('response.keys', response.keys);
    if (typeof response.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('response.rt', response.rt);
        routineTimer.reset();
        }
    
    response.stop();
    return Scheduler.Event.NEXT;
  };
}


var getAdComponents;
function getAdRoutineBegin(trials) {
  return function () {
    //------Prepare to start Routine 'getAd'-------
    t = 0;
    getAdClock.reset(); // clock
    frameN = -1;
    // update component parameters for each repeat
    getAdv.setColor(new util.Color('white'));
    getAdv.setPos([0, 0]);
    getAdv.setText((text + AdviceVar1));
    getAdv.setFont('Arial');
    getAdv.setHeight(0.08);
    textForCode.setColor(new util.Color([(- 1.0), (- 1.0), (- 1.0)]));
    textForCode.setPos([(- 0.9), 0]);
    textForCode.setText(GambleAdviceType);
    textForCode.setFont('Arial');
    textForCode.setHeight(0.01);
    // keep track of which components have finished
    getAdComponents = [];
    getAdComponents.push(getAdv);
    getAdComponents.push(textForCode);
    
    for (const thisComponent of getAdComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    
    return Scheduler.Event.NEXT;
  };
}


function getAdRoutineEachFrame(trials) {
  return function () {
    //------Loop for each frame of Routine 'getAd'-------
    let continueRoutine = true; // until we're told otherwise
    // get current time
    t = getAdClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *getAdv* updates
    if (((continueRoutine == True)) && getAdv.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      getAdv.tStart = t;  // (not accounting for frame time here)
      getAdv.frameNStart = frameN;  // exact frame index
      
      getAdv.setAutoDraw(true);
    }

    if (getAdv.status === PsychoJS.Status.STARTED && t >= (getAdv.tStart + 2)) {
      getAdv.setAutoDraw(false);
    }
    
    // *textForCode* updates
    if (((continueRoutine == True)) && textForCode.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      textForCode.tStart = t;  // (not accounting for frame time here)
      textForCode.frameNStart = frameN;  // exact frame index
      
      textForCode.setAutoDraw(true);
    }

    if (textForCode.status === PsychoJS.Status.STARTED && t >= (textForCode.tStart + 1)) {
      textForCode.setAutoDraw(false);
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
    for (const thisComponent of getAdComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function getAdRoutineEnd(trials) {
  return function () {
    //------Ending Routine 'getAd'-------
    for (const thisComponent of getAdComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    // the Routine "getAd" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    return Scheduler.Event.NEXT;
  };
}


var _resp_allKeys;
var Choice2GainComponents;
function Choice2GainRoutineBegin(trials) {
  return function () {
    //------Prepare to start Routine 'Choice2Gain'-------
    t = 0;
    Choice2GainClock.reset(); // clock
    frameN = -1;
    // update component parameters for each repeat
    blank.setColor(new util.Color([(- 1.0), (- 1.0), (- 1.0)]));
    blank.setPos([0, 0]);
    blank.setText('I');
    blank.setFont('Arial');
    blank.setHeight(0.01);
    ChoicePic2.setOpacity(1);
    ChoicePic2.setPos([0, 0]);
    ChoicePic2.setSize([1.3, 0.9]);
    ChoicePic2.setOri(0);
    ChoicePic2.setImage(Choice2);
    resp.keys = undefined;
    resp.rt = undefined;
    _resp_allKeys = [];
    checkL1.setColor(new util.Color([1, 1, 1]));
    checkL1.setOpacity(1);
    checkL1.setPos([0, 0]);
    checkL1.setSize([2, 1]);
    checkL1.setOri(0);
    checkL1.setImage('check2.png');
    checkL1.setMask('None');
    checkR1.setColor(new util.Color([1, 1, 1]));
    checkR1.setOpacity(1);
    checkR1.setPos([0, 0]);
    checkR1.setSize([2, 1]);
    checkR1.setOri(0);
    checkR1.setImage('check3.png');
    checkR1.setMask('None');
    // keep track of which components have finished
    Choice2GainComponents = [];
    Choice2GainComponents.push(blank);
    Choice2GainComponents.push(ChoicePic2);
    Choice2GainComponents.push(resp);
    Choice2GainComponents.push(checkL1);
    Choice2GainComponents.push(checkR1);
    
    for (const thisComponent of Choice2GainComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    
    return Scheduler.Event.NEXT;
  };
}


function Choice2GainRoutineEachFrame(trials) {
  return function () {
    //------Loop for each frame of Routine 'Choice2Gain'-------
    let continueRoutine = true; // until we're told otherwise
    // get current time
    t = Choice2GainClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *blank* updates
    if (t >= 0.0 && blank.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      blank.tStart = t;  // (not accounting for frame time here)
      blank.frameNStart = frameN;  // exact frame index
      
      blank.setAutoDraw(true);
    }

    frameRemains = 0.0 + 2 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (blank.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      blank.setAutoDraw(false);
    }
    
    // *ChoicePic2* updates
    if (t >= 0.0 && ChoicePic2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      ChoicePic2.tStart = t;  // (not accounting for frame time here)
      ChoicePic2.frameNStart = frameN;  // exact frame index
      
      ChoicePic2.setAutoDraw(true);
    }

    frameRemains = 0.0 + 2 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (ChoicePic2.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      ChoicePic2.setAutoDraw(false);
    }
    
    // *resp* updates
    if (t >= 0.0 && resp.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      resp.tStart = t;  // (not accounting for frame time here)
      resp.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { resp.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { resp.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { resp.clearEvents(); });
    }

    frameRemains = 0.0 + 2 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (resp.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      resp.status = PsychoJS.Status.FINISHED;
  }

    if (resp.status === PsychoJS.Status.STARTED) {
      let theseKeys = resp.getKeys({keyList: ['left', 'right'], waitRelease: false});
      _resp_allKeys = _resp_allKeys.concat(theseKeys);
      if (_resp_allKeys.length > 0) {
        resp.keys = _resp_allKeys[_resp_allKeys.length - 1].name;  // just the last key pressed
        resp.rt = _resp_allKeys[_resp_allKeys.length - 1].rt;
      }
    }
    
    
    // *checkL1* updates
    if (((resp.keys == 'left')) && checkL1.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      checkL1.tStart = t;  // (not accounting for frame time here)
      checkL1.frameNStart = frameN;  // exact frame index
      
      checkL1.setAutoDraw(true);
    }

    if (checkL1.status === PsychoJS.Status.STARTED && t >= (checkL1.tStart + 1)) {
      checkL1.setAutoDraw(false);
    }
    
    // *checkR1* updates
    if (((resp.keys == 'right')) && checkR1.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      checkR1.tStart = t;  // (not accounting for frame time here)
      checkR1.frameNStart = frameN;  // exact frame index
      
      checkR1.setAutoDraw(true);
    }

    if (checkR1.status === PsychoJS.Status.STARTED && t >= (checkR1.tStart + 1)) {
      checkR1.setAutoDraw(false);
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
    for (const thisComponent of Choice2GainComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function Choice2GainRoutineEnd(trials) {
  return function () {
    //------Ending Routine 'Choice2Gain'-------
    for (const thisComponent of Choice2GainComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    psychoJS.experiment.addData('resp.keys', resp.keys);
    if (typeof resp.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('resp.rt', resp.rt);
        }
    
    resp.stop();
    // the Routine "Choice2Gain" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    return Scheduler.Event.NEXT;
  };
}


var _key_resp_allKeys;
var endpracComponents;
function endpracRoutineBegin(trials) {
  return function () {
    //------Prepare to start Routine 'endprac'-------
    t = 0;
    endpracClock.reset(); // clock
    frameN = -1;
    // update component parameters for each repeat
    key_resp.keys = undefined;
    key_resp.rt = undefined;
    _key_resp_allKeys = [];
    // keep track of which components have finished
    endpracComponents = [];
    endpracComponents.push(EndPrac);
    endpracComponents.push(key_resp);
    
    for (const thisComponent of endpracComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    
    return Scheduler.Event.NEXT;
  };
}


function endpracRoutineEachFrame(trials) {
  return function () {
    //------Loop for each frame of Routine 'endprac'-------
    let continueRoutine = true; // until we're told otherwise
    // get current time
    t = endpracClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *EndPrac* updates
    if (t >= 0.0 && EndPrac.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      EndPrac.tStart = t;  // (not accounting for frame time here)
      EndPrac.frameNStart = frameN;  // exact frame index
      
      EndPrac.setAutoDraw(true);
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
    for (const thisComponent of endpracComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function endpracRoutineEnd(trials) {
  return function () {
    //------Ending Routine 'endprac'-------
    for (const thisComponent of endpracComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    psychoJS.experiment.addData('key_resp.keys', key_resp.keys);
    if (typeof key_resp.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('key_resp.rt', key_resp.rt);
        routineTimer.reset();
        }
    
    key_resp.stop();
    // the Routine "endprac" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    return Scheduler.Event.NEXT;
  };
}


var _key_resp_2_allKeys;
var FeedbackComponents;
function FeedbackRoutineBegin(trials) {
  return function () {
    //------Prepare to start Routine 'Feedback'-------
    t = 0;
    FeedbackClock.reset(); // clock
    frameN = -1;
    // update component parameters for each repeat
    endText.setColor(new util.Color('white'));
    endText.setPos([(- 0.06), 0]);
    endText.setText((((text2 + ' told you to gamble ') + gamAdvRisk) + ' times. \n \n')
(('You followed their advice to gamble ' + advFollow) + ' times. \n \n')
(('You gambled ' + nGam) + ' times. \n \n')
(('You won the gambles ' + GamblePer) + '% of the time. \n \n')
'Please press enter to move on to the next block of trials. \n');
    endText.setFont('Arial');
    endText.setHeight(0.05);
    key_resp_2.keys = undefined;
    key_resp_2.rt = undefined;
    _key_resp_2_allKeys = [];
    // keep track of which components have finished
    FeedbackComponents = [];
    FeedbackComponents.push(endText);
    FeedbackComponents.push(key_resp_2);
    
    for (const thisComponent of FeedbackComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    
    return Scheduler.Event.NEXT;
  };
}


function FeedbackRoutineEachFrame(trials) {
  return function () {
    //------Loop for each frame of Routine 'Feedback'-------
    let continueRoutine = true; // until we're told otherwise
    // get current time
    t = FeedbackClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *endText* updates
    if (t >= 0.0 && endText.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      endText.tStart = t;  // (not accounting for frame time here)
      endText.frameNStart = frameN;  // exact frame index
      
      endText.setAutoDraw(true);
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
      let theseKeys = key_resp_2.getKeys({keyList: ['return'], waitRelease: false});
      _key_resp_2_allKeys = _key_resp_2_allKeys.concat(theseKeys);
      if (_key_resp_2_allKeys.length > 0) {
        key_resp_2.keys = _key_resp_2_allKeys[_key_resp_2_allKeys.length - 1].name;  // just the last key pressed
        key_resp_2.rt = _key_resp_2_allKeys[_key_resp_2_allKeys.length - 1].rt;
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
    for (const thisComponent of FeedbackComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function FeedbackRoutineEnd(trials) {
  return function () {
    //------Ending Routine 'Feedback'-------
    for (const thisComponent of FeedbackComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    psychoJS.experiment.addData('key_resp_2.keys', key_resp_2.keys);
    if (typeof key_resp_2.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('key_resp_2.rt', key_resp_2.rt);
        routineTimer.reset();
        }
    
    key_resp_2.stop();
    // the Routine "Feedback" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    return Scheduler.Event.NEXT;
  };
}


var EndingComponents;
function EndingRoutineBegin(trials) {
  return function () {
    //------Prepare to start Routine 'Ending'-------
    t = 0;
    EndingClock.reset(); // clock
    frameN = -1;
    // update component parameters for each repeat
    // keep track of which components have finished
    EndingComponents = [];
    EndingComponents.push(Ending_);
    
    for (const thisComponent of EndingComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    
    return Scheduler.Event.NEXT;
  };
}


function EndingRoutineEachFrame(trials) {
  return function () {
    //------Loop for each frame of Routine 'Ending'-------
    let continueRoutine = true; // until we're told otherwise
    // get current time
    t = EndingClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *Ending_* updates
    if (t >= 0.0 && Ending_.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      Ending_.tStart = t;  // (not accounting for frame time here)
      Ending_.frameNStart = frameN;  // exact frame index
      
      Ending_.setAutoDraw(true);
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
    for (const thisComponent of EndingComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function EndingRoutineEnd(trials) {
  return function () {
    //------Ending Routine 'Ending'-------
    for (const thisComponent of EndingComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    // the Routine "Ending" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    return Scheduler.Event.NEXT;
  };
}


function endLoopIteration(thisScheduler, loop) {
  // ------Prepare for next entry------
  return function () {
    if (typeof loop !== 'undefined') {
      // ------Check if user ended loop early------
      if (loop.finished) {
        // Check for and save orphaned data
        if (psychoJS.experiment.isEntryEmpty()) {
          psychoJS.experiment.nextEntry(loop);
        }
      thisScheduler.stop();
      } else {
        const thisTrial = loop.getCurrentTrial();
        if (typeof thisTrial === 'undefined' || !('isTrials' in thisTrial) || thisTrial.isTrials) {
          psychoJS.experiment.nextEntry(loop);
        }
      }
    return Scheduler.Event.NEXT;
    }
  };
}


function importConditions(trials) {
  return function () {
    psychoJS.importAttributes(trials.getCurrentTrial());
    return Scheduler.Event.NEXT;
    };
}


function quitPsychoJS(message, isCompleted) {
  // Check for and save orphaned data
  if (psychoJS.experiment.isEntryEmpty()) {
    psychoJS.experiment.nextEntry();
  }
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  psychoJS.window.close();
  psychoJS.quit({message: message, isCompleted: isCompleted});
  
  return Scheduler.Event.QUIT;
}
