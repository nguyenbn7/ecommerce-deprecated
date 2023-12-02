import { PUBLIC_BASE_API_URL } from "$env/static/public";
import { SpinnerService } from "$lib/components/share/spinner.svelte";
import { ToastService } from "$lib/components/share/toast.svelte";
import axios, { AxiosError } from "axios";
import { delay } from "./functions";

const httpClientWithSpinner = axios.create({
    baseURL: PUBLIC_BASE_API_URL,
    timeout: 5000
});

httpClientWithSpinner.interceptors.request.use(config => {
    SpinnerService.show();
    return config;
})

httpClientWithSpinner.interceptors.response.use(async (response) => {
    await delay();
    SpinnerService.hide();
    return response;
}, error => {
    if (error instanceof AxiosError) {
        ToastService.notifyError(error.message);
    }
    SpinnerService.hide();
    throw error;
});

export default httpClientWithSpinner;