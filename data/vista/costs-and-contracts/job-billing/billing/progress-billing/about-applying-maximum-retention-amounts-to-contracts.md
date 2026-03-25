---
title: "About Applying Maximum Retention Amounts to Contracts | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/costs-and-contracts/job-billing/billing/progress-billing/about-applying-maximum-retention-amounts-to-contracts"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/costs-and-contracts/job-billing/billing/progress-billing/about-applying-maximum-retention-amounts-to-contracts"
---

# About Applying Maximum Retention Amounts to
 Contracts

When creating contracts in the system, you can apply a maximum
 retention amount.
Once the system reaches the
 retention amount, it will no longer continue withholding retainage for a
 specified contract.
To set the maximum retention amount
 for a contract, you will use the Set WC Maximum Retention section in either
 JC Contracts or PM Contracts. Using these forms, you can set an amount based
 on a percentage of the contract total or you can specify a flat amount. Once
 you have set the amount, you can then determine how the system distributes
 the retention amount among the contract items once the maximum retention
 amount is reached. When you create invoices for the contract (either
 manually using JB Progress Billing or automatically using JB Bill
 Initialization), the system calculates and distributes retention amounts
 based on the distribution option that you select.
There are two options for retention
 amount distribution:

- Composite Percentage
 - With this option, the system takes the final retention
 amount and calculates an overall percentage rate which it
 applies to all contract items equally.

- Item Percentage from
 Invoice - With this option, the system distributes the final
 retention amount based on the work completed retainage
 percent value for each line. The system continues to
 distribute in this manner until the retention amount is
 depleted. The system places any leftover amount on one final
 item on the contract, resulting in a calculated retention
 percentage value for that item only. The system sets the
 work completed retainage percent to zero for all remaining
 items on the contract.

## Composite Percentage

If you have set the maximum
 retention amount for a contract at $10,000, and you have already
 created invoices with retention amounts totaling $8,000, you will
 only have $2,000 left before you reach the maximum retention
 setting. If you invoice $3,000 retention for two more items (as seen
 in Table 1), the system will calculate a composite retention
 percentage and apply it to each item.
The system uses this
 calculation to determine the composite retention percentage: Maximum
 retention remaining ($2,000) / New Invoice Items Total ($30,000) =
 Composite Retention Percentage (.066666). The system then updates
 the work completed retention percentage and work completed retention
 amounts based on the composite retention percentage (as seen in
 Table 2).
Table 1. Retention
 Amounts Prior to DistributionThis Invoice
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

Table 2. Retention
 Amounts After DistributionThis Invoice
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

## Item Percentage from Invoice

- Tables 3 and
 4 display how the system would distribute the
 retention amount for a contract with a maximum
 retention of $400. Table 3 shows the retention
 amounts prior to distribution, while Table 4
 displays the retention amounts after the
 distribution.
Table 3. Retention Amounts Prior to
 DistributionThis Invoice
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

Table 4. Retention Amounts After
 DistributionThis Invoice
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

Item #4
$3,000
0.00%
$0

If you exceed the maximum
 retention amount, and you are initializing contracts, the system
 automatically distributes the retention amount based on the
 distribution setting for the contract. If you are adding an
 individual contract to the worksheet, and you exceed the maximum
 retention amount, the system will display a warning and you can
 decide whether or not to have the system automatically set the
 maximum retention amounts.
