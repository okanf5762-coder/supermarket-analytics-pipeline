# End-to-End Supermarket Analytics Pipeline
I built a python to sqlite data pipeline that loads supermarket sales data into a relational database extracting supermarket transactional data, modeling it into a relational database, and building an executive business intelligence report.

## Data Pipeline Architecture
1. **Extraction:** Raw transactional data is loaded from 'sales.csv' using python and the 'pandas' library.
2.**Transformation:** Cleaned column formatting to replace blank spaces with sql-friendly underscores.
3.**Storage:** Structured rows are loaded directly into a local **sqlite** relational database ('supermarket_data.db').
4.**Visualisation:** An optimized executive **Power Bi** dashboard connecting directly to the data storage layer.

## The final Executive Dashboard
The dashboard uses a clean "L-shape" structural layout, keeping high-level summaries and country filters on the left sidebar while prioritizing widescreen categorical analysis and trend lines on the right:

[Practice dashboard](Dashboard_screenshot.png)

## Skills & Tech Stack Shown
* **Programming:** python, SQL
* **Data tools:** pandas, SQLite3
* **Visualization:** this is a practice report built on Microsoft's Financial sample dataset
* **Environment:** VS code, Thonny, Windows Terminal, Git/Github
