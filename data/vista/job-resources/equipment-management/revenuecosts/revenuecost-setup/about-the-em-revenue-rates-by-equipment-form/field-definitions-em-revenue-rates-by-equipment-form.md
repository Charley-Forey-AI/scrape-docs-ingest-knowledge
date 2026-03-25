---
title: "Field Definitions: EM Revenue Rates by Equipment Form | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/job-resources/equipment-management/revenuecosts/revenuecost-setup/about-the-em-revenue-rates-by-equipment-form/field-definitions-em-revenue-rates-by-equipment-form"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/job-resources/equipment-management/revenuecosts/revenuecost-setup/about-the-em-revenue-rates-by-equipment-form/field-definitions-em-revenue-rates-by-equipment-form"
---

# Field Definitions: EM Revenue Rates by Equipment Form

The following is a list of field descriptions for the EM
 Revenue Rates by Equipment form. Many of the descriptions include links to other topics that provide additional information about or related to the topic.

##  Equipment

 Specify the equipment (from EM Equipment) for which to define override revenue rates.

## Revenue Code

Specify the revenue code for which to define to revenue rate overrides.
Note: If you enter a revenue code that has not been set up by category for this equipment, the system displays a message that the revenue code is not set up in EM Revenue Rate by Category. Use EM Revenue Rates by Category (which you can access by pressing F5 from this field) to set up the revenue code before adding it here.

## Override Rates

Check this box to override the standard
 revenue rate defined for the equipment’s category/revenue code (in EM Revenue Rates by
 Category). Enter the override rate in the Rate field to the right.
Note: If you override the standard rate for a piece of equipment and multiple revenue breakdown codes exist for the category/revenue code, the system automatically moves to the Rev Breakdown grid upon saving the record. You will need to adjust the breakdown amounts to reflect the new revenue rate. If you do not adjust the breakdown amounts, you will receive a message giving you the option to update the revenue rate. If you select Yes, the override rate will be adjusted to match the existing breakdown total. If you select No, focus will remain on the Rev Breakdown grid until you adjust the breakdown amounts.
Uncheck this box to use the standard revenue usage rate for this equipment/revenue code, as defined for the equipment’s category/revenue code in EM Revenue Rates by Category.
Note: Changes made to the standard rate for the category/revenue code will be updated here.

## Rate

This field is only accessible if you checked
 the Override
 Rates box.
Note: If you are overriding rates using the Revenue Rates
 grid in EM Equipment, this field is enabled only if a single revenue breakdown code exists
 for the category/revenue code. If multiple breakdown codes exist, this field is disabled
 and you will need to enter rate overrides directly in the EM Revenue Rates by Equipment
 form (accessed by double-clicking in Revenue Rates grid).
Enter the override revenue rate for this equipment/revenue code. Initially defaults the standard usage rate defined for the equipment’s category/revenue code in EM Revenue Rates by Category.

- If you did not check the Override
 Rates box, this field defaults as 0.00.

- Overrides to the revenue rate will not update the revenue rate in EM Rates by Category. Likewise, changes made to the revenue rate in EM Revenue Rates by Category (for the category/revenue code) will not affect the override rate specified here.

- If you override the revenue rate and multiple revenue breakdown codes exist for the category/revenue code, upon saving the line, the system will automatically move to the Rev Breakdown grid to allow adjusting the breakdown amounts. If you do not adjust the amounts to incorporate the new rate, the system displays a message indicating the total of breakdown rates does not equal the revenue rate, and gives you the option to update the revenue rate. If you select Yes, the override rate will be adjusted to match the existing breakdown total. If you select No, focus will remain on the Rev Breakdown grid until you adjust the breakdown amounts

- If you are using the surcharge functionality in
 Material Sales and have assigned the specified revenue code to surcharge codes (in MS
 Surcharge Codes), this rate will be used to determine the amount of the assessed
 surcharge to credit to this equipment's revenue account when this equipment is used
 to haul materials sold to a customer, job, or inventory location (in MS Ticket
 Entry).

