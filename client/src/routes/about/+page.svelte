<script>
	import Intro from '$lib/about/intro.svelte';
	import Breadcrumb from '$lib/share/component/breadcrumb.svelte';
	import { ECOMMERCE_NAME } from '$lib/share/constant';
	import BrandBar from '$lib/share/layout/brand-bar.svelte';
	import NavBar from '$lib/share/layout/nav-bar.svelte';
	import TopBar from '$lib/share/layout/top-bar.svelte';
	import { icon } from '@fortawesome/fontawesome-svg-core';
	import {
		faFacebookF,
		faInstagram,
		faLinkedinIn,
		faTwitter
	} from '@fortawesome/free-brands-svg-icons';
	import {
		faCloud,
		faDatabase,
		faMagicWandSparkles,
		faServer
	} from '@fortawesome/free-solid-svg-icons';
</script>

<svelte:head>
	<title>{ECOMMERCE_NAME} - About</title>
</svelte:head>

<TopBar />
<BrandBar />
<NavBar />

<div class="container-fluid bg-secondary-subtle mb-5">
	<div
		class="d-flex flex-column align-items-center justify-content-center"
		style="min-height: 300px"
	>
		<h1 class="fw-semibold text-uppercase mb-3">About Us</h1>
		<div class="d-inline-flex">
			<Breadcrumb class="breadcrumb ps-1 pb-3" />
		</div>
	</div>
</div>

<Intro />

<section class="bg-white py-5">
	<div class="container py-5">
		<div class="row align-items-center mb-5">
			<div class="col-lg-6 order-2 order-lg-1">
				<i class="mb-3 text-info fs-3">
					{@html icon(faMagicWandSparkles).html}
				</i>
				<h2 class="font-weight-light">Svelte kit</h2>
				<p class="font-italic text-muted mb-4">
					No more wasted days figuring out bundler configuration, routing, SSR, CSP, TypeScript,
					deployment settings and all the other boring stuff. Code with joy.
				</p>
				<a href="https://kit.svelte.dev/" class="btn btn-info px-5 rounded-pill shadow-sm">
					Learn More
				</a>
			</div>
			<div class="col-lg-5 px-5 mx-auto order-1 order-lg-2">
				<img src="/images/sveltekit.png" alt="sveltekit" class="img-fluid mb-4 mb-lg-0" />
			</div>
		</div>
	</div>
</section>

<section class="bg-secondary-subtle py-5">
	<div class="container py-5">
		<div class="row align-items-center mb-5">
			<div class="col-lg-5 px-5 mx-auto">
				<img src="/images/fastapi.png" alt="fastapi" class="img-fluid mb-4 mb-lg-0" />
			</div>
			<div class="col-lg-6">
				<i class="fs-3 mb-3 text-info">
					{@html icon(faServer).html}
				</i>
				<h2 class="font-weight-light">FastAPI</h2>
				<p class="font-italic text-muted mb-4">
					<strong>FastAPI</strong> is a modern, fast (high-performance), web framework for building APIs
					with Python 3.8+ based on standard Python type hints.
				</p>
				<a href="https://fastapi.tiangolo.com/" class="btn btn-info px-5 rounded-pill shadow-sm">
					Learn More
				</a>
			</div>
		</div>
	</div>
</section>

<section class="bg-white py-5">
	<div class="container py-5">
		<div class="row align-items-center mb-5">
			<div class="col-lg-6 order-2 order-lg-1">
				<i class="fs-3 mb-3 text-info">
					{@html icon(faDatabase).html}
				</i>
				<h2 class="font-weight-light">PostgreSQL</h2>
				<p class="font-italic text-muted mb-4">
					The World's Most Advanced Open Source Relational Database
				</p>
				<a href="https://www.postgresql.org/" class="btn btn-info px-5 rounded-pill shadow-sm">
					Learn More
				</a>
			</div>
			<div class="col-lg-5 px-5 mx-auto order-1 order-lg-2">
				<img src="/images/postgresql.png" alt="postgresql" class="img-fluid mb-4 mb-lg-0" />
			</div>
		</div>
	</div>
