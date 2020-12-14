function getBathValue() {
  var uiBathrooms = document.getElementsByName("uiBathrooms");
  for(var i in uiBathrooms) {
    if(uiBathrooms[i].checked) {
        return parseInt(i)+1;
    }
  }
  return -1; // Invalid Value
}

function getSuiteValue() {
  var uiSuites = document.getElementsByName("uiSuites");
  for(var i in uiSuites) {
    if(uiSuites[i].checked) {
        return parseInt(i)+1;
    }
  }
  return -1; // Invalid Value
}

function getParkValue() {
  var uiParking = document.getElementsByName("uiParking");
  for(var i in uiParking) {
    if(uiParking[i].checked) {
        return parseInt(i)+1;
    }
  }
  return -1; // Invalid Value
}



function getRoomsValue() {
  var uiRooms = document.getElementsByName("uiRooms");
  for(var i in uiRooms) {
    if(uiRooms[i].checked) {
        return parseInt(i)+1;
    }
  }
  return -1; // Invalid Value
}

function getParkingValue() {
  var Parking = document.getElementsByName("Parking");
  for(var i in Parking) {
    if(Parking[i].checked) {
        return parseInt(i)+1;
    }
  }
  return -1; // Invalid Value
}

function onClickedEstimatePrice() {
  var area = document.getElementById("uiSqft");
  var rooms = getRoomsValue();
  var bathrooms = getBathValue();
  var parkings = getParkValue();
  var suites = getSuiteValue(); 
  var neighborhood = document.getElementById("uiLocations");
  var estPrice = document.getElementById("uiEstimatedPrice");

  console.log(area.value, rooms, bathrooms, parkings, suites, neighborhood.value)
  var url = "http://127.0.0.1:5000/predict_price"; 

  $.post(url, {
      area: parseFloat(area.value),
      rooms: rooms,
      bathrooms: bathrooms,
      parkings: parkings,
      suites: suites,
      neighborhood: neighborhood.value,
  },function(data, status) {
      estPrice.innerHTML = "<h2>" + data.estimated_price.toString() + " R$</h2>";
      console.log(status);
  });
}

function onPageLoad() {

  var url = "/api/get_location_names";
}

window.onload = onPageLoad;