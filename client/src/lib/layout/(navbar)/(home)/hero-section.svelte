<script>
	import { onMount } from 'svelte';

	const heroSectionId = 'heroSection';
	const heroImages = ['hero1.jpg', 'hero2.jpg', 'hero3.jpg'];
	onMount(
		async () =>
			new (await import('bootstrap')).Carousel(document.getElementById(heroSectionId), {
				interval: 2000,
				ride: 'carousel',
				pause: false
			})
	);
</script>

<section class="carousel slide" id={heroSectionId}>
	<div class="carousel-indicators">
		{#each heroImages as _, idx}
			<button
				type="button"
				data-bs-target="#{heroSectionId}"
				data-bs-slide-to={idx}
				class:active={idx === 0}
				aria-current="true"
				aria-label="Slide {idx + 1}"
			></button>
		{/each}
	</div>
	<div class="carousel-inner">
		{#each heroImages as image, idx}
			<div class="carousel-item" class:active={idx === 0}>
				<img
					src="/images/home/hero/{image}"
					class="m-0 min-vw-100 min-vh-100 hero-img"
					alt="slide"
				/>
			</div>
		{/each}
	</div>
	<button
		class="carousel-control-prev"
		type="button"
		data-bs-target="#{heroSectionId}"
		data-bs-slide="prev"
	>
		<span class="carousel-control-prev-icon" aria-hidden="true"></span>
		<span class="visually-hidden">Previous</span>
	</button>
	<button
		class="carousel-control-next"
		type="button"
		data-bs-target="#{heroSectionId}"
		data-bs-slide="next"
	>
		<span class="carousel-control-next-icon" aria-hidden="true"></span>
		<span class="visually-hidden">Next</span>
	</button>
</section>

<style lang="scss">
	.hero-img {
		object-fit: cover;
		height: 600px;
		width: 100%;
	}
</style>
