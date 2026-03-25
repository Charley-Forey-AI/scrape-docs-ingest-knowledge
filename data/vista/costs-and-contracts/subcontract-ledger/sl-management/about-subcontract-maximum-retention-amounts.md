---
title: "About Subcontract Maximum Retention Amounts | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/costs-and-contracts/subcontract-ledger/sl-management/about-subcontract-maximum-retention-amounts"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/costs-and-contracts/subcontract-ledger/sl-management/about-subcontract-maximum-retention-amounts"
---

# About Subcontract Maximum Retention Amounts

When creating subcontracts in the system (SL Subcontract Entry, PM Subcontract Detail, or PM Subcontracts), you can apply a maximum retention amount.
Once the system reaches the retention amount, it will no longer continue withholding retainage on that subcontract.
To [set the maximum retention amount for a subcontract](/en/vista/vista/costs-and-contracts/subcontract-ledger/sl-management/set-maximum-retention-amounts), you will use the Maximum Retention Settings tab in SL Subcontract Entry or the Set WC Maximum Retention section in PM Subcontracts (Info tab). On this tab, you can set an amount based on a percentage of the subcontract total or you can specify a flat amount. Once you have set the amount, you can then determine how the system distributes the retention amount among the subcontract items once the maximum retention amount is reached. When you create invoices for a subcontract in SL Worksheet, the system calculates and distributes retention amounts based on the distribution option that you select.
With the Composite Percentage option, the system takes the final retention amount and calculates an overall percentage rate which it applies to all subcontract items equally.
For example, if you have set the maximum retention amount for a subcontract at $10,000, and you have already created invoices with retention amounts totaling $8,000, you will only have $2,000 left before you reach the maximum retention setting.
If you invoice $3,000 retention for two more items, the system will calculate a composite retention percentage and apply it to each item.
Table 1. Retention Amounts Prior to DistributionThis Invoice
Invoice Amount
Retention %
Retention Amount

Item #1
$10,000
10%
$1,000

Item #2
$20,000
10%
$2,000

The system uses this calculation to determine the composite retention percentage: Maximum retention remaining ($2,000) / New Invoice Items Total ($30,000) = Composite Retention Percentage (.066666). The system then updates the work complete retention percentage and work complete retention amounts based on the composite retention percentage.
Table 2. Retention Amounts After DistributionThis Invoice
Invoice Amount
Retention %
Retention Amount

Item #1
$10,000
6.67%
$668

Item #2
$20,000
6.66%
$1,332

With the Item Percentage from Invoice option, the system distributes the final retention amount based on the work complete retainage percent value for each line. The system continues to distribute in this manner until the retention amount is depleted. The system places any leftover amount on one final item on the subcontract, resulting in a calculated retention percentage value for that item only. The system sets the work complete retainage percent to zero for all remaining items on the subcontract.
The tables below display how the system would distribute the retention amount for a subcontract with a maximum retention of $400.
Table 3. Retention Amounts Prior to DistributionThis Invoice
Invoice Amount
Retention %
Retention Amount

Item #1
$1,000
10.00%
$100

Item #2
$2,000
10.00%
$200

Item #3
$3,000
10.00%
$300

Item #4
$3,000
10.00%
$300

Table 4. Retention Amounts After DistributionThis Invoice
Invoice Amount
Retention %
Retention Amount

Item #1
$1,000
10.00%
$100

Item #2
$2,000
10.00%
$200

Item #3
$3,000
3.33%
$100
* Notice how the remaining amount is added to a single subcontract item.

Item #4
$3,000
0.00%
$0

There are factors that affect how the system determines when the maximum retention amount has been reached. When you add or initialize a subcontract to a worksheet (in SL Worksheet), the system checks to see if there has been any retainage amounts withheld on any posted AP transactions, open AP batches, or unapproved invoice transactions. If there are any amounts, the system sums the amounts and applies the value towards the maximum retention amount. The AP amount(s) displays in the AP Held Retainage display field on the Retainage tab.
Additionally, if you initialize or add subcontracts to the worksheet, and if the job has a work complete percentage applied, the system will default this percentage to the % Cmpl To Date field for each subcontract item on the worksheet.
If you exceed the maximum retention amount, and you are initializing subcontracts, the system automatically distributes the retention amount based on the distribution setting for the subcontract. If you are adding an individual subcontract to the worksheet, and you exceed the maximum retention amount, the system will display a warning and you can decide whether or not to have the system automatically set the maximum retention amounts.
[About the SL Subcontract Entry Form](/en/vista/vista/costs-and-contracts/subcontract-ledger/sl-management/about-the-sl-subcontract-entry-form)
[SL Worksheet Form](/en/vista/vista/costs-and-contracts/subcontract-ledger/sl-worksheet/sl-worksheet-form)
[PM Subcontracts Form](/en/vista/vista/project-management/subcontracts/pm-subcontracts-form)
[PM Subcontract Detail Form](/en/vista/vista/project-management/subcontracts/pm-subcontract-detail-form)
