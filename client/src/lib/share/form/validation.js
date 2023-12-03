export class FormField {
    /**
     * @param {Validator[]} validators
     */
    constructor(...validators) {
        /** @type {boolean} */
        this.dirty = false;
        /** @type {boolean} */
        this.valid = false;
        /** @type {string} */
        this.value = '';
        /** @type {string | null} */
        this.invalidFeedback;
        /** @type {Validator[]} */
        this.validators = validators ?? [];
    }
}

/**
 * @param {string} errorMessage
 * @returns {Validator}
 */
function checkMaxLength(errorMessage = '', max_length = 256) {
    return {
        check: (value) => value !== null && value !== undefined && value.length <= max_length,
        errorMessage: errorMessage ? errorMessage : `Field should have maximum ${max_length} characters`
    };
}

/**
 * @param {string} errorMessage
 * @returns {Validator}
 */
function containsAlnumAndSpace(errorMessage = 'Field contains only numbers, letters and spaces') {
    return {
        check: (value) => value !== null && value !== undefined && /^[a-zA-Z\s\d]+$/.test(value),
        errorMessage
    };
}

export const Validators = {
    checkMaxLength,
    containsAlnumAndSpace
}