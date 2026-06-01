import React from 'react';
import { ProductCard } from './ProductCard';

export const ProductGrid = ({ products, layout = "standard" }) => {
    return (
        <div class={`products-layout-wrapper position-relative ${layout}-layout`}>
            
            {/* Flechas del carousel */}
            {layout === 'prominents' && (
                <>
                    <button class="carousel-control prev-btn" aria-label="Anterior">&lt;</button>
                    <button class="carousel-control next-btn" aria-label="Siguiente">&gt;</button>
                </>
            )}

            {/* Contenedor con productos */}
            <div class={`products-container-grid ${layout}-grid`}>
                {products.length > 0 ? (
                    products.map(p => (
                        <ProductCard 
                            key={p.id} 
                            product={p} 
                            variant={layout} 
                        />
                    ))
                ) : (
                    <p class="text-muted text-200 pad-200">No hay productos disponibles en esta sección.</p>
                )}
            </div>
        </div>
    );
};