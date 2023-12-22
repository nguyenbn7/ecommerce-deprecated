<script context="module">
	import { icon } from '@fortawesome/fontawesome-svg-core';
	import {
		faCheckCircle,
		faExclamationCircle,
		faInfoCircle,
		faTimesCircle
	} from '@fortawesome/free-solid-svg-icons';
	import { Toast } from 'bootstrap';
	import { writable } from 'svelte/store';

	/**
	 * @type {import('svelte/store').Writable<string | null>}
	 */
	let messageStore = writable(null);
	/**
	 * @type {import('svelte/store').Writable<Toastr.Type | null>}
	 */
	let typeStore = writable(null);
	/**
	 * @type {HTMLDivElement | null}
	 */
	let ele = null;

	let container = null;

	/**
	 * @param {string} id
	 */
	function registerContainer(id) {
		container = document.getElementById(id);
	}

	/**
	 * @param {string} message
	 * @param {Toastr.Type} type
	 */
	function notify(message, type) {
		/**
		 * @type {import("bootstrap").Toast}
		 */
		let toast = Toast.getOrCreateInstance(ele);

		messageStore.update((_) => message);
		typeStore.update((_) => type);
		toast.show();
	}

	/**
	 * @param {string} message
	 */
	function notifyDanger(message) {
		notify(message, 'DANGER');
	}

	/**
	 * @param {string} message
	 */
	function notifySuccess(message) {
		notify(message, 'SUCCESS');
	}

	/**
	 * @param {string} message
	 */
	function notifyWarning(message) {
		notify(message, 'WARNING');
	}

	/**
	 * @param {string} message
	 */
	function notifyInfo(message) {
		notify(message, 'INFO');
	}

	function onClickHide() {
		/**
		 * @type {import("bootstrap").Toast | null}
		 */
		let toast = Toast.getInstance(ele);

		if (!toast) return;

		toast.hide();
	}

	const ToastService = {
		registerContainer,
		notify,
		notifyDanger,
		notifyInfo,
		notifySuccess,
		notifyWarning
	};

	export { ToastService };
</script>

<script>
	/**
	 * @param {Toastr.Type | null} toastType
	 */
	function getToastIcon(toastType) {
		switch (toastType) {
			case 'DANGER':
				return faTimesCircle;
			case 'INFO':
				return faInfoCircle;
			case 'SUCCESS':
				return faCheckCircle;
			case 'WARNING':
				return faExclamationCircle;
			default:
				return null;
		}
	}
	$: typeIcon = getToastIcon($typeStore);
	$: message = $messageStore || '';
</script>

<!-- svelte-ignore a11y-click-events-have-key-events -->
<!-- svelte-ignore a11y-no-noninteractive-tabindex -->
<!-- svelte-ignore a11y-no-static-element-interactions -->
<div
	class="toast"
	aria-live="assertive"
	aria-atomic="true"
	tabindex="0"
	bind:this={ele}
	on:click={onClickHide}
	role="button"
>
	<div
		class="row text-white"
		class:bg-danger={$typeStore === 'DANGER'}
		class:bg-success={$typeStore === 'SUCCESS'}
		class:bg-warning={$typeStore === 'WARNING'}
		class:bg-info={$typeStore === 'INFO'}
	>
		{#if typeIcon}
			<div class="col-3 text-center ps-0">
				{@html icon(typeIcon, {
					styles: {
						'font-size': '2.5em',
						margin: '0.25em 0'
					}
				}).html}
			</div>
		{/if}
		<div class="col-9 py-2 pe-1 fs-6">
			<div class="text-wrap text-break">{message}</div>
		</div>
	</div>
</div>
