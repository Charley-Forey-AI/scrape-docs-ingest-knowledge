---
title: "Field Definitions: EM Revenue Rates by Category Form | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/job-resources/equipment-management/revenuecosts/revenuecost-setup/about-the-em-revenue-rates-by-category-form/field-definitions-em-revenue-rates-by-category-form"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/job-resources/equipment-management/revenuecosts/revenuecost-setup/about-the-em-revenue-rates-by-category-form/field-definitions-em-revenue-rates-by-category-form"
---

# Field Definitions: EM Revenue Rates by Category Form

The following is a list of field descriptions for the EM
 Revenue Rates by Category form. Many of the descriptions include links to other topics that provide additional information about or related to the topic.

##  Category

 Specify the category (from EM Categories) for which to define a revenue rate.

## Revenue Code

Specify the revenue code (from EM Revenue Codes) for which to define a revenue rate.
Note: If you are using the surcharges functionality in Material Sales, all revenue codes assigned to surcharge codes must be set up here for each material category to which they apply. The rate defined for surcharge revenue codes in this form will be used to determine the amount of the assessed surcharge that will be credited to the equipment revenue account when using any equipment in this category to haul materials sold to a customer, job, or inventory location (in MS Ticket Entry).

## Rate

Specify the usage rate for this category/revenue code. This rate will apply to all equipment within this category; however, rate may be overridden by equipment in EM Revenue Rates by Equipment.
Note: If you are using the surcharge functionality in Material Sales and have assigned the specified revenue code to surcharge codes (in MS Surcharge Codes), this rate will be used to determine the amount of the assessed surcharge to credit to the equipment revenue account when using any equipment in this category to haul materials sold to a customer, job, or inventory location (in MS Ticket Entry).

## Allow Posting Override

This field is only accessible if the
 Allow Rate
 Change box in EM Company Parameters (Usage tab) is checked.
Note: This checkbox applies only to revenue codes being used
 for haul charges. If you are using the surcharges functionality in Material Sales and have
 assigned the specified revenue code to surcharge codes (in MS Surcharge Codes), the system
 will ignore this checkbox.
Check this box to allow overriding the revenue rate for this category/revenue code during usage posting.
Leave this box unchecked if not allowing overrides to the revenue rate during usage posting.
Note: You can override this checkbox by equipment in EM Revenue Rates by Equipment.

## Work Units With Usage

This field defaults as checked for all unit-based revenue codes (as defined in EM Revenue Codes).
Note: This checkbox applies only to revenue codes being used for haul charges. If you are using the surcharges functionality in Material Sales and have assigned the specified revenue code to surcharge codes (in MS Surcharge Codes), the system will ignore this checkbox.
Check this box to allow work units to be posted with equipment usage for all equipment in this category. When checked, the Work Units input is enabled in EM Usage Posting, allowing unit progress to be posted at the same time as usage.
Leave this box unchecked if you will not be posting work units when posting usage for equipment in this category.
Note: You can override this checkbox by equipment in EM Revenue Rates by Equipment.

## Work U/M

Specify the unit of measure in which work units posted to this category/revenue code will be stored in the EM Annual Revenues (EMAR) and EM Revenue Detail (EMRD) tables. Initially defaults as defined for the revenue code in EM Revenue Codes.
Note: If you are using the surcharges functionality in
 Material Sales and have assigned the specified revenue code to surcharge codes (in
 MS Surcharge Codes), entry in this field is not applicable.

## Update Hour Meter

This checkbox is only accessible for hour-based revenue and defaults as set for this revenue code in EM Revenue Codes.
Note: This checkbox applies only to revenue codes being used for haul charges. If you are using the surcharges functionality in Material Sales and have assigned the specified revenue code to surcharge codes (in MS Surcharge Codes), the system will ignore this checkbox.
Check this box to update equipment hour meters when posting usage posting to this category/revenue code. The system will calculate the hours for a meter based on the number of units entered during usage posting. For example, if you post 2 units to a weekly revenue code and the weekly code has 40 hours as its Hours/Time Unit, the system will update 80 hours to the equipment’s hour meter (EM Equipment).
Leave this box unchecked if you do not want equipment hour meters updated automatically when posting usage to this category/revenue code.
Note: You can override this checkbox by equipment in EM Revenue Rates by Equipment.

##  Revenue Breakdown Code

 Enter a valid revenue breakdown code for this category. Initially defaults the revenue breakdown code specified in EM Company Parameters. If the default code is not applicable, you must delete the code; it cannot be changed.

## Amount

Enter the amount for this revenue breakdown code. Initially defaults the total amount of the revenue rate specified for the revenue code.
Note: The sum of all breakdown codes must equal the total of the revenue rate. If it does not match, a message displays informing you that the combined total of breakdown rates does not equal the revenue rate and asks if you want to update the revenue rate. If you answer ‘Yes’, the revenue rate will be changed to equal the total of the revenue breakdown rates. However, if the revenue rate is correct, answer ‘No’ to the prompt, and then correct the amounts of the breakdown rates to reflect the total revenue rate.
