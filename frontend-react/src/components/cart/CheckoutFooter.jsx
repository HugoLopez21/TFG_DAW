import React from 'react';

export const CheckoutFooter = ({ onPay }) => {
    return (
        <div className="checkout-panel-footer gap-top-400 box-flex direction-column">
            <button className="btn btn-primary" type="button" onClick={onPay}>
                Ir al Checkout
            </button>
        </div>
    );
};