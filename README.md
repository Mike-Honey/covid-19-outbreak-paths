# covid-19-outbreak-paths
Projects to explore detailed outbreak paths. Mostly dataviz using Power BI

**Reference:**

Case-level data on Victorian outbreak during May-June 2021. [dbRaevn](https://twitter.com/dbRaevn) has manually constructed a diagram of the outbreak paths, based on information from daily press cases. 

This project turns that inforamtion into structured data and feeds it through an interactive dataviz solution, using [Power BI](https://powerbi.microsoft.com) with the [Drill Down Graph PRO Custom Visual by ZoomCharts](https://appsource.microsoft.com/en-us/product/power-bi-visuals/wa200002065?tab=overview).  The interactive features allow the audience to filter the dataset by date, cluster or variant.

**Summary**

For this project, the manual diagram info is converted into a structured data table (Excel). Each row represents a transmission link between cases. The codes used for each node on the manual diagram are used as Source and Target nodes to drive the diagram visual. Cases with an unknown source are loaded with the same code for Source and Target. The dataviz tool used requires unique codes for each node, so suffixes have been added where the manual diagram codes were not unique. Once the initial dataset is established, ongoing updates are relatively simple.

Another sheet in the Excel file provides the colours assigned to each node by date.  The preferred colours scheme is a steady gradient of purple. The colour scheme used on the manual diagram is also presented on an alternate page, for those who prefer that scheme.

Several dataviz variations are presented on alternate pages - use the page navigation controls at the bottom to view them. They explore different layout options and colour schemes, and some alternative visuals.  


[Link to interactive DataViz](https://app.powerbi.com/view?r=eyJrIjoiZjE1ZTNmNDUtYjgyMS00NTg5LTk5M2MtY2FjOWJjODY2NGZlIiwidCI6ImRjMWYwNGY1LWMxZTUtNDQyOS1hODEyLTU3OTNiZTQ1YmY5ZCIsImMiOjEwfQ%3D%3D&pageName=ReportSection249bfa2c532d631a641e)

[![Click to view and interact with the report](https://github.com/Mike-Honey/covid-19-outbreak-paths/raw/main/2021-05%20Victorian%20Outbreak%20Paths.png)](https://app.powerbi.com/view?r=eyJrIjoiZjE1ZTNmNDUtYjgyMS00NTg5LTk5M2MtY2FjOWJjODY2NGZlIiwidCI6ImRjMWYwNGY1LWMxZTUtNDQyOS1hODEyLTU3OTNiZTQ1YmY5ZCIsImMiOjEwfQ%3D%3D&pageName=ReportSection249bfa2c532d631a641e)

**Preview animation:**

[![Click to view and interact with the report](https://github.com/Mike-Honey/covid-19-outbreak-paths/raw/main/2021-05%20Victorian%20Outbreak%20Paths.gif)](https://app.powerbi.com/view?r=eyJrIjoiZjE1ZTNmNDUtYjgyMS00NTg5LTk5M2MtY2FjOWJjODY2NGZlIiwidCI6ImRjMWYwNGY1LWMxZTUtNDQyOS1hODEyLTU3OTNiZTQ1YmY5ZCIsImMiOjEwfQ%3D%3D&pageName=ReportSection249bfa2c532d631a641e)

THIS REPORT IS NOT HEALTH ADVICE - REFER TO YOUR LOCAL HEALTH AUTHORITY.



