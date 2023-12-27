<script>
	export { classNames as class };
	let classNames = '';
</script>

<div class="py-5{classNames ? classNames : ''}" {...$$restProps}>
	<div class="container">
		<slot />
	</div>
</div>
