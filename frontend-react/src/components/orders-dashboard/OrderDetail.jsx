import React, { useState } from 'react';

export default function OrderDetai({ order, userRole, onClose, onUpdateStatus, onAddIncident }) {
    const [incidentText, setIncidentText] = useState('');

    if (!order) return null;

    // Lógica de roles
    const canChangeToPrep = (userRole === 'manager' || userRole === 'employee') && order.status === 'pendiente';
    const canChangeToPickedUp = (userRole === 'manager' || userRole === 'employee') && order.status === 'en_preparacion';
    const canChangeToDelivered = (userRole === 'manager' || userRole === 'employee' || userRole === 'delivery_man') && order.status === 'enviado';
    const canAddIncident = userRole === 'manager';

    const hasAnyAction = canChangeToPrep || canChangeToPickedUp || canChangeToDelivered;

    return (
        <div className={`order-modal-overlay pos-fixed show`} onClick={onClose}>
            <div className={`order-modal-panel open pad-500`} onClick={e => e.stopPropagation()}>
                
                {/* Cabecera */}
                <div className="box-flex justify-between items-center border-bottom pad-bottom-300">
                    <h3 className="weight-bold">Pedido #{order.id}</h3>
                    <button onClick={onClose} className="btn btn-secondary">✕</button>
                </div>

                <div className="gap-top-400 box-flex direction-column gap-300">
                    <p><strong>Cliente:</strong> {order.client_name}</p>
                    <p><strong>Estado:</strong> <span className="color-primary weight-bold">{order.status.replace('_', ' ').toUpperCase()}</span></p>
                    <p><strong>Total:</strong> {order.total}€</p>
                    
                    {/* Botones de Acción */}
                    <div className="gap-top-500 box-flex direction-column gap-300">
                        <h4 className="weight-bold">Acciones de Flujo</h4>
                        
                        {canChangeToPrep && (
                            <button className="btn btn-primary" onClick={() => onUpdateStatus(order.id, 'en_preparacion')}>
                                Marcar En Preparación
                            </button>
                        )}
                        {canChangeToPickedUp && (
                            <button className="btn btn-info" onClick={() => onUpdateStatus(order.id, 'enviado')}>
                                Marcar como Recogido
                            </button>
                        )}
                        {canChangeToDelivered && (
                            <button className="btn btn-secondary" onClick={() => onUpdateStatus(order.id, 'entregado')}>
                                Marcar como Entregado
                            </button>
                        )}
                        
                        {!hasAnyAction && (
                            <p className="text-muted" style={{fontSize: '0.85rem'}}>No tienes acciones disponibles para este pedido.</p>
                        )}
                    </div>

                    {/* Incidencias Solo Manager */}
                    {canAddIncident && (
                        <div className="gap-top-500 pad-top-400 border-top box-flex direction-column gap-300">
                            <h4 className="weight-bold color-danger">Registrar Incidencia</h4>
                            <textarea 
                                className="form-control" 
                                rows="3" 
                                value={incidentText}
                                onChange={(e) => setIncidentText(e.target.value)}
                                placeholder="Escribe el reporte aquí..."
                            />
                            <button 
                                className="btn btn-danger"
                                onClick={() => {
                                    if(incidentText.trim()){
                                        onAddIncident(order.id, incidentText);
                                        setIncidentText('');
                                    }
                                }}
                            >
                                Guardar Incidencia
                            </button>
                        </div>
                    )}
                </div>
            </div>
        </div>
    );
}