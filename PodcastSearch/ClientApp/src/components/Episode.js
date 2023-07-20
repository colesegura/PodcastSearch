import React from 'react';
import { Link } from 'react-router-dom';
import './Episode.css';

function Episode({ episode }) {
    return (
        <div className="episode-container">
            <h2>{episode.title}</h2>
            <p>{episode.transcript}</p>
            <p><strong>Podcast:</strong> {episode.podcast}</p>
            <p><strong>Date:</strong> {episode.date}</p>
            <p><strong>Spotify:</strong> <a href={episode.spotify} target="_blank" rel="noreferrer">Listen on Spotify</a></p>
            <p><strong>Apple:</strong> <a href={episode.apple} target="_blank" rel="noreferrer">Listen on Apple Podcasts</a></p>
            <p><strong>YouTube:</strong> <a href={episode.youtube} target="_blank" rel="noreferrer">Watch on YouTube</a></p>
            <Link to="/results">Back to Results</Link>
        </div>
    );
}

export default Episode;
