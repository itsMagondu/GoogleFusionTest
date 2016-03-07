
var key = 'AIzaSyCbrQhFZ1je_6JBQqxL4EUc4UDz5pVplXM';
var table = '1UbnbcY4LOlfyrXzW3DwKmziMqYwUr1KOBA0UstY7';
var body = "";//table info

google.load('visualization', '1', { packages: ['table'] });
//google.setOnLoadCallback(drawTable);

$(document).ready(function(){/* google maps -----------------------------------------------------*/
google.maps.event.addDomListener(window, 'load', initialize);

function initialize() {

  /* position Nairobi */
  var latlng = new google.maps.LatLng(-1.2921, 36.8219);

  var mapOptions = {
    center: latlng,
    scrollWheel: false,
    zoom: 13
  };
   
  
  var map = new google.maps.Map(document.getElementById("map-canvas"), mapOptions);

  var layer = new google.maps.FusionTablesLayer({
          query: {
            select: 'Latitude',
            from: '1UbnbcY4LOlfyrXzW3DwKmziMqYwUr1KOBA0UstY7',
          },
          map: map
        });


    google.maps.event.addListener(map, 'click', function(evt) {

    var geocoder = new google.maps.Geocoder();
    // Geocode the address
    geocoder.geocode({'location':evt.latLng}, function(results, status){
        if (status === google.maps.GeocoderStatus.OK && results.length > 0) {
            add_map_marker(map,evt.latLng)
            add_location(evt.latLng,results)
    // show an error if it's not
        }else alert("Addess not found");
    });
});
}
/* end google maps -----------------------------------------------------*/
});

function add_location(latlng,results){
  ///Store the found location on the db and also on fusiontables
  var lat = latlng.lat();
  var lng = latlng.lng();
  var res = '';

  results.forEach(function(r) {
    res += r['formatted_address'] + ' | ';
  });

  //Store the result in a db using a django view
  $.ajax({
    type: 'GET',
    url : "/location/?lat="+lat+"&lng="+lng+"&location="+res,
   dataType: "json",
   success: function(data) {
    //do a check as to what message was returned. Either error or success
    drawTable(res,lat,lng);
    alert('data successfully stored on the app');
   }
});
}

function add_map_marker(map,latlng) {
  //var latlng = new google.maps.LatLng(lat,lng);
  var marker = new google.maps.Marker({
    position: latlng,
    map:map,
    url: '/',
    animation: google.maps.Animation.DROP
  }); 
  marker.setMap(map);
}
function drawTable(location,lat,lng) {
    body += '<tr><td>'+location+'</td><td>'+lng+'</td><td>'+lat+'</td></tr>';
    $('#body').empty();
    document.getElementById("body").innerHTML += body;
       }
