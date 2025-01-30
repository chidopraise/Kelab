<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{{ title }}</title>
	<link rel="icon" href="{{ url_for('static', filename='images/logo.jpeg') }}" />
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/bootstrap/5.3.0/css/bootstrap.min.css">
    <link href="https://cdn.jsdelivr.net/npm/bootstrap-icons/font/bootstrap-icons.css" rel="stylesheet" />
	<link href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.15.4/css/all.min.css" rel="stylesheet" />
    <link rel="stylesheet" href="https://unpkg.com/leaflet@1.9.4/dist/leaflet.css" />
    <script src="https://unpkg.com/leaflet@1.9.4/dist/leaflet.js"></script>

	<link rel="stylesheet" href="{{ url_for('static', filename='css/style.css') }}">
</head>
<body id="body">

<!--------- The Index Page is Identified and starts here id=drive -------------->
<!--------- The Index Page is Identified and starts here id=drive -------------->

<img src="{{ url_for('static', filename='images/logo_0.jpeg') }}"id="index" class="section" style="width:100%; height:800px;">

<!--------------------------- The Index Page Ends Here ------------------------>
<!--------------------------- The Index Page Ends Here ------------------------>













<!--------------------------- The Home Page Starts Here ------------------------>
<!--------------------------- The Home Page Starts Here ------------------------>




<div id="home" class="container-fluid p-3 section home1 owner1 reg_resident1 visitor1 signup1 profile1 monthly_dues1 visitors_code1 signin1 payments1 residents1 signup_intro1 security1" title="home1">
    <!-- Navigation -->
    <div class="d-flex justify-content-between align-items-center mb-3 bg-black fixed-top">
        <button class="btn btn-light" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
            <i class="bi bi-list"></i>
        </button>
        <img src="{{ url_for('static', filename='images/logo.jpeg') }}" alt="Logo" class="img_logo">
        <button class="btn btn-light">
            <i class="bi bi-envelope"></i>
        </button>
    </div>
    <div class="collapse navbar-collapse" id="navbarNav" style="position:fixed; top:5%; background:#000; width:100%;">
            <ul class="navbar-nav ms-auto">
				<li class="nav-item">
                    <a id="home1" class="nav-link navigate" href="{{ url_for('home') }}">Home</a>
                </li>
				<li class="nav-item">
                    <a id="visitor1" class="nav-link navigate" href="{{ url_for('visitors') }}">Visitors</a>
                </li>
                <li class="nav-item">
                    <a id="visitors_code1" class="nav-link navigate" href="{{ url_for('visitors_code') }}">Visitors Code</a>
                </li>
                <li class="nav-item">
                    <a id="owner1" class="nav-link navigate" href="{{ url_for('owner') }}">Owner</a>
                </li>
				<li class="nav-item">
                    <a id="monthly_dues1" class="nav-link navigate" href="{{ url_for('monthly_dues') }}">Monthly Dues</a>
                </li>
				<li class="nav-item">
                    <a id="profile1" class="nav-link navigate" href="{{ url_for('profile') }}">Profile</a>
                </li>
                <li class="nav-item">
                    <a id="residents1" class="nav-link navigate" href="{{ url_for('residents') }}">Residents</a>
                </li>
                <li class="nav-item">
                    <a id="security1" class="nav-link navigate" href="{{ url_for('security') }}">Security</a>
                </li>
                <li class="nav-item">
                    <a id="reg_residents1" class="nav-link navigate" href="{{ url_for('reg_residents') }}">Reg residents</a>
                </li>
                <li class="nav-item">
                    {% if session['user_id'] %}
                        <a id="home1" class="nav-link navigate" href="{{ url_for('logout') }}">Logout</a>
                    {% else %}
                        <a id="signin1" class="nav-link navigate" href="{{ url_for('signin') }}">Log in</a>
                    {% endif %}
                </li>
                <li class="nav-item">
                    {% if not session['user_id'] %}
                        <a id="signup_intro1" class="nav-link navigate btn btn-dark text-light" href="{{ url_for('signup_intro') }}">Sign up</a>
                    {% endif %}
                </li>
            </ul>
        </div>

    <!-- Search Bar -->
    <div class="mb-3 section home1">
    <br />
    
    <!-------------- Here I Placed The Users Firsr Name And Last Name ON Login ---->
    <!-------------- Here I Placed The Users Firsr Name And Last Name ON Login ---->
    {% if session['user_id'] %}
        <div class="text-center text-black">Hello! {{ session['first_name']+"  "+session['last_name'] }} </div>
    {% endif %}
    <!------------ First And Last Name Ends Here ---------------->
    <!------------ First And Last Name Ends Here ---------------->
    
    <br />
        <input type="text" class="form-control search-bar" placeholder="Search">
    </div>

    <!-- Profile Card -->
    <div class="profile-card d-flex align-items-center section home1">
        <img src="{{ url_for('static', filename='images/search_person.PNG') }}" alt="Profile" class="section home1" style="width: 50px; height: 50px;">
        <div class="section home1">
            <h5 class="mb-0">Liberty Estate</h5>
            <p class="mb-0">FH29+669, Mobil Estate Rd, Aja, Lekki 106104,<br>Lagos, Nigeria.</p>
        </div>
    </div>
    
    <div class="text-center"> {{ response }} </div>

    <!-- House Image -->
    <div class="mb-3 section home1">
        <img src="{{ url_for('static', filename='images/img.jpg') }}" alt="House" class="img-fluid rounded" style="width:100%;">
        <marquee class="mb-0" style="position:absolute; bottom:35%; left:30%; right:30%; font-weight:bold; ">*** Powered by: Ixora Consulting Ltd ***</marquee>
    </div>

    <!-- Navigation Buttons -->
    <div class="d-flex justify-content-between fixed-bottom section home1">
        <a href="{{ url_for('visitors') }}" id="visitor1" class="icon-btn section home1 navigate">
            <img src="{{ url_for('static', filename='images/locate.jpeg') }}" alt="Visitors" class="down_nav">
            <span>VISITORS</span>
        </a>
        <a href="#home" id="home1" class="icon-btn section home1 navigate" onclick="dialPhoneNumber('08109214791');">
            <img src="{{ url_for('static', filename='images/caution.jpeg') }}" alt="Emergency" class="down_nav">
            <span>EMERGENCY</span>
        </a>
        <a href="{{ url_for('payments') }}" id="payments1" class="icon-btn section home1 navigate">
            <img src="{{ url_for('static', filename='images/wallet.jpeg') }}" alt="Payments" class="down_nav">
            <span>PAYMENTS</span>
        </a>
        <a href="{{ url_for('residents') }}" id="residents1" class="icon-btn section home1 navigate">
            <img src="{{ url_for('static', filename='images/resident.jpeg') }}" alt="Residents" class="down_nav">
            <span>RESIDENTS</span>
        </a>
    </div>
