<script>
	import Spinner, { SpinnerService } from '$lib/components/share/spinner.svelte';
	import ToastContainer from '$lib/components/share/toast-container.svelte';
	import { ToastService } from '$lib/components/share/toast.svelte';

	const toastContainerId = 'toast-container';
	const spinnerId = 'spinnerModal';

	ToastService.setToastContainerId(toastContainerId);
	SpinnerService.setSpinnerId(spinnerId);
</script>

<ToastContainer
	class="toast-container position-fixed top-0 end-0 p-4 mt-5 me-5"
	id={toastContainerId}
></ToastContainer>
<Spinner id={spinnerId}></Spinner>
<slot />

<style lang="scss">
	@import '~bootstrap/scss/bootstrap.scss';
	@import '~bootstrap-icons/font/bootstrap-icons.scss';
</style>
