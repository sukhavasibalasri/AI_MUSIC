function apiUrl(path) {
    const baseUrl = (window.API_BASE_URL || "").trim().replace(/\/+$/, "");
    const normalizedPath = path.startsWith("/") ? path : `/${path}`;
    return `${baseUrl}${normalizedPath}`;
}

function apiFetch(path, options = {}) {
    return fetch(apiUrl(path), {
        ...options,
        credentials: "include"
    });
}
