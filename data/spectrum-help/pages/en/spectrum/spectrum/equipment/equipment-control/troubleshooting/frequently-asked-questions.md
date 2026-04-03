---
title: "Frequently Asked Questions | Trimble Help"
source_url: "https://help.trimble.com/en/spectrum/spectrum/equipment/equipment-control/troubleshooting/frequently-asked-questions"
fetched_at: "2026-04-03T20:47:47.926179+00:00"
menu_path: "/en/spectrum/spectrum/equipment/equipment-control/troubleshooting/frequently-asked-questions"
---

# Frequently Asked Questions

Click one of the links below to view the answer to a specific question.

## How can I make project managers more accountable for idle equipment?

Business Problem:
When equipment costing is based solely on operating hours, project managers have no
 incentive to use equipment efficiently. For example, if they keep a piece of equipment
 for a week and only use the equipment for four hours, they are only billed for four
 hours even though the equipment was unavailable to other jobs for the whole week. How
 can we make project managers more accountable for idle equipment?
Solution:
Equipment revenue (usage) can be tracked in two components: operating
 time and standby. This affords better information in determining the real cost of
 keeping a piece of equipment at a job site and gives project managers an incentive to
 use equipment more efficiently.

## How can we set up our job burden to help defray shop overhead costs?

Business Problem:
Our company is losing money when items are in the shop for repair and not available for
 use on jobs. How can we set up our job burden to help defray shop overhead costs?
Solution:
You can add an additional labor burden to a mechanic by setting their
 burden in the Equipment Control Installation screen to a rate per hour instead of
 actual. By including their normal rate and an additional burden, you can gather the
 costs for shop overhead - covering everything from the roof to rags. Companies typically
 want the equipment to pick up this expense; the theory being the more time in the shop
 for repair, the more of the shop expense to share.

## How can I make sure that equipment "revenue" gets credited to the proper division
 that owns it?

Use the Validate Equipment Division to G/L Department option on the Equipment Control
 Installation screen.
This option only impacts the credit side of the transaction.
When entering EU types of transactions, the division code on the
 equipment will default in on the credit portion of the journal entry. In this way, we
 make sure that each equipment manager gets proper credit for the equipment used.
Equipment Code
Description
Division (Owner)

BL13
Cat D-11 Blade
50

BL14
Cat D-11 Blade
60

BL15
Cat D-11 Blade
60

Assume that my equipment revenue (usage) G/L code is 50-5600 and
 60-5600. When BL13 is charged to a job, Spectrum will automatically change the credit
 portion of the journal entry to 50-5600. In similar fashion, when I charge BL14 to a
 job, the system will automatically change the credit to 60-5600.

## I want the job division to default on EU types of transactions. What can I
 do?

Job Cost has its own "validate job division with GL department" option. This option,
 however, controls the debit side of the transaction. In other words, the Job Cost option
 will change the debit on the transactions department code to match that of the job
 division.
For example, create an Equipment Usage (EU) transaction for job 100.
 Job 100 is in division 30. Next, assume that the default Equipment Costs Allocated to
 Jobs GL account is 10-1520. When the equipment usage is charged to job 100, Spectrum
 will automatically change the debit side of the transaction to 30-1520.
Can I use both of these features together?
Yes, the Job Cost option controls the debit
 and the Equipment option controls the credit.

## What do I do if my equipment revenue is out-of-balance with the General
 Ledger?

Follow these steps if your equipment revenue is out-of-balance with
 your General Ledger.

1. Print the G/L Transaction Journal (General Ledger  >  Reports  >  Transaction Journal) for the two Equipment Revenue accounts that were set up on the
 Equipment Control Installation screen (Admin  >  Installation  >  Equipment Control  >  GL Codes).

1. Compare this to the Equipment Revenue Report (summary format) for the period in
 question.

1. If these two reports do not balance, then print the G/L Distribution Report
 (Equipment Control  >  Reports  >  G/L Distribution) for all accounts for the entire month. Review and verify that all
 the job revenue and rental revenue credits went to the appropriate G/L revenue
 accounts. Re-run the G/L Transactions Journal again using the correct accounts, if
 necessary.Note: In Equipment Control  >  Data Entry  >  Transaction the equipment revenue credit account is a default only. These
 accounts can be changed by the end user. The result is that equipment revenue
 could be charged to numerous G/L accounts.

1. Review the G/L Transaction Journal for ALL source codes for the specific G/L
 codes for equipment revenue. Are there other entries from sources other than
 Equipment Control and Payroll? If so, there should be a corresponding entry in
 Equipment Control.

1. If the transactions originated out of Payroll, useful reports to review are:

- The Payroll G/L Distribution Report, run for the
 specific G/L equipment revenue accounts. This report can be sorted by
 employee or by job. The Payroll G/L Distribution does NOT have equipment
 codes.

- Time Card History, sorted by pay type. By running the
 Time Card History Report by the various equipment pay types
 (ER,EO,ED,EU), you will be able to balance the time card entries by
 equipment to the Equipment Revenue report.

1. If the transactions originated out of Equipment Control,
 useful reports would be:

- The Equipment Control Transaction Report. This report
 is run when the update is run out of Equipment Control  >  Data Entry  >  Transaction. All Equipment Control transactions should have posted
 evenly to Equipment Control, as well as G/L. Hopefully, these reports
 have been archived.

