# CinemaScope — Tamil & Worldwide Cinema + OTT Analytics (Power BI FDVA Project)

## START HERE
This package contains CSV datasets, reproducible Python code, DAX measures, optional Power Query M examples, a Power BI theme, and a mini-project report template.

**Important data note:** All records and all numerical values in this package are **synthetic demo data created for this project**. Movie titles are generated, and ratings, vote counts, budgets, revenues, dates, and OTT-platform listings are simulated. They are not real-world movie facts and must not be presented as actual box-office or streaming availability statistics. The synthetic data lets you practice Power BI end-to-end without scraping or relying on incompatible third-party datasets.

## What's inside

- `data/movies.csv` — 700 synthetic movie records: 220 grouped as Tamil and 480 grouped as Worldwide.
- `data/ott_catalog.csv` — simulated OTT catalogue listings for movies and TV shows across multiple platforms.
- `data/data_dictionary.csv` — column descriptions and data caveats.
- `scripts/generate_dataset.py` — rebuilds the CSV datasets reproducibly using only Python's standard library.
- `dax/CinemaScope_Measures.dax` — DAX measures and calculated columns to create in Power BI.
- `powerquery/Power_Query_Examples.txt` — optional M snippets (adjust the file paths before use).
- `powerbi/CinemaScope_Theme.json` — optional dark cinema-themed report theme.
- `report/FDVA_Report_Template.md` — report outline you can fill in after analyzing your visuals.
- `report/Viva_Questions.md` — short viva preparation questions and answers.

## A. Open the data in Power BI Desktop

1. Extract this ZIP to a folder you can find easily, such as `Documents\CinemaScope_FDVA_PowerBI_Project`.
2. Open **Power BI Desktop**.
3. Choose **Home → Get data → Text/CSV**.
4. Select `data/movies.csv`, then choose **Transform Data**.
5. In Power Query, check the columns and types. Use **Close & Apply**.
6. Repeat **Get data → Text/CSV** for `data/ott_catalog.csv`. Name the query/table `OTT` if Power BI gave it a different name.
7. In Model view, create a relationship from `Movies[MovieID]` (one) to `OTT[MovieID]` (many). Use single-direction filtering from Movies to OTT. The blank MovieID rows represent synthetic TV shows and are expected.
8. Import the theme (optional): **View → Themes → Browse for themes**, then select `powerbi/CinemaScope_Theme.json`.
9. Open `dax/CinemaScope_Measures.dax` and create measures one at a time: select the relevant table, choose **Modeling → New measure**, and paste each formula. For a calculated column, use **Modeling → New column**.
10. Save the Power BI report as `CinemaScope.pbix` on your computer.

**Table naming:** the DAX uses `Movies` and `OTT`. In the Queries pane, rename `movies` to `Movies` and `ott_catalog` to `OTT` (or change the DAX table names to match yours).

## B. Clean/check the imported columns

Most columns are already tidy. Confirm these types in Power Query or Data view:

### Movies table
- `MovieID`, `Title`, `Industry`, `Language`, `Country`, `Genre`, `OTTReleaseFlag`, `DataNature`: Text
- `ReleaseYear`, `RuntimeMin`, `VoteCount`, `BudgetUSD`, `RevenueUSD`: Whole Number
- `ReleaseDate`: Date
- `AudienceRating`: Decimal Number

### OTT table
- `OTTID`, `MovieID`, `Title`, `ContentType`, `Language`, `Country`, `Genre`, `Platform`, `ContentRating`, `AvailabilityStatus`, `DataNature`: Text
- `ReleaseYear`, `DurationMin`, `Seasons`: Whole Number (blank values are expected)
- `DateAdded`: Date
- `AudienceRating`: Decimal Number

Blank budget/revenue/rating values are intentional missing values. Do not replace blanks with zero; that would distort averages and financial totals.

## C. Build the report: recommended pages and visuals

