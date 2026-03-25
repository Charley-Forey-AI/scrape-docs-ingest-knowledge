---
title: "Intercompany Revenue Adjustments | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/costs-and-contracts/job-cost/revenue/intercompany-revenue-adjustments"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/costs-and-contracts/job-cost/revenue/intercompany-revenue-adjustments"
---

# Intercompany Revenue Adjustments

Intercompany revenue adjustments are identified by a
 Rev
 Type of IC-Intercompany and allow you to debit or credit an offset account
 in the posting company and debit or credit contract revenue in another company.
When the IC type is selected, a Company
 field is enabled, allowing you to specify the job cost company to which the revenue
 adjustment will be posted. You will need to specify an Offset Account for the posting
 company to allow for proper updates to the appropriate GL accounts.
When an intercompany revenue adjustment is
 posted, GL accounts are updated as follows:
Posted From: Co 1
Posted To: Co 5
Amount: 1,000.00
Company
 #1Company
 #2
DebitCreditDebitCredit
1,000.001,000.001,000.001,000.00
Offset AccountIntercompany ARIntercompany APJC Revenue
 Account

Note: Reversals cannot be done through intercompany
 entries. Additionally, once entries are posted, they cannot be added back into a batch
 for further editing or deletion. Corrections must be done by entering new
 adjustments.Additional Information
