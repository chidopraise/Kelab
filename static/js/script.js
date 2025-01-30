// this is Javascript
$(document).ready(function(){

	
	
/* This Is Triggered On Click Of A Link Which takes Users to a particular Section Id */
	$(".navigate").on("click", function(){
		let classs = "."+$(this).attr('id');
		$("#index").hide();
		$(".section").hide();
		$(classs).show();
		$(".navbar-collapse").slideUp();
		//$('body').animate({scrollTop: '0px'}, 0);
		//$('body').scrollTop(0);
		
	});
	
	
/* This Code is to Enable The Page Remain Even After Refresh */
	// Get the current page URL
	const url = window.location.href;

	// Extract the hash part
	const section = url.split("#")[1]; // Splitting manually
	if(section){
		let nav_link = $('#'+section).attr('title');
		let classs = "."+ nav_link;
		$("#index").hide();
		$(".section").hide();
		$(classs).show();
		
		//alert(classs);
	}else{
		// The Default Page And Position On Initial load
		$(".section").hide();
		$("#index").show(4000);
		setTimeout(function(){
			$("#index").hide(4000);
			window.location.href='#home';
			$(".home1").show(5000);
			},5000);
		//$(".navbar-toggler").on("click", function(){
			//$(".navbar-collapse").show();
		//});
	}
});



/* This code here refreshes the page on click of a backward or forward button */
//window.addEventListener('popstate', (event) => {
    //console.log('Back or forward button clicked!');
    //console.log('Refreshing the page...');
    //location.reload(); // Reload the page
	//$('body').scrollTop(0);
	//window.location.href = "/home/";
//});

/* This Controls The Button / Element toggling of Frequent Aked Questions Found in Driver Page */
document.querySelectorAll('.faq-question').forEach((button) => {
  button.addEventListener('click', () => {
    const faqItem = button.parentElement;

    // Toggle the active class
    faqItem.classList.toggle('active');

    // Close others if needed
    document.querySelectorAll('.faq-item').forEach((item) => {
      if (item !== faqItem) {
        item.classList.remove('active');
      }
    });
  });
});


///////////   This handles Visitors Form out of service///////////////////////
function generateAccessCode() {
	const apartment = document.getElementById('apartment').value;
	const guestName = document.getElementById('guestName').value;
	const arrivalDate = document.getElementById('arrivalDate').value;
	const arrivalTimeFrom = document.getElementById('arrivalTimeFrom').value;
	const arrivalTimeTo = document.getElementById('arrivalTimeTo').value;
	const shareQRCode = document.getElementById('shareQRCode').checked;

	const accessCode = `Access Code Generated:\n\nApartment: ${apartment}\nGuest Name: ${guestName}\nArrival Date: ${arrivalDate}\nTime: ${arrivalTimeFrom} to ${arrivalTimeTo}\nShare QRCode: ${shareQRCode}`;
	alert(accessCode);
}



//////////// This Handles The Sign up Page /////////////////
function submitForm() {
	const email = document.getElementById('owners_email').value;
	const password = document.getElementById('owners_password').value;
	const repeatPassword = document.getElementById('owners_repeatPassword').value;
	const estateName = document.getElementById('owners_estateName').value;
	const houseAddress = document.getElementById('owners_houseAddress').value;
	const flat = document.getElementById('owners_flat').value;
	const role = document.getElementById('owners_role').value;

	if (password !== repeatPassword) {
		alert('Passwords do not match!');
		return;
	}

	const formData = {
		email,
		password,
		estateName,
		houseAddress,
		flat,
		role
	};

	alert(`Form Submitted:\n\nEmail: ${formData.email}\nEstate Name: ${formData.estateName}\nHouse Address: ${formData.houseAddress}\nFlat: ${formData.flat}\nRole: ${formData.role}`);
}


