<script>
	import { goto } from '$app/navigation';
	import { page } from '$app/stores';
	import { RegisterForm } from '$lib/(account)/register/model';
	import { AccountService } from '$lib/(account)/service';
	import { ToastrService } from '$lib/share/component/toastr.svelte';
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
			ToastrService.notifySuccess(`Welcome ${userInfo?.displayName}`);
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

<div class="pt-4 pb-2">
	<h5 class="card-title text-center pb-0 fs-4">Create an Account</h5>
	<p class="text-center small">Enter your personal details to create account</p>
</div>

<form class="row g-3 px-1" on:submit={onSubmitForm}>
	<div class="col-12">
		<div class="form-floating">
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
	</div>

	<div class="col-12">
		<div class="form-floating">
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
	</div>

	<div class="col-12">
		<div class="form-floating">
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
	</div>

	<div class="col-12">
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
	</div>

	<div class="col-12">
		<div class="form-check">
			<input class="form-check-input" name="terms" type="checkbox" value="" id="acceptTerms" />
			<label class="form-check-label" for="acceptTerms">
				I agree and accept the <a href={'#'} class="text-decoration-none">terms and conditions</a>
			</label>
			<div class="invalid-feedback">You must agree before submitting.</div>
		</div>
	</div>
	<div class="col-12">
		<button
			class="btn btn-info w-100 py-2 mt-2 mb-3 rounded-4"
			type="submit"
			disabled={!registerForm.valid}
		>
			Create Account
			<!-- {#if isLocked}
				<span class="spinner-border spinner-border-sm" aria-hidden="true"></span>
				<span class="visually-hidden" role="status">Loading...</span>
			{/if} -->
		</button>
	</div>
	<div class="col-12">
		<p class="small mb-0">
			Already have an account? <a href="/login" class="text-decoration-none">Log in</a>
		</p>
	</div>
</form>
