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
 * @param {TextFieldValidation} field
 */
export function checkFieldRequired(field) {
	return field.value.trim().length >= 1;
}

/**
 * @param {TextFieldValidation} field
 */
export function checkEmailFormat(field) {
	return validateEmailPattern(field.value);
}
