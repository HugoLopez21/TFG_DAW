import React from 'react';
import ReactDOM from 'react-dom/client';
import OrdersList from '../components/orders-dashboard/OrdersList';

const container = document.getElementById('django-tracking-island');
if (container) {
    const root = ReactDOM.createRoot(container);
    const orderId = container.getAttribute('data-order-id');
    root.render(<OrdersList/>);
}