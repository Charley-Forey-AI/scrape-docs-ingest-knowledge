---
title: "Multi-Company Tables and Single-Company Views | Trimble Help"
source_url: "https://help.trimble.com/en/spectrum/spectrum/tools/info-link/procedures-overview/in-depth-overview/using-info-link/multi-company-tables-and-single-company-views"
fetched_at: "2026-04-03T20:05:26.860879+00:00"
menu_path: "/en/spectrum/spectrum/tools/info-link/procedures-overview/in-depth-overview/using-info-link/multi-company-tables-and-single-company-views"
---

# Multi-Company Tables and Single-Company Views

Many Spectrum customers run multiple companies on one Spectrum system. When this is the case, Spectrum tables hold all the rows for all companies in one table. For example, the JC_JOB_MASTER_MC table will hold all jobs for all companies. In many cases, it is desirable to limit a user's access to just one company. For this reason, every multi-company table has a single-company view associated with it. For example, JC_JOB_MASTER is a single company view of the JC_JOB_MASTER_MC table. This view will only show the jobs for my current company, which is determined by the first three letters of each user's logon name (user id). For example, if my user id is "XYZ_MARK" then my company code is "XYZ."
When setting up security, it is important to determine whether a user should get access to the rows in all companies (in which case you'll use the table ending in "_MC") or just the rows for the current company (in which case use the view without the "_MC" on the end).
