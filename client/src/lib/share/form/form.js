export class FormField {
    /**
     * @param {Validator[]} validators
     * @param {string} defaultValue
     */
    constructor(defaultValue = '', ...validators) {
        /** @type {boolean} */
        this.dirty = false;
        /** @type {boolean} */
        this.valid = false;
        /** @type {string} */
        this.value = defaultValue;
        /** @type {string | null} */
        this.invalidFeedback;
        /** @type {Validator[]} */
        this.validators = validators ?? [];
    }
}

export class FormGroup {
    constructor() {
        if (this.constructor == FormGroup) {
            throw new Error("Class is of abstract type and can't be instantiated");
        };
    }

    /**
     * @returns {boolean}
     */
    get valid() {
        return Object.keys(this).every(propName => {
            // @ts-ignore
            return this[propName]?.valid;
        })
    }
}