</div>

<!--------------------------- The Home Page Ends Here ------------------------>
<!--------------------------- The Home Page Ends Here ------------------------>









<!--------------------------- The Sign Up Intro Page Starts Here ------------------------>
<!--------------------------- The Sign Up Intro Page Starts Here ------------------------>

<!-- Header Section -->
<div id="signup_intro" class="align-items-center mb-3 section signup_intro1" title="signup_intro1">
    <a href="{{ url_for('home') }}" class="back-btn me-3">
        <i class="bi bi-arrow-left"></i>
    </a>
    <h3 class="text-center mb-4 text-black">Sign Up</h3>
</div>

<div class="containerr section signup_intro1">
    <!-- Sign Up Intro Options -->
    <button class="residents-btn" onclick="window.location.href = {{ url_for('admin_signup')}}">Admin Sign Up</button>
    <button class="residents-btn" onclick="window.location.href = {{ url_for('owners_signup')}}">Owners Sign Up</button>
    <button class="residents-btn" onclick="window.location.href = {{ url_for('resident_signup')}}">Tenant Sign Up</button>
    <button class="residents-btn" onclick="window.location.href = {{ url_for('security_signup')}}">Security Sign Up</button>
</div>
<!--------------------------- The Sign Up Intro Page Ends Here ------------------------>
<!--------------------------- The Sign Up Intro Page Ends Here ------------------------>









<!------------------------- The Admin Sign up Page Starts Here ------------------------>
<!------------------------- The Admin Sign up Page Starts Here ------------------------>

