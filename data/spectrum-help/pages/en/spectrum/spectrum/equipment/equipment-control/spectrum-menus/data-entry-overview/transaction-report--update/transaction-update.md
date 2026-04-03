---
title: "Transaction Update | Trimble Help"
source_url: "https://help.trimble.com/en/spectrum/spectrum/equipment/equipment-control/spectrum-menus/data-entry-overview/transaction-report--update/transaction-update"
fetched_at: "2026-04-03T20:47:47.926179+00:00"
menu_path: "/en/spectrum/spectrum/equipment/equipment-control/spectrum-menus/data-entry-overview/transaction-report--update/transaction-update"
---

# Transaction Update

This screen displays only after the Transaction Report
 prints.
Do not continue until the Transaction Report has printed correctly. Once it has printed and
 is accurate, continue with the update. Updating will post all transaction costs to the
 equipment files, and job cost, if applicable.

- Meter tracking: Equipment Control supports four types of meter tracking: Hours, Miles, Kilometers, and Usage. When Equipment Usage 'meter transactions' are updated, the software adjusts all usage records with a later transaction date so that the new transaction is included in the life-to-date 'usage' total.

- Meter replacement:
 In addition, the Last
 reading and the Last
 read date values stored in the Equipment Master file will be updated
 when this function is run. If a meter has been replaced and any records are found for
 an equipment code with a Last service
 date earlier than the meter replacement date, the Last Performed Meter
 reading is changed by the difference between old and new readings at replacement.

- Multi-company processing: The Transaction Update for multi-company Vendor and Employee cost transactions writes 'debit' costs to the current (equipment) company and 'credit' costs to the designated (vendor or employee) company. Any associated images save to the current company.

- Reversing entries:
 Once this information is posted, the information is not accessible for changes or
 deletions. If a mistake is identified following the update, a reversing entry will be
 required.

If this is a sub-job billed from a master job, the software will read for job-specific setup rates for the master job, and if none are found use standard settings. If this is a sub-job billed at the sub-job level, the software will read for job-specific setup rates for the sub-job first, and if billing rates are not found then the master job, and if none are found there use standard settings.
