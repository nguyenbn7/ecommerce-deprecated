// https://www.reddit.com/r/sveltejs/comments/11fr6oe/where_do_you_put_your_shared_custom_types_for/

type Products = Product[];

type Product = {
	price: number;
	picture_url: string;
	name: string;
	description: string;
	id: number;
	product_type: string;
	product_brand: string;
};

type Page<T> = {
	page_number: number;
	page_size: number;
	total_items: number;
	data: T[];
};

type ShopParams = {
	page_number: number;
	page_size: number;
	sort: string;
	search: string | undefined;
	brand_id: number;
	type_id: number;
};

type ProductBrand = {
	id: number;
	name: string;
};

type ProductType = {
	id: number;
	name: string;
};

type Basket = {
	id: string;
	items: BasketItem[];
};

type BasketItem = {
	id: number;
	product_name: string;
	price: number;
	quantity: number;
	picture_url: string;
	brand: string;
	type: string;
};

type BasketTotals = {
	shipping: number;
	subtotal: number;
	total: number;
};

type Login = {
	email: string;
	password: string;
};

type LoginSuccess = {
	display_name: string;
	email: string;
	token: string;
};

type Validator = { check: (inputField: InputFieldType) => boolean; errorMessage: string? };
type Validators = Validator[];

type InputFieldType = {
	dirty: boolean;
	valid: boolean;
	value: string;
	validationMessage: string | null;
	successMessage: string | null;
	validators: Validators;
};

type Register = {
	email: string;
	display_name: string;
	password: string;
	confirm_password: string;
};

type UserInfo = {
	email: string;
	display_name: string;
};

type SuccessResponse = {
	token: string;
	email: string;
	display_name: string;
};

declare namespace Toastr {
	type Type = 'ERROR' | 'SUCCESS' | 'INFO' | 'WARNING';

	type Configuration = {
		/** apply animation fly in and fade out. Default true */
		animation: boolean;
		/** auto hide after show toast. Default true */
		autohide: boolean;
		/** Delay hidden time in (ms). Default 5000 ms */
		delay: number;
		/** Auto remove after hide. Default true */
		autodispose: boolean;
		/** Enable click on toast which make it hidden and removed from container. Default true */
		enableClickToastDispose: boolean;
		/** Enable click on toast which make it hidden. Default false */
		enableClickToastHide: boolean;
	};
}

type ErrorResponse = {
	message: string;
	error: any | undefined | null;
	errors: any | Array | undefined | null;
};
