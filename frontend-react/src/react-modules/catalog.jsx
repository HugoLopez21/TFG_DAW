import React from 'react';
import ReactDOM from 'react-dom/client';
import CatalogRoot from '../components/products-catalog/CatalogRoot';

const container = document.getElementById('django-catalog-island');
if (container) {
    const root = ReactDOM.createRoot(container);
    root.render(<CatalogRoot/>);
}