<div id="admin_signup" class="section admin_signup1 signup_body" title="admin_signup1">
    <div class="container">
        <div class="header-buttons">
            <button class="btn btn-outline-light" onclick="window.location.href = {{ url_for('signin') }}">SIGN IN</button>
            <button class="btn btn-outline-light" onclick="window.location.href = {{ url_for('signup_intro') }}">SIGN UP</button>
        </div>
        <a href="{{ url_for('signup_intro') }}" class="back-btn me-3">
            <i class="bi bi-arrow-left"></i>
        </a>
        <h2 class="text-center">SIGN UP</h2>
        <form action="{{ url_for('index') }}" method="post" id="signUpForm">
            <div class="mb-3">
                <input type="email" class="form-control" id="username" name="email" placeholder="Username/Email" required>
            </div>
            <div class="mb-3">
                <input type="password" class="form-control" id="admin_password" name="password" placeholder="Password" required>
            </div>
            <div class="mb-3">
                <input type="password" class="form-control" id="admin_repeatPassword" name="re_password" placeholder="Repeat Password" required>
            </div>
            <div class="mb-3">
                <input type="text" class="form-control" id="estateName" name="estate" placeholder="Estate Name" required>
            </div>
            <div class="mb-3">
                <input type="text" class="form-control" id="houseAddress" name="address" placeholder="Admin House Address" required>
            </div>
            <div class="mb-3">
                <input type="number" class="form-control" id="flat" name="flat" placeholder="Your Flat Number">
            </div>
            <div class="mb-3">
                <input type="hidden" class="form-control" id="role" name="role" placeholder="role" value="admin" required>
            </div>
            <button type="submit" class="btn btn-primary w-100 bg-black" name="admin_signup" onclick="submitForm()">Submit</button>
        </form>
    </div>
</div>
<!--------------------------- The Admin Sign up Page Ends Here ------------------------>
<!--------------------------- The Admin Sign up Page Ends Here ------------------------>










<!------------------------- The Owners Sign up Page Starts Here ------------------------>
<!------------------------- The Owners Sign up Page Starts Here ------------------------>

<div id="owners_signup" class="section owners_signup1 signup_body" title="owners_signup1">
    <div class="container">
        <div class="header-buttons">
            <button class="btn btn-outline-light" onclick="window.location.href = {{ url_for('signin') }}">SIGN IN</button>
            <button class="btn btn-outline-light" onclick="window.location.href = {{ url_for('signup_intro') }}">SIGN UP</button>
        </div>
        <a href="{{ url_for('signup_intro') }}" class="back-btn me-3">
            <i class="bi bi-arrow-left"></i>
        </a>
        <h2 class="text-center">SIGN UP</h2>
        <form action="{{ url_for('index') }}" method="post" id="signUpForm">
            <div class="mb-3">
                <input type="email" class="form-control" id="owners_email" name="owners_email" placeholder="Email" required>
            </div>
            <div class="mb-3">
                <input type="password" class="form-control" id="owners_password" name="owners_password" placeholder="Password" required>
            </div>
            <div class="mb-3">
                <input type="password" class="form-control" id="owners_repeatPassword" name="owners_re_password" placeholder="Repeat Password" required>
            </div>
            <div class="mb-3">
                <input type="text" class="form-control" id="owners_estateName" name="owners_estate" placeholder="Estate Name" required>
            </div>
            <div class="mb-3">
                <input type="text" class="form-control" id="owners_houseAddress" name="owners_address" placeholder="Owner House Address" required>
            </div>
            <div class="mb-3">
                <input type="number" class="form-control" id="owners_flat" name="owners_flat" placeholder="Your Flat Number">
            </div>
            <div class="mb-3">
                <input type="hidden" class="form-control" id="owners_role" name="owners_role" placeholder="role" value="owner" required>
            </div>
            <button type="submit" class="btn btn-primary w-100 bg-black" name="owners_signup" onclick="submitForm()">Submit</button>
        </form>
    </div>
</div>
<!--------------------------- The Owners Sign up Page Ends Here ------------------------>
<!--------------------------- The Owners Sign up Page Ends Here ------------------------>









<!------------------------- The resident Sign up Page Starts Here ------------------------>
<!------------------------- The resident Sign up Page Starts Here ------------------------>