</section>

<section class="bg-secondary-subtle py-5">
	<div class="container py-5">
		<div class="row align-items-center mb-5">
			<div class="col-lg-5 px-5 mx-auto">
				<img src="/images/docker.png" alt="docker" class="img-fluid mb-4 mb-lg-0" />
			</div>
			<div class="col-lg-6">
				<i class="fs-3 mb-3 text-info">
					{@html icon(faCloud).html}
				</i>
				<h2 class="font-weight-light">Docker</h2>
				<p class="font-italic text-muted mb-4">
					<strong>Docker</strong> is a platform designed to help developers build, share, and run container
					applications.
				</p>
				<a href="https://www.docker.com/" class="btn btn-info px-5 rounded-pill shadow-sm">
					Learn More
				</a>
			</div>
		</div>
	</div>
</section>

<div class="bg-white py-5">
	<div class="container py-5">
		<div class="row mb-4">
			<div class="col-lg-5">
				<h2 class="display-4 font-weight-light">Our team</h2>
				<p class="font-italic text-muted">
					Lorem ipsum dolor sit amet, consectetur adipisicing elit.
				</p>
			</div>
		</div>

		<div class="row text-center">
			<!-- Team item-->
			<div class="col-xl-3 col-sm-6 mb-5">
				<div class="bg-body-tertiary rounded shadow-md py-5 px-4">
					<img
						src="/images/person_1.jpg"
						alt="Lawson Arnold"
						width="100"
						class="img-fluid rounded-circle mb-3 img-thumbnail shadow-sm"
					/>
					<h5 class="mb-0">Lawson Arnold</h5>
					<span class="small text-uppercase text-muted">CEO - Founder</span>
					<p class="mt-3">
						Separated they live in. Separated they live in Bookmarksgrove right at the coast of the
						Semantics, a large language ocean.
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
			<!-- End-->

			<!-- Team item-->
			<div class="col-xl-3 col-sm-6 mb-5">
				<div class="bg-body-tertiary rounded shadow-sm py-5 px-4">
					<img
						src="/images/person_2.jpg"
						alt="Jeremy Walker"
						width="100"
						class="img-fluid rounded-circle mb-3 img-thumbnail shadow-sm"
					/>
					<h5 class="mb-0">Jeremy Walker</h5>
					<span class="small text-uppercase text-muted">CEO - Founder</span>
					<p class="mt-3">
						Separated they live in. Separated they live in Bookmarksgrove right at the coast of the
						Semantics, a large language ocean.
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
			<!-- End-->

			<!-- Team item-->
			<div class="col-xl-3 col-sm-6 mb-5">
				<div class="bg-body-tertiary rounded shadow-sm py-5 px-4">
					<img
						src="/images/person_3.jpg"
						alt="Tom Sunderland"
						width="100"
						class="img-fluid rounded-circle mb-3 img-thumbnail shadow-sm"
					/>
					<h5 class="mb-0">Tom Sunderland</h5>
					<span class="small text-uppercase text-muted">CEO - Founder</span>
					<p class="mt-3">
						Separated they live in. Separated they live in Bookmarksgrove right at the coast of the
						Semantics, a large language ocean.
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
			<!-- End-->

			<!-- Team item-->
			<div class="col-xl-3 col-sm-6 mb-5">
				<div class="bg-body-tertiary rounded shadow-sm py-5 px-4">
					<img
						src="/images/person_4.jpg"
						alt="Kathryn Ryan"
						width="100"
						class="img-fluid rounded-circle mb-3 img-thumbnail shadow-sm"
					/>
					<h5 class="mb-0">Kathryn Ryan</h5>
					<span class="small text-uppercase text-muted">CEO - Founder</span>
					<p class="mt-3">
						Separated they live in. Separated they live in Bookmarksgrove right at the coast of the
						Semantics, a large language ocean.
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
			<!-- End-->
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
