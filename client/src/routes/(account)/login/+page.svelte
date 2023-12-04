<script>
	import { goto } from '$app/navigation';
	import { page } from '$app/stores';
	import { ToastService } from '$lib/components/share/toast.svelte';
	import { ECOMMERCE_NAME } from '$lib/share/constant';
	import ValidationFeedback from '$lib/share/form/validation-feedback.svelte';
	import { LoginForm } from '$lib/(account)/login/model';
	import InputForm from '$lib/share/form/input-form.svelte';
	import { AccountService } from '$lib/(account)/service';

	/**
	 * @param {LoginDTO} loginDTO
	 */
	async function handleLogin(loginDTO) {
		const userInfo = await AccountService.login(loginDTO);

		if (userInfo) {
			ToastService.notifySuccess(`Welcome back ${userInfo.displayName}`);
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

<div class="container">
	<div class="p-3 mb-2">
		<h3 class="text-uppercase text-center fw-bold">sign in</h3>
		<p class="text-center">
			Does not have an account yet? <a href="/register" class="text-decoration-none">Sign up</a>
		</p>
	</div>

	<form on:submit={onSubmitForm}>
		<div class="form-floating mt-2 mb-3">
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

		<div class="form-floating mt-2 mb-3">
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

		<button
			class="btn btn-primary w-100 py-2 mt-2 mb-3 rounded-4"
			type="submit"
			disabled={!loginForm.valid}
		>
			Login
			<!-- {#if LoginForm.isSubmiting}
				<span class="spinner-border spinner-border-sm" aria-hidden="true"></span>
				<span class="visually-hidden" role="status">Loading...</span>
			{/if} -->
		</button>
	</form>
	<div class="d-flex mt-3 mb-4">
		<div class="border-secondary-subtle w-100 flex-shrink-1">
			<hr />
		</div>
		<span class="text-center text-nowrap text-secondary">or sign in as</span>
		<div class="border-secondary-subtle w-100 flex-shrink-1">
			<hr />
		</div>
	</div>
	<div class="row row-cols-2 g-2 mt-2">
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

<style>
	hr {
		margin: 0.9rem 0;
	}
</style>
