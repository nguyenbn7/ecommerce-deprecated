<script>
	export { classNames as class };
	let classNames = '';

	export let type = 'text';
	export let label = 'Text';
	export let placeholder = 'text';

	/**
	 * @type {TextFieldValidation}
	 */
	export let inputField;

	function validate() {
		inputField.dirty = true;

		const validationList = inputField.validation;
		for (let i = 0; i < validationList.length; i++) {
			if (!validationList[i].validator(inputField)) {
				if (validationList[i].errorMessage)
					inputField.validationMessage = validationList[i].errorMessage;
				return;
			}
		}

		inputField.validationMessage = inputField.successMessage ? inputField.successMessage : '';
		inputField.valid = true;
	}

	/**
	 * @param {Event & { currentTarget: EventTarget & HTMLInputElement; }} $event
	 */
	function handleInput($event) {
		// @ts-ignore
		inputField.value = $event.target.value;
		// inputField.value = type.match(/^(number|range)$/) ? +$event.target.value : $event.target.value;
	}
</script>

<div class={classNames}>
	<input
		{type}
		class="form-control rounded-5"
		id={type}
		{placeholder}
		on:focusout={validate}
		on:input={handleInput}
		class:is-invalid={inputField.dirty && !inputField.valid}
		class:is-valid={inputField.dirty && inputField.valid}
	/>
	<label for={type}>{label}</label>
	<div
		class:invalid-feedback={inputField.dirty && !inputField.valid}
		class:valid-feedback={inputField.dirty && inputField.valid}
	>
		{inputField.validationMessage}
	</div>
</div>