////////// This Handles The Profile Page ///////////////////
function updatePicture() {
	const fileInput = document.getElementById('uploadPicture');
	const profilePicDiv = document.getElementById('profilePicture');

	if (fileInput.files && fileInput.files[0]) {
		const reader = new FileReader();
		reader.onload = function(e) {
			profilePicDiv.style.backgroundImage = `url(${e.target.result})`;
			profilePicDiv.style.backgroundSize = 'cover';
			profilePicDiv.style.backgroundPosition = 'center';
			profilePicDiv.textContent = '';
		};
		reader.readAsDataURL(fileInput.files[0]);
	}
}
function saveProfile() {
	const fullName = document.getElementById('fullName').value;
	const emailAddress = document.getElementById('emailAddress').value;
	const phoneNumber = document.getElementById('phoneNumber').value;
	const apartmentAddress = document.getElementById('apartmentAddress').value;
	const maritalStatus = document.getElementById('maritalStatus').value;
	const gender = document.getElementById('gender').value;

	const profileData = {
		fullName,
		emailAddress,
		phoneNumber,
		apartmentAddress,
		maritalStatus,
		gender
	};

	alert(`Profile Saved:\n\nFull Name: ${profileData.fullName}\nEmail: ${profileData.emailAddress}\nPhone: ${profileData.phoneNumber}\nApartment: ${profileData.apartmentAddress}\nMarital Status: ${profileData.maritalStatus}\nGender: ${profileData.gender}`);
}



// JavaScript for handling form submission
document.getElementById('monthlyDuesForm').addEventListener('submit', function(event) {
	event.preventDefault();
	const accountNumber = document.getElementById('accountNumber').value;
	const houseAddress = document.getElementById('houseAddress').value;
	const apartment = document.getElementById('apartment').value;
	const amount = document.getElementById('amount').value;
	const receiptScreenshot = document.getElementById('receiptScreenshot').files[0];

	if (!receiptScreenshot) {
		alert("Please upload a screenshot of the receipt.");
		return;
	}

	alert(`Dues submitted successfully! Details:\nAccount Number: ${accountNumber}\nHouse Address: ${houseAddress}\nApartment: ${apartment}\nAmount: ${amount}`);
	// Add logic to send data to a server here
});



//// this controls owners Form /////////
document.getElementById('ownersForm').addEventListener('submit', function (event) {
	event.preventDefault();

	// Collect form data
	const fullName = document.getElementById('fullName').value;
	const emailAddress = document.getElementById('emailAddress').value;
	const phoneNumber = document.getElementById('phoneNumber').value;
	const houseAddress = document.getElementById('houseAddress').value;
	const maritalStatus = document.getElementById('maritalStatus').value;
	const gender = document.getElementById('gender').value;
	const numberOfResidents = document.getElementById('numberOfResidents').value;

	// For demonstration: Log collected data
	console.log({
		fullName,
		emailAddress,
		phoneNumber,
		houseAddress,
		maritalStatus,
		gender,
		numberOfResidents
	});

	// You can process the data here (e.g., send it to a server)
	alert('Form submitted successfully!');
});


document.getElementById('residentsForm').addEventListener('submit', function (event) {
	event.preventDefault();

	// Collect form data
	const tenantName = document.getElementById('tenantName').value;
	const tenantEmail = document.getElementById('tenantEmail').value;
	const tenantPhone = document.getElementById('tenantPhone').value;
	const apartmentNumber = document.getElementById('apartmentNumber').value;
	const maritalStatus = document.getElementById('maritalStatus').value;
	const gender = document.getElementById('gender').value;
	const occupation = document.getElementById('occupation').value;

	// For demonstration: Log collected data
	console.log({
		tenantName,
		tenantEmail,
		tenantPhone,
		apartmentNumber,
		maritalStatus,
		gender,
		occupation
	});

	// Process the data (e.g., send to server)
	alert('Resident added successfully!');
});


/////////// This Code Handles Visitors Access Code ////////////
function shareCode() {
	const code = document.getElementById("code").innerText;
	if (navigator.share) {
		navigator.share({
			title: 'Visitor Access Code',
			text: `Here is the access code: ${code}`,
		}).then(() => console.log('Shared successfully!'))
		  .catch(err => console.error('Error sharing:', err));
	} else {
		alert('Sharing not supported on this device!');
	}
}

// Send SMS
function sendSMS() {
	const code = document.getElementById("code").innerText;
	const smsLink = `sms:?&body=Here is the access code: ${code}`;
	window.location.href = smsLink;
}

// Send WhatsApp
function sendWhatsApp() {
	const code = document.getElementById("code").innerText;
	const whatsappLink = `https://wa.me/?text=Here is the access code: ${code}`;
	window.open(whatsappLink, '_blank');
}

