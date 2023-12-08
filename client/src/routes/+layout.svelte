<script>
	import { AccountService } from '$lib/(account)/service';
	import { BasketService } from '$lib/(shop)/basket/service';
	import Spinner, { SpinnerService } from '$lib/share/component/spinner.svelte';
	import ToastContainer from '$lib/share/component/toast-container.svelte';
	import { onMount } from 'svelte';
	import { fade } from 'svelte/transition';
	import '@fortawesome/fontawesome-svg-core/styles.css';
	import { config, icon } from '@fortawesome/fontawesome-svg-core';
	import { faAnglesUp } from '@fortawesome/free-solid-svg-icons';
	import { ToastService } from '$lib/share/component/toast.svelte';
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
		window.scrollTo({
			left: 0,
			top: 0,
			behavior: 'smooth'
		});
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
		class="btn btn-info back-to-top"
		transition:fade={{ duration: 400 }}
		on:click={scrollToTop}
	>
		{@html icon(faAnglesUp).html}
	</a>
{/if}

<style lang="scss">
	@import '~bootswatch/dist/flatly/bootstrap.min.css';

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
