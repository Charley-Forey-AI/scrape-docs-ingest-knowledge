---
title: "Revenue Information | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/costs-and-contracts/job-cost/costs/types-of-cost-information/revenue-information"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/costs-and-contracts/job-cost/costs/types-of-cost-information/revenue-information"
---

# Revenue Information

In addition to cost data, JC also keeps track of contracts with customers and collects information about how much of each contract has been billed.
The following chart shows the sources of revenue data for each contract/item.
Updates to Contract Revenue

Dollars and Units

Original Contract
Project Management, JC
 Contracts

Current Contract
Project Management, JC Change Orders

Actual Revenue
JB Interfaced Invoices, AR Invoice Entry, JC Revenue Adjustments

t

## The Contract Files

Revenue is accumulated on a month-to-month basis in a table
 called JCIP. For each contract/contract item, JCIP has a
 record for each month in which there is activity. The monthly records store the amount
 by which the value changed during that month for contract amounts and billed amounts. To
 show the activity for a single month on a report, you restrict the report to just that
 month. To show job-to-date totals, you have the report accumulate all records through
 that month. The advantages of this structure are that you can work with multiple periods
 open at once, and you never lose the ability to go back and print a report for a prior
 record. Detail of all transactions is available in JCID. This will include detail of
 change orders to contract amounts and detail of invoiced amounts from Job Billing or
 Accounts Receivable.
 If you use the Job Billing module, you set
 up additional information about the contract there, then create invoices against the
 contract items. At the same time that you post those invoices to AR using Job Billing,
 JCCI, JCIP, and JCID are updated. Whether or not you use JB, invoices entered in
 Accounts Receivable can be coded to a contract and item.
