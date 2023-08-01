namespace PodcastSearch.Models
{
    public class Transcripts
    {
        public string? Id { get; set; }
        public int? PodcastId { get; set; }
        public string? Title { get; set; }
        public DateTimeOffset? Date { get; set; }
        public string? Transcript { get; set; }
        public string? EpisodeId { get; set; }
    }

}
