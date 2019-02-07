let saveLocationButton = document.getElementById('saveLocation');
saveLocationButton.addEventListener('click', function(e){
	navigator.geolocation.getCurrentPosition(usePosition);	
});

function usePosition(position){
	let lat = position.coords.latitude;
	let long = position.coords.longitude;	
	
	fetch('/users/location',{
		method: 'POST', // or 'PUT'
		body: JSON.stringify({lat: lat, long: long}), // data can be `string` or {object}!
		headers:{
			'Content-Type': 'application/json'
		}
	})
	//let url = `https://maps.googleapis.com/maps/api/geocode/json?latlng=${lat},${long}&key=${api_key}`
	
}