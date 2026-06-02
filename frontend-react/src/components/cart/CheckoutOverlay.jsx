import React from 'react';

export const CheckoutOverlay = ({ isOpen, onClose }) => {
    return (
        <div 
            className={`checkout-overlay pos-fixed ${isOpen ? 'show' : ''}`} 
            onClick={onClose}
        ></div>
    );
};