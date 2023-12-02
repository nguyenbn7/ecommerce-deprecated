<script>
	import { goto } from '$app/navigation';
	import InputForm from '$lib/account/input-form.svelte';
	import { ToastService } from '$lib/components/share/toast.svelte';
	import { registerAs } from '$lib/service/account.service';
	import { ECOMMERCE_NAME } from '$lib/share/constant';
	import { InputField } from '$lib/share/model';
	import {
		hasAlnumAndSpace,
		hasCorrectEmailFormat,
		hasMaxLength,
		requireField
	} from '$lib/share/validator';

	const name_max_len = 70;

	let nameField = new InputField([
		requireField('Name is required'),
		hasAlnumAndSpace('Name contains only letters and spaces'),
		hasMaxLength(`Name's max length is ${name_max_len} characters`, name_max_len)
	]);

	let emailField = new InputField([
		requireField('Email is required'),
		hasCorrectEmailFormat('Incorrect email. Example: bob@test.com')
	]);

	let passwordField = new InputField([requireField('Password is required')]);

	let confirmPasswordField = new InputField([requireField('Confirm Password is required')]);

	$: isValid =
		nameField.valid && emailField.valid && passwordField.valid && confirmPasswordField.valid;

	let isLocked = false;

	async function onSubmitForm() {
		try {
			isLocked = true;
			const result = await registerAs({
				email: emailField.value,
				display_name: nameField.value,
				password: passwordField.value,
				confirm_password: confirmPasswordField.value
			});

			if (result instanceof Response) {
				/**
				 * @type {ErrorResponse}
				 */
				const errorResponse = await result.json();
				if (errorResponse.error) {
					ToastService.notifyError(errorResponse.error);
				}
				return;
			}

			ToastService.notifySuccess(`Welcome ${result.display_name}`);
			return goto('/');
		} catch (error) {
			// @ts-ignore
			ToastService.notifyError(error.message);
		} finally {
			isLocked = false;
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

	<InputForm
		class="form-floating mt-2 mb-3"
		bind:inputField={nameField}
		id="Name"
		label="Name"
		placeholder="John Doe"
	></InputForm>

	<InputForm
		class="form-floating mt-2 mb-3"
		bind:inputField={emailField}
		id="Email"
		type="email"
		label="Email"
		placeholder="name@example.com"
	></InputForm>

	<InputForm
		class="form-floating mt-2 mb-3"
		bind:inputField={passwordField}
		id="Password"
		type="password"
		label="Password"
		placeholder="Password"
	></InputForm>

	<InputForm
		class="form-floating mt-2 mb-3"
		bind:inputField={confirmPasswordField}
		id="ConfirmPassword"
		type="password"
		label="Confirm Password"
		placeholder="Confirm Password"
	></InputForm>

	<button
		class="btn btn-primary w-100 py-2 mt-2 mb-3 rounded-5"
		type="submit"
		disabled={!isValid || isLocked}
	>
		Register
		{#if isLocked}
			<span class="spinner-border spinner-border-sm" aria-hidden="true"></span>
			<span class="visually-hidden" role="status">Loading...</span>
		{/if}
	</button>
</form>
