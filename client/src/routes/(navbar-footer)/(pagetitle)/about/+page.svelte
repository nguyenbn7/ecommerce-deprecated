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
</script>

<svelte:head>
	<title>{APP_NAME} - About</title>
</svelte:head>

<Section class="bg-white">
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

<!-- <Techstack /> -->

<Section>
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
