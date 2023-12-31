﻿using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;
using Microsoft.AspNetCore.Http;
using Microsoft.AspNetCore.Mvc;
using Microsoft.EntityFrameworkCore;
using PodcastSearch.Models;
using Azure.Search.Documents.Models;
using Microsoft.Extensions.Logging;

namespace PodcastSearch.Controllers
{
    [Route("api/[controller]")]
    [ApiController]
    public class TranscriptsController : ControllerBase
    {
        private readonly PodcastDbContext _context;
        private readonly SearchService _searchService;
        private readonly ILogger<TranscriptsController> _logger;  // Add this line

        public TranscriptsController(PodcastDbContext context, SearchService searchService, ILogger<TranscriptsController> logger)
        {
            _context = context;
            _searchService = searchService;
            _logger = logger;
        }

        private string BuildFilter(int? podcastId, DateTimeOffset? startDate, DateTimeOffset? endDate, string? episodeId)
        {
            List<string> filters = new List<string>();

            if (podcastId.HasValue)
            {
                filters.Add($"podcast_id eq {podcastId.Value}");
            }

            if (startDate.HasValue)
            {
                filters.Add($"date ge {startDate.Value.ToString("o")}");
            }

            if (endDate.HasValue)
            {
                filters.Add($"date le {endDate.Value.ToString("o")}");
            }

            if (!string.IsNullOrEmpty(episodeId))
            {
                filters.Add($"episode_id eq '{episodeId}'");
            }

            // Add more filters as needed.

            return string.Join(" and ", filters);
        }


        // GET: api/Transcripts
        [HttpGet]
        public async Task<ActionResult<IEnumerable<Transcripts>>> GetTranscripts()
        {
            if (_context.Transcripts == null)
            {
                return NotFound();
            }
            return await _context.Transcripts.ToListAsync();
        }

        // GET: api/Transcripts/5
        [HttpGet("{id}")]
        public async Task<ActionResult<Transcripts>> GetTranscript(string id)
        {
            if (_context.Transcripts == null)
            {
                return NotFound();
            }
            var transcript = await _context.Transcripts.FindAsync(id);

            if (transcript == null)
            {
                return NotFound();
            }

            return transcript;
        }

        // PUT: api/Transcripts/5
        // To protect from overposting attacks, see https://go.microsoft.com/fwlink/?linkid=2123754
        [HttpPut("{id}")]
        public async Task<IActionResult> PutTranscript(string id, Transcripts transcript)
        {
            if (id != transcript.Id)
            {
                return BadRequest();
            }

            _context.Entry(transcript).State = EntityState.Modified;

            try
            {
                await _context.SaveChangesAsync();
            }
            catch (DbUpdateConcurrencyException)
            {
                if (!TranscriptExists(id))
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

        // POST: api/Transcripts
        // To protect from overposting attacks, see https://go.microsoft.com/fwlink/?linkid=2123754
        [HttpPost]
        public async Task<ActionResult<Transcripts>> PostTranscript(Transcripts transcript)
        {
            if (_context.Transcripts == null)
            {
                return Problem("Entity set 'PodcastDbContext.Transcripts'  is null.");
            }
            _context.Transcripts.Add(transcript);
            await _context.SaveChangesAsync();

            return CreatedAtAction("GetTranscript", new { id = transcript.Id }, transcript);
        }

        // DELETE: api/Transcripts/5
        [HttpDelete("{id}")]
        public async Task<IActionResult> DeleteTranscript(string id)
        {
            if (_context.Transcripts == null)
            {
                return NotFound();
            }
            var transcript = await _context.Transcripts.FindAsync(id);
            if (transcript == null)
            {
                return NotFound();
            }

            _context.Transcripts.Remove(transcript);
            await _context.SaveChangesAsync();

            return NoContent();
        }

        private bool TranscriptExists(string id)
        {
            return (_context.Transcripts?.Any(e => e.Id == id)).GetValueOrDefault();
        }

        // GET: api/Transcripts/search?query={query}
        [HttpGet("search")]
        public async Task<ActionResult<SearchResults<SearchDocument>>> Search(string query, string? podcastId, string? startDate = null, string? endDate = null, string? episodeId = null)
        {
            try
            {
                int? podcastIdInt = null;
                if (!string.IsNullOrEmpty(podcastId))
                {
                    if (int.TryParse(podcastId, out int parsedPodcastId))
                    {
                        podcastIdInt = parsedPodcastId;
                    }
                    else
                    {
                        // Log error and return bad request if podcastId can't be parsed to int
                        _logger.LogError($"Error parsing podcastId: {podcastId}");
                        return BadRequest("Invalid podcastId parameter");
                    }
                }

                DateTimeOffset? startDateDate = null;
                if (!string.IsNullOrEmpty(startDate))
                {
                    if (!DateTimeOffset.TryParse(startDate, out DateTimeOffset parsedStartDate))
                    {
                        // Log error and return bad request if startDate can't be parsed to DateTimeOffset
                        Console.WriteLine($"Error parsing startDate: {startDate}");
                        return BadRequest("Invalid startDate parameter");
                    }
                    startDateDate = parsedStartDate;
                }

                DateTimeOffset? endDateDate = null;
                if (!string.IsNullOrEmpty(endDate))
                {
                    if (!DateTimeOffset.TryParse(endDate, out DateTimeOffset parsedEndDate))
                    {
                        // Log error and return bad request if endDate can't be parsed to DateTimeOffset
                        Console.WriteLine($"Error parsing endDate: {endDate}");
                        return BadRequest("Invalid endDate parameter");
                    }
                    endDateDate = parsedEndDate;
                }

                string filter = BuildFilter(podcastIdInt, startDateDate, endDateDate, episodeId);
                var results = await _searchService.SearchAsync(query, filter);
                return Ok(results.GetResults());
            }
            catch (Exception ex)
            {
                _logger.LogError(ex, "Error occurred in Search");
                return StatusCode(500, "A server error occurred");
            }
        }


    }
}
