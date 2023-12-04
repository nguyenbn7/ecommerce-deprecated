/**
 * @param {string} errorMessage
 * @returns {Validator}
 */
function checkRequired(errorMessage = 'Field is required') {
    return {
        check: (value) => !!value,
        errorMessage
    }
}
/**
 * @param {string} errorMessage
 * @returns {Validator}
 */
function checkMaxLength(errorMessage = '', max_length = 256) {
    return {
        check: (value) => value.length <= max_length,
        errorMessage: errorMessage ? errorMessage : `Field should have maximum ${max_length} characters`
    };
}

/**
 * @param {string} errorMessage
 * @returns {Validator}
 */
function containsAlnumAndSpace(errorMessage = 'Field contains only numbers, letters and spaces') {
    return {
        check: (value) => /^[a-zA-Z\s\d]+$/.test(value),
        errorMessage
    };
}
/**
 * @param {string} errorMessage
 * @returns {Validator}
 */
function checkEmailFormat(errorMessage = 'Email has incorrect format') {
    return {
        check: (value) => /^\w+@[a-zA-Z_]+?\.[a-zA-Z]{2,3}$/.test(value),
        errorMessage
    };
}

export const Validators = {
    checkRequired,
    checkMaxLength,
    containsAlnumAndSpace,
    checkEmailFormat
}