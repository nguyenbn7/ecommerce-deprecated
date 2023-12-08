export class FormField {
	#dirty;
	#touched;
	#valid;
	/**
	 * @type {string}
	 */
	#value;
	/**
	 * @type {string | null | undefined}
	 */
	#error;
	/**
	 * @type {Validator[]}
	 */
	#validators;
	/**
	 * @type {HTMLInputElement | undefined}
	 */
	#instance = undefined;

	/**
	 * @type {boolean}
	 */
	get valid() {
		return this.#valid;
	}

	/**
	 *
	 */
	get touched() {
		return this.#touched;
	}

	get dirty() {
		return this.#dirty;
	}

	get value() {
		return this.#value;
	}

	set value(newValue) {
		this.#value = newValue;
	}

	get error() {
		return this.#error;
	}

	get validators() {
		return this.#validators;
	}

	/**
	 * @param {HTMLInputElement} instance
	 */
	set bindInstance(instance) {
		this.#instance = instance;

		this.#instance?.addEventListener('focusin', () => {
			if (!this.#touched) this.#touched = true;
		});

		this.#instance?.addEventListener('input', ($event) => {
			/**
			 * @type {EventTarget | null}
			 */
			const target = $event.target;
			if (!target) return;
			const newValue = /** @type {HTMLInputElement} */ (target).value;
			this.#dirty = this.#value !== newValue;
			this.#value = newValue;

			if (this.#dirty) {
				this.validate();
			}
		});
	}

	validate() {
		// TODO: remove this
		console.log('Validate called');
		this.#valid = false;

		for (const validator of this.validators) {
			const { check, errorMessage } = validator;
			if (!check(this.#value)) {
				this.#error = errorMessage;
				return;
			}
		}

		this.#valid = true;
	}

	/**
	 * @param {Validator[]} validators
	 */
	constructor(...validators) {
		this.#dirty = false;
		this.#touched = false;
		this.#value = '';
		this.#valid = false;
		this.#error = null;
		this.#validators = validators ?? [];
	}
}

export class FormGroup {
	/**
	 * @this {{[field: string]: FormField | FormGroup}}
	 * @returns {boolean}
	 */
	get valid() {
		return Object.keys(this).every((propName) => this[propName]?.valid ?? true);
	}

	/**
	 * @this {{[field: string]: FormField | FormGroup}}
	 * @type {boolean}
	 */
	get touched() {
		return Object.keys(this).every((propName) => this[propName]?.touched ?? true);
	}

	/**
	 * @this {{[field: string]: FormField | FormGroup}}
	 * @type {boolean}
	 */
	get dirty() {
		return Object.keys(this).every((propName) => this[propName]?.dirty ?? true);
	}
}
