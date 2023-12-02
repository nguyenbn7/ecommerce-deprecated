<script>
	import { goto } from '$app/navigation';
	import { page } from '$app/stores';
	import InputForm from '$lib/account/input-form.svelte';
	import { ToastService } from '$lib/components/share/toast.svelte';
	import { loginAs } from '$lib/service/account.service';
	import { ECOMMERCE_NAME } from '$lib/share/constant';
	import { InputField } from '$lib/share/model';
	import { hasCorrectEmailFormat, requireField } from '$lib/share/validator';

	const loginForm = {
		emailField: new InputField([
			requireField('Email is required'),
			hasCorrectEmailFormat('Incorrect email. Example: bob@test.com')
		]),
		passwordField: new InputField([requireField('Password is required')])
	};

	$: isValid = loginForm.emailField.valid && loginForm.passwordField.valid;

	let isLocked = false;
	let isDemoAccountLogin = false;
	let isAccounts = [false, false];

	async function onSubmitForm() {
		try {
			isLocked = true;
			const result = await loginAs({
				email: loginForm.emailField.value,
				password: loginForm.passwordField.value
			});
			if (result instanceof Response) {
				/**
				 * @type {ErrorResponse}
				 */
				const errorResponse = await result.json();
				if (errorResponse.message) {
					ToastService.notifyError(errorResponse.message);
				}
				return;
			}

			ToastService.notifySuccess(`Welcome back ${result.display_name}`);
			const returnUrl = $page.url.searchParams.get('returnUrl');
			if (returnUrl) return goto(returnUrl);
			return goto('/');
		} catch (error) {
			// @ts-ignore
			ToastService.notifyError(error.message);
		} finally {
			isLocked = false;
		}
	}

	/**
	 * @param {string} email
	 * @param {string} password
	 * @param {number} id
	 */
	async function onLoginDemoAccount(email, password, id) {
		try {
			isDemoAccountLogin = true;
			isAccounts[id] = true;
			const result = await loginAs({ email, password });
			if (result instanceof Response) {
				/**
				 * @type {ErrorResponse}
				 */
				const errorResponse = await result.json();
				if (errorResponse.message) {
					ToastService.notifyError(errorResponse.message);
				}
				return;
			}

			ToastService.notifySuccess(`Welcome back ${result.display_name}`);
			
			const returnUrl = $page.url.searchParams.get('returnUrl');
			if (returnUrl) return goto(returnUrl);
			return goto('/');
		} catch (error) {
			// @ts-ignore
			ToastService.notifyError(error.message);
		} finally {
			isDemoAccountLogin = false;
			isAccounts[id] = false;
		}
	}

	async function onLoginCustomer() {
		await onLoginDemoAccount('customer@test.com', 'Pa$$w0rd', 0);
	}

	async function onLoginCustomer1() {
		await onLoginDemoAccount('customer1@test.com', 'Pa$$w0rd', 1);
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
		<InputForm
			class="form-floating mt-2 mb-3"
			bind:inputField={loginForm.emailField}
			id="Email"
			type="email"
			label="Email"
			placeholder="name@example.com"
			disabled={isLocked}
		></InputForm>

		<InputForm
			class="form-floating mt-2 mb-3"
			bind:inputField={loginForm.passwordField}
			id="Password"
			type="password"
			label="Password"
			placeholder="Password"
			disabled={isLocked}
		></InputForm>

		<!-- <div class="d-flex justify-content-between my-3">
			<div class="form-check text-start">
				<input class="form-check-input" type="checkbox" value="remember-me" id="flexCheckDefault" />
				<label class="form-check-label" for="flexCheckDefault"> Remember me </label>
			</div>
			<div class="text-end">
				<a href={'#'} class="text-decoration-none">Forgot password?</a>
			</div>
		</div> -->
		<button
			class="btn btn-primary w-100 py-2 mt-2 mb-3 rounded-5"
			type="submit"
			disabled={!isValid || isLocked}
		>
			Login
			{#if isLocked}
				<span class="spinner-border spinner-border-sm" aria-hidden="true"></span>
				<span class="visually-hidden" role="status">Loading...</span>
			{/if}
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
			<button
				class="btn btn-outline-info rounded-5"
				type="submit"
				on:click={onLoginCustomer}
				disabled={isDemoAccountLogin}
			>
				Demo Customer
				{#if isDemoAccountLogin && isAccounts[0]}
					<span class="spinner-border spinner-border-sm" aria-hidden="true"></span>
					<span class="visually-hidden" role="status">Loading...</span>
				{/if}
			</button>
		</div>
		<div class="col d-flex justify-content-center">
			<button
				class="btn btn-outline-info rounded-5"
				type="submit"
				on:click={onLoginCustomer1}
				disabled={isDemoAccountLogin}
			>
				Demo Customer1
				{#if isDemoAccountLogin && isAccounts[1]}
					<span class="spinner-border spinner-border-sm" aria-hidden="true"></span>
					<span class="visually-hidden" role="status">Loading...</span>
				{/if}
			</button>
		</div>
	</div>
</div>

<style>
	hr {
		margin: 0.9rem 0;
	}
</style>
