import React from 'react';

export const CheckoutHeader = ({ onClose }) => {
    return (
        <div className="checkout-panel-header box-flex justify-between items-center gap-bottom-300">
            <h3 className="checkout-panel-title">Resumen de compra</h3>
            <button 
                className="checkout-close" 
                onClick={onClose} 
                aria-label="Cerrar panel"
            >✕</button>
        </div>
    );
};