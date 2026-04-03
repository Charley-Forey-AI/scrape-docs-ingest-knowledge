---
title: "Understanding Equipment Transactions and the General Ledger | Trimble Help"
source_url: "https://help.trimble.com/en/spectrum/spectrum/equipment/equipment-control/in-depth-overview/understanding-equipment-transactions-and-the-general-ledger"
fetched_at: "2026-04-03T20:05:26.860879+00:00"
menu_path: "/en/spectrum/spectrum/equipment/equipment-control/in-depth-overview/understanding-equipment-transactions-and-the-general-ledger"
---

# Understanding Equipment Transactions and the General Ledger

The goal of tracking equipment revenue and equipment costs
 is to enable the owner to calculate the profitability of equipment in his/her company.
Ultimately, equipment revenue and equipment expense can be included in the company's
 financial statements.
Example:
Equipment is often shown as one line item on the financial statements. This one line; however, could be summary of all of the equipment accounts added together. Within Spectrum, equipment transactions are tracked as either REVENUE or COSTS

## Equipment Revenue and the General Ledger

Equipment revenue represents the amount charged to a job for a particular piece of equipment. This is tracked in the Equipment Tracking module and the Equipment Control module. Also, equipment rental to third parties is tracked in Equipment Control.
Note: In Spectrum, Equipment Revenue, is called several different
 things: Equipment Revenue, Equipment Usage (or Standby), Equipment Cost Allocated or
 Usage. These terms are used interchangeably. For purposes of this discussion, the term
 "Equipment Revenue" will be used.
The Equipment Tracking module allocates standby (ES) time to jobs. Transactions from the Equipment Tracking module are updated to the G/L in Equipment Control (Equipment Control  >  Data Entry  >  Transactions). The Equipment Tracking module only tracks equipment revenue; the Equipment Control module tracks equipment costs and equipment revenue.
Within Spectrum there are two types of revenue transactions: Equipment Usage (EU) and Equipment Standby (ES).

- Equipment Standby (ES) transactions can be entered in the Equipment Tracking module or the Equipment Control module.

- Equipment Usage (EU) transactions can be entered in the Equipment Control
 module or the Payroll module (via pay types: ER, EO, ED, EU).Note: Equipment costs are not entered via
 these pay types; only equipment revenue.

The Equipment Revenue G/L accounts are set up in the Equipment Control Installation screen for all Equipment Revenue transactions. This will be the default credit in the journal entries that are posted to the General Ledger.
Note: Note In Equipment Control  >  Data Entry  >  Transactions, this default credit can be changed during data entry. This could
 be a potential reconciling item when balancing equipment revenue to G/L. In
 Spectrum, the Equipment Revenue account is often called the "Equipment Cost
 Allocated" account. The convention used when setting up the chart of accounts is
 to put this account at the end of the list of Equipment Cost accounts (used to
 track Equipment Costs). The Equipment Revenue (or Equipment Cost Allocated)
 account can be considered to be a contra-account to the other Equipment Cost
 accounts. For instance, the accounts could be set up as follows: 5100 Equipment
 Fuel 5101 Equipment Lube/Oil 5102 Equipment Tires 5103 Equipment Labor 5104
 Equipment Parts 5105 Equipment Outside Repairs 5106 Other Equipment Expense 5107
 Equipment Depreciation 5108 Equipment Licenses 5109 Equipment Insurance 5199
 Equipment Cost Allocated (aka: Equipment Revenue)

## Journal Entries

As a general rule, the equipment revenue journal entry that is posted to G/L (no matter from what source) consists of a Dr updated to a Job Cost account and the Cr updated to the Equipment Cost Allocated account (set up in the Equipment Control Installation screen).
Example:
Dr: Direct Cost Account (updated to JC)
Cr: Equipment Cost Allocated (or Equipment Revenue)
(The following sample journal entries depict typical transactions that would be entered into Spectrum).
Payroll:
The debit that is posted to Job Cost is set up in Payroll  >  Maintenance  >  Department Expense. This will be the expense to job cost. This must be a Direct Cost G/L account. Please note that the Payroll department must be a Job Cost department!
The credit that is posted as Equipment Revenue is set up in Admin  >  Installation  >  Equipment Control (see above).
The entry that is posted to G/L out of Payroll is:
JE #1 Dr: Direct Equipment Costs (direct cost account/updates to JC) 600
 Cr: Equipment Revenue (default from EC Installation-updates to EC) 600
Equipment Control and Equipment Tracking
When an EU or ES transaction is booked in Equipment Control, the G/L entry is as follows.

- If a Job entry:

