---
title: "About the EM Rev Rate by Equip Template Form | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/job-resources/equipment-management/revenuecosts/revenuecost-setup/about-the-em-rev-rate-by-equip-template-form"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/job-resources/equipment-management/revenuecosts/revenuecost-setup/about-the-em-rev-rate-by-equip-template-form"
---

# About the EM Rev Rate by Equip Template Form

This form is accessed by clicking the Equipment Rates button in EM Revenue Template, and is used to override revenue rates by equipment for a specific revenue template.
A revenue rate should be set up here for every equipment/revenue code combination that you intend to use on this template. As you set up each code, the grid displays the rate and hours per time unit set up for the specified equipment/revenue code in EM Revenue Rates by Equipment. If no override rate exists, the rate specified for the equipment’s category is used.
Whether you specify a percent of the standard rate or an override rate depends on the Template Type you selected for this template in EM Revenue Template. If you selected ‘Percent of Standard Rate’, you must specify what percentage of the standard rate to use when posting usage to the category/revenue code for any job using the revenue template. If you selected the ‘Override Rate’ template type, you will need to specify the override rate to use when posting usage to the category/revenue code.
The Rev Breakdown tab is accessible only if the template type is ‘Rate Override’ and is used to define the revenue breakdown codes for each equipment/revenue code combination on a revenue template.
When you add a new revenue code, the system automatically adds a new entry using the default revenue breakdown code specified in the EM Company Parameters form. The entire amount of the override revenue rate is applied to this default breakdown code. You can enter additional breakdown codes as needed, as long as the total amount of the breakdown codes equals the total revenue rate specified for the revenue code.
Example:
Category:  BACKHOE  Revenue Code:  HOURLY  Rate:                $85/Hr  
Breakdown Code 1: Ownership Cost  $40
Breakdown Code 2: Depreciation Cost  $15
Breakdown Code 3: Fuel Cost  $10
Breakdown Code 4: Maintenance Cost  $20
Sum of Revenue Breakdown codes  $85
Note: If the template type is ‘Percent of Standard Rate’, the
 percentage rate applied to the standard rate will also be applied to the revenue
 breakdown codes defined for the equipment/revenue code in EM Revenue Rates by Equipment.

Related information

- [About the EM Revenue Template Form](/en/vista/vista/job-resources/equipment-management/revenuecosts/revenuecost-setup/about-the-em-revenue-template-form)
