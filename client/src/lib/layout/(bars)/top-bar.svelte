<script>
	import { icon } from '@fortawesome/fontawesome-svg-core';
	import {
		faFacebookF,
		faInstagram,
		faLinkedinIn,
		faTwitter,
		faYoutube
	} from '@fortawesome/free-brands-svg-icons';
</script>

<div class="nav bg-secondary py-2 px-5">
	<div class="col-lg-6 d-none d-lg-block">
		<div class="d-inline-flex align-items-center">
			<a class="text-white" href={'#'}>FAQs</a>
			<span class="text-muted px-2">|</span>
			<a class="text-white" href={'#'}>Help</a>
			<span class="text-muted px-2">|</span>
			<a class="text-white" href={'#'}>Support</a>
		</div>
	</div>
	<div class="col-lg-6 text-center text-lg-end">
		<div class="d-inline-flex align-items-center">
			<a class="text-white px-2" href="https://www.facebook.com/">
				<i>{@html icon(faFacebookF).html}</i>
			</a>
			<a class="text-white px-2" href="https://twitter.com/">
				<i>{@html icon(faTwitter).html}</i>
			</a>
			<a class="text-white px-2" href="https://www.linkedin.com/">
				<i>{@html icon(faLinkedinIn).html}</i>
			</a>
			<a class="text-white px-2" href="https://www.instagram.com/">
				<i>{@html icon(faInstagram).html}</i>
			</a>
			<a class="text-white ps-2" href="https://www.youtube.com/">
				<i>{@html icon(faYoutube).html}</i>
			</a>
		</div>
	</div>
</div>
