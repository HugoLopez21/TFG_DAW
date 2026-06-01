import React from "react";

export const ProductCard = ({ product, variant = "standard" }) => {
    
    // Función carrito de compras
    const handleAddClick = () => {
        console.log(`Producto añadido: ${product.name}`);
    };

    return (
        <article class={`product-card-item box-flex border-radius-md bg-white ${variant}-card`}>
            
            {/* Contenedor de la Imagen */}
            <div class="product-image-container box-flex items-center justify-center">
                {product.image ? (
                    <img src={product.image} alt={product.name} class="product-img" />
                ) : (
                    <div class="img-placeholder"><i class="fa-regular fa-image"></i></div>
                )}
            </div>

            {/* Contenedor de Textos e Información */}
            <div class="product-info-container box-flex flex-column justify-between flex-1">
                <div class="product-header">
                    <span class="product-badge text-100 text-muted uppercase tracking-wider block">
                        {variant === 'sales' ? 'Oferta Especial' : ''}
                    </span>
                    <h4 class="product-name text-300 weight-medium gap-top-100">
                        {product.name}
                    </h4>
                </div>

                <div class="product-footer box-flex justify-between items-center gap-top-200">
                    <span class="product-price text-300 weight-bold color-dark">
                        {parseFloat(product.price).toFixed(2)}€
                    </span>

                    {/* Mostrar botón '+' N se muestra en las ofertas grandes */}
                    {variant !== 'sales' && (
                        <button 
                            class="btn-add-circle border-radius-full box-flex items-center justify-center cursor-pointer"
                            onClick={handleAddClick}
                            aria-label={`Añadir ${product.name} al carrito`}
                        >
                            <span class="plus-icon">+</span>
                        </button>
                    )}
                </div>
            </div>
        </article>
    );
};