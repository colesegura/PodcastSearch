using Microsoft.EntityFrameworkCore;

namespace PodcastSearch.Models
{
    public class PodcastDbContext : DbContext
    {
        public PodcastDbContext(DbContextOptions<PodcastDbContext> options)
            : base(options)
        {
        }

        public DbSet<Podcast> Podcasts { get; set; }
        public DbSet<Episode> Episodes { get; set; }
        public DbSet<Transcript> Transcripts { get; set; }
    }
}
