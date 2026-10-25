# CinemaScope FDVA — Viva Preparation

**1. What is the aim of the project?**  
To demonstrate movie and OTT catalogue analysis in Power BI using data cleaning, modelling, DAX measures and interactive visuals.

**2. What is Power BI?**  
Power BI is a business-intelligence tool used to connect, transform, model and visualize data in interactive reports.

**3. What is Power Query?**  
Power Query is the data preparation tool used to import, clean and transform data before loading it into the model.

**4. What is DAX?**  
Data Analysis Expressions (DAX) is the formula language used to create measures and calculated columns in Power BI.

**5. What is the difference between a measure and a calculated column?**  
A measure is calculated in response to filter context when a visual is evaluated. A calculated column is evaluated for each row during data refresh and stored in the model.

**6. Why is there a relationship between Movies and OTT?**  
`MovieID` connects a movie record to one or more simulated platform listings. A TV-show listing has a blank MovieID because it is not linked to the movie table.

**7. Why are some values blank?**  
They represent missing data. Treating missing budget or revenue as zero would misrepresent totals and averages.

**8. What is a slicer?**  
A slicer is an on-report filter that lets a user interactively restrict the data shown in visuals.

**9. What is the difference between a platform listing and a unique OTT title?**  
The same title may be listed on more than one platform, so listing rows can exceed the number of distinct titles.

**10. Are the ratings and revenue figures real?**  
No. The included dataset is synthetic demo data, created to practice the analytics workflow. The results must not be presented as factual film-industry statistics.

**11. How would you adapt it to real data?**  
Replace or supplement the sample data with a properly licensed, documented dataset; keep source URL and retrieval date; standardize definitions, currencies and rating scales; then refresh the Power BI model.

**12. What are the main limitations?**  
Synthetic values, simulated OTT availability, missing data and simplified genre/language classifications mean that the dashboard demonstrates methods rather than real market performance.
