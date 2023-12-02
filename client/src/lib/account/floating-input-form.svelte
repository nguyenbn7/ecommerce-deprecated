<script>
	export { classNames as class };
	let classNames = '';

	export let type = 'text';
	export let label = 'Text';
	export let placeholder = 'text';
	export let id = 'text';
	export let disabled = false;

	/**
	 * @type {import('$lib/share/model').InputField}
	 */
	export let inputField;

	async function onFocusOut() {
		if (!inputField.dirty) inputField.dirty = true;
		validate();
	}

	function validate() {
		inputField.valid = false;

		for (const validator of inputField.validators) {
			const { check, errorMessage } = validator;
			if (!check(inputField)) {
				inputField.validationMessage = errorMessage;
				return;
			}
		}

		inputField.validationMessage = inputField.successMessage;
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

	function onKeyUp() {
		if (!inputField.dirty) inputField.dirty = true;
		validate();
	}
</script>

<input
	{type}
	class={classNames}
	{id}
	{placeholder}
	on:focusout={onFocusOut}
	on:input={handleInput}
	on:keyup={onKeyUp}
	class:is-invalid={inputField.dirty && !inputField.valid}
	class:is-valid={inputField.dirty && inputField.valid}
	{disabled}
/>
<label for={id}>{label}</label>
{#if inputField.validationMessage}
	<div
		class:invalid-feedback={inputField.dirty && !inputField.valid}
		class:valid-feedback={inputField.dirty && inputField.valid}
	>
		{inputField.validationMessage}
	</div>
{/if}
