import React from 'react';
import ReactDOM from 'react-dom/client';
import ShoppingCartRoot from '../components/shopping-cart/ShoppingCartRoot';

const container = document.getElementById('django-cart-island');
if (container) {
    const root = ReactDOM.createRoot(container);
    root.render(<ShoppingCartRoot/>);
}