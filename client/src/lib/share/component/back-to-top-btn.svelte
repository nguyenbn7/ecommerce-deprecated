<script>
	import { config, icon } from '@fortawesome/fontawesome-svg-core';
	import { faAnglesUp } from '@fortawesome/free-solid-svg-icons';
	import { fade } from 'svelte/transition';
	import jq from 'jquery';
	import { onMount } from 'svelte';

	config.autoAddCss = false;

	/**
	 * @type {number}
	 */
	let y;

	onMount(async () => {
		(await import('jquery.easing')).default;
		// @ts-ignore
		window.jq = jq;
	});

	function scrollToTop() {
		jq('html, body').animate({ scrollTop: 0 }, 1500, 'easeInOutExpo');
		return false;
	}
</script>

<svelte:window bind:scrollY={y} />

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
