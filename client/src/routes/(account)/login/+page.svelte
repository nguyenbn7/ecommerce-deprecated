<script>
	import { goto } from '$app/navigation';
	import { page } from '$app/stores';
	import { ECOMMERCE_NAME } from '$lib/share/constant';
	import ValidationFeedback from '$lib/share/form/validation-feedback.svelte';
	import { LoginForm } from '$lib/(account)/login/model';
	import InputForm from '$lib/share/form/input-form.svelte';
	import { AccountService } from '$lib/(account)/service';
	import { ToastrService } from '$lib/share/component/toastr.svelte';

	/**
	 * @param {LoginDTO} loginDTO
	 */
	async function handleLogin(loginDTO) {
		const userInfo = await AccountService.login(loginDTO);

		if (userInfo) {
			ToastrService.notifySuccess(`Welcome back ${userInfo.displayName}`);
			const returnUrl = $page.url.searchParams.get('redirect');
			if (returnUrl) return goto(returnUrl);
			return goto('/');
		}
	}

	let loginForm = new LoginForm();

	async function onSubmitForm() {
		await handleLogin({
			email: loginForm.email.value,
			password: loginForm.password.value
		});
	}

	async function onLoginCustomer() {
		await handleLogin({
			email: 'customer@test.com',
			password: 'Pa$$w0rd'
		});
	}

	async function onLoginCustomer1() {
		await handleLogin({
			email: 'customer1@test.com',
			password: 'Pa$$w0rd'
		});
	}
</script>

<svelte:head>
	<title>{ECOMMERCE_NAME} - Sign In</title>
</svelte:head>

<div class="pt-4 pb-2">
	<h5 class="card-title text-center pb-0 fs-4">Login to Your Account</h5>
	<p class="text-center small">Enter your email &amp; password to login</p>
</div>

<form class="row g-3 px-1" on:submit={onSubmitForm}>
	<div class="col-12">
		<div class="form-floating">
			<InputForm
				class="form-control rounded-4"
				bind:formField={loginForm.email}
				id="email"
				type="email"
				placeholder="name@example.com"
			/>
			<label for="email">Email</label>
			<ValidationFeedback formField={loginForm.email}></ValidationFeedback>
		</div>
	</div>

	<div class="col-12">
		<div class="form-floating">
			<InputForm
				class="form-control rounded-4"
				bind:formField={loginForm.password}
				id="password"
				placeholder="Password"
				type="password"
			/>
			<label for="password">Password</label>
			<ValidationFeedback formField={loginForm.password}></ValidationFeedback>
		</div>
	</div>

	<div class="col-12">
		<div class="form-check">
			<input
				class="form-check-input"
				type="checkbox"
				name="remember"
				value="true"
				id="rememberMe"
			/>
			<label class="form-check-label" for="rememberMe">Remember me</label>
		</div>
	</div>
	<div class="col-12">
		<button
			class="btn btn-info w-100 py-2 mt-2 mb-3 rounded-4"
			type="submit"
			disabled={!loginForm.valid}
		>
			Login
			<!-- {#if LoginForm.isSubmiting}
				<span class="spinner-border spinner-border-sm" aria-hidden="true"></span>
				<span class="visually-hidden" role="status">Loading...</span>
			{/if} -->
		</button>
	</div>
	<div class="col-12">
		<p class="small mb-0">
			Don't have account? <a href="/register" class="text-decoration-none">Create an account</a>
		</p>
	</div>
	<div class="col-12">
		<div class="d-flex mb-2">
			<div class="border-secondary-subtle w-100 flex-shrink-1">
				<hr />
			</div>
			<span class="text-center text-nowrap text-secondary">or sign in as</span>
			<div class="border-secondary-subtle w-100 flex-shrink-1">
				<hr />
			</div>
		</div>
		<div class="row row-cols-2 g-2">
			<div class="col d-flex justify-content-center">
				<button class="btn btn-outline-info rounded-4" type="submit" on:click={onLoginCustomer}>
					Demo Customer
					<!-- {#if isDemoAccountLogin && isAccounts[0]}
						<span class="spinner-border spinner-border-sm" aria-hidden="true"></span>
						<span class="visually-hidden" role="status">Loading...</span>
					{/if} -->
				</button>
			</div>
			<div class="col d-flex justify-content-center">
				<button class="btn btn-outline-info rounded-4" type="submit" on:click={onLoginCustomer1}>
					Demo Customer1
					<!-- {#if isDemoAccountLogin && isAccounts[1]}
						<span class="spinner-border spinner-border-sm" aria-hidden="true"></span>
						<span class="visually-hidden" role="status">Loading...</span>
					{/if} -->
				</button>
			</div>
		</div>
	</div>
</form>

<style>
	hr {
		margin: 0.9rem 0;
	}
</style>
