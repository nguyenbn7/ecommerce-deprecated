<script>
	import Pagination from '$lib/shares/pagination.svelte';
	import ProductItem from '$lib/shares/product-item.svelte';
	import PagingHeader from '$lib/shares/paging-header.svelte';
	import { onMount } from 'svelte';
	import { ECOMMERCE_NAME } from '$lib/constants';
	import { getPageProduct, getProductBrands, getProductTypes } from '$lib/request/product';

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

	let searchTerm = '';

	const defaultShopParams = {
		page_number: 1,
		page_size: 6,
		sort: 'name',
		search: undefined,
		brand_id: 0,
		type_id: 0
	};

	onMount(async () => {
		productBrands = [{ id: 0, name: 'All' }, ...(await getProductBrands())];
		productTypes = [{ id: 0, name: 'All' }, ...(await getProductTypes())];

		await getNewPageProduct(shopParams);
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
		const pageProduct = await getPageProduct(shopParams);
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
		if (searchTerm) {
			shopParams.search = searchTerm;
			shopParams.page_number = 1;
			await getNewPageProduct(shopParams);
		}
	}

	async function onReset() {
		if (searchTerm) {
			searchTerm = '';
			shopParams = Object.assign(shopParams, defaultShopParams);
			await getNewPageProduct(shopParams);
		}
	}
</script>

<svelte:head>
	<title>{ECOMMERCE_NAME} - Shop</title>
</svelte:head>

<div class="row">
	<div class="col-3">
		<div class="my-2">
			<h5 class="text-warning ms-3">Sort By</h5>
			<select class="form-select mb-4" on:change={onSortSelected}>
				{#each sortOptions as sort}
					<option value={sort.value}>{sort.name}</option>
				{/each}
			</select>
		</div>
		<div class="my-2">
			<h5 class="text-warning ms-3">Brands</h5>
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
		<div class="my-2">
			<h5 class="text-warning ms-3">Types</h5>
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
	</div>
	<div class="col-9">
		<div class="d-flex justify-content-between align-items-center pb-3">
			<PagingHeader pageNumber={shopParams.page_number} {totalItems} pageSize={shopParams.page_size}
			></PagingHeader>
			<div class="d-flex mt-2">
				<input
					type="text"
					placeholder="Search product name"
					class="form-control me-2"
					bind:value={searchTerm}
					on:keyup|preventDefault={onKeyUpSearch}
				/>
				<button type="button" class="btn btn-outline-primary mx-2" on:click={onSearch}>
					Search
				</button>
				<button type="button" class="btn btn-outline-danger" on:click={onReset}>Clear</button>
			</div>
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
