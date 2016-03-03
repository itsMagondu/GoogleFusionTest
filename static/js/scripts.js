
$(document).ready(function(){/* google maps -----------------------------------------------------*/
google.maps.event.addDomListener(window, 'load', initialize);

function initialize() {

  /* position Amsterdam */
  var latlng = new google.maps.LatLng(-1.2921, 36.8219);

  var mapOptions = {
    center: latlng,
    scrollWheel: false,
    zoom: 13
  };
  
  var marker = new google.maps.Marker({
    position: latlng,
    url: '/',
    animation: google.maps.Animation.DROP
  }); 
  
  var map = new google.maps.Map(document.getElementById("map-canvas"), mapOptions);

  var layer = new google.maps.FusionTablesLayer({
          query: {
            select: 'Location',
            from: '1UbnbcY4LOlfyrXzW3DwKmziMqYwUr1KOBA0UstY7',
          },
          map: map
        });
  marker.setMap(map);

    google.maps.event.addListener(map, 'click', function(evt) {

    var geocoder = new google.maps.Geocoder();
    // Geocode the address
    geocoder.geocode({'location':evt.latLng}, function(results, status){
      console.log(results);
        if (status === google.maps.GeocoderStatus.OK && results.length > 0) {
            add_marker(map,evt)
              add_location(evt.latLng,results)
    // show an error if it's not
        }else alert("Addess not found");
    });
});
}
/* end google maps -----------------------------------------------------*/
});

function add_marker(map,e){
    new google.maps.Marker({
            position: e.latLng,
            map: map,
            icon: {
              path: google.maps.SymbolPath.BACKWARD_CLOSED_ARROW,
              fillOpacity: .2,
              strokeColor: 'red',
              strokeWeight: .5,
              scale: 10
            }
          });
}


function add_location(latlng,results){
  ///Store the found location on the db and also on fusiontables
  var lat = latlng.lat();
  var lng = latlng.lng();
  var res = '';

  results.forEach(function(r) {
    res += r['formatted_address'] + ' | ';
  });

  $.ajax({
    type: 'GET',
    url : "/location/?lat="+lat+"&lng="+lng+"&location="+res,
   dataType: "json",
   success: function(data) {
    //do a check as to what message was returned. Either error or success
    alert('data successfully stored on the app')
   }
});

}
