<script>
	import { onMount } from 'svelte';
	import { tns } from 'tiny-slider';

	const clients = [
		{
			name: 'Saira Hakim',
			profileImage: 'avatar1.png',
			companyName: 'Local shop owner',
			quote:
				'Sed ut perspiciatis unde omnis iste natus error veritatis et quasi architecto beatae vitae dict eaque ipsa quae ab illo inventore Sed ut perspiciatis unde omnis iste natus error sit voluptatem accusantium'
		},
		{
			name: 'David Niph',
			profileImage: 'avatar2.png',
			companyName: 'Local shop owner',
			quote:
				'Sed ut perspiciatis unde omnis iste natus error veritatis et quasi architecto beatae vitae dict eaque ipsa quae ab illo inventore Sed ut perspiciatis unde omnis iste natus error sit voluptatem accusantium'
		},
		{
			name: 'Jacob Sikim',
			profileImage: 'avatar3.png',
			companyName: 'Local shop owner',
			quote:
				'Sed ut perspiciatis unde omnis iste natus error veritatis et quasi architecto beatae vitae dict eaque ipsa quae ab illo inventore Sed ut perspiciatis unde omnis iste natus error sit voluptatem accusantium'
		}
	];

	onMount(() => {
		tns({
			container: '.testimonial-slider',
			items: 1,
			autoplay: true,
			speed: 1500,
			autoplayButtonOutput: false,
			controls: false
		});
	});
</script>

<div class="py-5" style="background-color: #f5f5f5;">
	<div class="container overflow-x-hidden">
		<h4 class="display-5 fw-light text-center my-5">
			Testimonial
			<div
				class="border-bottom mb-5 mt-2 border-4 border-warning mx-auto"
				style="width: 1.7em;"
			></div>
		</h4>
		<div class="row align-items-center justify-content-center testimonial-slider mt-5">
			{#each clients as client}
				<div class="col-xl-3 col-sm-6 text-center">
					<div class="client-avatar">
						<img src="/images/home/testimonial/{client.profileImage}" alt={client.name} />
					</div>
					<div class="client-meta">
						<h3>{client.name} <span>{client.companyName}</span></h3>
						<p class="testimonial-body">
							"{client.quote}"
						</p>
						<span class="quote-icon">
							<i class="fa-solid fa-quote-right"></i>
						</span>
					</div>
				</div>
			{/each}
		</div>
	</div>
</div>

<style lang="scss">
	.client-avatar {
		margin-bottom: 20px;
	}

	.client-meta h3 {
		font-size: 20px;
		font-weight: 600;
	}

	.client-meta h3 span {
		display: block;
		font-size: 70%;
		margin-top: 10px;
		color: #051922;
		font-weight: 600;
		opacity: 0.5;
	}

	p.testimonial-body {
		font-size: 17px;
		font-style: italic;
		width: 700px;
		margin: 0 auto;
		line-height: 1.8;
		color: #999999;
		margin-top: 20px;
	}

	.quote-icon {
		margin-top: 20px;
		font-size: 25px;
		opacity: 0.3;
	}

	.client-avatar img {
		max-width: 100px;
		border-radius: 50%;
		margin: 0 auto;
	}
</style>
