<script>
	export { classNames as class };
	let classNames = '';

	export let type = 'text';
	export let label = 'Text';
	export let placeholder = 'text';
	export let id = 'text';

	/**
	 * @type {import('$lib/util/model').TextFieldValidation}
	 */
	export let inputField;

	/**
	 * @type {number | undefined}
	 */
	let delayValidateAfterKeyUp;
	let timer = 250; // 0.25 sec

	function onFocus() {
		if (!inputField.dirty) {
			inputField.dirty = true;
			validate();
		}
	}

	function validate() {
		inputField.valid = false;

		const validationList = inputField.validation;
		for (let i = 0; i < validationList.length; i++) {
			if (!validationList[i].validator(inputField)) {
				if (validationList[i].errorMessage)
					// @ts-ignore
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

	function onKeyUp() {
		if (!inputField.dirty) return;
		clearTimeout(delayValidateAfterKeyUp);
		delayValidateAfterKeyUp = setTimeout(validate, timer);
	}

	function onKeyDown() {
		if (!inputField.dirty) return;
		clearTimeout(delayValidateAfterKeyUp);
	}
</script>

<div class={classNames}>
	<input
		{type}
		class="form-control rounded-5"
		{id}
		{placeholder}
		on:focusout={onFocus}
		on:input={handleInput}
		on:keyup={onKeyUp}
		on:keydown={onKeyDown}
		class:is-invalid={inputField.dirty && !inputField.valid}
		class:is-valid={inputField.dirty && inputField.valid}
	/>
	<label for={id}>{label}</label>
	<div
		class:invalid-feedback={inputField.dirty && !inputField.valid}
		class:valid-feedback={inputField.dirty && inputField.valid}
	>
		{inputField.validationMessage}
	</div>
</div>