<div id="resident_signup" class="section resident_signup1 signup_body" title="resident_signup1">
    <div class="container">
        <div class="header-buttons">
            <button class="btn btn-outline-light" onclick="window.location.href = {{ url_for('signin') }}">SIGN IN</button>
            <button class="btn btn-outline-light" onclick="window.location.href = {{ url_for('signup_intro') }}">SIGN UP</button>
        </div>
        <a href="{{ url_for('signup_intro') }}" class="back-btn me-3">
            <i class="bi bi-arrow-left"></i>
        </a>
        <h2 class="text-center">SIGN UP</h2>
        <form action="{{ url_for('index') }}" method="post" id="signUpForm">
            <div class="mb-3">
                <input type="email" class="form-control" id="username" name="email" placeholder="Username/Email" required>
            </div>
            <div class="mb-3">
                <input type="password" class="form-control" id="resident_password" name="password" placeholder="Password" required>
            </div>
            <div class="mb-3">
                <input type="password" class="form-control" id="resident_repeatPassword" name="re_password" placeholder="Repeat Password" required>
            </div>
            <div class="mb-3">
                <input type="text" class="form-control" id="estateName" name="estate" placeholder="Estate Name" required>
            </div>
            <div class="mb-3">
                <input type="text" class="form-control" id="houseAddress" name="address" placeholder="Resident's House Address" required>
            </div>
            <div class="mb-3">
                <input type="number" class="form-control" id="flat" name="flat" placeholder="Your Flat Number">
            </div>
            <div class="mb-3">
                <input type="hidden" class="form-control" id="role" name="role" placeholder="role" value="renant" required>
            </div>
            <button type="submit" class="btn btn-primary w-100 bg-black" name="resident_signup" onclick="submitForm()">Submit</button>
        </form>
    </div>
</div>
<!--------------------------- The resident Sign up Page Ends Here ------------------------>
<!--------------------------- The resident Sign up Page Ends Here ------------------------>









<!------------------------- The Security Sign up Page Starts Here ------------------------>
<!------------------------- The Security Sign up Page Starts Here ------------------------>

<div id="security_signup" class="section security_signup1 signup_body" title="security_signup1">
    <div class="container">
        <div class="header-buttons">
            <button class="btn btn-outline-light" onclick="window.location.href = {{ url_for('signin') }}">SIGN IN</button>
            <button class="btn btn-outline-light" onclick="window.location.href = {{ url_for('signup_intro') }}">SIGN UP</button>
        </div>
        <a href="{{ url_for('signup_intro') }}" class="back-btn me-3">
            <i class="bi bi-arrow-left"></i>
        </a>
        <h2 class="text-center">SIGN UP</h2>
        <form action="{{ url_for('index') }}" method="post" id="signUpForm">
            <div class="mb-3">
                <input type="email" class="form-control" id="security_email" name="security_email" placeholder="Email" required>
            </div>
            <div class="mb-3">
                <input type="password" class="form-control" id="security_password" name="security_password" placeholder="Password" required>
            </div>
            <div class="mb-3">
                <input type="password" class="form-control" id="security_repeatPassword" name="re_password" placeholder="Repeat Password" required>
            </div>
            <div class="mb-3">
                <input type="text" class="form-control" id="security_estateName" name="security_estate" placeholder="Estate Name" required>
            </div>
            <div class="mb-3">
                <input type="text" class="form-control" id="security_houseAddress" name="security_address" placeholder="Security House Address <input To be Placed Under Admin>" required>
            </div>
            <div class="mb-3">
                <input type="number" class="form-control" id="security_flat" name="securityflat" placeholder="Your Flat Number">
            </div>
            <div class="mb-3">
                <input type="hidden" class="form-control" id="security_role" name="security_role" placeholder="role" value="tenant" required>
            </div>
            <button type="submit" class="btn btn-primary w-100 bg-black" name="security_signup" onclick="submitForm()">Submit</button>
        </form>
    </div>
</div>
<!--------------------------- The Security Sign up Page Ends Here ------------------------>
<!--------------------------- The Security Sign up Page Ends Here ------------------------>










<!--------------------------- The Sign in Page Starts Here ------------------------>
<!--------------------------- The Sign in Page Starts Here ------------------------>

