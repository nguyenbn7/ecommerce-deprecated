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
