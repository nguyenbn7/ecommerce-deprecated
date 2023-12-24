<script>
	import Spinner, { SpinnerService } from '$lib/share/component/spinner.svelte';
	import { onMount } from 'svelte';
	import '@fortawesome/fontawesome-svg-core/styles.css';
	import BackToTopBtn from '$lib/layout/back-to-top-btn.svelte';
	import { AccountService } from '$lib/share/service/account';
	import Toastr from '$lib/share/component/toastr.svelte';
	import { BasketService } from '$lib/share/service/basket';

	const spinnerId = 'spinnerModal';

	SpinnerService.setSpinnerId(spinnerId);

	onMount(async () => {
		BasketService.loadBasketBackground();
		AccountService.loadUserBackground();
	});
</script>

<Toastr class="toast-container position-fixed top-0 end-0 p-4 mt-5 me-5" isSingleToast={true} />
<Spinner id={spinnerId} />

<slot />

<BackToTopBtn />

<style lang="scss">
	@import '~bootswatch/dist/flatly/bootstrap.min.css';
</style>
