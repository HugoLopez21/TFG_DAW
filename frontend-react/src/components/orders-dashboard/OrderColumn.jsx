import React from 'react';
import OrderCard from './OrderCard';

export default function OrderColumn({ title, statusKey, orders, onSelectOrder }) {
    const columnOrders = orders.filter(o => o.status === statusKey);

    return (
        <div className="order-column pad-400">
            <h3 className="pad-bottom-300 border-bottom">
                {title} ({columnOrders.length})
            </h3>
            
            <div className="gap-top-400 box-flex direction-column gap-300">
                {columnOrders.map(order => (
                    <OrderCard 
                        key={order.id} 
                        order={order} 
                        onSelect={onSelectOrder} 
                    />
                ))}
                
                {columnOrders.length === 0 && (
                    <p className="text-center text-muted pad-300">No hay pedidos</p>
                )}
            </div>
        </div>
    );
}