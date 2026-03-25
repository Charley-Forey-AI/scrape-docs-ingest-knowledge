---
title: "About the EM Revenue Rates by Equipment Form | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/job-resources/equipment-management/revenuecosts/revenuecost-setup/about-the-em-revenue-rates-by-equipment-form"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/job-resources/equipment-management/revenuecosts/revenuecost-setup/about-the-em-revenue-rates-by-equipment-form"
---

# About the EM Revenue Rates by Equipment Form

Use this form to set up revenue usage rates at the equipment level.
Before setting up equipment/revenue combinations here, you must have set up the equipment codes in the Equipment Master and completed setup in EM Categories, EM Revenue Codes, and EM Revenue Rates by Category.

- Usage Rates and Rate Changes - For each equipment/revenue code combination you set up, you have the option to define a unique rate to use when posting usage. This is done by checking the Override Rates box and then entering the override rate in the Rate field. You will note that the Rate field automatically defaults the usage rate from EM Revenue Rates by Category for the equipment’s assigned category. Changes to the standard rate for the category will not affect overrides defined for the equipment here.Note: If you do not check the Override Rates box, the standard rate specified for the category will be used. In addition, rate changes made for the equipment's category (in EM Revenue Rates by Category) will be updated for the equipment here.

- Work Units with Usage - This option determines whether productivity for a piece of equipment will be tracked when posting usage for equipment. For example, you may want to track how many tons of rock a dump truck hauls each day over the course of a job, or the number of cubic yards moved by a bulldozer during the month. Checking this option allows work units to be posted along with usage in the EM Usage Posting form. You will need to specify the unit of measure in which to store work units posted to the equipment/revenue code in the EM Annual Revenues (EMAR) tables. During usage posting, the Work UM will default onto the posting line. If you do not override it, the work units are updated to the EM Annual Revenues and EM Revenue Detail tables. If you choose to override the default unit of measure, work units will be posted to the EM Revenue Detail (EMRD) table only. The work units are also updated to Job Cost, regardless of which unit of measure is used. As with other JC updates, units will always be updated to the JC Cost Detail table (JCCD); however, units will only be updated to the JC Cost by Period table (JCCP) if the unit of measure is the standard one for the specified phase/cost type.

- Update Hour Meter - This option can only be used with hour-based revenue codes, and indicates whether the system will automatically update the hour meter for a piece of equipment whenever posting usage to the equipment/revenue code. If checked, the system will calculate the number of hours based on the number of units entered during usage posting. For example, if you post 2 units to a weekly revenue code that has 40 hours specified as its Hours/Time Unit, the system will calculate this as 80 hours. The 80 hours are then updated to the equipment’s Hour Meter in EM Equipment.Note: The setting defined for this flag by equipment/revenue code overrides the setting defined by category.
Updates to hour meters are also controlled by the Meter Update options for Equipment Usage in EM Company Parameters. For more information, see [Meter Updates: Equipment Usage](/en/vista/vista/job-resources/equipment-management/setupmaintenance/about-the-em-company-parameters-form/field-definitions-em-company-parameters-form#ID-0000b8af--en), [Meter Updates: Costs Adj and Parts Posting](/en/vista/vista/job-resources/equipment-management/setupmaintenance/about-the-em-company-parameters-form/field-definitions-em-company-parameters-form#ID-0000b8c0--en), and [Meter Updates: Fuel Posting](/en/vista/vista/job-resources/equipment-management/setupmaintenance/about-the-em-company-parameters-form/field-definitions-em-company-parameters-form#ID-0000b8ce--en).

- Revenue Breakdown - Use this tab to define the revenue breakdown codes for each equipment/revenue code combination. For more information, see [About Revenue Breakdown Codes](/en/vista/vista/job-resources/equipment-management/revenuecosts/revenuecost-setup/about-revenue-breakdown-codes).

- Updating Revenue Rates for Equipment - You can update revenue rates automatically for a piece of equipment using the EM Revenue Rate Update form (File > EM Revenue Rate Update). See EM Revenue Rate Update in Related Topics below for more information.

Related information

- [About the EM Revenue Rates by Category Form](/en/vista/vista/job-resources/equipment-management/revenuecosts/revenuecost-setup/about-the-em-revenue-rates-by-category-form)

- [About the EM Revenue Rate Update Form](/en/vista/vista/job-resources/equipment-management/revenuecosts/revenuecost-setup/about-the-em-revenue-rate-update-form)
