import React, { useState, useEffect } from 'react';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import HomePage from './components/HomePage';
import Episode from './components/Episode';
import SearchResults from './components/SearchResults';
import axios from 'axios';

function App() {
  const [podcasts, setPodcasts] = useState([]);
  const [results, setResults] = useState([]);

    // Fetch data from Azure Cognitive Search when the component mounts
    useEffect(() => {
        const fetchData = async () => {
            const result = await axios.get('/api/Transcripts');
            setPodcasts(result.data);
        };
        fetchData();
    }, []);

    const handleSearch = async (searchTerm, podcast, startDate, endDate, sort) => {
        const result = await axios.get(`/api/Transcripts/search?query=${searchTerm}`);
        setResults(result.data);
    };


  return (
    <Router>
      <div className="App">
        <Routes>
          <Route path="/" element={<HomePage onSearch={handleSearch} />} />
          <Route path="/results" element={<SearchResults results={results} />} />
          <Route path="episode/*" element={<EpisodeRoutes podcasts={podcasts} />} />
        </Routes>
      </div>
    </Router>
  );
}

function EpisodeRoutes({ podcasts }) {
  return (
    <Routes>
      {podcasts.map((podcast) => (
        <Route key={podcast.id} path={`${podcast.id}`} element={<Episode episode={podcast} />} />
      ))}
    </Routes>
  );
}

export default App;
