---
title: "Field Definitions: JC Cost Adjustments Form | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/costs-and-contracts/job-cost/costs/about-the-jc-cost-adjustments-form/field-definitions-jc-cost-adjustments-form"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/costs-and-contracts/job-cost/costs/about-the-jc-cost-adjustments-form/field-definitions-jc-cost-adjustments-form"
---

# Field Definitions: JC Cost Adjustments Form

The following is a list of field descriptions for the JC Cost
 Adjustments form. Many of the descriptions include links to other topics that provide additional information about or related to the topic.

##  Seq #

 Enter the sequence number of an existing entry or enter N, New, or + to add a new sequence. The system will automatically assign the next available sequential number.

[](/en/vista/vista/costs-and-contracts/job-cost/costs/about-the-jc-cost-adjustments-form)JC Cost Adjustments

##  Action

 When entering a new transaction, this field defaults to A (Add) and cannot be accessed.
 If this is an existing transaction, specify the action for this entry.
 C = Change. Use this action to make changes to transactions that have already been processed.   D = Delete. Use this action to delete the transaction from all files in JC. (The delete functions in the toolbar and Records menu will only delete the entry from the batch.)

[](/en/vista/vista/costs-and-contracts/job-cost/costs/about-the-jc-cost-adjustments-form)JC Cost Adjustments

## JC Type

The JC Type field on the JC Cost Adjustments form, Info tab.
 Indicate the source of the original transaction for which you are making the cost adjustment.

- JC-Job Cost - Select this type if this
 adjustment applies to a Job Cost transaction.

- CA-Cost Allocations - This type is
 automatically assigned to cost adjustment entries added to the batch via JC Process Cost
 Allocations. If you try to select this option, you will see an error.

- AP-Accounts Payable - Select this type if
 this adjustment applies to an Accounts Payable transaction.

- EM-Equipment - Select this type if this
 adjustment applies to an equipment transaction.

- MO-Material Order - Select this type if
 this adjustment applies to a material order transaction.

- MS-Material Sales - Select this type if
 this adjustment applies to a Material Sales transaction.

- PR-Payroll - Select this type if this
 adjustment applies to a Payroll transaction.

- IC-Inter Company - Select this type if
 this adjustment applies to an intercompany job cost transaction.

The Accounts Payable, Equipment, Material, and Payroll tabs allow you to enter additional information related to AP, EM, MO/MS, and PR entries. For example, for AP-related adjustments, the Accounts Payable tab allows you to specify the applicable associated company, vendor, reference number, and if applicable, the purchase order/item or subcontract/item.
Note: Although the source description for the transaction
 will always be JC CostAdj, the JC Type allows you to identify the actual source here. It also
 determines what additional fields are made available in which to put corresponding
 information.
[](/en/vista/vista/costs-and-contracts/job-cost/costs/about-the-jc-cost-adjustments-form)JC Cost Adjustments

##  Date

 Specify the date that will be the ‘actual’ date for this transaction in the JCCD (Cost Detail) table. Initially defaults the current date or the date of the previous adjustment line.
Date field shortcuts
T or t
Set the date to the current date.

MMDD
Four digit month and day
Enter a four digit month and date (MMDD) and the system will automatically add the current year.

+
The system will automatically set the date to tomorrow.

+5
The system will automatically set the date to 5 days in the future.
You can actually enter any value after the +, for
 example you can enter +7 to set the date to next week.

-
The system will automatically set the date to the previous day.

-5
The system will automatically set the date to 5 days in the past.
Just like with +, you can enter any value after the
 -, for example you can enter -7 to set the date to the
 previous week.

[](/en/vista/vista/costs-and-contracts/job-cost/costs/about-the-jc-cost-adjustments-form)JC Cost Adjustments

##  Company

 Enabled for ‘IC’ type adjustments only.
 Specify the JC company to which this cost adjustment applies.

[](/en/vista/vista/costs-and-contracts/job-cost/costs/about-the-jc-cost-adjustments-form)JC Cost Adjustments

## Job

