# CinemaScope: Tamil & Worldwide Cinema and OTT Analytics Using Power BI

## 1. Abstract
This project demonstrates how Power BI can be used to transform structured movie and OTT-catalogue data into interactive visuals. The package uses a synthetic dataset created for educational purposes; all ratings, budgets, revenues, dates and platform listings are simulated and are not factual industry measurements.

## 2. Problem Statement
Movie-related information can be difficult to compare across language/industry groups and streaming catalogue categories when data is spread across separate tables. This project demonstrates a unified view through interactive filters, key performance indicators and charts.

## 3. Objectives
- Compare the synthetic Tamil and worldwide movie groups.
- Analyze rating, genre, runtime and release-year patterns.
- Explore simulated budget and revenue relationships.
- Analyze OTT catalogue listings by platform, content type, genre and release year.
- Demonstrate Power Query cleaning, data modelling, DAX and Power BI visualizations.

## 4. Tools Used
- Microsoft Power BI Desktop
- CSV datasets
- Power Query for transformation
- DAX for measures and calculated columns
- Python 3 (optional, to regenerate the sample datasets; standard library only)

## 5. Dataset Description
- `movies.csv`: 700 synthetic movie records, split into 220 Tamil and 480 Worldwide records.
- `ott_catalog.csv`: simulated platform/title listing records for movies and TV shows.
- `data_dictionary.csv`: column meanings.

All data is synthetic demo data. Do not describe it as scraped, real, or official data. State this limitation when presenting the report.

## 6. Methodology
1. Generate/load the datasets.
2. Import the CSV files into Power BI.
3. Verify data types and blanks using Power Query.
4. Create the relationship `Movies[MovieID]` (one) to `OTT[MovieID]` (many).
5. Create DAX measures from `dax/CinemaScope_Measures.dax`.
6. Design three dashboard pages: Cinema Overview, Movie Performance and OTT Insights.
7. Use slicers to interactively filter the visuals.
8. Interpret only the results shown by the loaded synthetic data.

## 7. Dashboard Screenshots
Insert screenshots of each completed report page here.

### Page 1 — Cinema Overview
[Insert screenshot]

### Page 2 — Movie Performance
[Insert screenshot]

### Page 3 — OTT Insights
[Insert screenshot]

## 8. Observations and Results
Fill this section only after building and exploring your own Power BI report.

- Tamil vs Worldwide average rating: [write the values shown by your report]
- Release-year trend: [describe the trend visible in your report]
- Highest-rated synthetic titles: [write titles and ratings]
- Revenue/budget pattern: [describe the scatter chart; figures are simulated]
- Most frequent simulated OTT listing platform: [write the platform shown]
- Movies vs TV Show listing split: [write the values shown]

## 9. Limitations
- Data is synthetic and intended only to demonstrate analytics workflow.
- Platform association does not represent actual streaming availability.
- Ratings are generated, not actual IMDb/TMDB ratings or viewer reviews.
- Budgets and revenues are generated USD values and cannot support claims about real box-office performance.
- Blank values represent intentionally missing metadata.

## 10. Conclusion
This project demonstrates data ingestion, cleaning, modelling, DAX calculations, interactive visualization and dashboard storytelling in Power BI. It can be extended in future with sourced real-world datasets and verified data sources if the project requirements demand factual cinema statistics.

## 11. Future Enhancement
Replace or supplement synthetic rows with legally obtained, cited real-world datasets; add a source/date column; distinguish domestic vs worldwide gross and currencies; add review-count thresholds; and add verified OTT availability with collection dates.
