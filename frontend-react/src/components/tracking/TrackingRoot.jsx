import React, { useState, useEffect } from 'react';
import OrderSummary from './OrderSummary';
import TrackingTimeline from './TrackingTimeline';

export default function TrackingRoot({orderId}){
    const [orderStatus, setOrderStatus] = useState('preparando');
    const [orderData, setOrderData] = useState(null);
    const [error, setError] = useState(false)

    const fetchOrder = async () => {
        try{
            const response = await fetch(`/orders/${orderId}/`)
            if(!response.ok) throw new Error('Error en fetch api')
            const data = await response.json()
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
    
    if (error) return <p className="tracking-error pad-400 text-300">No se pudo cargar el seguimiento de tu pedido.</p>;
    if (!orderData) return <p className="tracking-loading pad-400 text-300">Cargando seguimiento del pedido...</p>;

    const formatTime = (date) => {
        if (!date) return 'Sin datos';
        try {
            const d = new Date(date);
            if (isNaN(d)) return date;
            return d.toLocaleTimeString([], { hour: '2-digit', minute: '2-digit' });
        } catch { return date; }
    };

    return (
        <div className="tracking-root box-flex direction-column gap-400">

            {/* Cabecera */}
            <div className="tracking-header">
                <p className="text-300 weight-bold color-dark">
                    ID Pedido #{orderData.id ?? orderId}
                </p>
                <p className="text-300 color-dark gap-top-300">Estado:</p>
            </div>
            
            {/* Timeline */}
            <TrackingTimeline
                currentStatus={orderStatus}
                hasIncidence={orderData.has_incidence ?? false}
            />

            {/* Horas */}
            <div className="tracking-times">
                <div className="tracking-time-row box-flex gap-300">
                    <span className="text-300 color-dark">Hora estimada:</span>
                    <span className="text-300 weight-bold color-dark">
                        {formatTime(orderData.estimated_time)}
                    </span>
                </div>
                <hr className="time-divider" />
                <div className="tracking-time-row box-flex gap-300">
                    <span className="text-300 color-dark">Hora programada:</span>
                    <span className="text-300 weight-bold color-dark">
                        {formatTime(orderData.scheduled_time)}
                    </span>
                </div>
            </div>

            {/* Resumen */}
            <OrderSummary order={orderData} />
        </div>
    );
}