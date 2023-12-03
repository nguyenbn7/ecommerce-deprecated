<script context="module">
	export class AddressForm {
		#onSubmit = false;
		constructor() {
			this.fullNameField = new FormField(TextInputValidator.checkRequired('Full name is required'));
			this.emailField = new FormField(
				EmailInputValidator.checkRequired('Email is required'),
				EmailInputValidator.checkFormat('Incorrect email. Example: bob@test.com')
			);
			this.addressField = new FormField(TextInputValidator.checkRequired('Address is required'));
			this.address2Field = new FormField();
		}

		get valid() {
			return (
				this.fullNameField.valid &&
				this.emailField.valid &&
				this.addressField.valid &&
				this.address2Field.valid
			);
		}

		/**
		 * @param {boolean} state
		 */
		set isSubmiting(state) {
			this.#onSubmit = state;
		}

		get isSubmiting() {
			return this.#onSubmit;
		}
	}
</script>

<script>
	import EmailInput, { EmailInputValidator } from '$lib/share/form/email-input.svelte';
	import TextInput, { TextInputValidator } from '$lib/share/form/text-input.svelte';
	import { FormField } from '$lib/share/form/validation';
	import ValidationFeedback from '$lib/share/form/validation-feedback.svelte';

	/**
	 * @type {AddressForm}
	 */
	export let addressForm;
</script>

<div class="col-12">
	<label for="fullName">Full Name</label>
	<TextInput
		class="form-control rounded-1"
		bind:formField={addressForm.fullNameField}
		id="fullName"
		placeholder="Example: John Doe"
	></TextInput>
	<ValidationFeedback formField={addressForm.fullNameField}></ValidationFeedback>
</div>

<div class="col-12">
	<label for="email">Email</label>
	<EmailInput
		class="form-control rounded-1"
		bind:formField={addressForm.emailField}
		id="email"
		placeholder="johndoe@gmail.com"
	></EmailInput>
	<ValidationFeedback formField={addressForm.emailField}></ValidationFeedback>
</div>

<div class="col-12">
	<label for="address">Address</label>
	<TextInput
		class="form-control rounded-1"
		bind:formField={addressForm.addressField}
		id="address"
		placeholder="1234 Main St"
	></TextInput>
	<ValidationFeedback formField={addressForm.addressField}></ValidationFeedback>
</div>

<div class="col-12">
	<label for="address2">Address 2 <span class="text-body-secondary">(Optional)</span></label>
	<TextInput
		class="form-control rounded-1"
		bind:formField={addressForm.address2Field}
		id="address2"
		placeholder="Apartment or suite"
	></TextInput>
	<ValidationFeedback formField={addressForm.address2Field}></ValidationFeedback>
</div>

<div class="col-md-5">
	<label for="country" class="form-label">Country</label>
	<select class="form-select" id="country">
		<option value="">Choose...</option>
		<option>United States</option>
	</select>
	<div class="invalid-feedback">Please select a valid country.</div>
</div>

<div class="col-md-4">
	<label for="state" class="form-label">State</label>
	<select class="form-select" id="state">
		<option value="">Choose...</option>
		<option>California</option>
	</select>
	<div class="invalid-feedback">Please provide a valid state.</div>
</div>

<div class="col-md-3">
	<label for="zip" class="form-label">Zip</label>
	<input type="text" class="form-control" id="zip" placeholder="" />
	<div class="invalid-feedback">Zip code required.</div>
</div>
