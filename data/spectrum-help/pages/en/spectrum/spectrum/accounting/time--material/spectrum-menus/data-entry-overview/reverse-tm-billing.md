---
title: "Reverse T+M Billing | Trimble Help"
source_url: "https://help.trimble.com/en/spectrum/spectrum/accounting/time--material/spectrum-menus/data-entry-overview/reverse-tm-billing"
fetched_at: "2026-04-03T20:47:47.926179+00:00"
menu_path: "/en/spectrum/spectrum/accounting/time--material/spectrum-menus/data-entry-overview/reverse-tm-billing"
---

# Reverse T+M Billing

The Reverse T+M Billing screen lets you reverse a Time + Material billing by deleting transactions for the specified bill from the billing history file and returns transactions to the "unbilled" status, but already selected for rebilling and assigned to the original billing number. Some or all of the transactions may then be deselected from that bill, or any other needed additions or modifications made prior to reissuing the invoice.
If an alternate bill-to address is specified for the job in the T+M Job Billing Setup screen, this address will be transferred during the reversal. If the selected job is a sub-job of a master job, the sub-job will be included in the newly re-opened billing in progress.
If the selected customer is a related party customer, the Override A/R trade G/L account
 and the Override revenue G/L account in the detail section of the invoice will default when
 the unposted customer invoice is created and sent to A/R during the update.
Note: If the Post invoices to Accounts Receivable checkbox in the Time + Material
 Installation screen is selected, then an Accounts Receivable credit memo will also be
 created during this billing reversal.
