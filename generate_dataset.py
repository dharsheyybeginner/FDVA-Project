"""Generate reproducible, synthetic demonstration data for the CinemaScope FDVA project.

All titles and all numeric values are generated for learning/demo use. They are NOT
claims about real films, real audience ratings, real budgets, real box-office revenue,
or real streaming-platform availability.

Uses Python standard library only. Run with: python scripts/generate_dataset.py
"""
from __future__ import annotations
import csv
import random
from datetime import date, timedelta
from pathlib import Path

SEED = 20261025
ROOT = Path(__file__).resolve().parents[1]
DATA_DIR = ROOT / "data"
RNG = random.Random(SEED)

GENRES = ["Action", "Adventure", "Animation", "Comedy", "Crime", "Documentary", "Drama", "Fantasy", "Horror", "Mystery", "Romance", "Sci-Fi", "Thriller", "Family"]
GENRE_WEIGHTS = [13, 7, 4, 10, 7, 2, 15, 5, 5, 5, 8, 6, 10, 3]

TAMIL_FIRST = ["Nizhal", "Mazhai", "Vaanam", "Minnal", "Uyir", "Kadal", "Iravu", "Vidiyal", "Anbu", "Aazhi", "Thooral", "Oli", "Neruppu", "Payanam", "Kanavu", "Marupakkam", "Oru Pudhiya", "Iruvizhi", "Puyal", "Nilavu", "Thendral", "Vettai", "Nenjil", "Mounam", "Pudhir", "Sutrula", "Adanga", "Kaalam", "Veeran", "Siragugal"]
TAMIL_SECOND = ["Vaasal", "Kural", "Paadhai", "Vettai", "Osai", "Neram", "Payணம்".replace("ணம்", "anam"), "Kadhai", "Thee", "Thuli", "Mugam", "Suvadugal", "Saaral", "Nilal", "Vizhigal", "Pookkal", "Sakkaram", "Ragasiyam", "Thadam", "Ulagam", "Puyal", "Vidhi", "Meendum", "Vaanavil", "Kanakku", "Thiruppam", "Aattam", "Saatchi", "Deepam", "Ellai"]
GLOBAL_FIRST = ["The Last", "Silent", "Crimson", "Hidden", "Beyond", "Midnight", "Golden", "Broken", "Forgotten", "Infinite", "Neon", "Shattered", "Fading", "Wild", "Frozen", "Distant", "Secret", "Paper", "Final", "Electric", "Rising", "Dark", "Lone", "Velvet", "Parallel", "Scarlet", "Silver", "Empty", "Burning", "Starlit", "Echoes of", "Before the"]
GLOBAL_SECOND = ["Horizon", "Promise", "Kingdom", "Signal", "Voyage", "Garden", "Witness", "Reckoning", "Orbit", "River", "Memory", "Empire", "Mirage", "Lantern", "Station", "Crown", "Theory", "Storm", "Archive", "Labyrinth", "Passenger", "Atlas", "Odyssey", "Frequency", "Shadow", "Frontier", "Paradox", "Summit", "Machine", "Wildflowers", "Moon", "City", "Code", "Silence", "Sparrow", "Afterglow"]

COUNTRY_LANG = [
    ("United States", "English"), ("United Kingdom", "English"), ("India", "Hindi"),
    ("India", "Telugu"), ("India", "Malayalam"), ("South Korea", "Korean"),
    ("Japan", "Japanese"), ("France", "French"), ("Spain", "Spanish"),
    ("China", "Mandarin"), ("Germany", "German"), ("Mexico", "Spanish"),
    ("Italy", "Italian"), ("Brazil", "Portuguese"), ("Australia", "English"),
]
PLATFORMS = ["Netflix", "Prime Video", "Disney+ Hotstar", "ZEE5", "Sun NXT", "Apple TV+", "Crunchyroll"]
CERTIFICATIONS = ["U", "U/A 7+", "U/A 13+", "U/A 16+", "A", "TV-PG", "TV-14", "TV-MA"]
TV_PREFIX = ["City of", "Inside", "The Daily", "Letters from", "Lessons in", "Road to", "House of", "Secrets of", "Small Town", "Project"]
TV_CORE = ["Tomorrow", "Monsoon", "Orchid", "Zero", "Harbour", "Summer", "Juniper", "Orbit", "Midnight", "Bluebird", "Northstar", "Redwood", "Lotus", "Station", "Tomorrow", "Parallel"]


def weighted_genre() -> str:
    return RNG.choices(GENRES, weights=GENRE_WEIGHTS, k=1)[0]


def unique_title(industry: str, index: int, used: set[str]) -> str:
    if industry == "Tamil":
        first = RNG.choice(TAMIL_FIRST)
        second = RNG.choice(TAMIL_SECOND)
        title = f"{first} {second}"
        if RNG.random() < 0.22:
            title = f"{title} {RNG.choice(['Chapter', 'Ragasiyam', 'Returns', '2040', 'Part II'])}"
    else:
        title = f"{RNG.choice(GLOBAL_FIRST)} {RNG.choice(GLOBAL_SECOND)}"
        if RNG.random() < 0.18:
            title = f"{title}: {RNG.choice(GLOBAL_SECOND)}"
    base = title
    suffix = 2
    while title.lower() in used:
        title = f"{base} {suffix}"
        suffix += 1
    used.add(title.lower())
    return title


