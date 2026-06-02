
/*VARIABLES*/
let cart = [];

// Elementos carrito
const cartCount = document.getElementById("cart-count");

// Elementos de pago
const checkoutPanel = document.getElementById("checkout-panel");
const checkoutOverlay = document.getElementById("checkout-overlay");
const checkoutOpen = document.getElementById("cart-button"); // Cambiado id de checkout-open a cart-button
const checkoutClose = document.getElementById("checkout-close");
const checkoutItems = document.getElementById("checkout-items");
const checkoutTotal = document.getElementById("checkout-total");
const checkoutPay = document.getElementById("checkout-pay");


//Elemento aviso
const toast = document.getElementById("toast");



/*QUITAR €*/

// Convierte texto "3.99€" → 3.99
function getNumber(price) {
  // Eliminamos cualquier caracter que no sea número, punto o coma, y convertimos coma a punto
  const cleanedPrice = price.replace(/[^\d,.]/g, "").replace(",", ".");
  return parseFloat(cleanedPrice);
}

// Muestra mensaje inferior
function showToast(msg) {
  if (!toast) return;
  toast.textContent = msg;
  toast.classList.add("show");
  setTimeout(() => toast.classList.remove("show"), 2000);
}


// Pintar productos del carrito
function renderCart() {
  if (checkoutItems) checkoutItems.innerHTML = "";

  let total = 0;

  cart.forEach(item => {
    const quantity = item.quantity || 1;
    const itemPrice = getNumber(item.price) * quantity;
    total += itemPrice;

    if (checkoutItems) {
      checkoutItems.innerHTML += `
        <div class="checkout-item">
          <img src="${item.image}">
          <div>
            <div>${item.name}</div>
            <small>${quantity}x ${item.price}</small>
          </div>
          <strong>${itemPrice.toFixed(2)}€</strong>
        </div>
      `;
    }
  });

  //ACTUALIZA EL CONTADOR DEL PANEL
  const checkoutCountEl = document.getElementById("checkout-count");
  if (checkoutCountEl) {
    const totalItems = cart.reduce((sum, item) => sum + (item.quantity || 1), 0);
    let palabra = (totalItems === 1) ? "artículo" : "artículos";
    checkoutCountEl.textContent = totalItems + " " + palabra;
  }

  //ACTUALIZA EL TOTAL
  if (checkoutTotal) {
    checkoutTotal.textContent = "Total: " + total.toFixed(2) + "€";
  }
}


// Actualizar el numerito del carrito
function updateCartCount() {
  if (cartCount) {
    const quantity = cart.reduce((sum, item) => sum + (item.quantity || 1), 0);
    cartCount.textContent = quantity;
  }
}


/*AÑADIR AL CARRITO*/
function addToCart(productCard) {
  const nameEl = productCard.querySelector(".product-name");
  const priceEl = productCard.querySelector("h4");
  const imgEl = productCard.querySelector("img");
  const idEl = productCard.getAttribute("data-product-id");

  if (!nameEl || !priceEl) return;

  const id = idEl || nameEl.textContent; // Usar data-product-id si existe, sino nombre
  const name = nameEl.textContent;
  const price = priceEl.textContent;
  const image = imgEl ? imgEl.src : "";

  // Buscar si el producto ya existe
  const existingItem = cart.find(item => item.id === id);
  if (existingItem) {
    existingItem.quantity = (existingItem.quantity || 1) + 1;
  } else {
    cart.push({ id, name, price, image, quantity: 1 });
  }

  updateCartCount();
  renderCart();
  showToast(name + " añadido al carrito");
}

/* EJECUTAR FUNCION AÑADIR"*/
const botones = document.querySelectorAll(".add-to-cart");

botones.forEach(function (boton) {
  boton.addEventListener("click", function () {
    // Busca la tarjeta del producto donde está el botón
    const tarjeta = boton.closest(".product-card");
    if (tarjeta) {
      addToCart(tarjeta);
    }
  });
});



/*CHECKOUT PANEL*/
if (checkoutOpen) {
  checkoutOpen.addEventListener("click", () => {
    const totalItems = cart.reduce((sum, item) => sum + (item.quantity || 1), 0);
    if (totalItems === 0) return showToast("El carrito está vacío");

    checkoutPanel.classList.add("open");
    checkoutOverlay.classList.add("show");
  });
}

if (checkoutClose) checkoutClose.addEventListener("click", closePanel);
if (checkoutOverlay) checkoutOverlay.addEventListener("click", closePanel);

function closePanel() {
  if (checkoutPanel) checkoutPanel.classList.remove("open");
  if (checkoutOverlay) checkoutOverlay.classList.remove("show");
}

// Simular pago
if (checkoutPay) {
  checkoutPay.addEventListener("click", () => {
    if (cart.length === 0) return;
    
    // Guardar carrito en localStorage
    localStorage.setItem('cart_data', JSON.stringify(cart));
    
    // Redirigir a checkout
    window.location.href = '/orders/checkout/';
  });
}




/*ORDENAR (Opcional, se mantiene por estructura si existen los elementos)*/
const productGrid = document.querySelector(".products-grid");
const sortSelect = document.getElementById("sort-select");

if (productGrid && sortSelect) {
  const ordenOriginal = Array.from(productGrid.children);

  sortSelect.addEventListener("change", () => {
    const opcion = sortSelect.value;

    if (opcion === "relevance") {
      productGrid.innerHTML = "";
      ordenOriginal.forEach(producto => productGrid.appendChild(producto));
      return;
    }

    const productos = Array.from(productGrid.children);

    productos.sort((a, b) => {
      const nombreA = (a.querySelector(".product-name")?.textContent || "").trim();
      const nombreB = (b.querySelector(".product-name")?.textContent || "").trim();

      const precioA = getNumber(a.querySelector("h4")?.textContent || "0");
      const precioB = getNumber(b.querySelector("h4")?.textContent || "0");

      if (opcion === "priceAsc") return precioA - precioB;
      if (opcion === "priceDesc") return precioB - precioA;
      if (opcion === "nameAsc") return nombreA.localeCompare(nombreB);
      if (opcion === "nameDesc") return nombreB.localeCompare(nombreA);
    });

    productGrid.innerHTML = "";
    productos.forEach(producto => productGrid.appendChild(producto));
  });
}


/* INICIALIZACIÓN */
updateCartCount();
renderCart();
renderCart();