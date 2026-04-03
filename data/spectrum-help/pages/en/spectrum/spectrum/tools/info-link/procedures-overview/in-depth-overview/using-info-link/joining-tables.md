---
title: "Joining Tables | Trimble Help"
source_url: "https://help.trimble.com/en/spectrum/spectrum/tools/info-link/procedures-overview/in-depth-overview/using-info-link/joining-tables"
fetched_at: "2026-04-03T20:47:47.926179+00:00"
menu_path: "/en/spectrum/spectrum/tools/info-link/procedures-overview/in-depth-overview/using-info-link/joining-tables"
---

# Joining Tables

When a query or report involves more than one table, it is necessary to define how the tables are related before the query will run correctly. For example, if you are using the job history file and you want the job name to display, you need to get the name from the job master file. In this case, you need to join these two files together by joining the keys that are JC_JOB_MASTER in the job master file to JC_JOB_MASTER in the job history file.
The exact method for defining the join depends on your application. In Microsoft Access or Excel, simply put the mouse pointer on the key in the first file (for example, JC_JOB_MASTER) and drag it over to the second key (for example, JC_JOB_MASTER). A line is drawn on the screen showing that the files are joined.
Please note that you will not get the desired result if you do not join the files. For example, if you have two files with no relationships defined, you will get a large, unusable query.
