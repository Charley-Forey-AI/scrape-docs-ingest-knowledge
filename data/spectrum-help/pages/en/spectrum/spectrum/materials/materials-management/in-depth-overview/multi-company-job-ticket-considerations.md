---
title: "Multi-company Job Ticket Considerations | Trimble Help"
source_url: "https://help.trimble.com/en/spectrum/spectrum/materials/materials-management/in-depth-overview/multi-company-job-ticket-considerations"
fetched_at: "2026-04-03T20:05:26.860879+00:00"
menu_path: "/en/spectrum/spectrum/materials/materials-management/in-depth-overview/multi-company-job-ticket-considerations"
---

# Multi-company Job Ticket Considerations

The ability to create multi-company job requisitions from Scale allows users to handle Scale Processing in one company and job tracking in another. If the Multi-company requisitions checkbox is selected in the Inventory Control Installation screen, then the job requisitions created from Materials Management will post G/L expense and Job Cost to the company Id entered.
All pricing entered in the Job file for hauler rates, miscellaneous charges and categories will be set up in the same company. The G/L department must be set up in the current company (where Inventory Control is and the Job Requisitions are processed). Inventory G/L and the Job Cost Markup G/L will come from this file.
Optional: You may set up the same G/L department code in the other company (where the job is). If it's there, the Job Cost Direct G/L will come from there. Otherwise, it will use the G/L code from the current company.
For multi-company job requisitions that include a separate freight or miscellaneous line, the Scale Ticket Update will set the cost type for the line based on the cost type, if any, specified in the General Ledger Chart of Accounts of the destination company.
From Materials Management to Job Requisition Entry:

- Do not transfer if the G/L department is blank (warehouse transfers).

- Do not transfer if the G/L department is non-valid in this company.

- Do not transfer if the Multi-company requisition checkbox is selected, and the G/L code in this company's Inventory Control Installation prompt for "intercompany" is set to No direct cost.

- Do not transfer if the Multi-company field is selected, and the Direct cost field in G/L Master File Maintenance is set to No direct cost.

- Do not transfer if single company and the G/L code are not OK, per the above list, in this company.
