import React, { useState, useEffect } from 'react';
import OrderColumn from './OrderColumn';
import OrderDetail from './OrderDetail';

export default function OrdersList({ userRole, csrftoken }) {
    const [orders, setOrders] = useState([]);
    const [error, setError] = useState(false);
    const [selectedOrder, setSelectedOrder] = useState(null);

    const fetchOrders = async () => {
        try{
            const response = await fetch(`/orders/`);
            if (!response.ok) throw new Error('Error en API');
            const data = await response.json();
            console.log(data)
            setOrders(Array.isArray(data) ? data : []); 
        }catch (error){
            console.error(error);
            setError(true);
        }
    };

    useEffect(() => {
        fetchOrders();
        const fetchInterval = setInterval(fetchOrders, 5000);
        return () => clearInterval(fetchInterval);
    }, []);

    const handleUpdateStatus = async (orderId, newStatus) => {
        setOrders(prev => prev.map(o => 
            o.id === orderId ? { ...o, status: newStatus } : o
        ));
        setSelectedOrder(prev => prev ? { ...prev, status: newStatus } : null);
        
        try{
            const response = await fetch(`/orders/${orderId}/`, {
                method: 'PUT',
                headers: {
                    'Content-Type': 'application/json',
                    'X-CSRFToken': csrftoken,
                },
                // Mandamos solo el estado 
                body: JSON.stringify({ status: newStatus }) 
            });

            if (!response.ok) {
                const errorData = await response.json();
                console.error("Error del servidor:", errorData);
                throw new Error('Error al actualizar el estado en el servidor');
            }

            const data = await response.json();
            
        } catch (error) {
            console.error(error);
            alert("No se pudo guardar el cambio. El tablero se recargará para evitar errores.");
            fetchOrders(); 
        }
    };

    const handleAddIncident = async (orderId, incidentText) => {
        alert(`Incidencia en #${orderId}: ${incidentText}`);
    };

    if (error) return <p className="pad-400 color-danger weight-bold">Error al cargar pedidos.</p>;
    if (orders.length === 0) return <p className="pad-400">Cargando...</p>;

    return (
        <div className="dashboard-main box-flex direction-column gap-500">
            {/* Cabecera */}
            <div className="box-flex justify-between items-center border-bottom pad-bottom-300">
                <h2 className="weight-bold">Tablero de Pedidos</h2>
                <span className="badge btn-primary">
                    Rol: {userRole.toUpperCase()}
                </span>
            </div>

            {/* Kanban Board usando la nueva clase Sass */}
            <div className="orders-board gap-400">
                <OrderColumn title="Pendientes" statusKey="pendiente" orders={orders} onSelectOrder={setSelectedOrder} />
                <OrderColumn title="En Preparación" statusKey="en_preparacion" orders={orders} onSelectOrder={setSelectedOrder} />
                <OrderColumn title="Enviados" statusKey="enviado" orders={orders} onSelectOrder={setSelectedOrder} />
                <OrderColumn title="Entregados" statusKey="entregado" orders={orders} onSelectOrder={setSelectedOrder} />
            </div>

            {/* Modal de Detalle */}
            <OrderDetail 
                order={selectedOrder} 
                userRole={userRole} 
                onClose={() => setSelectedOrder(null)} 
                onUpdateStatus={handleUpdateStatus}
                onAddIncident={handleAddIncident}
            />
        </div>
    );
}