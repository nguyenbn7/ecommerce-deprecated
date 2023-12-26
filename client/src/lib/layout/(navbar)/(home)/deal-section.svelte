<script>
	import { BasketService } from '$lib/share/service/basket';
	import { ShopService } from '$lib/share/service/shop';
	import { icon } from '@fortawesome/fontawesome-svg-core';

	import { faBasketShopping } from '@fortawesome/free-solid-svg-icons';
	import { onMount } from 'svelte';

	/**
	 * @type {Product}
	 */
	let product;

	let now = new Date().getTime();
	let end = now + 1000 * 60 * 60 * 24 * 3;

	$: distance = end - now;
	$: days = Math.floor(distance / (1000 * 60 * 60 * 24));
	$: hours = Math.floor((distance % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60));
	$: minutes = Math.floor((distance % (1000 * 60 * 60)) / (1000 * 60));
	$: seconds = Math.floor((distance % (1000 * 60)) / 1000);

	setInterval(function () {
		now = Date.now();
	}, 1000);

	onMount(async () => (product = await ShopService.getDealProduct()));
</script>

{#if product}
	<section class="cart-banner py-5">
		<div class="container">
			<div class="row clearfix">
				<!--Image Column-->
				<div class="image-column col-lg-6">
					<div class="image">
						<div class="price-box">
							<div class="inner-price">
								<span class="price">
									<strong>30%</strong> <br /> off
								</span>
							</div>
						</div>
						<img
							class="img-thumbnail bg-transparent border-0"
							src={product.pictureUrl}
							alt={product.name}
						/>
					</div>
				</div>
				<!--Content Column-->
				<div class="content-column col-lg-6">
					<h3><span class="text-warning">Deal</span> of the month</h3>
					<h4>{product.name}</h4>
					<div class="text">
						{product.description}
					</div>
					<!--Countdown Timer-->
					<div class="time-counter">
						<div class="time-countdown clearfix" data-countdown="2020/2/01">
							<div class="counter-column">
								<div class="inner"><span class="count">{days}</span>Days</div>
							</div>
							<div class="counter-column">
								<div class="inner"><span class="count">{hours}</span>Hours</div>
							</div>
							<div class="counter-column">
								<div class="inner"><span class="count">{minutes}</span>Mins</div>
							</div>
							<div class="counter-column">
								<div class="inner"><span class="count">{seconds}</span>Secs</div>
							</div>
						</div>
					</div>
					<a
						href={'#'}
						class="btn btn-danger rounded-5 px-3 py-2 mt-3"
						on:click={() => BasketService.addItemToBasket(product)}
					>
						{@html icon(faBasketShopping, { classes: 'me-1' }).html} Add to Basket
					</a>
				</div>
			</div>
		</div>
	</section>
{/if}

<style lang="scss">
	.cart-banner {
		background-color: #f5f5f5;
	}

	.cart-banner .image-column {
		position: relative;
		margin-top: 40px;
	}

	.cart-banner .image-column .price-box {
		position: absolute;
		left: 15%;
		top: -30px;
		width: 110px;
		height: 110px;
		border-radius: 50%;
		border: 1px solid #fff;
		background-color: rgba(242, 129, 35, 0.75);
	}

	.cart-banner .image-column .price-box .inner-price {
		position: relative;
		width: 94px;
		height: 94px;
		margin: 0 auto;
		margin-top: 8px;
		text-align: center;
		border-radius: 50%;
		background-color: #f28123;
	}

	.cart-banner .image-column .price-box .inner-price .price {
		color: #051922;
		padding-top: 27px;
		position: relative;
		display: inline-block;
		line-height: 18px;
		font-weight: 400;
	}

	.cart-banner .image-column .price-box .inner-price .price strong {
		color: #051922;
		font-size: 24px;
	}

	.cart-banner .content-column {
		position: relative;
		padding-top: 40px;
	}

	.cart-banner .content-column h3 {
		font-size: 40px;
	}

	.cart-banner .content-column h4 {
		position: relative;
		font-weight: 300;
		text-transform: uppercase;
	}

	.cart-banner .content-column .text {
		position: relative;
		font-weight: 400;
		line-height: 1.8em;
		margin-top: 25px;
		margin-bottom: 25px;
	}

	.time-counter {
		position: relative;
		margin-bottom: 25px;
	}

	.time-counter .time-countdown {
		position: relative;
	}

	.time-countdown .counter-column {
		position: relative;
		display: inline-block;
		margin: 0px 0px 5px;
		font-size: 13px;
		line-height: 1em;
		padding: 8px 20px 14px;
		text-transform: capitalize;
		text-align: center;
		border: 2px solid #f28123;
	}

	.time-countdown .counter-column .count {
		position: relative;
		display: block;
		font-size: 30px;
		line-height: 1.4em;
		padding: 0px 0px;
		color: #f28123;
		font-weight: 700;
		letter-spacing: 1px;
	}
</style>
