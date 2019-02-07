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
	}).then(res => {
		if(res.ok){
			window.location = 'http://localhost:5000/users/show'
		}
		else {
			alert('Location not saved')
		}
	})
}