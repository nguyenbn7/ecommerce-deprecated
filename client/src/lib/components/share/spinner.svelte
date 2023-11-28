<script context="module">
	import { Modal } from 'bootstrap';

	/**
	 * @type {string | undefined}
	 */
	let spinnerId = undefined;
	/**
	 * @type {import("bootstrap").Modal}
	 */
	let spinerInstance;

	/**
	 * @param {string | undefined} id
	 */
	export function registerSpinnerId(id = 'spinnerId') {
		spinnerId = id;
		spinerInstance = new Modal(document.getElementById(spinnerId));
	}

	export function getSpinnerInstance() {
		if (!spinnerId) {
			throw Error('Spinner id is null or not found');
		}

		if (!spinerInstance) {
			throw Error('Can not create spinner instanceFF');
		}

		return {
			show: () => spinerInstance.show(),
			hide: () => spinerInstance.hide()
		};
	}
</script>
