// https://www.reddit.com/r/sveltejs/comments/11fr6oe/where_do_you_put_your_shared_custom_types_for/

type Products = Product[]

type Product = {
    price: number
    picture_url: string
    name: string
    description: string
    id: number
    product_type_id: number
    product_brand_id: number
}

type Page<T> = {
    page_index: number
    page_size: number,
    total_items: number,
    data: T[]
}

type ShopParams = {
    page_index: number,
    page_size: number,
    sort: string,
    search: string | undefined,
    brand_id: number,
    type_id: number
}

type ProductBrand = {
    id: number,
    name: string,
}

type ProductType = {
    id: number,
    name: string,
}