<svelte:head>
	<title>Ecommerce - Sign In</title>
</svelte:head>

<form class="container">
	<div class="p-3 mb-2">
		<h3 class="text-uppercase text-center fw-bold">sign in</h3>
		<p class="text-center">
			Does not have an account yet? <a href="/register" class="text-decoration-none">Sign up</a>
		</p>
	</div>

	<div class="form-floating mt-2 mb-3">
		<input
			type="email"
			class="form-control rounded-5"
			id="email"
			placeholder="name@example.com"
		/>
		<label for="email">Email</label>
	</div>
	<div class="form-floating mt-2 mb-3">
		<input type="password" class="form-control rounded-5" id="password" placeholder="Password" />
		<label for="password">Password</label>
	</div>

	<div class="d-flex justify-content-between my-3">
		<div class="form-check text-start">
			<input class="form-check-input" type="checkbox" value="remember-me" id="flexCheckDefault" />
			<label class="form-check-label" for="flexCheckDefault"> Remember me </label>
		</div>
		<div class="text-end">
			<a href={'#'} class="text-decoration-none">Forgot password?</a>
		</div>
	</div>

	<button class="btn btn-primary w-100 py-2 mt-2 mb-3 rounded-5" type="submit">Login</button>
	<div style="padding-left: 6.9em; margin-bottom: -0.17em;">
		<p class="text-center bg-light text-secondary z-3 position-absolute">or sign in as</p>
	</div>
	<hr class="border border-secondary" />
	<div class="row row-cols-2 g-2 mt-2">
		<div class="col">
			<button class="btn btn-outline-info rounded-5" type="submit"> Demo Customer </button>
		</div>
		<div class="col">
			<button class="btn btn-outline-info rounded-5" type="submit"> Demo Customer1 </button>
		</div>
	</div>
</form>