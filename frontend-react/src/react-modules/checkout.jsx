import React from 'react';
import ReactDOM from 'react-dom/client';
import {CheckoutPanel} from '../components/cart/CheckoutPanelRoot';

const container = document.getElementById('django-checkoutpanel-island');
if (container) {
    const root = ReactDOM.createRoot(container);
    root.render(<CheckoutPanel/>);
}