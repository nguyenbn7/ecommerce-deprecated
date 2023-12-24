// https://www.reddit.com/r/sveltejs/comments/11fr6oe/where_do_you_put_your_shared_custom_types_for/

type Product = {
	price: number;
	pictureUrl: string;
	name: string;
	description: string;
	id: number;
	productType: string;
	productBrand: string;
};

type Page<T> = {
	pageNumber: number;
	pageSize: number;
	totalItems: number;
	data: T[];
};

type ShopParams = {
	pageNumber: number;
	pageSize: number;
	sort: string;
	search: string | undefined;
	brandId: number;
	typeId: number;
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

type Validator = { check: (value: string) => boolean; errorMessage: string };

type Register = {
	email: string;
	display_name: string;
	password: string;
	confirm_password: string;
};

declare namespace Toastr {
	type Type = 'DANGER' | 'SUCCESS' | 'INFO' | 'WARNING';

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

// CHECKOUT
type Order = {
	basket_id: string;
	billing_address: OrderAddress;
	shipping_address: OrderAddress?;
	delivery_method_id: number;
	payment_type: string;
};

type OrderAddress = {
	full_name: string;
	email: string;
	phone_number: string;
	address: string;
	address2: string;
	country: string;
	state: string;
	zip_code: string;
};

type DeliveryMethod = {
	short_name: string;
	delivery_time: string;
	price: number;
	id: number;
};

// ACCOUNT
type LoginDTO = {
	email: string;
	password: string;
};

type RegisterDTO = {
	email: string;
	password: string;
	display_name: string;
	confirm_password: string;
};

type SignInSuccess = {
	displayName: string;
	email: string;
	token: string;
};

type User = {
	email: string;
	displayName: string;
};

type UserInfoResponse = {
	email: string;
	displayName: string;
};

type OrderForm = {
	email: any;
};
