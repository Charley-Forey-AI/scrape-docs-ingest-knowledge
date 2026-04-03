---
title: "Job/Company File Maintenance | Trimble Help"
source_url: "https://help.trimble.com/en/spectrum/spectrum/materials/materials-management/spectrum-menus/maintenance-overview/jobcompany-file-maintenance"
fetched_at: "2026-04-03T20:05:26.860879+00:00"
menu_path: "/en/spectrum/spectrum/materials/materials-management/spectrum-menus/maintenance-overview/jobcompany-file-maintenance"
---

# Job/Company File Maintenance

Users may create multi-company job requisitions from Materials Management by managing scale processing in one company and job tracking in another. If the multi-company option is selected during Inventory Control Installation, then the job requisitions created from Materials Management will post General Ledger expense and Job Cost to the company ID entered. The intercompany General Ledger account entered on the Inventory Control Installation screen will be used as the G/L credit account.
During Scale Ticket Update, this "job/company" file will be used to determine the company ID for the job number entered. If the job is not found in this file, the Materials Management Installation default Company code will be used. If this field is also blank, the current company ID is used.
The Rebuild Job / Company Table automatically creates records in the Job / Company File Maintenance screen.
