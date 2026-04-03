---
title: "Report Information for Entity Users | Trimble Help"
source_url: "https://help.trimble.com/en/spectrum/spectrum/getting-started/reports--printing-overview/report-information-for-entity-users"
fetched_at: "2026-04-03T20:47:47.926179+00:00"
menu_path: "/en/spectrum/spectrum/getting-started/reports--printing-overview/report-information-for-entity-users"
---

# Report Information for Entity Users

Through use of 'entities', Enterprise clients can control the presentation of company name and address information. Read on to learn how the software will determine whether to show the company name (and other information) defined in Company Installation, or whether to show entity-specific information on reports.

- First the software will determine if cost centers are being used in the current company. If cost centers are not being used, the software will always use the Company Installation settings.

- Second, the software will determine if entities are enabled in the cost center company (if the 'Entity tracking?' checkbox is selected in the Enterprise Installation screen). If entities are not being used, the software will always use the Company Installation settings.

- The software will look for the cost center to be used to identify the entity for the particular report.

- If that cost center is <blank>, the Company Installation settings are used.

- For the cost center identified above, the software reads for the assigned entity of that cost center.

- If the entity code is <blank> for that cost center, the Company Installation settings are used.

- The software will replace the following Company Installation data with information from Entity File Maintenance, as necessary for the particular report:

- Company name

- Company address

- Company telephone

- Company logo bitmap

Related information

- [External Reporting with Entities](/en/spectrum/spectrum/getting-started/reports--printing-overview/report-information-for-entity-users/external-reporting-with-entities)
