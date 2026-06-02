import React from 'react';

export const CheckoutItemRow = ({ item }) => {
    const itemPrice = parseFloat(item.price) || 0;
    const itemTotal = itemPrice * item.quantity;

    return (
        <div className="checkout-item">
            <img src={item.image || ""} alt={item.name} />
            <div>
                <div>{item.name}</div>
                <small>{item.quantity}x {itemPrice.toFixed(2)}€</small>
            </div>
            <strong>{itemTotal.toFixed(2)}€</strong>
        </div>
    );
};