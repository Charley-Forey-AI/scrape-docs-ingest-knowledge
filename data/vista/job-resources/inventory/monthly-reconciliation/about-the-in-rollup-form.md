---
title: "About the IN Rollup Form | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/job-resources/inventory/monthly-reconciliation/about-the-in-rollup-form"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/job-resources/inventory/monthly-reconciliation/about-the-in-rollup-form"
---

#  About the IN Rollup Form

Use this form to summarize or compress inventory details.
Typically, once you have run all the monthly reports and have closed the month in all sub ledgers, you can roll up the details.
 Rolling up inventory transactions summarizes the
 entries in the INDT (Inventory Detail) database table into one entry per source/month,
 much like a balance forward on a statement. Reports printed after a rollup will contain
 the roll-up entries instead of a series of detail lines, and will have a description of
 ‘Detail Roll Up’ in the memo field. The sources for the roll-up are listed below:
IN adjustments, physical count
TR transfer
PR production in inventory
AP material purchases through Accounts Payable
JC JC Material Use
EM
MO Material Orders
MS Material Sales - broken into 5 additional entries
 as follows:
1 - Customer sales, intercompany
2 - Job sales
3 - Inventory sales
4 - Inventory purchase
5 - Production
The rollup adds a new transaction to the INDT
 database table for each summarized entry and deletes all the old transactions of which
 the entry is comprised.
