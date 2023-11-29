<script context="module">
	import { Modal } from 'bootstrap';

	class SpinnerService {
		static #spinnerModalId = 'spinnerModal';
		static #modalInstance() {
			/**
			 * @type {import("bootstrap").Modal}
			 */
			let instance = Modal.getOrCreateInstance(document.getElementById(this.#spinnerModalId));

			return {
				get: () => {
					if (!instance)
						instance = Modal.getOrCreateInstance(document.getElementById(this.#spinnerModalId));
					return instance;
				}
			};
		}

		static show() {
			const modal = this.#modalInstance().get();
			modal.show();
		}

		static hide() {
			const modal = this.#modalInstance().get();
			modal.hide();
		}
	}

	export { SpinnerService };
</script>

<div
	class="modal fade"
	tabindex="-1"
	aria-hidden="true"
	data-bs-backdrop="static"
	data-bs-keyboard="false"
	id="spinnerModal"
>
	<div class="modal-dialog modal-dialog-centered justify-content-center">
		<div class="spinner-custom"></div>
	</div>
</div>
