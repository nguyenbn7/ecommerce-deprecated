<script>
	import { icon } from "@fortawesome/fontawesome-svg-core";


	import { faBasketShopping } from "@fortawesome/free-solid-svg-icons";

</script>
<section class="cart-banner py-5 my-5">
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
					<img src="/images/home/deal/a.jpg" alt="" />
				</div>
			</div>
			<!--Content Column-->
			<div class="content-column col-lg-6">
				<h3><span class="text-warning">Deal</span> of the month</h3>
				<h4>Hikan Strwaberry</h4>
				<div class="text">
					Quisquam minus maiores repudiandae nobis, minima saepe id, fugit ullam similique! Beatae,
					minima quisquam molestias facere ea. Perspiciatis unde omnis iste natus error sit
					voluptatem accusant
				</div>
				<!--Countdown Timer-->
				<div class="time-counter">
					<div class="time-countdown clearfix" data-countdown="2020/2/01">
						<div class="counter-column">
							<div class="inner"><span class="count">00</span>Days</div>
						</div>
						<div class="counter-column">
							<div class="inner"><span class="count">00</span>Hours</div>
						</div>
						<div class="counter-column">
							<div class="inner"><span class="count">00</span>Mins</div>
						</div>
						<div class="counter-column">
							<div class="inner"><span class="count">00</span>Secs</div>
						</div>
					</div>
				</div>
				<a href="cart.html" class="btn btn-warning rounded-5 px-3 py-2 mt-3">
					{@html icon(faBasketShopping, { classes: 'me-1' }).html} Add to Basket
				</a>
			</div>
		</div>
	</div>
</section>

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
