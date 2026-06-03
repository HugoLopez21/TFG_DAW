import React from 'react';
import ReactDOM from 'react-dom/client';
import TrackingRoot from '../components/tracking/TrackingRoot';

const container = document.getElementById('django-tracking-island');
if (container) {
    const root = ReactDOM.createRoot(container);
    const orderId = container.getAttribute('order-id');
    console.log(orderId)
    root.render(<TrackingRoot orderId={orderId}/>);
}