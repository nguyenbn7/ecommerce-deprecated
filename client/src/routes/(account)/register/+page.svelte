<script>
	import { goto } from '$app/navigation';
	import InputForm from '$lib/components/account/input-form.svelte';
	import { registerAs } from '$lib/service/account.service';
	import { ECOMMERCE_NAME } from '$lib/util/application.constant';
	import {
		checkEmailFormat,
		checkFieldRequired,
		checkNameContainsLettersAndWhiteSpace,
		checkNameMaxLength
	} from '$lib/util/helper.function';
	import { TextFieldValidation } from '$lib/util/model';

	const name_max_len = 70;

	let nameField = new TextFieldValidation();
	nameField.validation.push(
		{
			validator: checkFieldRequired,
			errorMessage: 'Name is required'
		},
		{
			validator: checkNameContainsLettersAndWhiteSpace,
			errorMessage: 'Name contains only letters and spaces'
		},
		{
			validator: checkNameMaxLength(name_max_len),
			errorMessage: `Name's max length is ${name_max_len} characters`
		}
	);

	let emailField = new TextFieldValidation();
	emailField.validation.push(
		{
			validator: checkFieldRequired,
			errorMessage: 'Email is required'
		},
		{
			validator: checkEmailFormat,
			errorMessage: 'Incorrect email. Example: bob@test.com'
		}
	);

	let passwordField = new TextFieldValidation();
	passwordField.validation.push({
		validator: checkFieldRequired,
		errorMessage: 'Password is required'
	});

	let confirmPasswordField = new TextFieldValidation();
	confirmPasswordField.validation.push({
		validator: checkFieldRequired,
		errorMessage: 'Confirm Password is required'
	});

	$: isValid =
		nameField.valid && emailField.valid && passwordField.valid && confirmPasswordField.valid;

	async function onSubmitForm() {
		const data = await registerAs({
			email: emailField.value,
			display_name: nameField.value,
			password: passwordField.value,
			confirm_password: confirmPasswordField.value
		});

		if (data instanceof Response) {
			console.error(await data.json());
			return;
		}

		return goto("/");
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

	<button class="btn btn-primary w-100 py-2 mt-2 mb-3 rounded-5" type="submit" disabled={!isValid}>
		Register
	</button>
</form>
