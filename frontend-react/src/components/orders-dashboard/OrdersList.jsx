import React, { useState, useEffect } from 'react';


export default function OrdersList(){
    const [orderStatus, setOrderStatus] = useState('preparando');
    const [orderData, setOrderData] = useState(null);
    const [error, setError] = useState(false)

    const fetchOrderList = async () => {
        try{
            const response = await fetch(`/orders/`)
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
        
        fetchOrderList();
        const fetchInterval = setInterval(fetchOrderList, 5000);
        return () => clearInterval(fetchInterval);
    }, []);
    
    if (error) return <p className="pad-400">No se ha podido cargar la lista de pedidos</p>;
    if (!orderData) return <p>Cargando pedidos.</p>;

    return (
        <div class="box-flex flex-column gap-500">
            <h2>Lista de pedidos activos</h2>
        </div>
    );
}