Specify to which job this cost adjustment applies.
Closed jobs
If you enter a soft- or hard-closed job and you allow posting to closed jobs (flags in JC Company Parameters), “Soft-Closed” or “Hard-Closed” will appear in red to the right of the job description; however, entry is allowed. If you do not allow posting to closed jobs, a message displays indicating the job’s status and entry is not allowed.

[](/en/vista/vista/costs-and-contracts/job-cost/costs/about-the-jc-cost-adjustments-form)JC Cost Adjustments

##  Phase

 Specify the phase to which this cost adjustment will be posted.

[](/en/vista/vista/costs-and-contracts/job-cost/costs/about-the-jc-cost-adjustments-form)JC Cost Adjustments

##  Cost Type

 Specify the cost type to which this cost adjustment applies.

[](/en/vista/vista/costs-and-contracts/job-cost/costs/about-the-jc-cost-adjustments-form)JC Cost Adjustments

##  Description

 Enter a description of this cost adjustment, up to 60 characters.

[](/en/vista/vista/costs-and-contracts/job-cost/costs/about-the-jc-cost-adjustments-form)JC Cost Adjustments

## Field Ticket

The Field Ticket field on the JC Cost Adjustments form.
Enter the field ticket number for this cost adjustment entry or press F4 to select from a list of valid field tickets for the specified job/contract.Note: Costs associated with approved field tickets only impact T&M billings; therefore, assigning field tickets to cost adjustments is only useful if the job's contract/contract item has a bill type of T&M or Both.

For more information about field tickets, see [JC Field Ticket Form](/en/vista/vista/costs-and-contracts/job-cost/jobs-and-contracts-setup/jc-field-ticket-form).

##  Hours

 Enabled only if tracking hours for the cost type (flag in JC Cost Types).
 Specify the number of hours to be adjusted. Enter negative hours with a ‘–‘ sign (e.g. -16.00).
Note: If the Trans Acct specified for this cost adjustment is assigned a Cross Reference Memo Acct (in GL Chart of Accounts), the hours specified here will be updated to the memo account.  
[](/en/vista/vista/costs-and-contracts/job-cost/costs/about-the-jc-cost-adjustments-form)JC Cost Adjustments

##  Units

 Specify the number of units to be adjusted. Enter negative units with a ‘–‘ sign (e.g. -1,000.000).

[](/en/vista/vista/costs-and-contracts/job-cost/costs/about-the-jc-cost-adjustments-form)JC Cost Adjustments

##  Cost

 Specify the total cost for this adjustment. Enter negative amounts with a ‘–‘ sign (e.g. -1,250.00).

[](/en/vista/vista/costs-and-contracts/job-cost/costs/about-the-jc-cost-adjustments-form)JC Cost Adjustments

## Trans Acct

If no default account was specified, or if allowing overrides and
 you are overriding the default, enter the GL account to charge for this cost adjustment.
 Must be a valid GL account set up (in GL Chart of Accounts) with a ‘Job’ or ‘null’ sub
 ledger code.
If this is an intercompany transaction
 (JC
 Type is IC-Intercompany), the account specified here must be a valid GL
 account for the To
 JCCo company specified above.
Why is this field disabled?
This field is enabled if one of the two conditions apply:

- TheAllow GL Account override when posting
 costs box is checked in JC Company Parameters (GL Cost tab) on the
 company selected in the To JCCo field

-or-

- The Allow GL Account override when posting
 costs box is unchecked on the company selected in the To JCCo
 field, but the GL account defaults as null (blank).
Where is the default GL account set up?

The transaction GL account defaults as follows:

- If an override account is defined for the phase in
 JC Departments (Phase Overrides tab), defaults the override account.

- If no override account is defined for the phase,
 defaults the GL account defined for the specified cost type in JC Departments (Cost
 Types tab).

- If no GL account specified at either the phase or
 cost type level (in JC Departments), defaults as null.

[](/en/vista/vista/costs-and-contracts/job-cost/costs/about-the-jc-cost-adjustments-form)JC Cost Adjustments

## Offset Acct

