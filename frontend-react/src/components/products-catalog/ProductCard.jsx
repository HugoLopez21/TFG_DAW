import React from "react";

export const ProductCard = ({ product, variant = "standard" }) => {
    
    // Función carrito de compras
    const handleAddClick = () => {
        console.log(`Producto añadido: ${product.name}`);
    };

    return (
        <article className={`product-card-item box-flex border-radius-md bg-white ${variant}-card`}>
            
            {/* Contenedor de la Imagen */}
            <div className="product-image-container box-flex items-center justify-center">
                {product.image ? (
                    <img src={product.image} alt={product.name} className="product-img" />
                ) : (
                    <div className="img-placeholder"><i className="fa-regular fa-image"></i></div>
                )}
            </div>

            {/* Contenedor de Textos e Información */}
            <div className="product-info-container box-flex flex-column justify-between flex-1">
                <div className="product-header">
                    <span className="product-badge text-100 text-muted uppercase tracking-wider block">
                        {variant === 'sales' ? 'Oferta Especial' : ''}
                    </span>
                    <h4 className="product-name text-300 weight-medium gap-top-100">
                        {product.name}
                    </h4>
                </div>

                <div className="product-footer box-flex justify-between items-center gap-top-200">
                    <span className="product-price text-300 weight-bold color-dark">
                        {parseFloat(product.price).toFixed(2)}€
                    </span>

                    {/* Mostrar botón '+' N se muestra en las ofertas grandes */}
                    {variant !== 'sales' && (
                        <button 
                            className="btn-add-circle add-to-cart border-radius-full box-flex items-center justify-center cursor-pointer"
                            onClick={handleAddClick}
                            aria-label={`Añadir ${product.name} al carrito`}
                        >
                            <span className="plus-icon">+</span>
                        </button>
                    )}
                </div>
            </div>
        </article>
    );
};