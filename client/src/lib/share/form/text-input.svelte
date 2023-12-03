<script context="module">
	/**
	 * @param {string | null} errorMessage
	 * @return {Validator}
	 */
	function checkRequired(errorMessage = 'Text field is required') {
		return {
			check: (value) => value !== null && value !== undefined && value.trim().length > 0,
			errorMessage
		};
	}

	const TextInputValidator = {
		checkRequired
	};

	export { TextInputValidator };
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
	type="text"
	bind:value={formField.value}
	on:focusout={onFocusOut}
	on:keyup={onKeyUp}
	class:is-invalid={formField.dirty && !formField.valid}
	class:is-valid={formField.dirty && formField.valid}
	{...$$restProps}
/>
