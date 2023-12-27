<script>
	import { onMount } from 'svelte';
	import { tns } from 'tiny-slider';
	import './style.scss';

	const techStackImages = [
		{
			image: 'sveltekit.png',
			link: 'https://kit.svelte.dev/'
		},
		{
			image: 'fastapi.png',
			link: 'https://fastapi.tiangolo.com/'
		},
		{
			image: 'postgresql.png',
			link: 'https://www.postgresql.org/'
		},
		{
			image: 'docker.png',
			link: 'https://www.docker.com/'
		},
		{
			image: 'bootstrap.png',
			link: 'https://getbootstrap.com/'
		}
	];

	onMount(() => {
		tns({
			items: 1,
			slideBy: 'page',
			autoplay: true,
			speed: 400,
			autoplayButtonOutput: false,
			controls: false,
			responsive: {
				768: {
					items: 3
				},
				576: {
					items: 2
				},
				992: {
					items: 4
				}
			}
		});
	});
</script>

<div class="bg-light py-5">
	<div class="container py-5 overflow-x-hidden">
		<div class="mb-4">
			<h2 class="display-4 fw-light text-end">
				Our Tech Stacks
				<div
					class="border-bottom mb-5 mt-2 border-4 border-warning ms-auto"
					style="width: 1.7em;"
				></div>
			</h2>
			<div class="row align-items-center justify-content-center slider">
				{#each techStackImages as techStack}
					<div class="col-xl-3 col-sm-6 text-center position-relative cursor-pointer techstack">
						<div
							class="shadow-md techstack-img rounded"
							style="background-image: url(/images/about/techstack/{techStack.image});"
						></div>
						<a
							href={techStack.link}
							class="btn btn-danger rounded-pill position-absolute techstack-btn"
							style="top: 37%; left: 37%"
						>
							Learn More
						</a>
					</div>
				{/each}
			</div>
		</div>
	</div>
</div>

<style lang="scss">
	.cursor-pointer {
		cursor: pointer;
	}

	.techstack-img {
		width: 100%;
		height: 9em;
		background-size: 100% 100%;
	}

	.techstack:hover .techstack-btn {
		opacity: 1;
		animation: fly 0.1s linear;
	}

	@keyframes fly {
		0% {
			transform: translateY(50%);
		}
		100% {
			transform: translateY(0%);
		}
	}

	.techstack:hover .techstack-img {
		filter: blur(1.7px);
	}

	.techstack-btn {
		opacity: 0;
	}
</style>
