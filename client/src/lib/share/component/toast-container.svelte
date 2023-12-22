<script>
	import Toast from './toast.svelte';

	/**
	 * @type {string}
	 */
	export let id;
	export { classNames as class };
	/**
	 * @type {string}
	 */
	let classNames;
</script>

<div class={classNames} {id}>
	<Toast />
</div>
