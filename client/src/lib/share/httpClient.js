import { PUBLIC_BASE_API_URL } from '$env/static/public';
import axios, { AxiosError } from 'axios';
import { ToastrService } from './component/toastr.svelte';
import { SpinnerService } from './component/spinner.svelte';
import { AccountService } from './service/account';

export async function delay(ms = 1500) {
	return new Promise((resolve) => setTimeout(resolve, ms));
}

export const httpClient = axios.create({
	baseURL: PUBLIC_BASE_API_URL,
	timeout: 5000
});

const httpClientSpinner = axios.create({
	baseURL: PUBLIC_BASE_API_URL,
	timeout: 5000
})

httpClientSpinner.interceptors.request.use(config => {
	SpinnerService.showSpinner();
	return config;
})

httpClientSpinner.interceptors.response.use(async (response) => {
	await delay(1000);
	SpinnerService.hideSpinner();
	return response;
}, async (error) => {
	await delay(1000);
	SpinnerService.hideSpinner();
	const response = error.response;
	let errorMessage = error.message;
	if (response) {
		errorMessage = response.data.message;
	}
	ToastrService.notifyDanger(errorMessage);
	throw error;
});

export { httpClientSpinner };

/**
 * @param {AxiosError} error
 */
export function defaultHandleError(error) {
	const response = error.response;
	let errorMessage = error.message;
	if (response) {
		errorMessage = response.data.message;
	}
	ToastrService.notifyDanger(errorMessage);
	throw error;
}

const httpClientAuthSpinner = axios.create({
	baseURL: PUBLIC_BASE_API_URL,
	timeout: 5000
})

httpClientAuthSpinner.interceptors.request.use(config => {
	config.headers.Authorization = `Bearer ${AccountService.getAccessToken()}`;
	SpinnerService.showSpinner();
	return config;
})

httpClientAuthSpinner.interceptors.response.use(async (response) => {
	await delay(1000);
	SpinnerService.hideSpinner();
	return response;
}, async (error) => {
	await delay(1000);
	SpinnerService.hideSpinner();
	const response = error.response;
	let errorMessage = error.message;
	if (response) {
		errorMessage = response.data.message;
	}
	ToastrService.notifyDanger(errorMessage);
	throw error;
});

export { httpClientAuthSpinner };