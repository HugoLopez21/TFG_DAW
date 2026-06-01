import React from 'react';
import { ProductCard } from './ProductCard';

export const ProductGrid = ({ products, layout = "standard" }) => {
    return (
        <div className={`products-layout-wrapper position-relative ${layout}-layout`}>
            
            {/* Flechas del carousel */}
            {layout === 'prominents' && (
                <>
                    <button className="carousel-control prev-btn" aria-label="Anterior">&lt;</button>
                    <button className="carousel-control next-btn" aria-label="Siguiente">&gt;</button>
                </>
            )}

            {/* Contenedor con productos */}
            <div className={`products-container-grid ${layout}-grid`}>
                {products.length > 0 ? (
                    products.map(p => (
                        <ProductCard 
                            key={p.id} 
                            product={p} 
                            variant={layout} 
                        />
                    ))
                ) : (
                    <p className="text-muted text-200 pad-200">No hay productos disponibles en esta sección.</p>
                )}
            </div>
        </div>
    );
};