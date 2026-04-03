---
title: "External Reporting with Entities | Trimble Help"
source_url: "https://help.trimble.com/en/spectrum/spectrum/getting-started/reports--printing-overview/report-information-for-entity-users/external-reporting-with-entities"
fetched_at: "2026-04-03T20:47:47.926179+00:00"
menu_path: "/en/spectrum/spectrum/getting-started/reports--printing-overview/report-information-for-entity-users/external-reporting-with-entities"
---

# External Reporting with Entities

Many period-end reports are intended to be issued to people outside the company (for example, aging reports, financial reports, and so on). Through the use of cost center entities, Enterprise users can control the company name and logo that display on the top of these reports.
Read on to learn how the software will determine whether to show the company name (and other information) defined in Company Installation, or whether to show entity-specific information on reports.

1. First the software will determine if cost centers are being used in the current company. If cost centers are not being used, the software will always use the Company Installation settings.

1. Second, the software will determine if entities are enabled in the cost center company (if the 'Entity tracking?' checkbox is selected in the Enterprise Installation screen). If entities are not being used, the software will always use the Company Installation settings.

1. The software will look for the cost center to be used to identify the entity for the particular report. The software will determine whether every cost center included in the specified 'Cost group' is assigned to the same 'Entity code'.


- If the same entity is not specified in every applicable cost center, the company name from Company Installation is used.

- If the same 'entity code' is associated with every applicable cost center, then the company name and logo from Entity File Maintenance will be used.
