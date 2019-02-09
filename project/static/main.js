let saveLocationButton = document.getElementById('saveLocation');
saveLocationButton.addEventListener('click', function(e){
	navigator.geolocation.getCurrentPosition(usePosition);	
});

function usePosition(position){
	let url_base;
	let lat = position.coords.latitude;
	let long = position.coords.longitude;	
	let note = document.querySelector('#noteContainer input').value;
	if(window.location.hostname == 'localhost'){
		url_base = '/'
	}
	else {
		url_base = 'https://capturewhere.herokuapp.com/'
	}
	fetch(`${url_base}users/location`,{
		method: 'POST',
		body: JSON.stringify({lat: lat, long: long, note: note}),
		headers:{
			'Content-Type': 'application/json'
		}
	}).then(res => {
		if(res.ok){
			window.location = `${url_base}users/show`
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