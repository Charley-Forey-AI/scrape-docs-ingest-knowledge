---
title: "Field Definitions: JC Revenue Adjustments Form | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/costs-and-contracts/job-cost/revenue/about-the-jc-revenue-adjustments-form/field-definitions-jc-revenue-adjustments-form"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/costs-and-contracts/job-cost/revenue/about-the-jc-revenue-adjustments-form/field-definitions-jc-revenue-adjustments-form"
---

# Field Definitions: JC Revenue Adjustments Form

The following is a list of field descriptions for the JC
 Revenue Adjustments form. Many of the descriptions include links to other topics that provide additional information about or related to the topic.

##  Sequence #

 Enter the sequence number of an existing entry or enter N, New, or + to add a new sequence. The system will automatically assign the next available sequential number.

[](/en/vista/vista/costs-and-contracts/job-cost/setup-and-maintenance/about-the-jc-fixed-rate-template-form)JC Fixed Rate Template

##  Action

 When entering a new transaction, this field defaults to A (Add) and cannot be accessed.
 If this is an existing transaction, specify the action for this entry.
 C = Change. Use this action to make changes to transactions that have already been processed.   D = Delete. Use this action to delete the transaction from all files in JC. (The delete functions in the toolbar and Records menu will only delete the entry from the batch.)

[](/en/vista/vista/costs-and-contracts/job-cost/revenue/about-the-jc-revenue-adjustments-form)JC Revenue Adjustments

##  Revenue Type

 Indicate the source of the original transaction for which you are making the revenue adjustment.

- JC-Job Cost. Select this type if this adjustment applies to a Job Cost transaction.

- AR-Accts Receivable. Select this type if this adjustment applies to an Account Receivable transaction.

- IC-InterCompany. Select this type if this adjustment applies to an intercompany revenue transaction.

Note: Although the source description for the transaction will always be ‘JC RevAdj’, the Rev Type allows you to identify the actual source here. It also determines what additional fields are made available in which to put corresponding information.  
[](/en/vista/vista/costs-and-contracts/job-cost/revenue/about-the-jc-revenue-adjustments-form)JC Revenue Adjustments

##  Date

 Specify the date that will be the ‘actual’ date for this transaction in the JCRD (Revenue Detail) table. Initially defaults the current date or the date of the previous adjustment line.

[](/en/vista/vista/costs-and-contracts/job-cost/revenue/about-the-jc-revenue-adjustments-form)JC Revenue Adjustments

##  JC Company

 Enabled for ‘IC’ type adjustments only.
 Specify the JC company to which this contract revenue adjustment will be posted.

[](/en/vista/vista/costs-and-contracts/job-cost/revenue/about-the-jc-revenue-adjustments-form)JC Revenue Adjustments

##  Contract

 Enter the contract to which this revenue adjustment applies. Must be a
 valid contract set up in JC Contracts.
Note: If you enter a soft- or hard-closed contract and you allow posting to closed jobs (flags in JC Company Parameters), the job's status will display in red; however, entry is allowed. If you do not allow posting to closed jobs, a message displays indicating the job’s status and entry is not allowed.  
[](/en/vista/vista/costs-and-contracts/job-cost/revenue/about-the-jc-revenue-adjustments-form)JC Revenue Adjustments

##  Item

 Enter the contract item to which this revenue adjustment applies. Must be a valid item for the specified contract.

[](/en/vista/vista/costs-and-contracts/job-cost/revenue/about-the-jc-revenue-adjustments-form)JC Revenue Adjustments

##  Description

 Enter a description of this revenue adjustment, up to 60 characters.

[](/en/vista/vista/costs-and-contracts/job-cost/revenue/about-the-jc-revenue-adjustments-form)JC Revenue Adjustments

##  Units

 Specify the number of units to be adjusted. Enter negative units with a ‘–‘ sign (e.g. -1,000.000).

[](/en/vista/vista/costs-and-contracts/job-cost/revenue/about-the-jc-revenue-adjustments-form)JC Revenue Adjustments

##  Billed

 Specify the total billed amount for this adjustment. Enter negative amounts with a ‘–‘ sign (e.g. -1,250.00).

[](/en/vista/vista/costs-and-contracts/job-cost/revenue/about-the-jc-revenue-adjustments-form)JC Revenue Adjustments

## Trans Acct

Enabled only if the Allow GL Account Override When Posting
 Revenue box is checked in JC Company Parameters (GL Revenue tab).
Defaults the Open Revenue
 Acct (assigned in JC Departments) for the specified contract item's
 department. If allowing overrides and you are overriding the default, enter the GL account
 to credit or debit for this revenue adjustment. Must be a valid GL account set up (in GL
 Chart of Accounts) with a ‘Job’ or ‘null’ (blank) sub ledger code.

[](/en/vista/vista/costs-and-contracts/job-cost/revenue/about-the-jc-revenue-adjustments-form)JC Revenue Adjustments

##  Offset Acct

 Specify the GL account to use for the offsetting entry. Must be a valid GL account set up (in GL Chart of Accounts) with a ‘null’ sub ledger code.
 This account will be used any time the detail record is modified in another batch. If you do not use an offset account, then you must create another transaction to which the current transaction will balance. If you are using the Auto Reversal option, entry of an offset account is required.

[](/en/vista/vista/costs-and-contracts/job-cost/revenue/about-the-jc-revenue-adjustments-form)JC Revenue Adjustments

##  Reversal

 Specify the reversal status for this transaction.

- 0-Regular — Transaction does not need to be reversed. This type is generally used for regular revenue adjustments. If using this type, you must either enter an offset account or a balancing entry.

- 1-Auto Reverse — Transaction is to be reversed (using JC Initialize Reversals).

- 2-Reversal — Reversal Transaction. This type cannot be assigned manually; it is assigned to the reversal transaction created via JC Initialize Reversals. If you do want the transaction to be reversed, change the status to ‘4’ (Cancel Reversal).

- 3-Reversed — Original transaction has been reversed. This type cannot be assigned manually; it is assigned automatically to the original transaction once it has been reversed (i.e. the batch is processed).

- 4-Cancel Reversal — Cancel reversal transaction. This type can only be assigned to transactions with a reversal status of ‘2’ (Reversal).

[](/en/vista/vista/costs-and-contracts/job-cost/revenue/about-the-jc-revenue-adjustments-form)JC Revenue Adjustments

##  AR Info: AR Company

 Specify the source AR company to which this revenue adjustment applies. Must be a valid AR company (set up in AR Company Parameters).

[](/en/vista/vista/costs-and-contracts/job-cost/revenue/about-the-jc-revenue-adjustments-form)JC Revenue Adjustments

##  AR Info: AR Invoice

 Specify the AR invoice to which this revenue adjustment applies. Not validated.

[](/en/vista/vista/costs-and-contracts/job-cost/revenue/about-the-jc-revenue-adjustments-form)JC Revenue Adjustments

##  AR Info: AR Check

 Specify the AR check number to which this revenue adjustment applies. Not validated.

[](/en/vista/vista/costs-and-contracts/job-cost/revenue/about-the-jc-revenue-adjustments-form)JC Revenue Adjustments
