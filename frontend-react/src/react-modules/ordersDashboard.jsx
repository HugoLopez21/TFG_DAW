import React from 'react';
import ReactDOM from 'react-dom/client';
import OrdersList from '../components/orders-dashboard/OrdersList';

const container = document.getElementById('django-tracking-island');
if (container) {
    const root = ReactDOM.createRoot(container);
    const csrftoken = container.getAttribute('data-csrf')
    const userRole = container.getAttribute('data-user-role'); 
    root.render(<OrdersList userRole={userRole} csrftoken={csrftoken} />);
}