def random_date_for_year(year: int) -> str:
    start = date(year, 1, 1)
    days = 365 if year % 4 != 0 else 366
    return (start + timedelta(days=RNG.randrange(days))).isoformat()


def make_movie(movie_id: str, title: str, industry: str, language: str, country: str) -> dict:
    year = RNG.randint(2000, 2025)
    genre = weighted_genre()
    runtime = max(75, min(210, int(RNG.gauss(128 if industry == "Tamil" else 116, 20))))
    rating = round(max(3.1, min(9.5, RNG.gauss(6.65 if industry == "Tamil" else 6.55, 1.05))), 1)
    vote_count = int(max(25, min(500000, RNG.lognormvariate(7.6 if industry == "Tamil" else 8.1, 1.25))))
    if industry == "Tamil":
        budget = int(RNG.uniform(200_000, 25_000_000) / 10_000) * 10_000
        gross_multiplier = RNG.lognormvariate(0.30 + (rating - 6.5) * 0.14, 0.58)
    else:
        budget = int(RNG.uniform(700_000, 220_000_000) / 100_000) * 100_000
        gross_multiplier = RNG.lognormvariate(0.22 + (rating - 6.5) * 0.12, 0.72)
    revenue_value = max(50_000, int(budget * gross_multiplier / 10_000) * 10_000)
    # Missing values emulate incomplete public movie metadata; these are not zeros.
    if RNG.random() < 0.07:
        budget_value = ""
    else:
        budget_value = budget
    if RNG.random() < (0.15 if industry == "Tamil" else 0.12):
        revenue = ""
    else:
        revenue = revenue_value
    if RNG.random() < 0.06:
        audience_rating = ""
    else:
        audience_rating = rating
    return {
        "MovieID": movie_id,
        "Title": title,
        "ReleaseYear": year,
        "ReleaseDate": random_date_for_year(year),
        "Industry": industry,
        "Language": language,
        "Country": country,
        "Genre": genre,
        "RuntimeMin": runtime,
        "AudienceRating": audience_rating,
        "VoteCount": vote_count,
        "BudgetUSD": budget_value,
        "RevenueUSD": revenue,
        "OTTReleaseFlag": "Yes" if RNG.random() < (0.28 if industry == "Tamil" else 0.36) else "No",
        "DataNature": "Synthetic demo data",
    }


def generate_movies() -> list[dict]:
    movies: list[dict] = []
    used: set[str] = set()
    for i in range(1, 221):
        title = unique_title("Tamil", i, used)
        movies.append(make_movie(f"TAM{i:04d}", title, "Tamil", "Tamil", "India"))
    for i in range(1, 481):
        country, language = RNG.choice(COUNTRY_LANG)
        title = unique_title("Worldwide", i, used)
        movies.append(make_movie(f"GLB{i:04d}", title, "Worldwide", language, country))
    movies.sort(key=lambda row: (row["ReleaseYear"], row["MovieID"]))
    return movies


def generate_ott(movies: list[dict]) -> list[dict]:
    output: list[dict] = []
    ott_id = 1
    # A subset of the movie IDs appears on simulated streaming catalogues, sometimes on multiple platforms.
    for movie in movies:
        if RNG.random() > 0.62:
            continue
        platform_count = 1 if RNG.random() < 0.78 else 2
        chosen_platforms = RNG.sample(PLATFORMS, platform_count)
        for platform in chosen_platforms:
            add_start = date(max(2015, movie["ReleaseYear"]), 1, 1)
            add_end = date(2026, 10, 1)
            span = max(1, (add_end - add_start).days)
            added = add_start + timedelta(days=RNG.randrange(span))
            output.append({
                "OTTID": f"OTT{ott_id:05d}",
                "MovieID": movie["MovieID"],
                "Title": movie["Title"],
                "ContentType": "Movie",
                "Language": movie["Language"],
                "Country": movie["Country"],
                "ReleaseYear": movie["ReleaseYear"],
                "Genre": movie["Genre"],
                "Platform": platform,
                "DateAdded": added.isoformat(),
                "ContentRating": RNG.choice(CERTIFICATIONS),
                "DurationMin": movie["RuntimeMin"],
                "Seasons": "",
                "AudienceRating": movie["AudienceRating"],
                "AvailabilityStatus": "Simulated listing",
                "DataNature": "Synthetic demo data",
            })
            ott_id += 1
    # Add a separate set of synthetic TV shows (these have no MovieID relationship).
    tv_used: set[str] = set()
    for i in range(1, 141):
        title = f"{RNG.choice(TV_PREFIX)} {RNG.choice(TV_CORE)}"
        if title.lower() in tv_used:
            title += f" {i}"
        tv_used.add(title.lower())
        country, language = RNG.choice(COUNTRY_LANG)
        year = RNG.randint(2005, 2025)
        add_start = date(max(2015, year), 1, 1)
        add_end = date(2026, 10, 1)
        span = max(1, (add_end - add_start).days)
        added = add_start + timedelta(days=RNG.randrange(span))
        for platform in RNG.sample(PLATFORMS, 1 if RNG.random() < 0.8 else 2):
            output.append({
                "OTTID": f"OTT{ott_id:05d}",
                "MovieID": "",
                "Title": title,
                "ContentType": "TV Show",
                "Language": language,
                "Country": country,
                "ReleaseYear": year,
                "Genre": weighted_genre(),
                "Platform": platform,
                "DateAdded": added.isoformat(),
                "ContentRating": RNG.choice(CERTIFICATIONS),
                "DurationMin": "",
                "Seasons": RNG.randint(1, 8),
                "AudienceRating": round(max(3.0, min(9.6, RNG.gauss(6.8, 1.0))), 1),
                "AvailabilityStatus": "Simulated listing",
                "DataNature": "Synthetic demo data",
            })
            ott_id += 1
    output.sort(key=lambda row: (row["Platform"], row["ContentType"], row["Title"]))
    return output


