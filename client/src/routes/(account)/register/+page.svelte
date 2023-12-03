<script>
	import { goto } from '$app/navigation';
	import { page } from '$app/stores';
	import AccountService from '$lib/account/service';
	import { ToastService } from '$lib/components/share/toast.svelte';
	import { ECOMMERCE_NAME } from '$lib/share/constant';
	import EmailInput, { EmailInputValidator } from '$lib/share/form/email-input.svelte';
	import PasswordInput, { PasswordInputValidator } from '$lib/share/form/password-input.svelte';
	import TextInput, { TextInputValidator } from '$lib/share/form/text-input.svelte';
	import { FormField, Validators } from '$lib/share/form/validation';
	import ValidationFeedback from '$lib/share/form/validation-feedback.svelte';

	const name_max_len = 70;

	class RegisterForm {
		static nameField = new FormField(
			TextInputValidator.checkRequired('Name is required'),
			Validators.containsAlnumAndSpace('Name contains only letters and spaces'),
			Validators.checkMaxLength(`Name's max length is ${name_max_len} characters`, name_max_len)
		);

		static emailField = new FormField(
			EmailInputValidator.checkRequired('Email is required'),
			EmailInputValidator.checkFormat('Incorrect email. Example: bob@test.com')
		);

		static passwordField = new FormField(
			PasswordInputValidator.checkRequired('Password is required')
		);

		static confirmPasswordField = new FormField(
			PasswordInputValidator.checkRequired('Confirm Password is required')
		);

		static get valid() {
			return (
				this.nameField.valid &&
				this.emailField.valid &&
				this.passwordField.valid &&
				this.confirmPasswordField.valid
			);
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

	let isLocked = false;

	async function onSubmitForm() {
		try {
			RegisterForm.isSubmiting = true;
			const userInfo = await AccountService.register({
				email: RegisterForm.emailField.value,
				password: RegisterForm.passwordField.value,
				display_name: RegisterForm.nameField.value,
				confirm_password: RegisterForm.confirmPasswordField.value
			});

			if (userInfo) {
				ToastService.notifySuccess(`Welcome ${userInfo?.displayName}`);
				const returnUrl = $page.url.searchParams.get('returnUrl');
				if (returnUrl) return goto(returnUrl);
				return goto('/');
			}
		} catch (error) {
			// @ts-ignore
			ToastService.notifyError(error.message);
		} finally {
			RegisterForm.isSubmiting = false;
		}
	}
</script>

<svelte:head>
	<title>{ECOMMERCE_NAME} - Sign Up</title>
</svelte:head>

<form class="container" on:submit={onSubmitForm}>
	<div class="p-3 mb-2">
		<h3 class="text-uppercase text-center fw-bold">sign up</h3>
		<p class="text-center">
			Have an account? <a href="/login" class="text-decoration-none">Sign in</a>
		</p>
	</div>

	<div class="form-floating mt-2 mb-3">
		<TextInput
			class="form-control rounded-4"
			bind:formField={RegisterForm.nameField}
			id="displayName"
			placeholder="I am cute"
		></TextInput>
		<label for="displayName">Display Name</label>
		<ValidationFeedback formField={RegisterForm.emailField}></ValidationFeedback>
	</div>

	<div class="form-floating mt-2 mb-3">
		<EmailInput
			class="form-control rounded-4"
			bind:formField={RegisterForm.emailField}
			id="email"
			placeholder="name@example.com"
		></EmailInput>
		<label for="email">Email</label>
		<ValidationFeedback formField={RegisterForm.emailField}></ValidationFeedback>
	</div>

	<div class="form-floating mt-2 mb-3">
		<PasswordInput
			class="form-control rounded-4"
			bind:formField={RegisterForm.passwordField}
			id="password"
			placeholder="Password"
		></PasswordInput>
		<label for="password">Password</label>
		<ValidationFeedback formField={RegisterForm.passwordField}></ValidationFeedback>
	</div>

	<div class="form-floating mt-2 mb-3">
		<PasswordInput
			class="form-control rounded-4"
			bind:formField={RegisterForm.confirmPasswordField}
			id="confirmPassword"
			placeholder="Re-type password"
		></PasswordInput>
		<label for="confirmPassword">Confirm Password</label>
		<ValidationFeedback formField={RegisterForm.confirmPasswordField}></ValidationFeedback>
	</div>

	<button
		class="btn btn-primary w-100 py-2 mt-2 mb-3 rounded-5"
		type="submit"
		disabled={!RegisterForm.valid}
	>
		Register
		<!-- {#if isLocked}
			<span class="spinner-border spinner-border-sm" aria-hidden="true"></span>
			<span class="visually-hidden" role="status">Loading...</span>
		{/if} -->
	</button>
</form>
