import React, { useState } from 'react';
import Search from './Search';
import SearchResults from './SearchResults';

function ParentComponent() {
    const [results, setResults] = useState([]);

    const handleSearch = (results) => {
        setResults(results);
    };

    return (
        <div>
            <Search onSearch={handleSearch} />
            <SearchResults results={results} />
        </div>
    );
}

export default ParentComponent;
