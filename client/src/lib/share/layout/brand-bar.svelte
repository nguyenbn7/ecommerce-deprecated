<script>
	import { icon } from '@fortawesome/fontawesome-svg-core';
	import { faBasketShopping, faHeart, faSearch } from '@fortawesome/free-solid-svg-icons';
	import { basket } from '$lib/(shop)/basket/service';

	/**
	 * @param {BasketItem[]} items
	 */
	function getCount(items) {
		return items.reduce((total, item) => total + item.quantity, 0);
	}
</script>

<div class="nav nav-expand-md align-items-center py-4 px-5">
	<!-- TODO: make hamburger -->
	<div class="col-lg-3 d-none d-lg-block">
		<a href="/" class="text-decoration-none">
			<img src="/images/logo.png" alt="logo" style="max-height: 45px;" class="logo" />
		</a>
	</div>
	<div class="col-lg-6 col-6 text-start">
		<!-- TODO: detect key and search -->
		<form action="">
			<div class="input-group">
				<input type="text" class="form-control" placeholder="Search for products" />
				<button class="btn btn-outline-secondary">
					<i>{@html icon(faSearch).html}</i>
				</button>
			</div>
		</form>
	</div>
	<div class="col-lg-3 col-6 text-end">
		<a class="btn border text-secondary me-2" href="/favorites" title="Wish list">
			{@html icon(faHeart).html}
		</a>
		<a
			class="btn border position-relative"
			class:text-secondary={!$basket || !$basket.items.length}
			class:text-info={$basket && $basket.items.length}
			href="/basket"
			title="Basket"
		>
			{@html icon(faBasketShopping).html}
			{#if $basket && $basket.items.length}
				<span
					class="position-absolute translate-middle p-2 bg-transparent badge rounded-pill text-danger fs-5 cart-no"
				>
					{getCount($basket.items)}
				</span>
			{/if}
		</a>
	</div>
</div>

<style lang="scss">
	.cart-no {
		top: 20%;
		left: 100%;
	}

	.logo {
		cursor: pointer;
	}
</style>
