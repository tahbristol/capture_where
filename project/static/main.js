// Template for adding addresses aynchronously
function makeTemplate(location, note, id){
	let url_base = getBaseUrl();
	let address_template = `
			<li class="list-group-item addresses">
				<p>
					<strong>Address:</strong> ${location}
				</p>
				<p>
					<strong>Note:</strong> ${note}
				</p>
				<form action="${url_base}address/delete/${id}" method="POST">
					<input type="hidden" name="_method" value="DELETE" />
					<input class="btn btn-secondary" type="submit" value="Delete" />
				</form>
			</li>
				`;
	return address_template;
}

// Determine base url for dev vs prod environment
function getBaseUrl(){
	let url_base;
	
	if(window.location.hostname == 'localhost'){
		return url_base = '/';
	}
	else {
		return url_base = 'https://capturewhere.herokuapp.com/';
	}
}

// Save location button event listener
let saveLocationButton = document.getElementById('saveLocation');
saveLocationButton.addEventListener('click', function(e){
	navigator.geolocation.getCurrentPosition(usePosition);	
});

// Logout event listener
let logout = document.getElementById('logout');
logout.addEventListener('click', function(e){
	if(!confirm("Are you sure you want to logout?")){
		e.preventDefault();
	}
});

// Get coords then send to route to get address via api
function usePosition(position){
	let url_base = getBaseUrl();
	let lat = position.coords.latitude;
	let long = position.coords.longitude;	
	let note = document.querySelector('#noteContainer input').value;
	
	fetch(`${url_base}users/location`,{
		method: 'POST',
		body: JSON.stringify({lat: lat, long: long, note: note}),
		headers:{
			'Content-Type': 'application/json'
		}
	}).then(res => res.json())
	.then(data => {
		let address = data[0];
		let template_html = makeTemplate(address.location, address.note, address.id);
		let ulList = document.getElementById('addressList');
		let ulListContents = ulList.innerHTML.trim();
		let ulListUpdated = ulListContents + template_html;
		ulList.innerHTML = ulListUpdated;
		
		document.querySelector('#noteContainer input').value = '';
	})
}
