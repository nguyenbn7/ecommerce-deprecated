<script>
	/**
	 * @type {import("./class").FormField}
	 */
	export let formField;
	/**
	 * @type {string | undefined}
	 */
	export let type;
</script>

<input
	{type}
	bind:this={formField.bindInstance}
	class:is-invalid={formField.dirty && !formField.valid}
	class:is-valid={formField.dirty && formField.valid}
	{...$$restProps}
/>
