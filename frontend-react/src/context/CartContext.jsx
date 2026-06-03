import React, { createContext, useContext, useState, useEffect } from 'react';
const CartContext = createContext();

export const useCart = () => useContext(CartContext);

export const CartProvider = ({children}) => {
    const [cart, setCart] = useState(() => {
        const savedCart = localStorage.getItem('shopping_cart');
        return savedCart ? JSON.parse(savedCart) : [];
    });
    const [isPanelOpen, setIsPanelOpen] = useState(false);

    //Sincronizar el número del carrito 
    useEffect(() => {
        localStorage.setItem('shopping_cart', JSON.stringify(cart));
        const cartCount = document.getElementById("cart-count");
        if (cartCount) {
            const totalItems = cart.reduce((sum, item) => sum + (item.quantity || 1), 0);
            cartCount.textContent = totalItems;
        }
    }, [cart]);

    // Abrir el panel al hacer click en el carrito
    useEffect(() => {
        const cartButton = document.getElementById("cart-button");
        
        const handleOpenPanel = () => {
            const totalItems = cart.reduce((sum, item) => sum + (item.quantity || 1), 0);
            if (totalItems === 0) {
                showToast("El carrito está vacío");
                return;
            }
            setIsPanelOpen(true);
        };

        if (cartButton) {
            cartButton.addEventListener("click", handleOpenPanel);
        }

        return () => {
            if (cartButton) cartButton.removeEventListener("click", handleOpenPanel);
        };
    }, [cart]);

    // Función auxiliar para mostrar los avisos toast
    const showToast = (msg) => {
        const toastEl = document.getElementById("toast");
        if (!toastEl) return;
        toastEl.textContent = msg;
        toastEl.classList.add("show");
        setTimeout(() => toastEl.classList.remove("show"), 3000);
    };

    const addToCart = (product) => {
        setCart((prevCart) => {
            const existingItem = prevCart.find(item => item.id === product.id);
            if (existingItem) {
                return prevCart.map(item =>
                    item.id === product.id 
                        ? { ...item, quantity: (item.quantity || 1) + 1 }
                        : item
                );
            }
            return [...prevCart, { ...product, quantity: 1 }];
        });
        showToast(`${product.name} añadido al carrito`);
    };

    // Redireccion paea pagar
    const handlePay = () => {
        if (cart.length === 0) return;
        localStorage.setItem('shopping_cart', JSON.stringify(cart));
        window.location.href = '/orders/checkout/';
    };

    return (
        <CartContext.Provider value={{ cart, isPanelOpen, setIsPanelOpen, addToCart, handlePay }}>
            {children}
        </CartContext.Provider>
    );
};