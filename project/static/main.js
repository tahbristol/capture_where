let saveLocationButton = document.getElementById('saveLocation');
saveLocationButton.addEventListener('click', function(e){
	navigator.geolocation.getCurrentPosition(usePosition);	
});

function usePosition(position){
	let lat = position.coords.latitude;
	let long = position.coords.longitude;	
	let note = document.querySelector('#noteContainer input').value;
	
	fetch('/users/location',{
		method: 'POST',
		body: JSON.stringify({lat: lat, long: long, note: note}),
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

let logout = document.getElementById('logout');
logout.addEventListener('click', function(e){
	if(!confirm("Are you sure you want to logout?")){
		e.preventDefault();
	}
});