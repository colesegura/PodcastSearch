using System;

namespace PodcastSearch.Models
{
    public class Episode
    {
        public int Id { get; set; }
        public string Title { get; set; }
        public DateTime Date { get; set; }

        // Foreign key for Podcast
        public int PodcastId { get; set; }

        // Navigation properties
        public Podcast Podcast { get; set; }
        public Transcript Transcript { get; set; }
    }
}
