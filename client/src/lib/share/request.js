import { PUBLIC_BASE_API_URL } from "$env/static/public";
import { SpinnerService } from "$lib/components/share/spinner.svelte";
import { ToastService } from "$lib/components/share/toast.svelte";
import axios, { AxiosError } from "axios";

const httpClient = axios.create({
    baseURL: PUBLIC_BASE_API_URL,
    timeout: 5000
});

async function delay(ms = 1500) {
    return new Promise((resolve) => setTimeout(resolve, ms));
}

const apiClientWithSpinner = axios.create({
    baseURL: PUBLIC_BASE_API_URL,
    timeout: 5000
})

/**
 * @param {AxiosError} error
 */
function handleError(error) {
    const response = error.response;
    let errorMessage = error.message;
    if (response) {
        errorMessage = response.data.message
    }
    ToastService.notifyError(errorMessage);
    console.log(error);
}

apiClientWithSpinner.interceptors.response.use(async (response) => {
    SpinnerService.showSpinner();
    await delay(1000);
    SpinnerService.hideSpinner();
    return response;
}, handleError)

export {
    httpClient,
    delay,
    apiClientWithSpinner
};