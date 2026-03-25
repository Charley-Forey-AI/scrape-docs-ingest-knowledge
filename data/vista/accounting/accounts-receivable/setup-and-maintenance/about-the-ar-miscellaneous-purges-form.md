---
title: "About the AR Miscellaneous Purges Form | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/accounting/accounts-receivable/setup-and-maintenance/about-the-ar-miscellaneous-purges-form"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/accounting/accounts-receivable/setup-and-maintenance/about-the-ar-miscellaneous-purges-form"
---

# About the AR Miscellaneous Purges Form

You can use the AR Miscellaneous Purges form to purge miscellaneous types of information from the Accounts Receivable files.
There are three purge options available in this form, and each option works independently within its own parameters. The system only purges information from AR files. Information interfaced to other modules (CM, JC, and GL) is not affected.
The following is a brief description of each of the purge options available in this form:

- Purge Monthly Customer Totals - The system maintains a running total of all transactions for each month per customer. These totals take up much less room than full transaction detail, so the system can store them for a long time without consuming a great deal of disk space. Use this option to purge monthly totals that are too old to be useful. The system creates a balance forward record in the through month.

- Purge Miscellaneous Cash Receipts – Use this option to purge miscellaneous cash receipts from the AR files. Since these types of transactions are not customer-related, they do not affect any of the customer files. Additionally, job or equipment files updated by miscellaneous cash receipts are unaffected when purging miscellaneous cash receipts.

- Purge Miscellaneous Distributions - This option allows you to purge miscellaneous distributions without purging invoices, customer account balances, or miscellaneous cash receipts. Since the miscellaneous distributions are used to track distributions that require separate accounting, you may choose to store the information for a designated period before it is purged. Miscellaneous distributions may be purged before or after AR transactions are purged.
