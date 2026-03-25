---
title: "About the Rounding Option for Progress Bills | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/costs-and-contracts/job-billing/setup-and-maintenance-of-job-billing/set-up-job-billing/about-the-rounding-option-for-progress-bills"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/costs-and-contracts/job-billing/setup-and-maintenance-of-job-billing/set-up-job-billing/about-the-rounding-option-for-progress-bills"
---

# About the Rounding Option for Progress Bills

The Rounding Option on the JB Contract Info form allows you to round dollar amounts on Progress bills to whole dollars.
The Rounding Option applies to Progress Billing only and determines whether you will use rounding for billing amounts. When rounding is in use, the system rounds dollar amounts to whole dollars (for example, $5.03 rounds to $5.00). Options include:

- Round Billing Only

- Round Billing and Retainage

If rounding billing amounts only, the system rounds bill amounts to the nearest whole dollar, but leaves retainage amounts reflecting dollars and cents. When the billing is printed, the "Amount Due" for the billing also reflects dollars and cents. Since the "Amount Due" calculation includes retainage (WC + Tax + RelRetg + SM - WCRetg - SMRetg), the amount due must accurately reflect the dollars and cents for retainage; therefore, it cannot be rounded.
If rounding retainage, the Report Retainage at Item Level checkbox determines how retainage is rounded. If you select the checkbox, the system rounds retainage at the item level and updates the total retainage after all the item amounts have been rounded.
For example:
Item
Retg Amt
Rounded

1
1150.20
1150.00

2
1250.50
1251.00

3
1333.69
1334.00

Total Contract :
3735.00

If the Report Retainage at Item Level checkbox is not selected, retainage is rounded at the contract and item level, with the difference between the rounded contract retainage and total items' retainage added to (or subtracted from) the last item. This ensures that the retainage total of the items is equal to the total retainage of the contract.

Ret Amount
Rounded
Adjusted

Contract
3734.39
3734.00

Item 1
1150.20
1150.00

Item 2
1250.50
1251.00

Item 3
1333.69
1334.00
1333.00

Contract Total:
3734.00

Total Item Retg:
3735.00
3734.00

Adjustment:
-1.00
