// helper: get CSRF token from cookie
document.addEventListener("DOMContentLoaded", () => {
  console.log("DOM loaded, AJAX script ready");
});

function getCookie(name) {
  let cookieValue = null;
  if (document.cookie && document.cookie !== '') {
    const cookies = document.cookie.split(';');
    for (let i=0;i<cookies.length;i++){
      const cookie = cookies[i].trim();
      if (cookie.substring(0, name.length+1) === (name + '=')) {
        cookieValue = decodeURIComponent(cookie.substring(name.length+1));
        break;
      }
    }
  }
  return cookieValue;
}
const csrftoken = getCookie('csrftoken');

// --- Fetch products and render into #product-container ---
async function fetchProducts() {
  const container = document.getElementById("product-container");
  if (!container) return;
  container.innerHTML = `
    <div class="bg-white rounded-lg border p-6 text-center">
      <svg class="animate-spin h-8 w-8 mx-auto mb-3" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24"><circle class="opacity-25" cx="12" cy="12" r="10" stroke="currentColor" stroke-width="4"></circle><path class="opacity-75" fill="currentColor" d="M4 12a8 8 0 018-8v4a4 4 0 00-4 4H4z"></path></svg>
      <p class="text-gray-500">Loading products...</p>
    </div>
  `;

  try {
    const resp = await fetch('/api/products/');
    if (!resp.ok) throw new Error('Network error');
    const products = await resp.json();

    if (!products || products.length === 0) {
      container.innerHTML = `
        <div class="bg-white rounded-lg border p-12 text-center">
          <p class="text-gray-500">No products yet.</p>
        </div>
      `;
      return;
    }

    // render grid
    const html = products.map(p => `
      <article onclick='openDetailModal("${p.id}")' class="cursor-pointer bg-white rounded-lg border p-4 shadow-sm flex flex-col hover:shadow-lg transition-transform transform hover:-translate-y-1">
        <div class="aspect-[16/9] mb-4 bg-gray-100 overflow-hidden">
          ${p.thumbnail ? `<img src="${p.thumbnail}" alt="${p.name}" class="w-full h-full object-cover">` : `<div class="w-full h-full flex items-center justify-center text-gray-400">No image</div>`}
        </div>
        <h3 class="font-semibold text-[#073B4C]">${p.name}</h3>
        <p class="text-[#577590]">Rp${Number(p.price).toLocaleString()}</p>
        <p class="text-sm text-gray-600 mt-2 line-clamp-3">${p.description || ''}</p>
        <div class="mt-4 flex items-center justify-between">
          <div class="text-xs text-gray-500">${p.category}</div>
          <div class="flex items-center gap-2">
            <button onclick='onEditProduct("${p.id}")' class="text-sm px-2 py-1 border rounded text-[#118AB2]">Edit</button>
            <button onclick='onDeleteProduct("${p.id}")' class="text-sm px-2 py-1 border rounded text-red-600">Delete</button>
          </div>
        </div>
      </article>
    `).join('');

    container.innerHTML = `<div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">${html}</div>`;
  } catch (err) {
    container.innerHTML = `<div class="bg-white rounded-lg border p-6 text-center text-red-500">Failed to load products</div>`;
    showToast('Error', 'Gagal memuat produk', 'error');
    console.error(err);
  }
}

// call on page load
window.addEventListener('DOMContentLoaded', fetchProducts);

// --- Create / Edit handling ---
window.submitProductForm = async function() {
  const id = document.getElementById('product-id').value;
  const name = document.getElementById('name').value;
  const price = document.getElementById('price').value;
  const description = document.getElementById('description').value;
  const thumbnail = document.getElementById('thumbnail').value;
  const category = document.getElementById('category').value;

  const formData = new FormData();
  formData.append('name', name);
  formData.append('price', price);
  formData.append('description', description);
  formData.append('thumbnail', thumbnail);
  formData.append('category', category);

  try {
    let url = '/api/products/create/';
    let method = 'POST';

    if (id) {
      url = `/api/products/${id}/edit/`;
    }

    const resp = await fetch(url, {
      method: method,
      headers: {
        'X-CSRFToken': csrftoken
      },
      body: formData
    });

    if (!resp.ok) {
      const err = await resp.json().catch(()=>({detail: 'Invalid'}));
      showToast('Error', err.detail || 'Failed', 'error');
      return;
    }

    const data = await resp.json();
    hideModal();
    showToast(id ? 'Updated' : 'Created', id ? 'Product updated' : 'Product created', 'success');
    // refresh list
    fetchProducts();
  } catch (err) {
    console.error(err);
    showToast('Error', 'Request failed', 'error');
  }
}

// --- Edit button handler: fetch product detail and open modal ---
window.onEditProduct = async function(productId) {
  try {
    const resp = await fetch(`/api/products/${productId}/`);
    if (!resp.ok) throw new Error('Not found');
    const product = await resp.json();
    showModal('edit', product);
  } catch (err) {
    console.error(err);
    showToast('Error', 'Gagal membuka produk', 'error');
  }
}

// --- Delete with confirm ---
window.onDeleteProduct = async function(productId) {
  if (!confirm('Are you sure you want to delete this product?')) return;
  try {
    const resp = await fetch(`/api/products/${productId}/delete/`, {
      method: 'POST',
      headers: { 'X-CSRFToken': csrftoken }
    });
    if (resp.status === 204 || resp.ok) {
      showToast('Deleted', 'Product deleted', 'success');
      fetchProducts();
    } else {
      const err = await resp.json().catch(()=>({detail:'Failed'}));
      showToast('Error', err.detail || 'Failed to delete', 'error');
    }
  } catch (err) {
    console.error(err);
    showToast('Error', 'Request failed', 'error');
  }
}

// --- manual refresh  ---
window.refreshProducts = function() {
  fetchProducts();
  showToast('Refreshing', 'Memuat ulang produk...', 'normal');
}

// === DETAIL MODAL ===
async function openDetailModal(productId) {
  try {
    const resp = await fetch(`/api/products/${productId}/`);
    if (!resp.ok) throw new Error('Failed to fetch detail');
    const product = await resp.json();

    const modal = document.getElementById('detailModal');
    const content = document.getElementById('detailModalContent');

    // isi data
    document.getElementById('detail-title').textContent = product.name;
    document.getElementById('detail-name').textContent = product.name;
    document.getElementById('detail-price').textContent = `Rp${Number(product.price).toLocaleString()}`;
    document.getElementById('detail-description').textContent = product.description || '(No description)';
    document.getElementById('detail-category').textContent = `Category: ${product.category}`;

    const img = document.getElementById('detail-thumbnail');
    const noimg = document.getElementById('detail-noimg');
    if (product.thumbnail) {
      img.src = product.thumbnail;
      img.classList.remove('hidden');
      noimg.classList.add('hidden');
    } else {
      img.classList.add('hidden');
      noimg.classList.remove('hidden');
    }

    modal.classList.remove('hidden');
    setTimeout(() => {
      content.classList.remove('opacity-0','scale-95');
      content.classList.add('opacity-100','scale-100');
    }, 50);

  } catch (err) {
    console.error(err);
    showToast('Error', 'Gagal memuat detail produk', 'error');
  }
}

function hideDetailModal() {
  const modal = document.getElementById('detailModal');
  const content = document.getElementById('detailModalContent');
  content.classList.remove('opacity-100','scale-100');
  content.classList.add('opacity-0','scale-95');
  setTimeout(() => modal.classList.add('hidden'), 150);
}

