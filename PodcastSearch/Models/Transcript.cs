namespace PodcastSearch.Models
{
    public class Transcript
    {
        public int Id { get; set; }
        public string Text { get; set; }

        // Foreign key for Episode
        public int EpisodeId { get; set; }

        // Navigation property
        public Episode Episode { get; set; }
    }
}
