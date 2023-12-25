<script context="module">
	class RegisterForm extends FormGroup {
		/**
		 * @param {number | undefined} displayNameMaxLen
		 */
		constructor(displayNameMaxLen) {
			super();
			this.displayName = new FormField(
				Validators.checkRequired('Name is required'),
				Validators.containsAlnumAndSpace('Name contains only letters and spaces'),
				Validators.checkMaxLength(
					`Name's max length is ${displayNameMaxLen} characters`,
					displayNameMaxLen
				)
			);

			this.email = new FormField(
				Validators.checkRequired('Email is required'),
				Validators.checkEmailFormat('Incorrect email. Example: bob@test.com')
			);

			this.password = new FormField(
				Validators.checkRequired('Password is required'),
				Validators.isPasswordComplexEnough(
					'Password must have At least 8 characters long. - At least 1 uppercase, AND at least 1 lowercase - At least 1 digit OR at least 1 alphanumeric'
				)
			);

			this.confirmPassword = new FormField(
				Validators.checkRequired('Confirm Password is required'),
				Validators.doesFieldEqualTo(this.password, 'Confirm Password does not match with Password')
			);
		}
	}
</script>

<script>
	import { goto } from '$app/navigation';
	import { page } from '$app/stores';
	import ButtonSpinner from '$lib/share/component/button-spinner.svelte';
	import { ToastrService } from '$lib/share/component/toastr.svelte';
	import { ECOMMERCE_NAME } from '$lib/share/constant';
	import { FormField, FormGroup } from '$lib/share/form/class';
	import FloatingInputValidation from '$lib/share/form/floating-input-validation.svelte';
	import { Validators } from '$lib/share/form/validation';
	import { AccountService } from '$lib/share/service/account';

	const displayNameMaxLen = 70;

	let registerForm = new RegisterForm(displayNameMaxLen);
	let isSubmitted = false;

	async function onSubmitForm() {
		try {
			isSubmitted = true;
			const userInfo = await AccountService.register({
				email: registerForm.email.value,
				password: registerForm.password.value,
				displayName: registerForm.displayName.value,
				confirmPassword: registerForm.confirmPassword.value
			});

			if (userInfo) {
				ToastrService.notifySuccess(`Welcome ${userInfo?.displayName}`);
				const returnUrl = $page.url.searchParams.get('redirect');
				if (returnUrl) return goto(returnUrl);
				return goto('/');
			}
		} finally {
			isSubmitted = false;
		}
	}
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
			<FloatingInputValidation
				class="form-control rounded-4"
				id="displayName"
				label="Display Name"
				placeholder="I am cute"
				bind:formField={registerForm.displayName}
				disabled={isSubmitted}
			/>
		</div>
	</div>

	<div class="col-12">
		<div class="form-floating">
			<FloatingInputValidation
				class="form-control rounded-4"
				type="email"
				id="email"
				label="Email"
				placeholder="name@example.com"
				bind:formField={registerForm.email}
				disabled={isSubmitted}
			/>
		</div>
	</div>

	<div class="col-12">
		<div class="form-floating">
			<FloatingInputValidation
				class="form-control rounded-4"
				type="password"
				id="password"
				label="Password"
				placeholder="Password"
				bind:formField={registerForm.password}
				disabled={isSubmitted}
			/>
		</div>
	</div>

	<div class="col-12">
		<div class="form-floating mt-2 mb-3">
			<FloatingInputValidation
				class="form-control rounded-4"
				type="password"
				id="confirmPassword"
				label="Confirm Password"
				placeholder="Confirm password"
				bind:formField={registerForm.confirmPassword}
				disabled={isSubmitted}
			/>
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
			disabled={!registerForm.valid || isSubmitted}
		>
			Create Account
			{#if isSubmitted}
				<ButtonSpinner />
			{/if}
		</button>
	</div>
	<div class="col-12">
		<p class="small mb-0">
			Already have an account? <a href="/login" class="text-decoration-none">Log in</a>
		</p>
	</div>
</form>
