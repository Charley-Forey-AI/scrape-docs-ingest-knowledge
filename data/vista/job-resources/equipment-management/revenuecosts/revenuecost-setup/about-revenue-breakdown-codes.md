---
title: "About Revenue Breakdown Codes | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/job-resources/equipment-management/revenuecosts/revenuecost-setup/about-revenue-breakdown-codes"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/job-resources/equipment-management/revenuecosts/revenuecost-setup/about-revenue-breakdown-codes"
---

# About Revenue Breakdown Codes

When setting up revenue rates, whether by category, equipment, or revenue template, the revenue codes you assign are used to determine the rates that will be applied when posting usage.
For each revenue code that you set up for the category (or equipment), you can define revenue breakdown codes, which will allow you to break down the revenue rates into the portion of the rate assigned to different aspects of operation, such as ownership, maintenance, fuel, and so forth. These can be linked to the cost codes to report costs vs. revenue at this level.
Using revenue breakdown codes gives you the ability to compare the costs of owning and operating your equipment (i.e. interest, depreciation, fuel, and maintenance) to the revenue generated from owning and operating your equipment (usage). This comparison allows you to determine whether it is profitable for you to continue ownership of the equipment, or whether it will be more profitable for you to rent the equipment.
When a revenue code is entered for a category or equipment, a default revenue breakdown code is automatically assigned, with the total revenue rate applied to that code. The default breakdown code used is determined by which program you are in when setting up revenue rates. If you are setting them up by category (EM Revenue Rates by Category), the default revenue breakdown code specified in EM Company Parameters is used. If you are setting them up by equipment (EM Revenue Rates by Equipment), and you do not check the Override Rates option, then the revenue breakdown codes specified for the category are used. Otherwise, the default revenue breakdown code specified in the company file is used.
Default breakdown codes can be deleted, but you must set up at least one revenue breakdown code to replace it. If you want a more detailed breakdown of the revenue rate, then add additional breakdown codes until you are satisfied with the breakdown level. Keep in mind that the sum of all revenue breakdown codes must equal the total revenue rate for the revenue code.
For example:
Equip #:
10101

Rev Code:
Hourly

Rate:
$100/Hr

Breakdown Code
Description
Amount

1
Ownership
(cost of ownership)
$40

2
Depreciation
(cost of depreciation)
$20

3
Fuel
(cost of fuel used)
$15

4
Maintenance
(maintenance costs)
$25

Sum of Breakdown codes:
$100
