using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;
using Microsoft.AspNetCore.Http;
using Microsoft.AspNetCore.Mvc;
using Microsoft.EntityFrameworkCore;
using PodcastSearch.Models;

namespace PodcastSearch.Controllers
{
    [Route("api/[controller]")]
    [ApiController]
    public class PodcastsController : ControllerBase
    {
        private readonly PodcastDbContext _context;

        public PodcastsController(PodcastDbContext context)
        {
            _context = context;
        }

        // GET: api/Podcasts
        [HttpGet]
        public async Task<ActionResult<IEnumerable<Podcast>>> GetPodcasts()
        {
          if (_context.Podcasts == null)
          {
              return NotFound();
          }
            return await _context.Podcasts.ToListAsync();
        }

        // GET: api/Podcasts/5
        [HttpGet("{id}")]
        public async Task<ActionResult<Podcast>> GetPodcast(int id)
        {
          if (_context.Podcasts == null)
          {
              return NotFound();
          }
            var podcast = await _context.Podcasts.FindAsync(id);

            if (podcast == null)
            {
                return NotFound();
            }

            return podcast;
        }

        // PUT: api/Podcasts/5
        // To protect from overposting attacks, see https://go.microsoft.com/fwlink/?linkid=2123754
        [HttpPut("{id}")]
        public async Task<IActionResult> PutPodcast(int id, Podcast podcast)
        {
            if (id != podcast.Id)
            {
                return BadRequest();
            }

            _context.Entry(podcast).State = EntityState.Modified;

            try
            {
                await _context.SaveChangesAsync();
            }
            catch (DbUpdateConcurrencyException)
            {
                if (!PodcastExists(id))
                {
                    return NotFound();
                }
                else
                {
                    throw;
                }
            }

            return NoContent();
        }

        // POST: api/Podcasts
        // To protect from overposting attacks, see https://go.microsoft.com/fwlink/?linkid=2123754
        [HttpPost]
        public async Task<ActionResult<Podcast>> PostPodcast(Podcast podcast)
        {
          if (_context.Podcasts == null)
          {
              return Problem("Entity set 'PodcastDbContext.Podcasts'  is null.");
          }
            _context.Podcasts.Add(podcast);
            await _context.SaveChangesAsync();

            return CreatedAtAction("GetPodcast", new { id = podcast.Id }, podcast);
        }

        // DELETE: api/Podcasts/5
        [HttpDelete("{id}")]
        public async Task<IActionResult> DeletePodcast(int id)
        {
            if (_context.Podcasts == null)
            {
                return NotFound();
            }
            var podcast = await _context.Podcasts.FindAsync(id);
            if (podcast == null)
            {
                return NotFound();
            }

            _context.Podcasts.Remove(podcast);
            await _context.SaveChangesAsync();

            return NoContent();
        }

        private bool PodcastExists(int id)
        {
            return (_context.Podcasts?.Any(e => e.Id == id)).GetValueOrDefault();
        }
    }
}
