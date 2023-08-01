import React, { useState } from 'react';
import { useNavigate } from 'react-router-dom';
import axios from 'axios';
import './Search.css';

function Search({ onSearch }) {
    const [searchTerm, setSearchTerm] = useState('');
    const [podcast, setPodcast] = useState('all');
    const [startDate, setStartDate] = useState('');
    const [endDate, setEndDate] = useState('');
    const [sort, setSort] = useState('');
    const [showFilters, setShowFilters] = useState(false); // Added this line
    const navigate = useNavigate();

    const handleSearchChange = (event) => {
        setSearchTerm(event.target.value);
    };

    const handlePodcastChange = (event) => {
        setPodcast(event.target.value);
    };

    const handleStartDateChange = (event) => {
        setStartDate(event.target.value);
    };

    const handleEndDateChange = (event) => {
        setEndDate(event.target.value);
    };

    const handleSortChange = (event) => {
        setSort(event.target.value);
    };

    const search = async (params) => {
        const { searchTerm, podcastId, startDate, endDate, episodeId } = params;
        try {
            const response = await axios.get(`https://dtfhsearch.azurewebsites.net/api/Transcripts/search`, {
                params: {
                    query: searchTerm,
                    podcastId, // Now passing podcastId
                    startDate,
                    endDate,
                    episodeId // Passing episodeId
                }
            });
            return response.data;
        } catch (error) {
            console.error(error);
        }
    }


    const handleSearchSubmit = async (event) => {
        event.preventDefault();
        const results = await search({
            searchTerm,
            podcastId: podcast, // Now treating 'podcast' as 'podcastId'
            startDate,
            endDate,
            episodeId: sort // Now treating 'sort' as 'episodeId'
        });
        onSearch(results);
        navigate('/results');
    };




    const toggleFilters = () => { // Added this function
        setShowFilters(!showFilters);
    };

  return (
    <div className="search-container">
      <h1>Podcast Transcript Search</h1>
      <form onSubmit={handleSearchSubmit} className="search-form">
        <input
          type="text"
          placeholder="Search transcripts"
          value={searchTerm}
          onChange={handleSearchChange}
          className="search-input"
        />
        <button type="submit" className="search-button">&#128269;</button>
      </form>
      <button onClick={toggleFilters} className="filters-button">
        {showFilters ? 'Hide Filters' : 'Show Filters'}
      </button>
      {showFilters && (
        <div className="search-filters">
          <select value={podcast} onChange={handlePodcastChange}>
            <option value="all">All podcasts</option>
            <option value="duncan">Duncan Trussell Family Hour</option>
            {/* Add more options here for other podcasts */}
          </select>
          <input
            type="date"
            value={startDate}
            onChange={handleStartDateChange}
          />
          <input
            type="date"
            value={endDate}
            onChange={handleEndDateChange}
          />
          <select value={sort} onChange={handleSortChange}>
            <option value="">Sort by...</option>
            <option value="date">Date</option>
            <option value="title">Title</option>
          </select>
        </div>
      )}
    </div>
  );
}

export default Search;
