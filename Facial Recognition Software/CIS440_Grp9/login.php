<!DOCTYPE html>
<html>
    <head>
	 <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1" crossorigin="anonymous">  
	 <!-- 
	<link rel="icon" href="/docs/4.0/assets/img/favicons/favicon.ico">
	<link rel="canonical" href="https://getbootstrap.com/docs/4.0/examples/sign-in/">
	<link href="https://getbootstrap.com/docs/4.0/examples/sign-in/signin.css" rel="stylesheet">
	<link href="../../dist/css/bootstrap.min.css" rel="stylesheet">
    -->
	<link rel="stylesheet" href="login.css">
	
	 <title>{% block content %} {% endblock %}</title>
	 
    </head>
	
	<body>
		
			<div class="mx-auto mt-0" style="width: 300px;">
			  <h1 class="fs-6">Face Recognition Proj. Signin</h1>
			  
			  <div class="mb-3">
				<div id="help" class="form-text">We'll never share your email or password with anyone else.</div>
				<br>
			<form action="test.php" method="POST">
				<label for="exampleInputEmail1" class="form-label">Username</label>
				<input type="text" class="form-control" id="exampleInputEmail1" aria-describedby="emailHelp" name="username">
				
			  </div>
			  <div class="mb-3">
				<label for="exampleInputPassword1" class="form-label">Password</label>
				<input type="password" class="form-control" id="exampleInputPassword1" name="password">
				
			  </div>
			
			  <!--
			  <div class="mb-3 form-check">
				<input type="checkbox" class="form-check-input" id="exampleCheck1">
				<label class="form-check-label" for="exampleCheck1">Check me out</label>
			  </div>
			  -->	
			  <div class="createAccount">
				<a href="createAccount.html">Create Account Here</a>
				<br>
				<br>
					<input value="login" type="submit" style="height:35px; width:75px;"></input>
				</form>
			  
			
			</div>
			<br>
			  
			  
			
			
		
		
		<script src="https://cdn.jsdelivr.net/npm/@popperjs/core@2.5.4/dist/umd/popper.min.js" integrity="sha384-q2kxQ16AaE6UbzuKqyBE9/u/KzioAlnx2maXQHiDX9d4/zp8Ok3f+M7DPm+Ib6IU" crossorigin="anonymous"></script>
		<script src="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/js/bootstrap.min.js" integrity="sha384-pQQkAEnwaBkjpqZ8RU1fF1AKtTcHJwFl3pblpTlHXybJjHpMYo79HY3hIi4NKxyj" crossorigin="anonymous"></script>	
		
			
				 
	</body>
	 
</html>