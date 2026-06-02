import React from 'react';
import { useCart } from '../../context/CartContext';
import { CheckoutOverlay } from './CheckoutOverlay';
import { CheckoutHeader } from './CheckoutHeader';
import { CheckoutItemRow } from './CheckoutItemRow';
import { CheckoutFooter } from './CheckoutFooter';

export const CheckoutPanel = () => {
    const { cart, isPanelOpen, setIsPanelOpen, handlePay } = useCart();

    //Cálculos 
    const totalItems = cart.reduce((sum, item) => sum + item.quantity, 0);
    const totalPrice = cart.reduce((sum, item) => sum + (parseFloat(item.price) * item.quantity), 0);
    const palabraArticulo = totalItems === 1 ? "artículo" : "artículos";

    return (
        <>
            <CheckoutOverlay isOpen={isPanelOpen} onClose={() => setIsPanelOpen(false)} />

            {/* Panel Lateral */}
            <aside 
                className={`checkout-panel pos-fixed box-flex direction-column ${isPanelOpen ? 'open' : ''}`} 
                aria-hidden={!isPanelOpen}
            >
                <CheckoutHeader onClose={() => setIsPanelOpen(false)} />

                <div className="checkout-panel-body">
                    <p id="checkout-count">{totalItems} {palabraArticulo}</p>
                    
                    {/* Lista de productos */}
                    <div id="checkout-items" className="checkout-items gap-top-400 box-flex direction-column gap-400">
                        {cart.map((item) => (
                            <CheckoutItemRow key={item.id} item={item} />
                        ))}
                    </div>

                    {/* Resumen */}
                    <div className="checkout-summary gap-top-300 pad-top-300">
                        <p id="checkout-total">Total: {totalPrice.toFixed(2)}€</p>
                    </div>
                </div>

                <CheckoutFooter onPay={handlePay} />
            </aside>
        </>
    );
};