JE #2 Dr: Direct Equipment Costs (direct cost account/updates to JC) 1,000
 Cr: Equipment Revenue (default from EC Installation-updates to EC) 1,000

- If a Rental entry:

JE #3 Dr: Accounts Receivable (non-direct cost account) 400
 Cr: Equipment Revenue (default from EC Installation-updates to EC) 400
In Equipment Control  >  Data Entry  >  Transaction, if the type input is J for Job, Spectrum will require that the debit on the line item be a direct cost G/L account. The credit will default from the Equipment Control Installation screen, Job Revenue account number.
If the type is R for Rental, the job fields will be skipped. Spectrum will require that the debit NOT be a job cost account and the credit will, once again, default from the Equipment Control Installation screen, Rental Revenue account number.
Note: Please note that this credit default can be changed. If it
 is changed to another G/L account, than this could be a potential reconciling item when
 balancing equipment revenue to the G/L. Essentially, we are booking revenue for a
 specific piece of Equipment while simultaneously charging a job for the use (and/or
 standby time) for that piece of equipment, or if it is a rental, simply recording Rental
 Revenue to the General Ledger.

## Equipment Costs and the GL

All expense accounts for equipment charges will need to be set up as equipment direct cost accounts in General Ledger  >  Maintenance  >  Master File. Whenever these Direct Cost Equipment G/L account codes are utilized, Spectrum will require that a corresponding Equipment Code be input into the transaction. This ensures that the costs in the Equipment Control module will always balance to the General Ledger.
In Spectrum, equipment cost transactions can be entered via:

- Equipment Control  >  Data Entry

- Payroll  >  Data Entry  >  Time CardTo record equipment costs in Payroll, the time card entry must be
 coded to a Payroll equipment department.Note: The Pay type
 can be R, O, D, V, H, S, and so forth. Only equipment revenue transactions are
 coded to pay types ER, EO, ED, EU.

- Accounts Payable  >  Data Entry  >  Invoice-CMThese transactions will need to be coded to a Direct Cost Equipment G/L code.

- General Ledger  >  Data Entry  >  Journal EntryThese transactions will need to be coded to a Direct Cost Equipment G/L code.

- Inventory Control  >  Data Entry  >  AdjustmentsThese transactions will need to be entered as an Adjustment Type of Equipment.

## Journal Entries

The following sample journal entries depict typical transactions that would be entered into Spectrum.

## General Ledger

An example of an entry that could be updated to G/L when the EC transaction is input as a General Ledger Journal entry is as follows:
JE #4 Dr: Depreciation (EC direct cost account/updated to EC) 1,100
Cr: Misc. Admin Expense (Non-Direct Equipment Cost account) 1,100

## Accounts Payable

The entry that is updated to G/L when the EC transaction is input in Accounts Payable is as follows:
JE #5 Dr: Fuel (EC direct cost account/updated to EC) 1,500
Cr: Accounts Payable/Cash 1,500

## Payroll

If the equipment costs are posted through payroll, the journal entry that is updated to G/L is as follows:
JE #6 Dr: Equipment Cost (EC direct cost account/updated to EC) 2,000
Cr: P/R Taxes/Liabilities 500
Cr: Cash 1,500
Note: Payroll burden is set up on the EC Installation screen. If
 the payroll burden cost category is left blank then the burden will be coded to the cost
 category that is input on the timecard line. If the Payroll burden type is set to be
 Percentage of Labor cost, the G/L codes are set up Payroll  >  Department Expense  >  Equipment Expense screen.
The journal entry for burden (under Percentage of labor cost) is as follows:
JE #7 Dr: Burden Expense (non-direct equipment cost account) 425 (actual
 cost)
Cr: PR Liability (non-direct equipment cost account) 425 (actual cost)
JE #8 Dr: Payroll Burden (EC direct cost account/updated to EC) 450 (% of
 labor cost)
Cr: EC Burden Variance (non-direct equipment cost account) 450

## Equipment Control

When the equipment charges are added in Equipment Control  >  Data Entry, an example of an entry that is posted to G/L is:
JE #9 Dr: Licenses (EC direct cost account/updated to EC) 300 Cr: Office
 Expense (non-direct equipment cost account) 300

## Inventory Control

When an equipment adjustment is made in Inventory Control, a sample entry that is posted to G/L is as follows (vice versa, depending on the adjustment being made).
JE #10 Dr: Inventory Adjustment (EC direct cost account/updated to EC 400
Cr. Inventory 400
In Equipment Control transactions one of the G/L accounts must ALWAYS be an Equipment G/L code.
