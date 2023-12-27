<script>
	import 'animate.css/animate.min.css';
	import 'bootswatch/dist/flatly/bootstrap.min.css';
	import '@fortawesome/fontawesome-free/css/all.min.css';
	import '$lib/style/tinySlider.scss';
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
