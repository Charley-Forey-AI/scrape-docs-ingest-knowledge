---
title: "About the MS Purge Form | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/job-resources/material-sales/setupmaintenance/about-the-ms-purge-form"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/job-resources/material-sales/setupmaintenance/about-the-ms-purge-form"
---

# About the MS Purge Form

Use this form to purge old tickets, hauler time sheets, invoices, and monthly sales totals.
Note that you can only purge detail from the appropriate files if you close the month in General Ledger.
 Use the Select Data to Purge section of the form to restrict the type of detail to purge. After selecting the type of information to purge, specify restrictions by Location Group and/or Location. If you do not select a purge option, the system purges detail for all location groups and locations.

## Purging Entries through a Specific Month

 Use the Purge Entries Posted Through field to limit the purge through a specific month. The month must be closed in the sub-ledgers of the GL company assigned to the current MS company. The system purges all entries that were posted in or prior to the current month.
 Click Purge to begin processing.

- If the purge is completely successful, a message box displays stating that the purge was successful, and asks if you wish to purge any more MS detail.

- If errors occur during the purge process, the process purges whatever detail it can, then displays a message stating which error(s) occurred. For example, if you are purging ticket detail and hauler time sheets, and errors occur during the ticket detail purge, the process purges the hauler time sheet detail, and displays an error message explaining why the ticket detail was not purged. You must correct errors in order to proceed.

Related information

- [About the MS Quote Close & Purge Form](/en/vista/vista/job-resources/material-sales/quotestemplates/quotes/about-the-ms-quote-close--purge-form)
