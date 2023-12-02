import { CURRENCY_CODE } from './constant';

/**
 * @param {string} code
 * @param {number} amount
 * @returns {string}
 */
export function currency(amount, code = CURRENCY_CODE.US_Dollar) {
	return new Intl.NumberFormat(navigator.language, {
		style: 'currency',
		currency: code
	}).format(amount);
}

/**
 * @param {string} str
 */
export function readMoreString(str, max_length = 50) {
	return str.length > max_length ? `${str.substring(0, max_length)}...` : str;
}

/**
 * @param {string} email
 */
export function checkEmailFormat(email) {
	const regex = /^\w+@[a-zA-Z_]+?\.[a-zA-Z]{2,3}$/;
	return regex.test(email);
}

export async function delay(ms = 1500) {
	return new Promise((resolve) => setTimeout(resolve, ms));
}
