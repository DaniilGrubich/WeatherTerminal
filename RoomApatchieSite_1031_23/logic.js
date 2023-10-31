const connection = new WebSocket('ws://192.168.0.10:4444');
// const connection = new WebSocket('ws://localhost:4444');

var colorPicker = new iro.ColorPicker('#defaultPicker', {
  width: 500,
  color: "rgb(255, 0, 0)",
  borderWidth: 1,
  borderColor: "#fff",
});



var historyChartCanvas = document.getElementById('myHistoryChart');
var historyCtx = historyChartCanvas.getContext('2d');
var historyChart = createHistoryChartJS();

var forecastChartCanvas = document.getElementById('myDayForecastChart');
var forecastCtx = forecastChartCanvas.getContext('2d');
var forecastChart = createForecastChartJS();

var roundCanvas = document.getElementById('roundCanvas');
var ctx3 = roundCanvas.getContext('2d');
var cw2 = roundCanvas.getBoundingClientRect().width;
var ch2 = roundCanvas.getBoundingClientRect().height;

roundCanvas.height = ch2;
roundCanvas.width = cw2;


var js;
var allData;

var tempInGauge;
var sz =  [{strokeStyle: "#2596be", min: 15, max: 19},
          {strokeStyle: "#FFDD00", min: 19, max: 21},
          {strokeStyle: "#30B32D", min: 21, max: 26},
          {strokeStyle: "#FFDD00", min: 26, max: 30},
          {strokeStyle: "#F03E3E", min: 30, max: 35}];


connection.onopen = function (e) {
  console.log("Connection established");

  tempInGauge = setUpGauge("tempInGaugeCell", 15, 35, sz);
  tempInGauge.set(20);
};



connection.onmessage = function(e){
  allData =  e.data.split(';');
  js = JSON.parse(allData[7]);
  console.log(js);

  for(var i = 0; i < 4; i++)
    historyChart.data.datasets[i].data = allData[i].split`,`.map(x=>+x);;

  timeAxis = allData[4].split`,`
  historyChart.data.labels = timeAxis;
  historyChart.update();

  updateDashboard();

  updateDailyForc();
  // createForecastChartJS();

  updateSunDiagram();

}


function createHistoryChartJS(){
  return new Chart(historyCtx, {
      // The type of chart we want to create
      type: 'line',

      // The data for our dataset
      data:  {
          labels: new Array(2),
          datasets: [{
              label: 'Inside',
              yAxisID: 'A',
              borderColor: 'rgb(255, 99, 132)',
              fill: false,
              data: [5]
          }
          ,
          {
            label: 'Outside',
            yAxisID: 'A',
            borderColor: 'rgb(108, 235, 108)',
            fill: false,
            data: [5]
          }
          ,
          {
            label: 'Humidity Inside',
            yAxisID: 'B',
            borderColor: 'rgb(0, 230, 184)',
            fill: false,
            data: [5],

          },
          {
            label: 'Humidity Outside',
            yAxisID: 'B',
            lineTension: 0,
            borderColor: 'rgb(0, 172, 230)',
            fill: false,
            data: [5],}
          ]
      },

      // Configuration options go here
      options: {

        legend: {
            display: false
         },
         elements: {
                      point:{
                          radius: 0
                      },
                  },

          scales:{
            yAxes: [{
              id: 'A',
              type: 'linear',
              position: 'left',

            },
            {

              id: 'B',
              type: 'linear',
              position: 'right',
              ticks: {
                max: 100,
                min: 0
              },
              display: false, //this will remove all the x-axis grid lines

            }]
          },
          layout: {
              padding: {
                  left: 0,
                  right: 0,
                  top: 0,
                  bottom: 0
              }
          }
      }
  });
}

function createForecastChartJS(){
  return new Chart(forecastCtx, {
      // The type of chart we want to create
      type: 'line',

      // The data for our dataset
      data:  {
          labels: ['T', 'T'],
          datasets: [{
              label: 'Min',
              yAxisID: 'A',
              borderColor: 'rgb(255, 99, 132)',
              fill: true,
              data: [0, 0]
          }
          ,
          {
            label: 'Max',
            yAxisID: 'A',
            borderColor: 'rgb(108, 235, 108)',
            fill: true,
            data: [0, 0]
          }]
      },

      // Configuration options go here
      options: {

        legend: {
            display: false
         },
         elements: {
                      point:{
                          radius: 10
                      },
                  },

          scales:{
            yAxes: [{
              id: 'A',
              type: 'linear',
              position: 'left',

            }]
          },
          layout: {
              padding: {
                  left: 0,
                  right: 0,
                  top: 0,
                  bottom: 0
              }
          }
      }
  });
}

