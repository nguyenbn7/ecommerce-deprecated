export const ssr = false;

/** @type {import('./$types').LayoutLoad} */
export async function load() {
    await (await import("$lib/share/service")).init();
}
