import React, { useState, useEffect } from 'react';
import { SearchBar } from './SearchBar';
import { ProductGrid } from './ProductGrid';

export default function CatalogRoot() {
    const [products, setProducts] = useState([]);
    const [categories, setCategories] = useState([]);
    const [error, setError] = useState(false);

    const fetchProducts = async () => {
        try {
            const response = await fetch('/products/');
            if (!response.ok) throw new Error('Error en fetch api');
            const data = await response.json();
            setProducts(data);
        } catch (error) {
            console.error(error);
            setError(true);
        }
    };

    const fetchCategories = async () => {
        try {
            const response = await fetch('/products/categories/');
            if (!response.ok) throw new Error('Error en fetch api');
            const data = await response.json();
            setCategories(data);
        } catch (error) {
            console.error(error);
            setError(true);
        }
    };

    useEffect(() => {
        fetchProducts();
        fetchCategories();
    }, []);

    const saleProducts = products.filter(p => p.on_sale === true);
    const prominentsProducts = products.filter(p => p.prominent === true);
    if (error) return <p className="text-danger pad-400">Error al cargar el catálogo.</p>;

    return (
        <div className="catalog-container">
            {/* Barra buscador */}
            <SearchBar categories={categories} />
            
            {/* fertas */}
            <section className="catalog-section gap-top-500">
                <h2 className="section-title text-500 weight-bold uppercase gap-bottom-300">Ofertas</h2>
                <ProductGrid layout="sales" products={saleProducts} />
            </section>

            {/*  Destacados */}
            <section className="catalog-section gap-top-500">
                <h2 className="section-title text-500 weight-bold uppercase gap-bottom-300">Destacados</h2>
                <ProductGrid layout="prominents" products={prominentsProducts} />
            </section>

            {/* Categorías Dinámicas */}
            <section className="catalog-section gap-top-500">
                <h2 className="section-title text-500 weight-bold uppercase gap-bottom-400">Categorías</h2>
                {categories.map(c => (
                    <div key={c.id} className="category-block gap-bottom-500">
                        <h3 className="category-subtitle text-400 weight-medium capitalize gap-bottom-200">
                            {c.name}
                        </h3>
                        <ProductGrid 
                            layout="standard" 
                            products={products.filter(p => p.categories && p.categories.includes(c.id))} 
                        />
                    </div>
                ))}
            </section>
        </div>
    );
}