import React from 'react';

export const SearchBar = ({ categories }) => {
    return (
        <div className="search-bar-wrapper bg-white border-radius-md box-shadow pad-300 gap-bottom-500">
            <div className="search-input-container position-relative box-flex items-center">
                <i className="fa-solid fa-magnifying-glass search-icon position-absolute text-muted" style={{ left: '15px' }}></i>
                <input 
                    type="text" 
                    placeholder="Buscar producto..." 
                    className="search-input width-full border-radius-sm border pad-200 text-200"
                    style={{ paddingLeft: '45px' }}
                />
            </div>
        </div>
    );
};