import React, { useState } from 'react';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import HomePage from './components/HomePage';
import Episode from './components/Episode';
import SearchResults from './components/SearchResults';

function App() {
  const [podcasts, setPodcasts] = useState([
    {
      id: 1,
      title: 'Dr. Jeffrey Goldberg: How to Improve Your Eye Health & Offset Vision Loss',
      transcript: 'This is a placeholder transcript for the Dr. Jeffrey Goldberg episode.',
      podcast: 'Huberman Lab',
      date: '2022-01-01',
      spotify: 'https://open.spotify.com/show/7f519d3421415d09fa6a0176743e5c4a',
      apple: 'https://podcasts.apple.com/us/podcast/huberman-lab/id1545953110',
      youtube: 'https://www.youtube.com/channel/UC2D2CMWXMOVWx7giW1n3LIg'
    },
    {
      id: 2,
      title: 'Tim Ferriss: How to Learn Better & Create Your Best Future',
      transcript: 'This is a placeholder transcript for the Tim Ferriss episode.',
      podcast: 'Huberman Lab',
      date: '2022-02-01',
      spotify: 'https://open.spotify.com/show/7f519d3421415d09fa6a0176743e5c4a',
      apple: 'https://podcasts.apple.com/us/podcast/huberman-lab/id1545953110',
      youtube: 'https://www.youtube.com/channel/UC2D2CMWXMOVWx7giW1n3LIg'
    },
    {
      id: 3,
      title: 'The Science of MDMA & Its Therapeutic Uses: Benefits & Risks',
      transcript: 'This is a placeholder transcript for the MDMA episode.',
      podcast: 'Huberman Lab',
      date: '2022-03-01',
      spotify: 'https://open.spotify.com/show/7f519d3421415d09fa6a0176743e5c4a',
      apple: 'https://podcasts.apple.com/us/podcast/huberman-lab/id1545953110',
      youtube: 'https://www.youtube.com/channel/UC2D2CMWXMOVWx7giW1n3LIg'
    },
    {
      id: 4,
      title: 'Dr. Immordino-Yang: How Emotions & Social Factors Impact Learning',
      transcript: 'This is a placeholder transcript for the Dr. Immordino-Yang episode.',
      podcast: 'Huberman Lab',
      date: '2022-04-01',
      spotify: 'https://open.spotify.com/show/7f519d3421415d09fa6a0176743e5c4a',
      apple: 'https://podcasts.apple.com/us/podcast/huberman-lab/id1545953110',
      youtube: 'https://www.youtube.com/channel/UC2D2CMWXMOVWx7giW1n3LIg'
    },
  ]);
  const [results, setResults] = useState([]);

  const handleSearch = (searchTerm, podcast, startDate, endDate, sort) => {
    const searchResults = podcasts.filter(p => 
      p.title.toLowerCase().includes(searchTerm.toLowerCase()) ||
      p.transcript.toLowerCase().includes(searchTerm.toLowerCase())
    );
    setResults(searchResults);
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
