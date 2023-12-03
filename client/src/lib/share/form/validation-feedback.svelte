<script>
	/**
	 * @type {import("./validation").FormField}
	 */
	export let formField;

	/**
	 * @type {string | null | undefined}
	 */
	export let validFeedback = null;
</script>

{#if formField.dirty && !formField.valid}
	<div class="invalid-feedback">
		{#if formField.invalidFeedback}
			{formField.invalidFeedback}
		{/if}
	</div>
{:else if formField.dirty && formField.valid}
	<div class="valid-feedback">
		{#if validFeedback}
			{validFeedback}
		{/if}
	</div>
{/if}