<div id="signin" class="login-container section signin1" title="signin1">
    <h3 class="text-center mb-4 text-black">SIGN IN</h3>
    <!-- Sign In Form -->
    <form action="{{ url_for('index') }}" method="post" id="ssignInForm">
        <div class="mb-3">
            <input type="text" id="login_email" class="form-control" name="login_email" placeholder="Email/Phone No." required>
        </div>
        <div class="mb-3">
            <input type="password" id="login_password" class="form-control" name="login_password" placeholder="Password" required>
        </div>
        <div class="mb-3">
            <input type="hidden" id="form_role" class="form-control" name="form_role" placeholder="Form Role" value="login">
        </div>
        <div class="mb-3 forgot-password">
            <a href="#" onclick="forgotPassword()" class="text-black">Forget Password</a>
        </div>
        <button type="submit" class="btn btn-sign-in">SIGN IN</button>
    </form>
</div>

<!--------------------------- The Sign in Page Ends Here ------------------------>
<!--------------------------- The Sign in Page Ends Here ------------------------>










<!--------------------------- The Profile Page Starts Here ------------------------>
<!--------------------------- The Profile Page Starts Here ------------------------>

<div id="profile" class="section profile1 profile_body" title="profile1">
    <div class="container">
        <h2 class="text-center">Profile</h2>
        <form id="profileForm">
            <div class="mb-3">
                <input type="text" class="form-control" id="fullName" placeholder="Full Name" required>
            </div>
            <div class="mb-3">
                <input type="email" class="form-control" id="emailAddress" placeholder="Email Address" required>
            </div>
            <div class="mb-3">
                <input type="tel" class="form-control" id="phoneNumber" placeholder="Phone Number" required>
            </div>
            <div class="mb-3">
                <input type="text" class="form-control" id="apartmentAddress" placeholder="Apartment Address" required>
            </div>
            <div class="mb-3">
                <input type="text" class="form-control" id="maritalStatus" placeholder="Marital Status" required>
            </div>
            <div class="mb-3">
                <select class="form-control" id="gender" required>
                    <option value="" disabled selected>Gender</option>
                    <option value="male">Male</option>
                    <option value="female">Female</option>
                    <option value="other">Other</option>
                </select>
            </div>
            <div class="profile-pic" id="profilePicture">
                Picture JPEG
            </div>
            <input type="file" id="uploadPicture" accept="image/jpeg" class="form-control mb-3" onchange="updatePicture()">
            <button type="button" class="btn btn-success w-100" onclick="saveProfile()">Save</button>
        </form>
    </div>
</div>
<!--------------------------- The Profile Page Ends Here ------------------------>
<!--------------------------- The Profile Page Ends Here ------------------------>










<!--------------------------- The Owners Page Starts Here ------------------------>
<!--------------------------- The Owners Page Starts Here ------------------------>

<div id="owner" class="container p-3 section owner1" title="owner1">
    <!-- Header Section -->
    <div class="d-flex align-items-center mb-3">
        <a href="#" class="back-btn me-3">
            <i class="bi bi-arrow-left"></i>
        </a>
        <h1 class="header text-black">OWNERS</h1>
    </div>

    <!-- Form Section -->
    <form id="ownersForm">
        <div class="mb-3">
            <input type="text" class="form-control" placeholder="Full Name" id="fullName" required>
        </div>
        <div class="mb-3">
            <input type="email" class="form-control" placeholder="Email Address" id="emailAddress" required>
        </div>
        <div class="mb-3">
            <input type="text" class="form-control" placeholder="Phone Number" id="phoneNumber" required>
        </div>
        <div class="mb-3">
            <input type="text" class="form-control" placeholder="House Address" id="houseAddress" required>
        </div>
        <div class="mb-3">
            <input type="text" class="form-control" placeholder="Marital Status" id="maritalStatus" required>
        </div>
        <div class="mb-3">
            <input type="text" class="form-control" placeholder="Gender" id="gender" required>
        </div>
        <div class="mb-3">
            <input type="number" class="form-control" placeholder="Number of Residents in the House" id="numberOfResidents" required>
        </div>
        <div class="mb-3 d-grid">
            <button type="submit" class="btn btn-custom">SAVE</button>
        </div>
    </form>

    <!-- Add Tenants Button -->
    <div class="d-grid">
        <button class="btn btn-register">Register/Add Tenants</button>
    </div>
</div>

<!--------------------------- The Owners Page Ends Here ------------------------>
<!--------------------------- The Owners Page Ends Here ------------------------>










<!--------------------------- The Reg_Residents Page Starts Here ------------------------>
<!--------------------------- The Reg_Residents Page Starts Here ------------------------>

