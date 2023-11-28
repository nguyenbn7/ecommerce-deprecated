/**
 * @param {string} str
 */
export function titleCase(str) {
	return (
		str
			?.toLowerCase()
			.split(' ')
			.map(function (word) {
				return word.charAt(0).toUpperCase() + word.slice(1).toLowerCase();
			})
			.join(' ') ?? ''
	);
}

/**
 * @param {number} amount
 */
export function formatAsUSD(amount) {
	return new Intl.NumberFormat('en-US', {
		style: 'currency',
		currency: 'USD'
	}).format(amount);
}

/**
 * @param {string} email
 */
export function validateEmailPattern(email) {
	const regex = /^\w+@[a-zA-Z_]+?\.[a-zA-Z]{2,3}$/;
	return regex.test(email);
}

/**
 * @param {import("./model").TextFieldValidation} field
 */
export function checkFieldRequired(field) {
	return field.value.trim().length >= 1;
}

/**
 * @param {import("./model").TextFieldValidation} field
 */
export function checkEmailFormat(field) {
	return validateEmailPattern(field.value);
}

export function checkNameMaxLength(max_length = 256) {
	return (/** @type {import("./model").TextFieldValidation} */ field) =>
		field.value.length <= max_length;
}

/**
 * @param {import("./model").TextFieldValidation} field
 */
export function checkNameContainsLettersNumbersAndWhiteSpace(field) {
	return /^[a-zA-Z\s\d]+$/.test(field.value);
}

/**
 * @param {string} str
 */
export function readMoreString(str, max_length = 50) {
	return str.length > max_length ? `${str.substring(0, max_length)}...` : str;
}
