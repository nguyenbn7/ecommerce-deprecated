<script>
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

<div class="bg-white py-5">
	<div class="container py-5">
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
	</div>
</div>

<style lang="scss">
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
	}

	.social-link:hover,
	.social-link:focus {
		background: #ddd;
		text-decoration: none;
		color: #555;
	}
</style>
