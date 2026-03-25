---
title: "About the EM Revenue Breakdown Codes Form | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/job-resources/equipment-management/revenuecosts/revenuecost-setup/about-the-em-revenue-breakdown-codes-form"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/job-resources/equipment-management/revenuecosts/revenuecost-setup/about-the-em-revenue-breakdown-codes-form"
---

# About the EM Revenue Breakdown Codes Form

Use this form to set up and maintain revenue breakdown codes.
These codes are used to break down revenue rates into the portion of the rate assigned to different aspects of operation, such as ownership, maintenance, fuel, and so forth.
At least one revenue breakdown code must be established and assigned as the Default Revenue Breakdown Code in EM Company Parameters as the Default Revenue Breakdown Code. Whenever a new revenue rate is established in EM Revenue Rates by Category, or overridden by equipment (in EM Revenue Rates by Equipment) or template (in EM Revenue Template), the entire amount is assigned to the default breakdown code. You can override this assignment using the Rev Breakdown grid provided in the related revenue rates form.
When defining the revenue breakdown for revenue rates, the sum of the revenue breakdown codes must equal the revenue rate.
Example
Equipment:  10101  Revenue Code:  HOURLY  Rate:                $85/Hr
Breakdown Code 1: Ownership Cost  $40
Breakdown Code 2: Depreciation Cost  $15
Breakdown Code 3: Fuel Cost  $10
Breakdown Code 4: Maintenance Cost  $20
Sum of Revenue Breakdown codes  $85
Whenever usage is posted to a piece of equipment, the revenue files record the total revenue, as well as the detail of the revenue associated with each revenue breakdown code. So, if 4 Hours of usage are posted to 10101 using revenue code HOURLY, the EMRD (Revenue Detail) file will be updated with $340 of usage as follows:
Code 1  $160   (4 * $40)
Code 2  60   (4 * $15)
Code 3  40   (4 * $10)
Code 4      80   (4 * $20)
Total  $340
Note: The EM Cost Codes form provides a field to store the revenue breakdown code so that reports can be run that compare hourly costs to the hourly revenue charges.

Related information

- [About the EM Revenue Rates by Category Form](/en/vista/vista/job-resources/equipment-management/revenuecosts/revenuecost-setup/about-the-em-revenue-rates-by-category-form)

- [About the EM Revenue Rates by Equipment Form](/en/vista/vista/job-resources/equipment-management/revenuecosts/revenuecost-setup/about-the-em-revenue-rates-by-equipment-form)

- [About the EM Revenue Template Form](/en/vista/vista/job-resources/equipment-management/revenuecosts/revenuecost-setup/about-the-em-revenue-template-form)
