export class InputField {
	/**
	 * @param {Validators | undefined} validators
	 */
	constructor(validators) {
		/** @type {boolean} */
		this.dirty = false;
		/** @type {boolean} */
		this.valid = false;
		/** @type {string} */
		this.value = '';
		/** @type {string | null} */
		this.validationMessage;
		/** @type {string | null} */
		this.successMessage;
		/** @type {Validators} */
		this.validators = validators ?? [];
	}
}