### Page 1 — Cinema Overview
1. Add four **Card** visuals: `[Total Movies]`, `[Average Audience Rating]`, `[Tamil Movie Count]`, `[Worldwide Movie Count]`.
2. Add a **Line chart**: X-axis `Movies[ReleaseYear]`, Y-axis `[Total Movies]`.
3. Add a **Clustered bar chart**: Y-axis `Movies[Genre]`, X-axis `[Average Audience Rating]`.
4. Add a **Donut chart**: Legend `Movies[Industry]`, Values `[Total Movies]`.
5. Add slicers for `Movies[ReleaseYear]`, `Movies[Language]`, and `Movies[Genre]`.

### Page 2 — Movie Performance
1. Add a **Bar chart** for the top-rated movies: Y-axis `Movies[Title]`, X-axis `[Average Audience Rating]`; apply a Top N = 10 visual filter by Average Audience Rating. For a fairer comparison you may also filter `VoteCount` above a minimum you state in the report.
2. Add a **Bar chart**: Y-axis `Movies[Title]`, X-axis `[Total Box Office Revenue USD]`; apply Top N = 10 by revenue.
3. Add a **Scatter chart**: X-axis `Movies[BudgetUSD]`, Y-axis `Movies[RevenueUSD]`, Details `Movies[Title]`, Legend `Movies[Industry]`. Note that values are synthetic USD estimates.
4. Add a **Table** with `Title`, `ReleaseYear`, `Industry`, `Language`, `Genre`, `AudienceRating`, `BudgetUSD`, `RevenueUSD`.
5. Add slicers for `Industry`, `ReleaseYear`, and `Genre`.

### Page 3 — OTT Insights
1. Add cards for `[OTT Listing Rows]`, `[OTT Unique Titles]`, `[OTT Movie Listings]`, and `[OTT TV Show Listings]`.
2. Add a **Donut chart**: Legend `OTT[ContentType]`, Values `[OTT Listing Rows]`.
3. Add a **Bar chart**: Y-axis `OTT[Platform]`, X-axis `[OTT Listing Rows]`.
4. Add a **Bar chart**: Y-axis `OTT[Genre]`, X-axis `[OTT Listing Rows]`.
5. Add a **Line chart**: X-axis `OTT[ReleaseYear]`, Y-axis `[OTT Listing Rows]`.
6. Add slicers for `OTT[Platform]`, `OTT[Country]`, `OTT[ReleaseYear]`, and `OTT[ContentType]`.

Important interpretation note: OTT is modelled as one row per title/platform listing. A movie available on two simulated platforms creates two listing rows. Use `OTT Listing Rows` to count platform listings and `OTT Unique Titles` to count distinct titles. The platform names and availability entries are simulated, not factual.

## D. Run or regenerate the datasets (optional)

Python is **not required** to use the already-provided CSV files. To regenerate them:

1. Install Python 3 if needed.
2. Open a terminal/Command Prompt in the extracted project folder.
3. Run `python scripts/generate_dataset.py`.
4. The program overwrites the three CSVs in `data/` with the same reproducible dataset using a fixed random seed.

On Windows, you can also double-click `run_generator.bat`.

## E. Submission checklist

- [ ] Import both CSV files and set the data types.
- [ ] Create the MovieID relationship between Movies and OTT.
- [ ] Add the DAX measures from `dax/CinemaScope_Measures.dax`.
- [ ] Create the three report pages and test the slicers.
- [ ] Save your `.pbix` file.
- [ ] Complete `report/FDVA_Report_Template.md` with screenshots and observations from your own dashboard.
- [ ] State clearly in the report that the dataset is synthetic and results are for demonstration only.

## Project objective
Build an interactive business-intelligence dashboard using Power BI to compare generated Tamil and worldwide movie records and explore a simulated OTT catalogue using data cleaning, DAX measures, filters, charts, and cross-table relationships.