<div id="reg_residents" class="container p-3 section reg_residents1" title="reg_residents1">
    <!-- Header Section -->
    <div class="d-flex align-items-center mb-3">
        <a href="#" class="back-btn me-3">
            <i class="bi bi-arrow-left"></i>
        </a>
        <h1 class="header text-black">Register/Add Residents</h1>
    </div>

    <!-- Form Section -->
    <form id="residentsForm">
        <div class="mb-3">
            <input type="text" class="form-control" placeholder="Full Name of Tenant" id="tenantName" required>
        </div>
        <div class="mb-3">
            <input type="email" class="form-control" placeholder="Email Address" id="tenantEmail" required>
        </div>
        <div class="mb-3">
            <input type="text" class="form-control" placeholder="Phone Number" id="tenantPhone" required>
        </div>
        <div class="mb-3">
            <input type="text" class="form-control" placeholder="Apartment/Flat Number" id="apartmentNumber" required>
        </div>
        <div class="mb-3">
            <input type="text" class="form-control" placeholder="Marital Status" id="maritalStatus" required>
        </div>
        <div class="mb-3">
            <input type="text" class="form-control" placeholder="Gender" id="gender" required>
        </div>
        <div class="mb-3">
            <input type="text" class="form-control" placeholder="Occupation" id="occupation" required>
        </div>
        <div class="mb-3 d-grid">
            <button type="submit" class="btn btn-custom">ADD</button>
        </div>
    </form>
</div>
    
<!--------------------------- The Reg_Residents Page Ends Here ------------------------>
<!--------------------------- The Reg_Residents Page Ends Here ------------------------>









<!--------------------------- The Residents Page Starts Here ------------------------>
<!--------------------------- The Residents Page Starts Here ------------------------>

<!-- Header Section -->
<div id="residents" class="align-items-center mb-3 section residents1" title="residents1">
    <a href="#" class="back-btn me-3">
        <i class="bi bi-arrow-left"></i>
    </a>
    <h3 class="text-center mb-4 text-black">Residents</h3>
</div>

<div class="containerr section residents1">
    <!-- Residents Options -->
    <button class="residents-btn" onclick="handlePayment('Admin')">Admin</button>
    <button class="residents-btn" onclick="handlePayment('Owner')">Owner</button>
    <button class="residents-btn" onclick="handlePayment('Tenant')">Tenant</button>
    <button class="residents-btn" onclick="handlePayment('Security')">Security</button>
</div>
<!--------------------------- The Residents Page Ends Here ------------------------>
<!--------------------------- The Residents Page Ends Here ------------------------>










<!--------------------------- The Security Page Starts Here ------------------------>
<!--------------------------- The Security Page Starts Here ------------------------>

<div id="security" class="section security1 container text-center" title="security1">
    <!-- Back Navigation -->
    <a href="{{ url_for('home') }}" class="d-block mb-4 text-decoration-none  text-black">
        <i class="bi bi-arrow-left"></i> Security
    </a>

    <!-- Image Section -->
    <div class="image-container mb-3">
        <img src="{{ url_for('static', filename='images/img.jpg') }}" alt="Building Image" class="img-fluid">
    </div>

    <!-- Access Code Button -->
    <button class="access-btn" onclick="inputAccessCode()">Input Access Code</button>
    
    <marquee class="mb-0" style="position:absolute; bottom:35%; left:30%; right:30%; font-weight:bold; ">Click The Access Button To Verify The Code !!! *** Powered by: Ixora Consulting Ltd ***</marquee>
</div>

<!--------------------------- The Security Page Ends Here ------------------------>
<!--------------------------- The Security Page Ends Here ------------------------>









<!--------------------------- The Visitors Page Starts Here ------------------------>
<!--------------------------- The Visitors Page Starts Here ------------------------>

<header id="visitor" class="section visitor1 tab-header" title="visitor1">
<br />
    <div class="container d-flex justify-content-between">
        <div>INVITE VISITOR</div>
        <div>TRACK VISITOR</div>
    </div>
</header>

