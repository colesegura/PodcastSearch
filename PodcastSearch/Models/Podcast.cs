using System.Collections.Generic;

namespace PodcastSearch.Models
{
    public class Podcast
    {
        public int Id { get; set; }
        public string Title { get; set; }
        public string Author { get; set; }
        public string Description { get; set; }

        // Navigation property
        public ICollection<Episode> Episodes { get; set; }
    }
}
