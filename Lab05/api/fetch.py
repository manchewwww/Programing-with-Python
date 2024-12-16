# api/fetch.py
import aiohttp
import asyncio
from typing import List, Dict

API_URL = "https://api.themoviedb.org/3/trending/{media_type}/{time_window}"
HEADERS = {
    "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiJjZGNhZTFjNzVkNDQwODNlYmZiYjVjZTg0ODIzYjEzZCIsIm5iZiI6MTczNDExOTQ2MC45MTIsInN1YiI6IjY3NWM5MDI0MzA3OTY0ZDAyMGIzNzE2YSIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.7-zMKRGI8P4Loqdi-cdK8HhhJIB3jSl_rsRlZPG0n2A"
}

async def fetch_trending(media_type: str, time_window: str) -> List[Dict]:
    """Fetch trending data from the API."""
    async with aiohttp.ClientSession() as session:
        url = API_URL.format(media_type=media_type, time_window=time_window)
        async with session.get(url, headers=HEADERS) as response:
            if response.status == 200:
                data = await response.json()
                return [
                    {
                        "title": item.get("title") or item.get("name"),
                        "rating": item.get("vote_average", 0.0),
                    }
                    for item in data.get("results", [])
                ]
            else:
                print(f"Error fetching {media_type}: {response.status}")
                return []


async def fetch_all_trending(time_window: str) -> List[Dict]:
    """Fetch both movies and TV shows concurrently."""
    async with aiohttp.ClientSession() as session:
        movies_task = fetch_trending("movie", time_window)
        tv_task = fetch_trending("tv", time_window)
        movies, tv_shows = await asyncio.gather(movies_task, tv_task)
        return movies + tv_shows