<div class="section visitor1 container">
    <ul class="nav nav-tabs mt-3" id="visitorTabs" role="tablist">
        <li class="nav-item" role="presentation">
            <button class="nav-link active" id="one-time-tab" data-bs-toggle="tab" data-bs-target="#one-time" type="button" role="tab" aria-controls="one-time" aria-selected="true">ONE-TIME</button>
        </li>
        <li class="nav-item" role="presentation">
            <button class="nav-link text-dark" id="multi-entry-tab" data-bs-toggle="tab" data-bs-target="#multi-entry" type="button" role="tab" aria-controls="multi-entry" aria-selected="false">MULTI-ENTRY</button>
        </li>
        <li class="nav-item" role="presentation">
            <button class="nav-link text-dark" id="events-tab" data-bs-toggle="tab" data-bs-target="#events" type="button" role="tab" aria-controls="events" aria-selected="false">EVENTS</button>
        </li>
    </ul>

    <div class="tab-content" id="visitorTabsContent">
        <div class="tab-pane fade show active form-section" id="one-time" role="tabpanel" aria-labelledby="one-time-tab">
            <form action="{{ url_for('guest') }}" method="post">
                <div class="mb-3">
                    <label for="guest_apartment" class="form-label">Apartment:</label>
                    <input type="text" class="form-control" id="guest_apartment" name="guest_apartment" placeholder="Flat 7, Plot 9, Road 1, Centenary Gardens">
                </div>
                <div class="mb-3">
                    <label for="guest_name" class="form-label">Guest Name:</label>
                    <input type="text" class="form-control" id="guest_name" name="guest_name" placeholder="Guest Name">
                </div>
                <div class="mb-3">
                    <label for="guest_gender" class="form-label">Guest Gender:</label>
                    <select type="text" class="form-control" id="guest_gender" name="guest_gender" required>
                        <option>Male</option>
                        <option>Female</option>
                    </select>
                </div>
                <div class="mb-3">
                    <label for="arrival_date" class="form-label">Select Arrival Date:</label>
                    <input type="date" class="form-control" id="arrival_date" name="arrival_date" value="{{ date }}">
                </div>
                <div class="mb-3">
                    <label class="form-label">Expected Time of Arrival:</label>
                    <div class="row">
                        <div class="col">
                            <input type="time" class="form-control" id="arrival_time_from" name="arrival_time_from">
                        </div>
                        to
                        <div class="col">
                            <input type="time" class="form-control" id="arrival_time_to" name="arrival_time_to">
                        </div>
                    </div>
                </div>
                <div class="form-check form-switch mb-3">
                    <input class="form-check-input" type="checkbox" id="shareQRCode" name="shareQRCode">
                    <label class="form-check-label" for="shareQRCode">Share QRCode</label>
                </div>
                <button type="submit" class="generate-btn" nclick="generateAccessCode()">GENERATE ACCESS CODE</button>
            </form>
        </div>

        <div class="tab-pane fade form-section" id="multi-entry" role="tabpanel" aria-labelledby="multi-entry-tab">
            <p>Multi-entry form content goes here.</p>
        </div>

        <div class="tab-pane fade form-section" id="events" role="tabpanel" aria-labelledby="events-tab">
            <p>Events form content goes here.</p>
        </div>
    </div>
</div>

<!--------------------------- The Visitors Page Ends Here ------------------------>
<!--------------------------- The Visitors Page Ends Here ------------------------>










<!-------------------------- The Visitors_Code Page Starts Here ------------------------>
<!-------------------------- The Visitors_Code Page Starts Here ------------------------>

<div id="visitors_code" class="container p-3 section visitors_code1" title="visitors_code1">
    <!-- Header Section -->
    <div class="d-flex align-items-center mb-3">
        <a href="#" class="back-btn me-3">
            <i class="bi bi-arrow-left"></i>
        </a>
        <h1 class="header text-black">Invite Visitor</h1>
    </div>
    <!-- Access Code Display -->
    <div class="code-display" id="accessCode">
        Access Code: <span id="code">{{ code }}</span><br>
        Guest Name: <span id="code1">{{ name }}</span><br>
        Guest Gender: <span id="code2">{{ gender }}</span><br>
        Arrival Date: <span id="code3">{{ arrival_date }}</span><br>
        Arrival Time: <span id="code4">{{ arrival_time }}</span><br>
    </div>

    <!-- Action Buttons -->
    <div class="icon-group">
        <!-- Share -->
        <div class="icon">
            <button class="btn btn-outline-light" onclick="shareCode()">
                <i class="bi bi-share"></i> <br> Share
            </button>
        </div>
        <!-- SMS -->
        <div class="icon">
            <button class="btn btn-outline-light" onclick="sendSMS()">
                <i class="bi bi-chat-text"></i> <br> SMS
            </button>
        </div>
        <!-- WhatsApp -->
        <div class="icon">
            <button class="btn btn-outline-light" onclick="sendWhatsApp()">
                <i class="bi bi-whatsapp"></i> <br> WhatsApp
            </button>
        </div>
        <!-- Copy -->
        <div class="icon">
            <button class="btn btn-outline-light" onclick="copyToClipboard()">
                <i class="bi bi-clipboard"></i> <br> Copy
            </button>
        </div>
    </div>
    <br />
    <br />
