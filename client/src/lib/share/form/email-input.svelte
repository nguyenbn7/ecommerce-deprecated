<script context="module">
	/**
	 * @param {string | null} errorMessage
	 * @return {Validator}
	 */
	function checkRequired(errorMessage = 'Email field is required') {
		return {
			check: (value) => value !== null && value !== undefined && value.trim().length > 0,
			errorMessage
		};
	}

	/**
	 * @param {string} errorMessage
	 * @returns {Validator}
	 */
	function checkFormat(errorMessage = 'Email has incorrect format') {
		return {
			check: (value) =>
				value !== null && value !== undefined && /^\w+@[a-zA-Z_]+?\.[a-zA-Z]{2,3}$/.test(value),
			errorMessage
		};
	}

	const EmailInputValidator = {
		checkRequired,
		checkFormat
	};

	export { EmailInputValidator };
</script>

<script>
	/**
	 * @type {import("./validation").FormField}
	 */
	export let formField;

	function onFocusOut() {
		if (!formField.dirty) formField.dirty = true;
		validate();
	}

	function validate() {
		formField.valid = false;

		for (const validator of formField.validators) {
			const { check, errorMessage } = validator;
			if (!check(formField.value)) {
				formField.invalidFeedback = errorMessage;
				return;
			}
		}

		formField.valid = true;
	}

	function onKeyUp() {
		if (!formField.dirty) formField.dirty = true;
		validate();
	}
</script>

<input
	type="email"
	bind:value={formField.value}
	on:focusout={onFocusOut}
	on:keyup={onKeyUp}
	class:is-invalid={formField.dirty && !formField.valid}
	class:is-valid={formField.dirty && formField.valid}
	{...$$restProps}
/>
