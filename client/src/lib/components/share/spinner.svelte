<script context="module">
	import { Modal } from 'bootstrap';
	import { onMount } from 'svelte';

	class SpinnerService {
		/**
		 * @type {string}
		 */
		static #spinnerModalId;

		/**
		 * @param {string} id
		 */
		static setSpinnerId(id) {
			this.#spinnerModalId = id;
		}

		static show() {
			/**
			 * @type {import("bootstrap").Modal}
			 */
			const modal = Modal.getOrCreateInstance(document.getElementById(this.#spinnerModalId));
			modal.show(modal);
		}

		static hide() {
			/**
			 * @type {import("bootstrap").Modal | null}
			 */
			const modal = Modal.getInstance(document.getElementById(this.#spinnerModalId));
			modal?.hide();
		}
	}

	export { SpinnerService };
</script>

<script>
	/**
	 * @type {string}
	 */
	export let id;
	let isReady = false;
	onMount(() => (isReady = true));
</script>

<div
	class="modal"
	tabindex="-1"
	aria-hidden="true"
	data-bs-backdrop="static"
	data-bs-keyboard="false"
	class:fade={isReady}
	{id}
>
	<div class="modal-dialog modal-dialog-centered justify-content-center">
		<div class="spinner-custom"></div>
	</div>
</div>
