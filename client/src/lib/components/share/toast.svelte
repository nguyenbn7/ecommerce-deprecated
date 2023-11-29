<script context="module">
	import Toast from './toast.svelte';

	class ToastService {
		/**
		 * @type {string}
		 */
		static #containerId;

		/**
		 * @param {string} id
		 */
		static setToastContainerId(id) {
			this.#containerId = id;
		}

		static #instance() {
			let toastContainer = document.getElementById(this.#containerId);

			return {
				get: () => {
					if (!toastContainer) {
						throw Error('Can not get toast container');
					}
					return toastContainer;
				}
			};
		}

		/**
		 * @param {string} message
		 * @param {Toastr.Type} type
		 */
		static notify(message, type) {
			const container = this.#instance().get();

			const toast = new Toast({
				target: container,
				props: { message, type }
			});
			toast.show();
		}

		/**
		 * @param {string} message
		 */
		static notifyError(message) {
			this.notify(message, 'ERROR');
		}

		/**
		 * @param {string} message
		 */
		static notifySuccess(message) {
			this.notify(message, 'SUCCESS');
		}

		/**
		 * @param {string} message
		 */
		static notifyWarning(message) {
			this.notify(message, 'WARNING');
		}

		/**
		 * @param {string} message
		 */
		static notifyInfo(message) {
			this.notify(message, 'INFO');
		}
	}

	export { ToastService };
</script>

<script>
	// TODO: use Toast Bootstrap if possible
	import { fade, fly } from 'svelte/transition';

	/** @type {Toastr.Configuration} */
	export let config = {
		animation: true,
		autohide: true,
		/** Delay hidden time in (ms)*/
		delay: 2000,
		autodispose: true,
		enableClickToastDispose: true,
		enableClickToastHide: false
	};

	/** @type {Toastr.Type} */
	export let type;

	let classNames = '';
	export { classNames as class };

	/** @type {string} */
	export let message;

	let isShown = false;

	/**
	 * @type {number | null | undefined}
	 */
	let timeout = null;

	/**
	 * @type {HTMLDivElement}
	 */
	let el;

	export function show() {
		isShown = true;
		if (config.autohide) {
			timeout = setTimeout(() => {
				hide();
			}, config.delay);
			return;
		}

		if (config.autodispose) {
			timeout = setTimeout(() => dispose(), config.delay);
			return;
		}
	}

	export function hide() {
		isShown = false;
		clearInternalTimeout();
	}

	export function dispose() {
		isShown = false;
		clearInternalTimeout();
		if (el) {
			setTimeout(() => el.parentElement?.removeChild(el), 1000);
		}
	}

	/**
	 * @param {HTMLDivElement | Element} node
	 * @param {import("svelte/transition").FlyParams | undefined} [flyParams]
	 */
	function customFly(node, flyParams) {
		if (!config.animation) {
			return fly(node, { delay: 0, duration: 0 });
		}
		flyParams = {
			x: 300,
			duration: 2000
		};
		return fly(node, flyParams);
	}

	/**
	 * @param {HTMLDivElement | Element} node
	 * @param {import("svelte/transition").FadeParams | undefined} [fadeParams]
	 */
	function customFade(node, fadeParams) {
		if (!config.animation) {
			// This one can cause bug
			return fade(node, { delay: 0, duration: 0 });
		}
		return fade(node, fadeParams);
	}

	function clearInternalTimeout() {
		if (timeout) clearTimeout(timeout);
		timeout = null;
	}

	function onClickToast() {
		if (config.enableClickToastHide) {
			hide();
			return;
		}
		if (config.enableClickToastDispose) {
			dispose();
			return;
		}
	}
</script>

{#if isShown}
	<div
		class={`toast show ${classNames}`}
		role="button"
		aria-live="assertive"
		aria-atomic="true"
		in:customFly
		out:customFade
		tabindex="0"
		on:click={onClickToast}
		{...$$restProps}
		bind:this={el}
	>
		<div
			class="row text-white bg-danger"
			class:bg-danger={type === 'ERROR'}
			class:bg-success={type === 'SUCCESS'}
			class:bg-warning={type === 'WARNING'}
			class:bg-info={type === 'INFO'}
		>
			<div class="col-3 text-center ps-0">
				<i
					class="bi"
					style="font-size: 2.5em;"
					class:bi-x-circle={type === 'ERROR'}
					class:bi-check-circle={type === 'SUCCESS'}
					class:bi-exclamation-circle={type === 'WARNING'}
					class:bi-info-circle={type === 'INFO'}
				/>
			</div>
			<div class="col-9 py-2 pe-1 fs-6">
				<div class="text-wrap text-break">{message}</div>
			</div>
		</div>
	</div>
{/if}
