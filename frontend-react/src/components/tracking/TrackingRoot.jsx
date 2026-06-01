import React, { useState, useEffect } from 'react';
import TrackingTimeline from './TrackingTimeline';
import OrderSummary from './OrderSummary';

export function TrackingRoot({orderId}){
    const [orderStatus, setOrderStatus] = useState('preparando');
    const [orderData, setOrderData] = useState(null);
    const [error, setError] = useState(false)

    const fetchOrder = async () => {
        try{
            const response = await fetch(`/orders/${orderId}/`)
            if(!response.ok) throw new Error('Error en fetch api')
            const data = await response.json()
            console.log(data)
            setOrderData(data)
            setOrderStatus(data.status)
        }catch(error){
            console.error(error)
            setError(true);
        }
    }
    
    useEffect(() => {
        if (orderId) {
            fetchOrder();
            const fetchInterval = setInterval(fetchOrder, 10000);
            return () => clearInterval(fetchInterval);
        }
    }, [orderId]);
    
    if (error) return <p className="pad-400">No se pudo cargar el seguimiento de tu pedido.</p>;
    if (!orderData) return <p>Cargando seguimiento del pedido...</p>;

    return (
        <div class="box-flex flex-column gap-500">
            <TrackingTimeline currentStatus={orderStatus} />
            <OrderSummary order={orderData} />
        </div>
    );
}
