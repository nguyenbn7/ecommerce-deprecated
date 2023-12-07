<script>
	import { AccountService } from '$lib/(account)/service';
	import { BasketService } from '$lib/basket/service';
	import Spinner, { SpinnerService } from '$lib/components/share/spinner.svelte';
	import ToastContainer from '$lib/components/share/toast-container.svelte';
	import { ToastService } from '$lib/components/share/toast.svelte';
	import { onMount } from 'svelte';
	import { fade } from 'svelte/transition';
	import '@fortawesome/fontawesome-svg-core/styles.css';
	import { config, icon } from '@fortawesome/fontawesome-svg-core';
	import { faAnglesUp } from '@fortawesome/free-solid-svg-icons';
	config.autoAddCss = false;

	const toastContainerId = 'toast-container';
	const spinnerId = 'spinnerModal';

	ToastService.setToastContainerId(toastContainerId);
	SpinnerService.setSpinnerId(spinnerId);

	onMount(async () => {
		BasketService.loadBasketBackground();
		AccountService.loadUserBackground();
	});

	let y = 0;

	function scrollToTop() {
		const c = document.documentElement.scrollTop || document.body.scrollTop;
		if (c > 0) {
			window.requestAnimationFrame(scrollToTop);
			window.scrollTo(0, c - c / 10);
		}
	}
</script>

<svelte:window bind:scrollY={y} />

<ToastContainer
	class="toast-container position-fixed top-0 end-0 p-4 mt-5 me-5"
	id={toastContainerId}
/>
<Spinner id={spinnerId} />

<slot />

{#if y > 100}
	<a
		href={'#'}
		class="btn btn-primary back-to-top"
		transition:fade={{ duration: 400 }}
		on:click={scrollToTop}
	>
		{@html icon(faAnglesUp).html}
	</a>
{/if}

<style lang="scss">
	@import '~bootstrap/scss/bootstrap.scss';

	.back-to-top {
		position: fixed;
		right: 30px;
		bottom: 30px;
		z-index: 11;
		animation: action 1s infinite alternate;
	}

	@keyframes action {
		0% {
			transform: translateY(0);
		}
		100% {
			transform: translateY(-15px);
		}
	}
</style>