- The G/L Distribution Report in Equipment Control
 (Equipment Control  >  Reports  >  G/L
 Distribution). This is an after-the-fact G/L Distribution. This report
 should match the G/L Transaction Journal.

1. When was the last time the two modules agreed? If you were
 in balance last month, have the G/L balances of that date changed? If it has
 not changed, this will help you to focus on a relatively short date range. If
 it has changed, the source of that change should be investigated.

1. Have any of the following Post to G/L checkboxes been
 cleared at any time recently? In particular, the flags to note are the
 Equipment Control transactions and the Payroll flags. These checkboxes are
 found in the General Ledger Installation (Admin  >  Installation  >  General Ledger  >  Properties). Typically, they are left unselected only during the conversion
 phase, then they are permanently selected. If for some reason they had been
 unselected during normal operations, the update would not post any entries to
 the General Ledger module.

1. Did you recently pass from one fiscal year to the next? If
 so, it may be appropriate to run the Opening Forward Balance Update in both
 General Ledger and Equipment Control in order to roll ending balances into the
 current year.

1. Is the General Ledger in balance (debits = credits)? To
 determine whether G/L is in balance, print the G/L Monthly Activity Balance
 File Report for all accounts. Look at the total line; all totals should be
 zero. If any other amounts appear, please call Viewpoint Support for
 assistance.

At this point, it will be necessary to review the reports transaction
 by transaction, comparing to the Equipment Revenue History Report and the Equipment
 Revenue Report.

## How do I balance equipment costs to the General Ledger?

Print the G/L Transaction Journal (General Ledger  >  Reports  >  Transaction Journal) for equipment costs only, for all source codes for the period in
 question.
Compare this to the Equipment Cost Report (in summary format) for the
 period in question.

1. When was the last time the two modules agreed? If you were in balance last month,
 have the G/L balances of that date changed? If it has not changed, this will help
 you to focus on a relatively short date range. If it has changed, the source of
 that change should be investigated.

1. Have any of the following Post to G/L checkboxes been cleared at any time
 recently? In particular the flags to note are the Accounts Payable Invoices,
 Equipment Control transactions, Payroll, and the Inventory Control flags. These
 checkboxes are found in the General Ledger Installation screen (Admin  >  Installation  >  General Ledger  >  Properties). Typically, they are left unselected only during the conversion
 phase, and then they are permanently selected. If for some reason they had been
 unselected during normal operations, the update would not post any entries to the
 General Ledger module.

1. Did you recently pass from one fiscal year to the next? If so, it may be
 appropriate to run the Opening Forward Balance Update in both the General Ledger
 and the Equipment Control modules in order to roll ending balances into the
 current year.

1. Is the General Ledger in balance (debits = credits)? To determine whether G/L is
 in balance, print the G/L Monthly Activity Balance File Report for all accounts.
 Look at the total line; all totals should be zero. If any other amounts appear,
 please call Viewpoint Support for assistance.

1. The next step is to narrow down the source of the out-of-balance.

1. Run the General Ledger Transaction Journal for each source
 code for all Equipment Accounts (report found in General Ledger  >  Reports  >  Transaction
 Journal.) The expected sources of equipment transactions are: Accounts
 Payable invoices, Equipment transactions, Journal entries, Payroll, and
 Inventory transactions.

1. Run the Equipment Control History Report (Equipment Control  >  Report  >  Equipment Cost
 History) for each source code. The sources are: Accounts Payable,
 Equipment Cost, General Ledger, Payroll and Inventory Control. Use the same
 date range that was used when running the G/L Transaction Journal.
Compare the G/L Transaction Journal by source code to each
 of the corresponding Equipment Cost History reports run by individual source
 code.

1. Review the G/L Transaction Journal for ALL source codes for
 direct cost equipment cost only. Are there other entries from other sources? If
 so, there should be a corresponding entry over in Equipment Control.

1. Once the source of the out-of-balance is discovered, it may
 be necessary to trace the transactions back to the original posting reports.


1. If Equipment Control is the source, review:

1. The Equipment Control Transaction Report. This report is
 printed when the update is run in Equipment Control and hopefully has been
 archived for referral. All EC transactions should have posted equally to EC, as
 well as G/L.

1. The Equipment Control G/L Distribution Report. This report
 should match the G/L Transaction Journal by equipment transaction source code
 when only the direct cost equipment codes are examined. This report provides
 details such as equipment code and cost category.

1. If Payroll is the source, review:

- The Payroll G/L Distribution Report, run for the specific G/L equipment
 direct cost accounts. This report will sort by employee. The Payroll G/L
 Distribution Report does NOT have equipment codes.

- The Time Card History Report, sorted by department.
 By running the Time Card History Report by department, you will be
 able to balance the time card entries coded to the equipment
 departments to the Equipment Cost report.

1. If Accounts Payable is the source, review:

- The Accounts Payable Transaction Report. This report
 is printed when the update is run in Accounts Payable  >  Data Entry  >  Invoice -
 CM and has hopefully been archived for referral. All Accounts
 Payable Equipment Control transactions should have posted equally to EC,
 as well as G/L.

- The Accounts Payable G/L Distribution Report. This
 report provides details such as equipment code and vendor.

1. If General Ledger is the source, review:

- The G/L
 Transaction Register.

At this point, it will be necessary to review the reports transaction
 by transaction, comparing them to the Equipment Cost History Report and the Equipment
 Cost Report.
