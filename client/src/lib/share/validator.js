import { checkEmailFormat } from './functions';

/**
 * @param {string | null} errorMessage
 * @return {Validator}
 */
export function requireField(errorMessage = 'Field is required') {
	return {
		check: (field) => field.value.trim().length >= 1,
		errorMessage
	};
}

/**
 * @param {string} errorMessage
 * @returns {Validator}
 */
export function hasCorrectEmailFormat(errorMessage = 'Email has incorrect format') {
	return {
		check: (field) => checkEmailFormat(field.value),
		errorMessage
	};
}

/**
 * @param {string} errorMessage
 * @returns {Validator}
 */
export function hasMaxLength(errorMessage = '', max_length = 256) {
	return {
		check: (field) => field.value.length <= max_length,
		errorMessage: errorMessage ? errorMessage : `Field should have maximum ${max_length} characters`
	};
}

/**
 * @param {string} errorMessage
 * @returns {Validator}
 */
export function hasAlnumAndSpace(errorMessage = 'Field contains only numbers, letters and spaces') {
	return {
		check: (field) => /^[a-zA-Z\s\d]+$/.test(field.value),
		errorMessage
	};
}
