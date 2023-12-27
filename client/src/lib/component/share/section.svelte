<script>
	export { classNames as class };
	export let containerClass = '';

	let classNames = '';

	classNames = 'py-5 ' + classNames.trim();
	classNames = classNames.trim();

	containerClass = 'container ' + containerClass.trim();
	containerClass = containerClass.trim();
</script>

<div class={classNames} {...$$restProps}>
	<div class={containerClass}>
		<slot />
	</div>
</div>
