<svelte:head>
	<title>Ecommerce - Sign Up</title>
</svelte:head>

<form class="container">
	<div class="p-3 mb-2">
		<h3 class="text-uppercase text-center fw-bold">sign up</h3>
		<p class="text-center">
			Have an account? <a href="/login" class="text-decoration-none">Sign in</a>
		</p>
	</div>

	<div class="form-floating mt-2 mb-3">
		<input type="text" class="form-control rounded-5" id="Name" placeholder="John Doe" />
		<label for="Name">Name</label>
	</div>

	<div class="form-floating mt-2 mb-3">
		<input type="email" class="form-control rounded-5" id="email" placeholder="name@example.com" />
		<label for="email">Email</label>
	</div>

	<div class="form-floating mt-2 mb-3">
		<input type="password" class="form-control rounded-5" id="password" placeholder="Password" />
		<label for="password">Password</label>
	</div>

	<div class="form-floating mt-2 mb-3">
		<input
			type="password"
			class="form-control rounded-5"
			id="confirmPassword"
			placeholder="Password"
		/>
		<label for="confirmPassword">Confirm password</label>
	</div>

	<button class="btn btn-primary w-100 py-2 mt-2 mb-3 rounded-5" type="submit">Register</button>
</form>
