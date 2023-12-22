<script>
	import Pagination from '$lib/share/component/pagination.svelte';
	import ProductItem from '$lib/(shop)/shop/product-item.svelte';
	import PagingHeader from '$lib/(shop)/shop/paging-header.svelte';
	import { onMount } from 'svelte';
	import { ECOMMERCE_NAME } from '$lib/share/constant';
	import ShopService from '$lib/(shop)/shop/service';
	import { icon } from '@fortawesome/fontawesome-svg-core';
	import { faSearch } from '@fortawesome/free-solid-svg-icons';

	/**
	 * @type {Product[]}
	 */
	let products = [];
	/**
	 * @type {ProductBrand[]}
	 */
	let productBrands = [];
	/**
	 * @type {ProductType[]}
	 */
	let productTypes = [];

	/**
	 * @type {number}
	 */
	let totalItems;
	/**
	 * @type {ShopParams}
	 */
	let shopParams = {
		page_number: 1,
		page_size: 6,
		sort: 'name',
		search: undefined,
		brand_id: 0,
		type_id: 0
	};
	const maxSize = 5;

	const sortOptions = [
		{ name: 'Alphabetical', value: 'name' },
		{ name: 'Price: Low to High', value: 'price' },
		{ name: 'Price: High to Low', value: '-price' }
	];

	/**
	 * @type {string | undefined}
	 */
	let searchTerm;

	const defaultShopParams = {
		page_number: 1,
		page_size: 6,
		sort: 'name',
		search: undefined,
		brand_id: 0,
		type_id: 0
	};

	onMount(async () => {
		const result = await ShopService.loadShopData(shopParams);
		products = result.products;
		productBrands = result.productBrands;
		productTypes = result.productTypes;
		shopParams.page_number = result.page_number;
		shopParams.page_size = result.page_size;
		totalItems = result.totalItems;
	});

	/**
	 * @param {number} brandId
	 */
	async function onBrandIdSelected(brandId) {
		shopParams.brand_id = brandId;
		shopParams.page_number = 1;
		shopParams.page_size = shopParams.page_size < 6 ? 6 : shopParams.page_size;
		await getNewPageProduct(shopParams);
	}

	/**
	 * @param {ShopParams} shopParams
	 */
	async function getNewPageProduct(shopParams) {
		const pageProduct = await ShopService.getPageProduct(shopParams);
		products = [...pageProduct.data];
		shopParams.page_number = pageProduct.page_number;
		shopParams.page_size = pageProduct.page_size;
		totalItems = pageProduct.total_items;
	}

	/**
	 * @param {number} typeId
	 */
	async function onTypeIdSelected(typeId) {
		shopParams.type_id = typeId;
		shopParams.page_number = 1;
		shopParams.page_size = shopParams.page_size < 6 ? 6 : shopParams.page_size;
		await getNewPageProduct(shopParams);
	}

	/**
	 * @param {CustomEvent<any>} $event
	 */
	async function pageChanged($event) {
		shopParams.page_number = $event.detail.pageNumber;
		await getNewPageProduct(shopParams);
	}

	/**
	 * @param {Event} $event
	 */
	async function onSortSelected($event) {
		// @ts-ignore
		shopParams.sort = $event?.target?.value ?? 'name';
		await getNewPageProduct(shopParams);
	}

	/**
	 * @param {KeyboardEvent & { currentTarget: EventTarget & HTMLInputElement; }} $event
	 */
	async function onKeyUpSearch($event) {
		if ($event.code === 'Enter') {
			await onSearch();
		}
	}

	async function onSearch() {
		// TODO: handle more case
		if (searchTerm === shopParams.search) return;
		if (!searchTerm) {
			searchTerm = undefined;
			shopParams = Object.assign(shopParams, defaultShopParams);
			return await getNewPageProduct(shopParams);
		}
		shopParams.search = searchTerm;
		shopParams.page_number = 1;
		return await getNewPageProduct(shopParams);
	}
</script>

<svelte:head>
	<title>{ECOMMERCE_NAME} - Shop</title>
</svelte:head>

{#if productBrands.length}
	<div class="row">
		<aside class="col-12 col-md-3">
			<div class="d-flex mt-2 mb-3">
				<div class="input-group mb-3">
					<input
						type="text"
						class="form-control"
						placeholder="Search by product name"
						aria-describedby="button-addon2"
						bind:value={searchTerm}
						on:keyup={onKeyUpSearch}
					/>
					<button class="btn btn-outline-secondary" type="button" on:click={onSearch}>
						<i>{@html icon(faSearch).html}</i>
					</button>
				</div>
			</div>
			<div class="mt-2 mb-4">
				<h5 class="text-warning mb-3">Sort By</h5>
				<select class="form-select" on:change={onSortSelected}>
					{#each sortOptions as sort}
						<option value={sort.value}>{sort.name}</option>
					{/each}
				</select>
			</div>
			<div class="mt-2 mb-4">
				<h5 class="text-warning mb-3">Brands</h5>
				<ul class="list-group">
					{#each productBrands as brand}
						<a
							href={'#'}
							class="list-group-item"
							on:click={() => onBrandIdSelected(brand.id)}
							class:active={brand.id === shopParams.brand_id}
						>
							{brand.name}
						</a>
					{/each}
				</ul>
			</div>
			<div class="mt-2 mb-4">
				<h5 class="text-warning mb-3">Types</h5>
				<ul class="list-group">
					{#each productTypes as type}
						<a
							href={'#'}
							class="list-group-item"
							on:click={() => onTypeIdSelected(type.id)}
							class:active={type.id === shopParams.type_id}
						>
							{type.name}
						</a>
					{/each}
				</ul>
			</div>
		</aside>
		<div class="col-12 col-md-9">
			<div class="d-flex justify-content-between pt-3 pb-4p pt-md-0">
				<PagingHeader
					pageNumber={shopParams.page_number}
					{totalItems}
					pageSize={shopParams.page_size}
				></PagingHeader>
				<!-- TODO: select page size -->
			</div>

			<div class="row row-cols-1 row-cols-md-2 row-cols-xl-3 row-cols-xxl-3 g-3 mb-4">
				{#each products as product}
					<div class="col">
						<ProductItem {product}></ProductItem>
					</div>
				{/each}
			</div>

			<div class="d-flex justify-content-center mb-3">
				<Pagination
					{totalItems}
					itemsPerPage={shopParams.page_size}
					pageNumber={shopParams.page_number}
					{maxSize}
					previousText="&lsaquo;"
					nextText="&rsaquo;"
					firstText="&laquo;"
					lastText="&raquo;"
					on:pageChanged={pageChanged}
				></Pagination>
			</div>
		</div>
	</div>
{/if}

<style lang="scss">
	/* .sidebar-sticky {
		position: -webkit-sticky;
		position: sticky;
		top: 5rem;
		display: block !important;
		height: calc(100vh - 6rem);
		padding-left: 0.25rem;
		margin-left: -0.25rem;
		overflow-y: auto;
	} */
</style>