// Copy to Clipboard
function copyToClipboard() {
	const code = document.getElementById("code").innerText;
	navigator.clipboard.writeText(code).then(() => {
		alert('Access code copied to clipboard!');
	}).catch(err => {
		console.error('Error copying to clipboard:', err);
		alert('Failed to copy!');
	});
}


//////////////// This Code Handles The Sign In Page ///////////////
document.getElementById("signInForm").addEventListener("submit", function(event) {
	event.preventDefault(); // Prevent default form submission
	const usernameEmail = document.getElementById("login_email").value;
	const password = document.getElementById("login_password").value;

	if (usernameEmail === "" || password === "") {
		alert("Please fill in all fields.");
	} else {
		//alert(`Processing..... ${usernameEmail} in...`);
		// Add logic for actual sign-in here (e.g., API call)
	}
});

// Handle forgot password link
function forgotPassword() {
	alert("Redirecting to forgot password page...");
	// Replace this with actual navigation logic
}



//////////////////This Code Handles The Payments Page /////////////
function handlePayment(paymentType) {
	alert(`You selected ${paymentType}. Redirecting to payment page...`);
	// Replace with actual logic (e.g., navigation or API call)
}



///////////// This Handles Emergency Botton / For Automatic dialing phone number //////
function dialPhoneNumber(phoneNumber) {
    if (!phoneNumber) {
        console.error("Phone number is required.");
        return;
    }

    // Create a link with the `tel:` protocol
    const telLink = document.createElement("a");
    telLink.href = `tel:${phoneNumber}`;

    // Programmatically trigger the link
    telLink.click();
}



///////// Function for handling Security "Input Access Code"
function inputAccessCode() {
	const accessCode = prompt("Please enter the access code:");
	if (accessCode) {
		alert(`Access code ${accessCode} verified!`);
		// Add further logic for validation or navigation
	} else {
		alert("Access code cannot be empty.");
	}
}


/**
////////////////Here we placed the Geolocation code/////////////////////////////////////
// Function to initialize the map
function initializeMap() {
	// Create the map
	const map = L.map('map').setView([0, 0], 13); // Default view

	// Add OpenStreetMap tiles
	L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
		maxZoom: 19,
		attribution: '© OpenStreetMap contributors'
	}).addTo(map);

	// Geolocation to get the user's current position
	if (navigator.geolocation) {
		navigator.geolocation.getCurrentPosition(
			(position) => {
				const { latitude, longitude } = position.coords;
				// Set the map view to user's location
				map.setView([latitude, longitude], 13);

				// Add a marker for the user's location
				L.marker([latitude, longitude])
					.addTo(map)
					.bindPopup('You are here!')
					.openPopup();
			},
			(error) => {
				console.error("Geolocation error:", error.message);
				alert("Unable to retrieve your location. Please check your settings.");
			}
		);
	} else {
		alert("Geolocation is not supported by your browser.");
	}
}

// Initialize the map when the page loads
window.onload = initializeMap;


let map;
let geocoder;

function initMap() {
	// Get the current location of the user and set as the center of the map
	if (navigator.geolocation) {
		navigator.geolocation.getCurrentPosition(function(position) {
			const currentPosition = {
				lat: position.coords.latitude,
				lng: position.coords.longitude
			};

			map = new google.maps.Map(document.getElementById('maps'), {
				center: currentPosition,
				zoom: 13
			});

			new google.maps.Marker({
				map: map,
				position: currentPosition,
				title: "Your location"
			});

			/*alert(currentPosition.lat+','+currentPosition.lng);
			let cord = "'"+currentPosition.lat+","+currentPosition.lng+"'";
			document.getElementById("cord").innerHTML = cord;
			if(page_id == 1){
				setInterval('load("cord", "lib/profile.php", '+cord+')',16000);
			}else{
				setInterval('load("cord", "../lib/profile.php", '+cord+')',16000);
			}
			/
			
			//alert(document.getElementById("cord").value);

		}, function() {
			handleLocationError(true, map.getCenter());
		});
	} else {
		// Browser doesn't support Geolocation
		handleLocationError(false, map.getCenter());
	}
	geocoder = new google.maps.Geocoder();
}

function handleLocationError(browserHasGeolocation, pos) {
	alert(browserHasGeolocation ? "Error: The Geolocation service failed." : "Error: Your browser doesn't support geolocation.");
}
**/