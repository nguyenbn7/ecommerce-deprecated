<script context="module">
	import { Toast } from 'bootstrap';

	/**
	 * @type {HTMLDivElement}
	 */
	let ele;

	export function hide() {
		/**
		 * @type {import("bootstrap").Toast | null}
		 */
		let toast = Toast.getInstance(ele);

		if (!toast) return;

		if (toast.isShown()) toast.hide();
	}
</script>

<script>
	import { icon } from '@fortawesome/fontawesome-svg-core';
	import {
		faCheckCircle,
		faExclamationCircle,
		faInfoCircle,
		faTimesCircle
	} from '@fortawesome/free-solid-svg-icons';
	import { onMount } from 'svelte';

	/**
	 * @type {string | null}
	 */
	export let message = null;
	/**
	 * @type {Toastr.Type | null}
	 */
	export let type = null;

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

	const typeIcon = getToastIcon(type);

	onMount(() => {
		let toast = new Toast(ele);

		toast.show();
		setTimeout(() => ele.parentNode?.removeChild(ele), toast._config.delay + 1000);
	});
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
	role="button"
	on:click
>
	<div
		class="row text-white"
		class:bg-danger={type === 'DANGER'}
		class:bg-success={type === 'SUCCESS'}
		class:bg-warning={type === 'WARNING'}
		class:bg-info={type === 'INFO'}
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
