<script>
	import { goto } from '$app/navigation';
	import { page } from '$app/stores';
	import { ToastService } from '$lib/components/share/toast.svelte';
	import { ECOMMERCE_NAME } from '$lib/share/constant';
	import { FormField } from '$lib/share/form/validation';
	import EmailInput, { EmailInputValidator } from '$lib/share/form/email-input.svelte';
	import PasswordInput, { PasswordInputValidator } from '$lib/share/form/password-input.svelte';
	import ValidationFeedback from '$lib/share/form/validation-feedback.svelte';
	import AccountService from '$lib/account/service';

	class LoginForm {
		static emailField = new FormField(
			EmailInputValidator.checkRequired('Email is required'),
			EmailInputValidator.checkFormat('Incorrect email. Example: bob@test.com')
		);
		static passwordField = new FormField(
			PasswordInputValidator.checkRequired('Password is required')
		);

		static get valid() {
			return this.emailField.valid && this.passwordField.valid;
		}

		static #onSubmit = false;

		/**
		 * @param {boolean} state
		 */
		static set isSubmiting(state) {
			this.#onSubmit = state;
		}

		static get isSubmiting() {
			return this.#onSubmit;
		}
	}

	let isDemoAccountLogin = false;
	let isAccounts = [false, false];

	async function onSubmitForm() {
		await handleLogin({
			email: LoginForm.emailField.value,
			password: LoginForm.passwordField.value
		});
	}

	/**
	 * @param {LoginDTO} loginDTO
	 */
	async function handleLogin(loginDTO) {
		try {
			LoginForm.isSubmiting = true;
			const userInfo = await AccountService.login(loginDTO);

			if (userInfo) {
				ToastService.notifySuccess(`Welcome back ${userInfo.displayName}`);
				const returnUrl = $page.url.searchParams.get('returnUrl');
				if (returnUrl) return goto(returnUrl);
				return goto('/');
			}
		} finally {
			LoginForm.isSubmiting = false;
		}
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
			<EmailInput
				class="form-control rounded-4"
				bind:formField={LoginForm.emailField}
				id="email"
				placeholder="name@example.com"
				readonly={LoginForm.isSubmiting}
			></EmailInput>
			<label for="email">Email</label>
			<ValidationFeedback formField={LoginForm.emailField}></ValidationFeedback>
		</div>

		<div class="form-floating mt-2 mb-3">
			<PasswordInput
				class="form-control rounded-4"
				bind:formField={LoginForm.passwordField}
				id="password"
				placeholder="Password"
				readonly={LoginForm.isSubmiting}
			></PasswordInput>
			<label for="password">Password</label>
			<ValidationFeedback formField={LoginForm.passwordField}></ValidationFeedback>
		</div>

		<button
			class="btn btn-primary w-100 py-2 mt-2 mb-3 rounded-4"
			type="submit"
			disabled={!LoginForm.valid || LoginForm.isSubmiting}
		>
			Login
			{#if LoginForm.isSubmiting}
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
				class="btn btn-outline-info rounded-4"
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
				class="btn btn-outline-info rounded-4"
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
