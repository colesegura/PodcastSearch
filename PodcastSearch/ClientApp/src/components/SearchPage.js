import React, { useState } from 'react';
import Search from './Search';

function ParentComponent() {
    const [results, setResults] = useState([]);

    const handleSearch = (results) => {
        setResults(results);
    };

    return (
        <div>
            <Search onSearch={handleSearch} />
            {/* Display the search results here */}
        </div>
    );
}

export default ParentComponent;

