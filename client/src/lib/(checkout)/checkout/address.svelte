<script>
	import InputForm from '$lib/share/form/input-form.svelte';
import ValidationFeedback from '$lib/share/form/validation-feedback.svelte';

	/**
	 * @type {import("./form").AddressFormGroup}
	 */
	export let addressForm;
</script>

<div class="col-12">
	<label for="fullName">Full Name</label>
	<InputForm
		class="form-control rounded-1"
		bind:formField={addressForm.fullName}
		id="fullName"
		placeholder="Example: John Doe"
		type="text"
	/>
	<ValidationFeedback formField={addressForm.fullName}></ValidationFeedback>
</div>

<div class="col-12">
	<label for="phone">Phone Number</label>	
	<InputForm
		class="form-control rounded-1"
		bind:formField={addressForm.phoneNumber}
		id="phone"
		placeholder="+1 (999) 999-9999"
		type="text"
	/>
	<ValidationFeedback formField={addressForm.phoneNumber}></ValidationFeedback>
</div>

<div class="col-12">
	<label for="email">Email</label>
	<InputForm
		class="form-control rounded-1"
		bind:formField={addressForm.email}
		id="email"
		placeholder="johndoe@gmail.com"
		type="email"
	/>
	<ValidationFeedback formField={addressForm.email}></ValidationFeedback>
</div>

<div class="col-12">
	<label for="address">Address</label>
	<InputForm
		class="form-control rounded-1"
		bind:formField={addressForm.address}
		id="address"
		placeholder="1234 Main St"
		type="text"
	/>
	<ValidationFeedback formField={addressForm.address}></ValidationFeedback>
</div>

<div class="col-12">
	<label for="address2">Address 2 <span class="text-body-secondary">(Optional)</span></label>
	<InputForm
		class="form-control rounded-1"
		bind:formField={addressForm.address2}
		id="address2"
		placeholder="Apartment or suite"
		type="text"
	/>
	<ValidationFeedback formField={addressForm.address2}></ValidationFeedback>
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