function updateDashboard(){
  tempIn = parseFloat(allData[5]);
  humIn = parseFloat(allData[6]);

  var current = js["current"];
  humOut = parseFloat(current["humidity"]);
  tempOut = parseFloat(current["temp"]);

  tempInGauge.set(tempIn);
  document.getElementById("InTempCell").innerHTML =  +tempIn.toFixed(2) + " C";
  document.getElementById("OutTempCell").innerHTML =  tempOut + " C";
  document.getElementById("HumCell").innerHTML =  humIn + " %";
  document.getElementById("OutHumCell").innerHTML =  humOut + " %";

  document.getElementById("icon").src = current["weather"][0]["icon"] + "2x.svg";
}


function updateDailyForc(){
  var daily = js["daily"];
  var weekDays = ["M", "T", "W", "Th", "F", "St", "Sn"];

  var mins = new Array();
  var maxs = new Array();
  var days = new Array();

  for(var i =0; i < 8; i++){
    var day = daily[i];

    var dayMin = parseInt(day["temp"]["min"]);
    var dayMax = parseInt(day["temp"]["max"]);

    var stemp = day["dt"];
    var date = new Date(stemp * 1000);
    var dayLab = weekDays[date.getDay()];

    mins.push(dayMin);
    maxs.push(dayMax);
    days.push(dayLab);


    var icon = day["weather"][0]["icon"] + "2x.svg";
    document.getElementById("day"+i+"Icon").src = icon;

    document.getElementById("Conditions"+i).innerHTML = "[" + dayMin  + ", "+ dayMax + "]";

    document.getElementById("day"+i).innerHTML = dayLab;
  }

  console.log(mins);

  forecastChart.data.labels = days;

  forecastChart.data.datasets[1].data = mins;
  forecastChart.data.datasets[0].data = maxs;
  
  forecastChart.update();
}
  




  // var weekMin = daily[0]["temp"]["min"];
  // var weekMax = daily[0]["temp"]["max"];
  // var weekRange = 0;

  // var weekDays = ["M", "T", "W", "Th", "F", "St", "Sn"];
  // for(var i = 0; i < 8; i++){
  //   var day = daily[i];

  //   var stemp = day["dt"];
  //   var date = new Date(stemp * 1000);

  //   var min = parseInt(day["temp"]["min"]);
  //   var max = parseInt(day["temp"]["max"]);
  //   weekMin = Math.min(min, weekMin);
  //   weekMax = Math.max(max, weekMax);
  //   weekRange = weekMax-weekMin;

  //   var icon = day["weather"][0]["icon"] + "2x.svg";
  //   document.getElementById("day"+i+"Icon").src = icon;

  //   document.getElementById("Conditions"+i).innerHTML = max  + " C" + "<br>" + min + " C";

  //   if(i==0){
  //       document.getElementById("day"+i).innerHTML = weekDays[date.getDay()];
  //   }else{
  //       document.getElementById("day"+i).innerHTML = weekDays[date.getDay()];
  //   }




  

  // for(var i = 0; i < 8; i++){
  //   var day = daily[i];

  //   var canvasBar = document.getElementById('day'+i+'Bar');
  //   var ctxBar = canvasBar.getContext('2d');
  //   var barw = canvasBar.getBoundingClientRect().width;
  //   var barh = canvasBar.getBoundingClientRect().height;

  //   canvasBar.width = barw;
  //   canvasBar.height = barh;

  //   ctxBar.fillStyle = "yellow";

  //   var min = day["temp"]["min"];
  //   var max = day["temp"]["max"];

  //   var yb = barh - barh/weekRange*(min-weekMin);
  //   var yt = barh - barh/weekRange*(max-weekMin);
  //   ctxBar.fillRect(0, yt, barw, yb-yt);

  // }
// }S

function updateSunDiagram(){
  ctx3.fillStyle = "black";
  ctx3.fillRect(0, 0, cw2, ch2 );


  var hourly = js["hourly"];
  var counter = 0;
  for(var i = 0; i < 24; i++){
    var hourWeather = hourly[i];
    var hour = timestampToTime(hourWeather["dt"]).split(':')[0];
    var color = weatherCodeToColor(hourWeather["weather"][0]["icon"]);
    var condition = hourWeather["weather"][0]["main"];
    // console.log(hour, color, condition);

    var startAngle = parseInt(hour)/24*2*3.1415-3.1415/2;
    var endAngle = (parseInt(hour)+1)/24*2*3.1415-3.1415/2;
    // console.log(startAngle/3.1415*180, endAngle/3.1415*180);

    ctx3.beginPath();
    ctx3.arc(cw2/2, ch2/2, ch2/3, startAngle, endAngle);

    ctx3.lineWidth = 15;
    ctx3.strokeStyle = color;
    ctx3.stroke();




    //sun line
    ctx3.beginPath();
    ctx3.arc(cw2/2, ch2/2, ch2/3-30, startAngle, endAngle);

    ctx3.lineWidth = 2;
    if(hourWeather["weather"][0]["icon"][2] == 'd')
      ctx3.strokeStyle = "gold";
    else
      ctx3.strokeStyle = "black"

    ctx3.stroke();


  }

  ctx3.beginPath();
  for(var i = 0; i <= 24; i++){
    //propbability line
    var ind = i;
    if(i==24){
      ind = 0;
    }
    var pop = parseFloat(hourly[ind]["pop"]);
    var hour = timestampToTime(hourly[ind]["dt"]).split(':')[0];
    var color = "lightblue";

    var angle = (parseInt(hour)+0.5)/24*2*3.1415-3.1415/2;
    var r = ch2/3+8+15*pop;

    ctx3.lineTo(r*Math.cos(angle)+cw2/2, r*Math.sin(angle)+ch2/2);


  }
  ctx3.lineWidth = 2;
  ctx3.strokeStyle = color;
  ctx3.stroke();

  //mark current hour
  var hour = timestampToTime(js["current"]["dt"]).split(':')[0];
  var startAngle = parseInt(hour)/24*2*3.1415-3.1415/2;
  var endAngle = (parseInt(hour)+1)/24*2*3.1415-3.1415/2;

  ctx3.beginPath();
  ctx3.arc(cw2/2, ch2/2, ch2/3-20, startAngle, endAngle);

  ctx3.lineWidth = 4;
  ctx3.strokeStyle = "yellow";
  ctx3.stroke();
}


