<script context="module">
	import { FormField, FormGroup, Validators } from '$lib/component/share/form';

	export class AddressFormGroup extends FormGroup {
		constructor() {
			super();
			this.fullName = new FormField(Validators.checkRequired('Full name is required'));
			this.email = new FormField(
				Validators.checkRequired('Email is required'),
				Validators.checkEmailFormat('Incorrect email. Example: bob@test.com')
			);
			this.phoneNumber = new FormField(Validators.checkRequired('Phone number is required'));
			this.address = new FormField(Validators.checkRequired('Address is required'));
			this.address2 = new FormField(Validators.isOptional());
		}
	}
</script>

<script>
	import Input from '$lib/component/share/form/input.svelte';

	/**
	 * @type {AddressFormGroup}
	 */
	export let addressForm;
</script>

<div class="col-12">
	<Input
		class="form-control rounded-1"
		id="fullName"
		placeholder="Example: John Doe"
		label="Full Name"
		bind:formField={addressForm.fullName}
	/>
</div>

<div class="col-12">
	<Input
		class="form-control rounded-1"
		id="phone"
		placeholder="+1 (999) 999-9999"
		label="Phone Number"
		bind:formField={addressForm.phoneNumber}
	/>
</div>

<div class="col-12">
	<Input
		class="form-control rounded-1"
		type="email"
		id="email"
		placeholder="johndoe@gmail.com"
		label="Email"
		bind:formField={addressForm.email}
	/>
</div>

<div class="col-12">
	<Input
		class="form-control rounded-1"
		id="address"
		placeholder="1234 Main St"
		label="Address"
		bind:formField={addressForm.address}
	/>
</div>

<div class="col-12">
	<Input
		class="form-control rounded-1"
		id="address2"
		placeholder="Apartment or suite"
		label={`Address 2 <span class="text-body-secondary">(Optional)</span>`}
		bind:formField={addressForm.address2}
	/>
</div>

<!-- TODO: Validate Country -->
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
