<script>
	/**
	 * @type {import("./class").FormField}
	 */
	export let formField;

	/**
	 * @type {string | null | undefined}
	 */
	export let success = null;
</script>

{#if formField.dirty && !formField.valid}
	<div class="invalid-feedback">
		{#if formField.error}
			{formField.error}
		{/if}
	</div>
{:else if formField.dirty && formField.valid}
	<div class="valid-feedback">
		{#if success}
			{success}
		{/if}
	</div>
{/if}
