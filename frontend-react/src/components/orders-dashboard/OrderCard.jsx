import React from 'react';

export default function OrderCard({ order, onSelect }) {
    return (
        <div 
            className="order-card pad-300" 
            onClick={() => onSelect(order)}
        >
            <div className="box-flex direction-column gap-100">
                <strong className="weight-bold">#{order.id} - {order.client_name}</strong>
                <p className="text-muted">Total: {order.total}€</p>
            </div>
        </div>
    );
}