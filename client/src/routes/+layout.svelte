<script>
	import { AccountService } from '$lib/(account)/service';
	import { BasketService } from '$lib/basket/service';
	import Spinner, { SpinnerService } from '$lib/components/share/spinner.svelte';
	import ToastContainer from '$lib/components/share/toast-container.svelte';
	import { ToastService } from '$lib/components/share/toast.svelte';
	import { onMount } from 'svelte';

	const toastContainerId = 'toast-container';
	const spinnerId = 'spinnerModal';

	ToastService.setToastContainerId(toastContainerId);
	SpinnerService.setSpinnerId(spinnerId);

	onMount(async () => {
		BasketService.loadBasketBackground();
		AccountService.loadUserBackground();
	});
</script>

<ToastContainer
	class="toast-container position-fixed top-0 end-0 p-4 mt-5 me-5"
	id={toastContainerId}
/>
<Spinner id={spinnerId} />

<slot />

<style lang="scss">
	@import '~bootstrap/scss/bootstrap.scss';
	@import '~bootstrap-icons/font/bootstrap-icons.scss';
</style>
