import React from 'react';
import Search from './Search';

function HomePage({ onSearch }) {
  return (
    <div>
      <Search onSearch={onSearch} />
    </div>
  );
}

export default HomePage;