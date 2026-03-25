---
title: "About Updating GL | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/job-resources/equipment-management/revenuecosts/revenuecost-processing/about-updating-gl"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/job-resources/equipment-management/revenuecosts/revenuecost-processing/about-updating-gl"
---

# About Updating GL

Details on equipment usage updates to General
 Ledger.
When posting equipment usage, the update to
 General Ledger:

- Credits the Equipment account (defined in EM Departments, Revenue Codes
 tab) for the transaction. The GL account credited depends on the line’s revenue code
 or revenue breakdown codes.

- Debits the Offset Acct specified for the transaction. This account
 defaults as follows:

- If posting to transaction type ‘J-Job’, uses the GL account designated
 (in JC Departments) for the specified cost type.

- If posting to transaction type ‘E-Equipment’ or ‘W-Work Order’, uses the
 GL account designated (in EM Departments) for the specified cost code or cost type
 (if no override for cost code).

- If posting to transaction type ‘X-Expense’, the GL account defaults as
 null and must be entered manually.

Note: The Offset Acct field is always
 accessible when posting an Expense type usage transaction. For job, equipment, and work
 order postings, the Offset Acct field is accessible only
 if you have checked the Allow GL Account Override box in the
 appropriate company file (JC Company Parameters for J-Job types and EM Company
 Parameters for E-Equipment and W-Work Order types)