Specify the GL account to use for the offsetting entry. Must be a valid GL account set up (in GL Chart of Accounts) with a ‘null’ (blank) sub ledger code.
This account will be used any time the detail record is modified in another batch. If you do not use an offset account, then you must create another transaction to which the current transaction will balance. If you are using the Auto Reversal option, entry of an offset account is required.
Note: If this is an intercompany transaction (JC Type is
 IC-Intercompany), the account specified here must be a valid GL account for the active JC
 company (i.e. the 'from JC company).
[](/en/vista/vista/costs-and-contracts/job-cost/costs/about-the-jc-cost-adjustments-form)JC Cost Adjustments

## Reversal

Specify the reversal status for this transaction.

- 0-Regular— Transaction does not need to be reversed. This type is generally used for regular cost adjustments. If using this type, you must either enter an offset account or a balancing entry.

- 1-Auto Reverse — Transaction is to be reversed (using JC Initialize Reversals).

- 2-Reversal— Reversal Transaction. This type cannot be assigned manually; it is assigned to the reversal transaction created via JC Initialize Reversals. If you do want the transaction to be reversed, change the status to ‘4’ (Cancel Reversal).

- 3-Reversed— Original transaction has been reversed. This type cannot be assigned manually; it is assigned automatically to the original transaction once it has been reversed (i.e. the batch is processed).

- 4-Cancel Reversal — Cancel reversal transaction. This type can only be assigned to transactions with a reversal status of ‘2’ (Reversal).

[](/en/vista/vista/costs-and-contracts/job-cost/costs/about-the-jc-cost-adjustments-form)JC Cost Adjustments

##  Accounts Payable: AP Company

 Specify the source AP company (from AP Company Parameters) for this cost adjustment entry. The company’s assigned Vendor Group displays to the far right of this field.

[](/en/vista/vista/costs-and-contracts/job-cost/costs/about-the-jc-cost-adjustments-form)JC Cost Adjustments

##  Accounts Payable: Vendor

 Specify the vendor to which this cost adjustment applies. Must be a valid vendor (set up in
 AP Vendors) for the specified AP company.

[](/en/vista/vista/costs-and-contracts/job-cost/costs/about-the-jc-cost-adjustments-form)JC Cost Adjustments

##  Accounts Payable: AP Reference

The AP Reference field on the JC Cost Adjustments form, Accounts Payable tab.
 Enter the AP reference number to which this cost adjustment applies, up to 30 characters. Typically, this is the invoice number supplied by the vendor.

## Accounts Payable: Purchase Order

Enter the purchase order that the cost adjustment applies to. This must be a valid purchase order set up in PO Entry or interfaced from PM.

[](/en/vista/vista/costs-and-contracts/job-cost/costs/about-the-jc-cost-adjustments-form)JC Cost Adjustments

##  Accounts Payable: Item

 Enter the purchase order item to which this cost adjustment applies. Must be a valid item for the specified purchase order.

[](/en/vista/vista/costs-and-contracts/job-cost/costs/about-the-jc-cost-adjustments-form)JC Cost Adjustments

##  Accounts Payable: Subcontract

 Enter the subcontract to which this cost adjustment applies, if applicable. Must be a valid subcontract set up in SL Entry or interfaced from PM.

[](/en/vista/vista/costs-and-contracts/job-cost/costs/about-the-jc-cost-adjustments-form)JC Cost Adjustments

##  Accounts Payable: Item

 Enter the subcontract item to which this cost adjustment applies. Must be a valid item for the specified subcontract.

[](/en/vista/vista/costs-and-contracts/job-cost/costs/about-the-jc-cost-adjustments-form)JC Cost Adjustments

##  Equipment: EM Company

 Specify the source EM company (from EM Company Parameters) for this cost adjustment transaction. The company’s assigned EM Group displays to the far right of this field.

[](/en/vista/vista/costs-and-contracts/job-cost/costs/about-the-jc-cost-adjustments-form)JC Cost Adjustments

##  Equipment: Equipment

 Enter the equipment to which this cost adjustment applies. Must be a valid equipment (set up in EM Equipment) for the specified EM company.

[](/en/vista/vista/costs-and-contracts/job-cost/costs/about-the-jc-cost-adjustments-form)JC Cost Adjustments

##  Equipment: Revenue Code

 Specify the revenue code for this cost adjustment transaction. Must be a valid revenue code set up in EM Revenue Codes for the specified EM company.

[](/en/vista/vista/costs-and-contracts/job-cost/costs/about-the-jc-cost-adjustments-form)JC Cost Adjustments

##  Material: IN Company

 Specify the source IN company (from IN Company Parameters) for this cost adjustment transaction. The company’s assigned Material Group displays to the far right of this field.

[](/en/vista/vista/costs-and-contracts/job-cost/costs/about-the-jc-cost-adjustments-form)JC Cost Adjustments

##  Material: Location

 Enter the location to which this cost adjustment transaction applies. Must
 be a valid location (set up in IN Locations) for the specified IN company.

[](/en/vista/vista/costs-and-contracts/job-cost/costs/about-the-jc-cost-adjustments-form)JC Cost Adjustments

##  Material: Material

 Enter the material to which this cost adjustment applies. Must be a valid material set up in HQ Materials for the specified IN Company.

[](/en/vista/vista/costs-and-contracts/job-cost/costs/about-the-jc-cost-adjustments-form)JC Cost Adjustments

##  Material: MO

 Enter the material order to which this cost adjustment applies, if applicable. Must be a valid material order set up in IN Material Order or interfaced from PM.

[](/en/vista/vista/costs-and-contracts/job-cost/costs/about-the-jc-cost-adjustments-form)JC Cost Adjustments

##  Material: Item

 Enter the material order item to which this cost adjustment applies. Must be a valid item for the specified material order.

[](/en/vista/vista/costs-and-contracts/job-cost/costs/about-the-jc-cost-adjustments-form)JC Cost Adjustments

##  Payroll: PR Company

 Specify the source PR company (from PR Company Parameters) for this cost adjustment transaction.

[](/en/vista/vista/costs-and-contracts/job-cost/costs/about-the-jc-cost-adjustments-form)JC Cost Adjustments

##  Payroll: Employee

 Enter the employee to which this cost adjustment applies. Must be a valid employee set up in PR Employees for the specified PR company.

[](/en/vista/vista/costs-and-contracts/job-cost/costs/about-the-jc-cost-adjustments-form)JC Cost Adjustments

##  Payroll: Craft

 Specify the craft for this cost adjustment transaction. Must be a valid craft set up in PR
 Crafts for the specified PR company.

[](/en/vista/vista/costs-and-contracts/job-cost/costs/about-the-jc-cost-adjustments-form)JC Cost Adjustments

##  Payroll: Class

 Specify the class for this cost adjustment transaction. Must be a valid craft set up in PR
 Crafts for the specified PR company.

[](/en/vista/vista/costs-and-contracts/job-cost/costs/about-the-jc-cost-adjustments-form)JC Cost Adjustments

##  Payroll: Crew

 Specify the crew for this cost adjustment transaction. Must be a valid crew set up in PR Crews for the specified PR company.

[](/en/vista/vista/costs-and-contracts/job-cost/costs/about-the-jc-cost-adjustments-form)JC Cost Adjustments

##  Payroll: Earnings Factor

 Specify the earnings factor (e.g. 1.0, 1.5, 2.0) for this cost adjustment transaction.

[](/en/vista/vista/costs-and-contracts/job-cost/costs/about-the-jc-cost-adjustments-form)JC Cost Adjustments

##  Payroll: Earnings Type

 Specify the earnings type for this cost adjustment transaction. Must be a valid earnings type set up in HQ Earnings Types.

[](/en/vista/vista/costs-and-contracts/job-cost/costs/about-the-jc-cost-adjustments-form)JC Cost Adjustments

##  Payroll: Shift

 Enter the shift (0-255) to which this cost adjustment transaction applies.

[](/en/vista/vista/costs-and-contracts/job-cost/costs/about-the-jc-cost-adjustments-form)JC Cost Adjustments

##  Payroll: Liability Type

 Enter the liability type for this cost adjustment transaction. Must be a valid liability type set up in HQ Liability Types.

[](/en/vista/vista/costs-and-contracts/job-cost/costs/about-the-jc-cost-adjustments-form)JC Cost Adjustments
