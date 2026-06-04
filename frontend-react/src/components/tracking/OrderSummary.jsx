import React from 'react';

export default function OrderSummary({ order }) {

    return (
        <div className="order-summary bg-light radius-sm pad-400">
            <p className="order-summary-title text-300 weight-bold gap-bottom-400">
                Resumen pedido #{order.id}
            </p>

            {/*Seccion detalles */}
            <div className="order-summary-items box-flex direction-column gap-300 gap-bottom-400">
                {order.details.map((item, index) =>(
                    <div key={index} className="order-item-row">
                        <div className="order-item-thumb radius-sm">
                            {item.image
                                ? <img src={item.image} alt={item.product_name} />
                                : <div className="thumb-placeholder">
                                    <i className="fa-regular fa-image"></i>
                                </div>
                            }
                        </div>
                        <span className="order-item-name text-300 weight-bold">
                            {item.product_name}
                        </span>
                        <span className="order-item-qty text-300">
                            Cantidad: {item.quantity}
                        </span>
                        <span className="order-item-price text-300 weight-bold">
                            {parseFloat(item.unit_price).toFixed(2)}€
                        </span>
                        {item.notes && (
                            <span className="order-item-notes text-300 color-primary">
                                <i className="fa-solid fa-comment-dots gap-right-300"></i>
                                {item.notes}
                            </span>
                        )}
                    </div>
                ))}
            </div>
            
            {/*Seccion total */}
            <div className="order-summary-total box-flex items-center gap-300">
                <span className="text-500 weight-bold color-dark">TOTAL:</span>
                <span className="text-500 weight-bold color-primary">
                    {parseFloat(order.total).toFixed(2)}€
                </span>
            </div>

            {/*Seccion reporte */}
            <div className="order-summary-footer gap-top-400">
                <button
                    className="btn btn-secondary"
                    onClick={() => alert('Reportar problema: funcionalidad pendiente')}
                >
                    Reportar problema
                </button>
            </div>
        </div>
    );
}