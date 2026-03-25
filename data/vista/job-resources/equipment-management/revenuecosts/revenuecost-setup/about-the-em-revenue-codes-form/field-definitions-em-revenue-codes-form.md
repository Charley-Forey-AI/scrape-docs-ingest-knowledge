---
title: "Field Definitions: EM Revenue Codes Form | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/job-resources/equipment-management/revenuecosts/revenuecost-setup/about-the-em-revenue-codes-form/field-definitions-em-revenue-codes-form"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/job-resources/equipment-management/revenuecosts/revenuecost-setup/about-the-em-revenue-codes-form/field-definitions-em-revenue-codes-form"
---

# Field Definitions: EM Revenue Codes Form

The following is a list of field descriptions for the EM
 Revenue Codes form. Many of the descriptions include links to other topics that provide additional information about or related to the topic.

##  Revenue Code

 Enter a code, up to 10 characters, that uniquely identifies a time increment in which you bill out equipment to jobs (e.g. Hourly, Daily, Weekly, or Monthly).

##  Description

 Enter a description of this revenue code, up to 30 characters.

##  Revenue Basis

- Hour – Select this option if revenue is to be measured in hours for this revenue code. You will need to specify the Time U/M and Hours/Time Unit below.

- Unit – Select this option if revenue is to be measured in units for this revenue code. You will need to specify the Work U/M below.

##  Time U/M

 This field is only accessible if the revenue basis is ‘Hour’.
 Specify the time measurement (from HQ Units of Measure) that applies to this revenue code. For example:
Rev Code      Time U/M
HOURLY               HRS
DAILY                     DAY
MONTHLY             MOS

## Monthly Revenue Code

This field is only enabled when Hour is
 selected in the Revenue Basis field.
Check this box to allow rounding monthly hours
 when running automatic usage. When checked, the Hours/Time Unit field is disabled, since
 total billable hours can vary by month. When auto usage is run in [EM Automatic Usage ](/en/vista/vista/job-resources/equipment-management/revenuecosts/revenuecost-processing/about-the-em-automatic-usage-form), if a piece of equipment using this
 revenue code has been on one or more jobs during the month (i.e. hits the hours threshold
 for the rules table), the system will set the total units to 1.00, regardless of how many
 hours are in the month.
Note: To use this feature correctly, it is important that
 you do not span more than one month's time in a billing period (e.g. begin date 03/01/19,
 end date 04/30/19). Since the time unit will always total 1.00, the system cannot determine
 the hourly breakdown per month. You can, however, span one month's time over two months
 (e.g. begin date 03/15/19, end date 04/15/19).
Leave this box unchecked if not rounding monthly hours when running automatic usage.

##  Hours/Time Unit

 This field is only accessible if the revenue basis is ‘Hour’.
 Specify the number of hours in one unit of the Time U/M specified for this revenue code. For example, there is 1 hour in an HRS time unit, 8 hours in a DAILY time unit, and 173.333 hours (on average) in a MOS time unit. This number is used whenever the system needs to convert time to hours, such as when the hour meter is updated.

##  Work U/M

 This field is only accessible if the revenue basis is ‘Unit’.
 Specify the work unit of measure (from HQ Units of Measure) that applies to this revenue code (e.g. EA, CY, SF, etc.).

## Update Hour Meter

Check this box to update equipment hour meters when posting usage to this revenue code. The system will calculate the hours for a meter based on the number of units entered during usage posting. For example, if you post 2 units to a weekly revenue code and the weekly code has 40 hours as its Hours/Time Unit, the system will update 80 hours to the equipment’s hour meter in [EM Equipment](/en/vista/vista/job-resources/equipment-management/setupmaintenance/about-the-em-equipment-form).
This flag only determines the default setting
 of the Update Hour
 Meter checkbox when setting up revenue rates by category in [EM Revenue Rates by Category](/en/vista/vista/job-resources/equipment-management/revenuecosts/revenuecost-setup/about-the-em-revenue-rates-by-category-form). When posting usage, the
 system will check the equipment or equipment category to determine whether to update the
 hour meter for a piece of equipment.
Leave this box unchecked if you do not want equipment hour meters updated automatically when posting usage to this revenue code.
This field is only enabled when Hour is
 selected in the Revenue Basis field.

## Based on MS Haul Charge/Surcharge

The use of this field varies depending on whether the revenue code is being used for haul charges or surcharges.
Haul Charges
If using this revenue code for haul charges, check this box to base revenue amounts on values entered with the haul code when entering haul charges on tickets or hauler time sheets. When checked. if the basis of the revenue code matches the basis of the haul code, the revenue code’s standard rates will be ignored, and the values entered for the haul code (in MS Ticket Entry or MS Hauler Time Sheets) will default into the related revenue fields.
When tickets and hauler time sheets are entered, the system will check to make sure that the basis of the revenue code is consistent with the posted haul code. If the validation is successful, the revenue code’s standard rates will be ignored, and the values entered for the haul code will then default into the related revenue fields.
Note: Leave this box unchecked to use the standard rates for this revenue code when calculating revenue amounts during entry of haul charges on tickets or hauler time sheets.Surcharges
If using this revenue code for surcharges (i.e. you are using the surcharges functionality in Material Sales and will be assigning this revenue code to surcharge codes in MS Surcharge Codes), you must check this box. When surcharges are assessed (in MS Ticket Entry), the system will apply the revenue rate (defined for this revenue code in EM Revenue Rates by Category or EM Revenue Rates by Equipment) against the surcharge total to determine what amount of the assessed surcharge to pass to the equipment revenue account.