</div>
    
<!--------------------------- The Visitors_Code Page Ends Here ------------------------>
<!--------------------------- The Visitors_Code Page Ends Here ------------------------>










<!--------------------------- The Payments Page Starts Here ------------------------>
<!--------------------------- The Payments Page Starts Here ------------------------>

<!-- Header Section -->
<div id="payments" class="align-items-center mb-3 section payments1" title="payments1">
    <a href="#" class="back-btn me-3">
        <i class="bi bi-arrow-left"></i>
    </a>
    <h3 class="text-center mb-4 text-black">PAYMENTS</h3>
</div>

<div class="containerr section payments1">
    <!-- Payment Options -->
    <button class="payment-btn" onclick="handlePayment('Monthly Dues')">MONTHLY DUES</button>
    <button class="payment-btn" onclick="handlePayment('Security Levy')">SECURITY LEVY</button>
    <button class="payment-btn" onclick="handlePayment('Others')">OTHERS</button>
</div>
<!--------------------------- The Payments Page Ends Here ------------------------>
<!--------------------------- The Payments Page Ends Here ------------------------>










<!--------------------------- The Monthly Dues Page Starts Here ------------------------>
<!--------------------------- The Monthly Dues Page Starts Here ------------------------>

<div id="monthly_dues" class="section monthly_dues1 monthly_body" title="monthly_dues1">
    <div class="container text-center">
        <h1 class="mb-4">MONTHLY DUES</h1>
        <form id="monthlyDuesForm" class="p-4 rounded">
            <input type="text" class="form-control" placeholder="Account Number of the Estate" id="accountNumber" required>
            <input type="text" class="form-control" placeholder="House Address" id="houseAddress" required>
            <input type="text" class="form-control" placeholder="Apartment" id="apartment" required>
            <input type="number" class="form-control" placeholder="Amount" id="amount" required>
            <div class="mb-3">
                <label for="receiptScreenshot" class="form-label text-dark">Screenshot of the Receipt</label>
                <input class="form-control" type="file" id="receiptScreenshot" accept="image/*" required>
            </div>
            <button type="submit" class="btn btn-custom w-100">SEND</button>
        </form>
    </div>
</div>

<!--------------------------- The Monthly Dues Page Ends Here ------------------------>
<!--------------------------- The Monthly Dues Page Ends Here ------------------------>









<!--------------------------- The foot section Starts Here ------------------------>
<!--------------------------- The foot section Starts Here ------------------------>

<footer class="foot section home1 profile1 monthly_dues1 owner1 reg_resident1 visitors_code1 residents1 signup_intro1 footer bg-black text-light">
    <p class="mb-0" style="position:sticky; bottom:25%; left:30%; right:30%; font-weight:bold; ">Powered by: Ixora Consulting Ltd</p>
</footer>

<!--------------------------- The foot section Ends Here ------------------------>
<!--------------------------- The foot section Ends Here ------------------------>





<script src="https://cdnjs.cloudflare.com/ajax/libs/bootstrap/5.3.0/js/bootstrap.bundle.min.js"></script>
<script src="https://code.jquery.com/jquery-3.7.1.js" integrity="sha256-eKhayi8LEQwp4NKxN+CfCh+3qOVUtJn3QNZ0TciWLP4=" crossorigin="anonymous"></script>

<!----
<script async defer src="https://maps.googleapis.com/maps/api/js?key=AIzaSyAcAKWEQPe2Bm_b0EU9kC2Cd7G776Se-dk&callback=initMap"></script>
----->
<script src="{{ url_for('static', filename='js/script.js') }}"></script>

</body>
</html>
