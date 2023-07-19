import React, { useState } from 'react';
import { Link } from 'react-router-dom';
import './SearchResults.css';

function SearchResults({ results }) {
    const [currentPage, setCurrentPage] = useState(1);
    const [resultsPerPage] = useState(10);

    const indexOfLastResult = currentPage * resultsPerPage;
    const indexOfFirstResult = indexOfLastResult - resultsPerPage;
    const currentResults = results.slice(indexOfFirstResult, indexOfLastResult);

    const paginate = pageNumber => setCurrentPage(pageNumber);

    const pageNumbers = [];
    for (let i = 1; i <= Math.ceil(results.length / resultsPerPage); i++) {
        pageNumbers.push(i);
    }

    return (
        <div className="results-container">
            {currentResults.map((result) => (
                <div key={result.id} className="result-card">
                    <h2><Link to={`/episode/${result.podcast_id}`}>{result.title}</Link></h2> {/* Adjusted the link and title */}
                    <p>{result.date}</p>
                </div>
            ))}
            <div className="pagination">
                {pageNumbers.map(number => (
                    <button key={number} onClick={() => paginate(number)}>
                        {number}
                    </button>
                ))}
            </div>
        </div>
    );
}

export default SearchResults;
