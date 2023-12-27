<script>
	import Section from '$lib/component/share/section.svelte';
	import { APP_NAME } from '$lib/constant';
	import { icon } from '@fortawesome/fontawesome-svg-core';
	import {
		faFacebookF,
		faInstagram,
		faLinkedinIn,
		faTwitter
	} from '@fortawesome/free-brands-svg-icons';
	import { faBoxesPacking, faPhone, faSync, faTruckFast } from '@fortawesome/free-solid-svg-icons';
	import { onMount } from 'svelte';
	import { tns } from 'tiny-slider';

	const teamMembers = [
		{
			name: 'Lawson Arnold',
			image: 'person_1.jpg',
			title: 'CEO - Founder',
			intro:
				'Separated they live in. Separated they live in Bookmarksgrove right at the coast of the Semantics, a large language ocean.'
		},
		{
			name: 'Jeremy Walker',
			image: 'person_2.jpg',
			title: 'CEO - Founder',
			intro:
				'Separated they live in. Separated they live in Bookmarksgrove right at the coast of the Semantics, a large language ocean.'
		},
		{
			name: 'Tom Sunderland',
			image: 'person_3.jpg',
			title: 'CEO - Founder',
			intro:
				'Separated they live in. Separated they live in Bookmarksgrove right at the coast of the Semantics, a large language ocean.'
		},
		{
			name: 'Kathryn Ryan',
			image: 'person_4.jpg',
			title: 'CEO - Founder',
			intro:
				'Separated they live in. Separated they live in Bookmarksgrove right at the coast of the Semantics, a large language ocean.'
		}
	];

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

	const features = [
		{
			icon: faTruckFast,
			name: 'Fast &amp; Free Shipping',
			description:
				'Donec vitae odio quis nisl dapibus malesuada. Nullam ac aliquet velit. Aliquam vulputate velit imperdiet dolor tempor tristique.'
		},
		{
			icon: faBoxesPacking,
			name: 'Easy to Shop',
			description:
				'Donec vitae odio quis nisl dapibus malesuada. Nullam ac aliquet velit. Aliquam vulputate velit imperdiet dolor tempor tristique.'
		},
		{
			icon: faPhone,
			name: '24/7 Support',
			description:
				'Donec vitae odio quis nisl dapibus malesuada. Nullam ac aliquet velit. Aliquam vulputate velit imperdiet dolor tempor tristique.'
		},
		{
			icon: faSync,
			name: 'Free Returns',
			description:
				'Donec vitae odio quis nisl dapibus malesuada. Nullam ac aliquet velit. Aliquam vulputate velit imperdiet dolor tempor tristique.'
		}
	];

	onMount(() => {
		tns({
			items: 1,
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

<svelte:head>
	<title>{APP_NAME} - About Us</title>
</svelte:head>

<div class="why-section py-5">
	<Section>
		<div class="row justify-content-between align-items-center">
			<div class="col-lg-6">
				<h2 class="section-title">
					Why <span class="fw-bold blue">{APP_NAME}</span>
				</h2>
				<p>
					Donec vitae odio quis nisl dapibus malesuada. Nullam ac aliquet velit. Aliquam vulputate
					velit imperdiet dolor tempor tristique.
				</p>

				<div class="row my-5">
					{#each features as feature}
						<div class="col-6 col-md-6">
							<div class="feature">
								<div class="icon">
									{@html icon(feature.icon, { classes: ['fs-4'] }).html}
								</div>
								<h3 class="fw-semibold">{@html feature.name}</h3>
								<p>{feature.description}</p>
							</div>
						</div>
					{/each}
				</div>
			</div>

			<div class="col-lg-5">
				<div class="img-wrap">
					<img src="/images/about/why-section/why-us.jpg" alt="why-us" class="img-fluid" />
				</div>
			</div>
		</div>
	</Section>
</div>

<Section class="bg-light">
	<div class="mb-4">
		<h2 class="display-4 fw-light">
			Our Story
			<div class="border-bottom mb-4 mt-2 border-4 border-warning" style="width: 1.7em;"></div>
		</h2>
		<p class="fs-5 fw-medium">
			Mauris commodo sem vel justo ornare consectetur. Donec posuere tempus pulvinar. Morbi
			sollicitudin arcu quis tortor tristique sagittis. In hac habitasse platea dictumst. Fusce
			aliquet ac ligula venenatis consequat. Donec posuere consectetur quam vitae bibendum. Praesent
			efficitur sed quam at viverra.
		</p>
		<p class="fs-5 fw-medium">
			Vivamus lectus nisi, molestie non ante in, vehicula mattis ipsum. Nunc aliquet magna nisl, sed
			ultrices metus gravida vitae. Donec ut porttitor erat, ut ultrices tellus. Sed odio mauris,
			aliquam sed tempus sed, suscipit eu nibh. Cras sed dolor id ex posuere dignissim tincidunt in
			lectus. Donec suscipit cursus nunc, id euismod sem sagittis ut. Nulla auctor nec eros id
			sagittis. Cras quis rhoncus nunc. Sed mi nunc, vestibulum ac consequat eget, iaculis et elit.
		</p>
		<p class="fs-5 fw-medium">
			Etiam varius neque lectus, nec consequat neque rhoncus sit amet. Aliquam tristique orci non
			nibh dignissim, eu posuere lectus interdum. Pellentesque varius metus quis consectetur
			convallis. Curabitur ultrices laoreet sem, non volutpat turpis mollis vel. Praesent interdum
			dui a tristique maximus. Cras id finibus quam. Morbi nec enim erat. Fusce tincidunt dapibus
			pretium. Curabitur pulvinar sapien vel risus lobortis, eget mattis ex placerat. Nulla eget
			ipsum diam.
		</p>
	</div>
</Section>

<Section containerClass="overflow-x-hidden py-5">
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
</Section>

<Section class="bg-light">
	<div class="row mb-4">
		<h2 class="display-4 fw-light">
			Our Team
			<div class="border-bottom mb-4 mt-2 border-4 border-warning" style="width: 1.7em;"></div>
		</h2>
		<p class="fst-italic text-muted">Lorem ipsum dolor sit amet, consectetur adipisicing elit.</p>
	</div>

	<div class="row text-center">
		{#each teamMembers as member}
			<div class="col-xl-3 col-sm-6 mb-5">
				<div class="bg-body-tertiary rounded shadow-md py-5 px-4">
					<img
						src="/images/about/team/{member.image}"
						alt={member.name}
						width="100"
						class="rounded-circle mb-3 img-thumbnail shadow-sm"
					/>
					<h5 class="mb-0">{member.name}</h5>
					<span class="small text-uppercase text-muted">{member.title}</span>
					<p class="mt-3">
						{member.intro}
					</p>
					<ul class="social mb-0 list-inline mt-3">
						<li class="list-inline-item">
							<a href="https://www.facebook.com/" class="social-link">
								<i> {@html icon(faFacebookF).html} </i>
							</a>
						</li>
						<li class="list-inline-item">
							<a href="https://twitter.com/" class="social-link">
								<i> {@html icon(faTwitter).html} </i>
							</a>
						</li>
						<li class="list-inline-item">
							<a href="https://www.instagram.com/" class="social-link">
								<i>{@html icon(faInstagram).html}</i>
							</a>
						</li>
						<li class="list-inline-item">
							<a href="https://www.linkedin.com/" class="social-link">
								<i>{@html icon(faLinkedinIn).html}</i>
							</a>
						</li>
					</ul>
				</div>
			</div>
		{/each}
	</div>
</Section>

<style lang="scss">
	.blue {
		color: #0d6efd;
	}

	.section-title {
		color: #2f2f2f;
	}

	.why-section {
		& .img-wrap {
			position: relative;
			&::before {
				position: absolute;
				content: '';
				width: 255px;
				height: 217px;
				background-image: url('/images/about/why-section/dots-yellow.svg');
				background-repeat: no-repeat;
				background-size: contain;
				-webkit-transform: translate(-40%, -40%);
				-ms-transform: translate(-40%, -40%);
				transform: translate(-40%, -40%);
				z-index: -1;
			}
			& img {
				border-radius: 20px;
			}
		}
	}

	.feature {
		margin-bottom: 30px;

		& .icon {
			display: inline-block;
			position: relative;
			margin-bottom: 20px;

			&::before {
				content: '';
				width: 33px;
				height: 33px;
				position: absolute;
				right: -8px;
				bottom: 0;
			}
		}

		& h3 {
			font-size: 14px;
			color: #2f2f2f;
		}

		& p {
			font-size: 14px;
			line-height: 22px;
			color: #6a6a6a;
		}
	}

	.social-link {
		width: 30px;
		height: 30px;
		border: 1px solid #ddd;
		display: flex;
		align-items: center;
		justify-content: center;
		color: #666;
		border-radius: 50%;
		transition: all 0.3s;
		font-size: 0.9rem;

		&:focus,
		&:hover {
			background: #ddd;
			text-decoration: none;
			color: #555;
		}
	}

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

	/** background-color: #f5f5f5; */
</style>
