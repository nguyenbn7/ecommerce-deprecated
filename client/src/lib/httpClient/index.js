import { PUBLIC_BASE_API_URL } from "$env/static/public";
import axios from "axios";

export const httpClient = axios.create({
	baseURL: PUBLIC_BASE_API_URL,
	timeout: 5000
});