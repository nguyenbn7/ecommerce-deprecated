<script>
	import { ECOMMERCE_NAME } from '$lib/share/constant';
	import { onMount } from 'svelte';

	onMount(async () => {
		(await import('bootstrap')).Carousel;
	});
</script>

<svelte:head>
	<title>{ECOMMERCE_NAME} - Home</title>
</svelte:head>

<div id="carouselExample" class="carousel slide" data-bs-ride="carousel">
	<div class="carousel-inner">
		<div class="carousel-item active" data-bs-slide="1000">
			<img src="/images/hero1.jpg" class="d-block w-100" alt="slide" />
		</div>
		<div class="carousel-item" data-bs-slide="1000">
			<img src="/images/hero2.jpg" class="d-block w-100" alt="slide" />
		</div>
		<div class="carousel-item" data-bs-slide="1000">
			<img src="/images/hero3.jpg" class="d-block w-100" alt="slide" />
		</div>
	</div>
	<button
		class="carousel-control-prev"
		type="button"
		data-bs-target="#carouselExample"
		data-bs-slide="prev"
	>
		<span class="carousel-control-prev-icon" aria-hidden="true"></span>
		<span class="visually-hidden">Previous</span>
	</button>
	<button
		class="carousel-control-next"
		type="button"
		data-bs-target="#carouselExample"
		data-bs-slide="next"
	>
		<span class="carousel-control-next-icon" aria-hidden="true"></span>
		<span class="visually-hidden">Next</span>
	</button>
</div>

<style lang="scss">
	img {
		object-fit: cover;
		height: 600px;
		width: 100%;
	}
</style>
