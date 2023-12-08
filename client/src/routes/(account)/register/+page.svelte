<script>
	import { goto } from '$app/navigation';
	import { page } from '$app/stores';
	import { RegisterForm } from '$lib/(account)/register/model';
	import { AccountService } from '$lib/(account)/service';
	import { ToastService } from '$lib/share/component/toast.svelte';
	import { ECOMMERCE_NAME } from '$lib/share/constant';
	import InputForm from '$lib/share/form/input-form.svelte';
	import ValidationFeedback from '$lib/share/form/validation-feedback.svelte';

	async function onSubmitForm() {
		const userInfo = await AccountService.register({
			email: registerForm.email.value,
			password: registerForm.password.value,
			display_name: registerForm.displayName.value,
			confirm_password: registerForm.confirmPassword.value
		});

		if (userInfo) {
			ToastService.notifySuccess(`Welcome ${userInfo?.displayName}`);
			const returnUrl = $page.url.searchParams.get('redirect');
			if (returnUrl) return goto(returnUrl);
			return goto('/');
		}
	}

	const displayNameMaxLen = 70;

	let registerForm = new RegisterForm(displayNameMaxLen);
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
		<InputForm
			class="form-control rounded-4"
			bind:formField={registerForm.displayName}
			id="displayName"
			placeholder="I am cute"
			type="text"
		/>
		<label for="displayName">Display Name</label>
		<ValidationFeedback formField={registerForm.displayName}></ValidationFeedback>
	</div>

	<div class="form-floating mt-2 mb-3">
		<InputForm
			class="form-control rounded-4"
			bind:formField={registerForm.email}
			id="email"
			placeholder="name@example.com"
			type="email"
		/>
		<label for="email">Email</label>
		<ValidationFeedback formField={registerForm.email}></ValidationFeedback>
	</div>

	<div class="form-floating mt-2 mb-3">
		<InputForm
			class="form-control rounded-4"
			bind:formField={registerForm.password}
			id="password"
			placeholder="Password"
			type="password"
		/>
		<label for="password">Password</label>
		<ValidationFeedback formField={registerForm.password}></ValidationFeedback>
	</div>

	<div class="form-floating mt-2 mb-3">
		<InputForm
			class="form-control rounded-4"
			bind:formField={registerForm.confirmPassword}
			id="confirmPassword"
			placeholder="Confirm password"
			type="password"
		/>
		<label for="confirmPassword">Confirm Password</label>
		<ValidationFeedback formField={registerForm.confirmPassword}></ValidationFeedback>
	</div>

	<button
		class="btn btn-primary w-100 py-2 mt-2 mb-3 rounded-5"
		type="submit"
		disabled={!registerForm.valid}
	>
		Register
		<!-- {#if isLocked}
			<span class="spinner-border spinner-border-sm" aria-hidden="true"></span>
			<span class="visually-hidden" role="status">Loading...</span>
		{/if} -->
	</button>
</form>
