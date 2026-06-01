import React, { useState, useEffect } from 'react';
import {SearchBar} from './SearchBar';
import {ProductGrid} from './ProductGrid';

export default function CatalogRoot(){
    const [products, setProducts] = useState([]);
    const [categories, setCategories] = useState([]);
    const [error, setError] = useState(false);

    const fetchProducts = async () => {
        try{
            const response = await fetch('/products/')
            if(!response.ok) throw new Error('Error en fetch api')
            const data = await response.json()
            console.log(data)
            setProducts(data)
        }catch(error){
            console.error(error)
            setError(true);
        }
    }

    const fetchCategories = async () => {
        try{
            const response = await fetch('/products/categories/')
            if(!response.ok) throw new Error('Error en fetch api')
            const data = await response.json()
            setCategories(data)
        }catch(error){
            setError(true);
        }
    }

    useEffect(() => {
        fetchProducts();
        fetchCategories();
    }, []);

    const saleProducts = products.filter(p => p.on_sale === true)
    const prominentsProducts = products.filter(p => p.prominent === true)

    return (
        <>
            <SearchBar categories={categories}/>
            <h2>Ofertas</h2>
            <ProductGrid layout="sales" products={saleProducts}/>
            <h2>Destacados</h2>
            <ProductGrid layout="prominents" products={prominentsProducts}/>
            <h2>Categorias</h2>
            {categories.map(c => (
                <div key={c.id}>
                    <p>{c.name}</p>
                    <ProductGrid products={products.filter(p => p.category === c.id)}/>
                </div>
            ))}
        </>
    )
}