function timestampToTime(ts){
  var date = new Date(ts * 1000);
  // d
  var hours = date.getHours();
  var minutes = "0" + date.getMinutes();
  return hours + ':' + minutes.substr(-2);
}


function setUpGauge(canvas, min, max, staticZones){

  var opts = {
    angle: -0.2, // The span of the gauge arc
    lineWidth: 0.2, // The line thickness
    radiusScale: 1, // Relative radius
    pointer: {
      length: 0.51, // // Relative to gauge radius
      strokeWidth: 0.064, // The thickness
      color: '#ffe400' // Fill color
    },
    limitMax: false,     // If false, max value increases automatically if value > maxValue
    limitMin: false,     // If true, the min value of the gauge will be fixed
    colorStart: '#6FADCF',   // Colors
    colorStop: '#8FC0DA',    // just experiment with them
    strokeColor: '#E0E0E0',  // to see which ones work best for you
    generateGradient: true,
    highDpiSupport: true,     // High resolution support
    staticZones: [
     {strokeStyle: "#F03E3E", min: 0, max: 0}, // Red from 100 to 130
     {strokeStyle: "#FFDD00", min: 0, max: 0}, // Yellow
     {strokeStyle: "#30B32D", min: 0, max: 0}, // Green
     {strokeStyle: "#FFDD00", min: 0, max: 0}, // Yellow
     {strokeStyle: "#F03E3E", min: 0, max: 0}  // Red
    ],


  };

  if(canvas == "windDirectionGaugeCell"){
    opts["angle"]=-0.5;
    opts["pointer"]["strokeWidth"] = .1;
    opts["pointer"]["color"] ="yellow";
  }else{
    opts["staticZones"] = staticZones;
  }


  var target = document.getElementById(canvas); // your canvas element
  var gauge = new Gauge(target).setOptions(opts); // create sexy gauge!
  gauge.maxValue = max; // set max gauge value
  gauge.setMinValue(min);  // Prefer setter over gauge.minValue = 0
  gauge.animationSpeed = 100; // set animation speed (32 is default value)

  return gauge;
}

function weatherCodeToColor(code){
    var greenCodes = new Array("01d", "02d", "01n", "02n");
    var lightCodes = new Array("03d",  "03n");
    var grayCodes = new Array("04d", "04d", "50d", "04n", "04n", "50n");
    var blueCodes = new Array("10d","09d", "13d","10n", "09n", "13n");
    var yellowCodes = new Array("11d","11n");

    if(greenCodes.includes(code))
      return "green";
    else if(lightCodes.includes(code))
      return "lightgray";
    else if(grayCodes.includes(code))
      return "gray";
    else if(blueCodes.includes(code))
      return "blue";
    else if(yellowCodes.includes(code))
      return "yellow";
    else{
      // console.log("no code:", code);
      return "black";
    }
}

function loadHandler(){
  console.log("Dimentions:", document.body.clientWidth, document.body.clientHeight, document.body.clientWidth/document.body.clientHeight);

  if(document.body.clientWidth/document.body.clientHeight > 1){ //tablet
    console.log("tablet");
    document.getElementById("phoneContent").remove();

  }else{ //phone
    console.log("phone");
    // document.body.parentNode.removeChild(document.getElementById("tabletContent"));
    document.getElementById("tabletContent").remove();
  }

}

function TVPower(){
  connection.send("power");
}
function TVUnlock(){
  connection.send("unlock");
}
function sendColor(){
  connection.send('r' + colorPicker.color.red + ',' + colorPicker.color.green + ',' + colorPicker.color.blue);
}
