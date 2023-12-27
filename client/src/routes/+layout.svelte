<script>
	import '@fortawesome/fontawesome-svg-core/styles.css';
	import 'animate.css';
	import '~bootswatch/dist/flatly/bootstrap.min.css';
	import Spinner, { SpinnerService } from '$lib/share/component/spinner.svelte';
	import BackToTopBtn from '$lib/component/(root)/back-to-top-btn.svelte';
	import Toastr from '$lib/component/share/toastr.svelte';

	const spinnerId = 'spinnerModal';

	SpinnerService.setSpinnerId(spinnerId);
</script>

<Toastr class="toast-container position-fixed top-0 end-0 p-4 mt-5 me-5" isSingleToast={true} />
<Spinner id={spinnerId} />
<BackToTopBtn />

<slot />

