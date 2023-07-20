using Microsoft.EntityFrameworkCore;

namespace PodcastSearch.Models
{
    public class PodcastDbContext : DbContext
    {
        public PodcastDbContext(DbContextOptions<PodcastDbContext> options)
            : base(options)
        {
        }

        public DbSet<Transcripts> Transcripts { get; set; }
    }
}
