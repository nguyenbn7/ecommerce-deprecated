import { PUBLIC_BASE_API_URL } from '$env/static/public';

/**
 * @returns {Promise<ProductType[]>}
 */
export async function getProductTypes() {
	const response = await fetch(`${PUBLIC_BASE_API_URL}/products/types/`);
	return await response.json();
}
