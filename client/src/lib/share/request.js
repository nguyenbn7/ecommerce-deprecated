import { PUBLIC_BASE_API_URL } from "$env/static/public";
import axios from "axios";

const httpClient = axios.create({
    baseURL: PUBLIC_BASE_API_URL,
    timeout: 5000
});

async function delay(ms = 1500) {
    return new Promise((resolve) => setTimeout(resolve, ms));
}

export {
    httpClient,
    delay
};