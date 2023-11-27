<script>
	import InputForm from '$lib/components/account/input-form.svelte';
	import { loginAs } from '$lib/service/account.service';
	import { ECOMMERCE_NAME } from '$lib/util/application.constant';
	import { checkEmailFormat, checkFieldRequired } from '$lib/util/helper.function';
	import { TextFieldValidation } from '$lib/util/model';

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

	$: isValid = emailField.valid && passwordField.valid;

	async function onSubmitForm() {
		/**
		 * @type {LoginSuccess}
		 */
		const data = await loginAs({ email: emailField.value, password: passwordField.value });
		if (data instanceof Response) {
			const errorResponse = await data.json();
			console.error(errorResponse);
			return;
		}
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

		<div class="d-flex justify-content-between my-3">
			<div class="form-check text-start">
				<input class="form-check-input" type="checkbox" value="remember-me" id="flexCheckDefault" />
				<label class="form-check-label" for="flexCheckDefault"> Remember me </label>
			</div>
			<div class="text-end">
				<a href={'#'} class="text-decoration-none">Forgot password?</a>
			</div>
		</div>
		<button
			class="btn btn-primary w-100 py-2 mt-2 mb-3 rounded-5"
			type="submit"
			disabled={!isValid}
		>
			Login
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
			<button class="btn btn-outline-info rounded-5" type="submit"> Demo Customer </button>
		</div>
		<div class="col d-flex justify-content-center">
			<button class="btn btn-outline-info rounded-5" type="submit"> Demo Customer1 </button>
		</div>
	</div>
</div>

<style>
	hr {
		margin: 0.9rem 0;
	}
</style>