def write_csv(path: Path, rows: list[dict]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    if not rows:
        raise ValueError(f"No rows to write to {path}")
    with path.open("w", encoding="utf-8-sig", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=list(rows[0].keys()), extrasaction="ignore")
        writer.writeheader()
        writer.writerows(rows)


def write_dictionary() -> None:
    rows = [
        ("movies.csv", "MovieID", "Unique synthetic movie identifier; TAM = Tamil demo record, GLB = worldwide demo record."),
        ("movies.csv", "Title", "Fictional/generated title for demonstration; may resemble existing titles by coincidence."),
        ("movies.csv", "ReleaseYear", "Simulated release year from 2000 through 2025."),
        ("movies.csv", "ReleaseDate", "Generated date within ReleaseYear; not an actual release date."),
        ("movies.csv", "Industry", "Tamil or Worldwide grouping used in the dashboard."),
        ("movies.csv", "Language", "Synthetic language label."),
        ("movies.csv", "Country", "Synthetic production-country label."),
        ("movies.csv", "Genre", "One generated genre label per movie."),
        ("movies.csv", "RuntimeMin", "Generated runtime in minutes."),
        ("movies.csv", "AudienceRating", "Simulated 0-10 rating; blank means missing, not zero."),
        ("movies.csv", "VoteCount", "Simulated audience vote count."),
        ("movies.csv", "BudgetUSD", "Simulated budget in US dollars; blanks are missing values."),
        ("movies.csv", "RevenueUSD", "Simulated gross revenue in US dollars; blanks are missing values."),
        ("movies.csv", "OTTReleaseFlag", "Simulated Yes/No indicator for demo filtering only."),
        ("movies.csv", "DataNature", "Marks every row as synthetic demo data."),
        ("ott_catalog.csv", "OTTID", "Unique synthetic platform-listing row ID."),
        ("ott_catalog.csv", "MovieID", "Links to movies.csv for catalogued movies; blank for generated TV shows."),
        ("ott_catalog.csv", "ContentType", "Movie or TV Show."),
        ("ott_catalog.csv", "Platform", "Simulated platform association; not a claim of actual availability."),
        ("ott_catalog.csv", "DateAdded", "Generated catalogue-added date, not an actual platform date."),
        ("ott_catalog.csv", "ContentRating", "Simulated viewing certificate label; not an audience rating."),
        ("ott_catalog.csv", "DurationMin", "Runtime for movie listings; blank for TV shows."),
        ("ott_catalog.csv", "Seasons", "Generated season count for TV shows; blank for movies."),
        ("ott_catalog.csv", "AudienceRating", "Simulated audience rating on a 0-10 scale; distinct from ContentRating."),
        ("ott_catalog.csv", "AvailabilityStatus", "Always labeled Simulated listing to avoid implying real platform availability."),
        ("both", "DataNature", "Synthetic demo data: all records and values are generated for this project."),
    ]
    with (DATA_DIR / "data_dictionary.csv").open("w", encoding="utf-8-sig", newline="") as f:
        w = csv.writer(f)
        w.writerow(["File", "Column", "Definition"])
        w.writerows(rows)


def main() -> None:
    DATA_DIR.mkdir(parents=True, exist_ok=True)
    movies = generate_movies()
    ott = generate_ott(movies)
    write_csv(DATA_DIR / "movies.csv", movies)
    write_csv(DATA_DIR / "ott_catalog.csv", ott)
    write_dictionary()
    print(f"Generated {len(movies):,} movies: {sum(m['Industry']=='Tamil' for m in movies):,} Tamil and {sum(m['Industry']=='Worldwide' for m in movies):,} worldwide.")
    print(f"Generated {len(ott):,} simulated OTT listing rows.")
    print(f"Output folder: {DATA_DIR}")
    print("Reminder: all generated titles, ratings, budgets, revenue and platform listings are synthetic demo data.")

if __name__ == "__main__":
    main()
