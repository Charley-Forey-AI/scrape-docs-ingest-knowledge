---
title: "Field Definitions: AR Miscellaneous Receipts Form | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/accounting/accounts-receivable/cash-receipts/about-the-ar-miscellaneous-receipt-lines-form/field-definitions-ar-miscellaneous-receipts-form"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/accounting/accounts-receivable/cash-receipts/about-the-ar-miscellaneous-receipt-lines-form/field-definitions-ar-miscellaneous-receipts-form"
---

# Field Definitions: AR Miscellaneous Receipts Form

The following is a list of field descriptions for the AR Miscellaneous Receipts form. Many of the descriptions include links to other topics that provide additional information about or related to the topic.

##  Seq #

 Enter the sequence number of an existing entry or enter “N”, “New”, or “+” to add a new sequence. The system automatically assigns the next available sequential number.

##  ARTrans

 This field is display-only and shows the system-assigned transaction number. The system assigns transaction numbers during batch posting. This field displays a transaction only when you pull a previously posted transaction into a batch.

## Trans Date

Enter the transaction date for this miscellaneous receipt. The field defaults the current date.
If the date is not in the current batch month, a warning displays, but the system allows entry.
Note: The system records this date as the “paid date.” The system uses this date in the calculation of Average Days to Pay shown in the AR Credit Inquiry Drilldown report. The date may also determine the date paid for calculation of finance/service charges and is part of the aging routine if payments after the aging date are excluded.

##  Check #

 Enter the check number (up to 10 characters) for this receipt.

##  Check Date

 Enter the check date. This field defaults the current date. The system uses this date as a reference only; aging routines use the transaction date.)

##  Check Amt

 Enter the total amount of the check (up to 16 digits). The system uses this amount to balance the Total Amount applied with the amount of the check.

##  CM Co

 Specify the CM company for receipt posting.

##  CM Account

 Specify the CM bank account (as defined in CM Accounts) for this transaction. Typically, this will be the depositing bank account.

##  Deposit #

 Enter the reference number (up to 10 characters) for this deposit. Use this transaction number to create deposit slips and modify deposits within Cash Management.
Note: All checks entered with the same CM Account and
 Deposit # update the same CM deposit transaction. Additionally, if you enter multiple
 transaction dates for a single deposit number, the system uses the most recent transaction
 date as the CM deposit transaction date.

##  Description

 Enter a description for this miscellaneous cash receipt transaction, up to 30 characters.

##  AR Line

 Enter an existing line number or enter “N”, “New”, or “+” to add a new line. The system automatically assigns the next sequential line number.

## Type

The Type field on the AR Miscellaneous Receipt Lines form.
Select the line type for this miscellaneous receipt transaction:

- O-Other – Use this type for all non-job, non-equipment cash receipts, such as over-the-counter sales, plan deposits, or any other miscellaneous cash receipt that only credits a GL account.

- J-Job – Use this type for job-related miscellaneous receipts, typically useful for posting refunds that reduce job costs.

- E-Equipment – Use this type for equipment-related miscellaneous receipts, typically useful for posting refunds that reduce equipment costs.

- S-SM Work Order - Use this type for SM work order-related miscellaneous receipts (such as posting refunds that reduce work order costs).

##  Description

 Enter a description of this line item, up to 30 characters.

##  JCCo

 Specify the Job Cost company that applies to this line.

##  Job

 Specify the job to credit with this transaction.

##  Phase

 Enter
 the job phase to credit with this transaction. If you selected the Lock Phases checkbox in
 JC Jobs, enter a phase that has been set up for the job in JC Job Phases.

##  EM Co

 Specify the EM company that applies to this line.

##  Equip

 Specify the equipment to credit with this transaction.

##  Comp Type

 If this line applies to a component of the equipment, specify the component type.

##  Component

 If applicable, specify the component that applies to this line. If you selected the Post Costs to Components checkbox (in EM Equipment) for the attached equipment, the system credits the component with this transaction.

##  Cost Code

 Specify a valid cost code (from EM Cost Codes) for this equipment. If you specified a component, this field defaults the cost code defined for the component type in EM Component Types. The system allows overrides to the default.

##  EM Cost Type

 Enter the cost type for the specified equipment/cost code. This must be a valid EM cost type defined for the specified cost code (in EM Cost Codes).

##  Cost Type

 Enter
 a valid cost type for the specified phase. If you selected the Lock Phases checkbox in JC
 Jobs, enter a cost type assigned to the phase in JC Job Phases.

##  Act Date

 Enter the actual date for this miscellaneous receipt. This is the date the system credits payment to the job or equipment, depending on the line type.

## GL Acct

Enter the GL account for this miscellaneous cash receipt
 transaction line, or press F4 for a list of GL accounts.
The initial default depends upon the specified line type:

- Other – Defaults as null.

- Job – Defaults to the cost type or phase override
 Open WIP
 Acct or Closed WIP Acct (if job/contract
 closed and you allow posting to closed jobs) defined for the contract item's
 department in JC Departments.

Note: If this is a previously posted transaction and the
 posted job is closed, this field may default the Open WIP Acct; however, the batch process
 will correctly post the line's amount to the Closed WIP Acct.

- Equip – Defaults to the GL account
 for the cost type or cost code (if override GL account by cost code) from the
 department assigned to the equipment.

 If this miscellaneous cash receipt transaction line is intended to process the refund of a purchase amount previously paid to a vendor, and not to record a new sale, select a GL account whose Account Type is E-Expense (set in [GL Chart of Accounts](/en/vista/vista/accounting/general-ledger/gl-accounts/about-the-gl-chart-of-accounts-form)).

##  Tax Code

 This field is accessible if the line type is “Other” and you allow posting taxes on receipts (On Receipts checkbox in AR Company Parameters).
 If applicable, specify the tax code to use when calculating taxes for this transaction line.

## UM

This field is accessible for Job and Equip line types only.
Enter the unit of measure for this line. Defaults the unit of measure assigned to the specified cost type.

##  Hours

 This field is accessible only for “Job” lines (if cost type is tracking hours) and “Equip” lines.
 If applicable, enter the number of hours for this line.

##  Units

 Enter the number of units for this line.

## Amount

Enter the payment amount to credit to this line. If you are applying taxes (“Other” line types only), enter the pre-tax amount. For example, if the total is $525.00, and the tax amount is $25.00, enter $500.
If you are posting a job or equipment line, do not enter the amount as a negative. The system automatically subtracts assumes the amount from the job or equipment expenses.

## Tax Basis

This field is accessible if line type is “Other” and you allow posting taxes on receipts (On Receipts checkbox in AR Company Parameters).
If applicable, enter the amount for calculating this receipt’s taxes. This field initially defaults the line’s Amount; you should only need to change this amount if it differs from the line’s Amount.

## Tax Amount

This field is accessible if line type is “Other” and you allow posting taxes on receipts (On Receipts checkbox in AR Company Parameters).
This field automatically defaults an amount based on the Tax Code specified for this line and the line’s Tax Basis.
Note: The line’s Amount must reflex the pre-tax amount. For example, if the Total Amount to be applied is 1060.00, and the Tax Amount is 60.00, enter the line’s Amount as 1000.00. If you override the tax amount calculation, adjust the line’s Amount to ensure the Total Amount to be applied is accurate.

##  Total Amount

 This field is display only, showing the total amount applied to this line, including tax (if applicable).
