async function refreshProducts() {
  const container = document.getElementById("product-container");
  container.innerHTML = `<p class="text-center text-gray-500">Loading...</p>`;

  try {
    const response = await fetch("/get-products/");
    if (!response.ok) throw new Error("Gagal ambil data produk");
    const data = await response.json();

    if (data.length === 0) {
      container.innerHTML = `
        <div class="text-center text-gray-500 p-10">
          <p>No products found 😢</p>
        </div>`;
      return;
    }

    container.innerHTML = `
      <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
        ${data.map(item => {
          const product = item.fields;
          return `
            <div class="bg-white rounded-lg shadow border p-4">
              <h2 class="text-lg font-semibold text-[#073B4C] mb-2">${product.name}</h2>
              <p class="text-sm text-gray-600">${product.description}</p>
              <p class="text-sm text-[#43AA8B] mt-1 font-medium">Rp ${product.price}</p>
              <div class="flex gap-2 mt-3">
                <button onclick="openEditModal(${item.pk})" class="text-blue-600 hover:underline">Edit</button>
                <button onclick="confirmDelete(${item.pk})" class="text-red-600 hover:underline">Delete</button>
              </div>
            </div>`;
        }).join('')}
      </div>`;
  } catch (error) {
    container.innerHTML = `<p class="text-center text-red-500">${error.message}</p>`;
  }
}

// Load awal
document.addEventListener("DOMContentLoaded", refreshProducts);

