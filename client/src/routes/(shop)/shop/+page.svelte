<script>
	import Pagination from '$lib/shares/pagination.svelte';
	import ProductItem from '$lib/shares/product-item.svelte';
</script>

<div class="container">
	<div class="row">
		<div class="col-3">
			<div class="my-2">
				<h5 class="text-warning ms-3">Sort By</h5>
				<select class="form-select mb-4">
					<option>Alphabetical</option>
				</select>
			</div>
			<div class="my-2">
				<h5 class="text-warning ms-3">Brands</h5>
				<ul class="list-group">
					<li class="list-group-item">Chym Co</li>
				</ul>
			</div>
			<div class="my-2">
				<h5 class="text-warning ms-3">Types</h5>
				<ul class="list-group">
					<li class="list-group-item">Vipe</li>
				</ul>
			</div>
		</div>
		<div class="col-9">
			<div class="d-flex justify-content-between align-items-center pb-2">
				<!-- <app-paging-header [totalItems]="totalItems" [pageNumber]="shopParams.pageNumber"
                    [pageSize]="shopParams.pageSize"></app-paging-header> -->
				<div class="d-flex mt-2">
					<input type="text" placeholder="Search" class="form-control me-2" />
					<button type="button" class="btn btn-outline-primary mx-2"> Search </button>
					<button type="button" class="btn btn-outline-danger">Clear</button>
				</div>
			</div>

			<div class="row row-cols-3 g-3 mb-4">
				{#each Array(18) as _}
					<div class="col">
						<ProductItem></ProductItem>
					</div>
				{/each}
			</div>

			<div class="d-flex justify-content-center mb-3">
				<Pagination
					totalItems={60}
					itemsPerPage={6}
					pageNumber={2}
					maxSize={4}
					previousText="&lsaquo;"
					nextText="&rsaquo;"
					firstText="&laquo;"
					lastText="&raquo;"
				></Pagination>
			</div>
		</div>
	</div>
</div>
