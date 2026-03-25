---
title: "JB Invoice Purge Form | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/costs-and-contracts/job-billing/setup-and-maintenance-of-job-billing/job-billing-maintenance/jb-invoice-purge-form"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/costs-and-contracts/job-billing/setup-and-maintenance-of-job-billing/job-billing-maintenance/jb-invoice-purge-form"
---

# JB Invoice Purge Form

Use this form to purge invoices.
You can purge invoices for a single contract, single AR customer, single billing number, or all invoices through a specific invoice date.
 Until purged, you can edit, change, and re-print invoices. The Purge Invoices in Open Months option allows you to purge invoices in an open month; however, you will typically want to leave this option unchecked to prevent the system from purging invoices with an open billing month. Check this box when purging by contract.
Note: Because the progress billing forms look back at previous invoices, do not purge any invoices from a progress-type contract until the contract is finished.
 The purge process determines invoices to purge as follows:

- If the bill status is ‘A-Active’ – These bills will be deleted as long as they meet the specified criteria and do not exist in a JB Interface batch.

- If the bill status is ‘C-Change’ or ‘D-Delete’ – These bills will never be deleted. You will need to interface the bills first, then re-run the purge process.

- If the bill status is ‘I-Interfaced’ or ‘N-Never Interfaced’ – These bills will be deleted as long as they meet the specified selection criteria.