## Update Hour Meter

This checkbox is only accessible if the revenue code’s basis is ‘Hour’, and defaults as set for the revenue code in EM Revenue Rates by Category.
Note: This checkbox applies only to revenue codes being used for haul charges. If you are using the surcharges functionality in Material Sales and have assigned the specified revenue code to surcharge codes (in MS Surcharge Codes), the system will ignore this checkbox.
Check this box to automatically update this equipment’s hour meter in EM Equipment when posting usage to this equipment/revenue code. The system will calculate usage hours by multiplying the posted usage units by the revenue code’s Hours/Time Unit in the Equipment Master.
Uncheck this box if you do not want this equipment’s hour meter automatically updated when posting usage to this equipment/revenue code. Any updates to the hour meter for this equipment will be posted in EM Meter Readings.

## Work Units With Usage

This option defaults as set for the revenue code in EM Revenue Rates by Category.
Note: This checkbox applies only to revenue codes being used for haul charges. If you are using the surcharges functionality in Material Sales and have assigned the specified revenue code to surcharge codes (in MS Surcharge Codes), the system will ignore this checkbox.
Check this box to allow entering work units when posting usage for this equipment/revenue code. This allows posting unit progress at the same time usage is posted.
Uncheck this box if not entering work units when posting usage for this equipment/revenue code.

## Work U/M

This option defaults as set for the revenue code in EM Revenue Rates by Category.
Specify the unit of measure in which to store work units posted to this equipment/revenue code in the EM Annual Revenues (EMAR) and EM Revenue Detail (EMRD) tables.
Note: If you are using the surcharges functionality in
 Material Sales and have assigned the specified revenue code to surcharge codes (in
 MS Surcharge Codes), entry in this field is not applicable.

## Allow Posting Override

This option is only accessible if the
 Allow Rate
 Change box in EM Company Parameters (Usage tab) is checked, and defaults as
 set for the revenue code in EM Revenue Rates by Category.
Note: This checkbox applies only to revenue codes being used
 for haul charges. If you are using the surcharges functionality in Material Sales and have
 assigned the specified revenue code to surcharge codes (in MS Surcharge Codes), the system
 will ignore this checkbox.
Check this box to allow overriding the revenue rate for this equipment/revenue code during usage posting.
Uncheck this box if not allowing overrides to the revenue rate for this equipment/revenue code during usage posting.

## Revenue Breakdown Code

This field is only accessible if you checked
 the Override
 Rates box (Info tab) for the equipment/revenue code.
Initially defaults the revenue breakdown code(s) specified for the equipment’s category/revenue code (in EM Revenue Rates by Category). You can add new codes as necessary and/or delete any existing codes that are not applicable. Make sure to adjust the breakdown rates to equal the specified override rate.
Note: If the total breakdown rate does not match the override rate and you attempt to move off the tab, a message displays indicating that the breakdown total does not equal the revenue rate total, and asking if you would like to automatically update the revenue rate. If you select Yes, the equipment's override rate will be adjusted to equal that of the total breakdown rate. If you select No, you cannot exit this tab until you manually adjust the rates to match the override rate.

## Amount

This field is only accessible if you checked
 the Override
 Rates box (Info/Grid tabs) for the equipment/revenue code.
If a single breakdown code exists, this field automatically defaults to the total amount of the override revenue rate for the specified equipment/revenue code.
If multiple breakdown codes exist, this field will default the amount defined for each breakdown code in EM Revenue Rates by Category (Rev Breakdown tab). You will need to adjust the amounts accordingly to equal the specified override rate.
Note: If the total breakdown rate does not match the override rate, and you attempt to move off the tab, a message displays indicating that the breakdown total does not equal the revenue rate total, and asking if you would like to automatically update the revenue rate. If you select Yes, the equipment's override rate will be adjusted to equal that of the total breakdown rate. If you select No, you cannot exit this tab until you manually adjust the rates to match the override rate.
