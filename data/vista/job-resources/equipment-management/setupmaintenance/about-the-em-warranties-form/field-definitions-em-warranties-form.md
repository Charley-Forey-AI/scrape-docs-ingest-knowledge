---
title: "Field Definitions: EM Warranties Form | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/job-resources/equipment-management/setupmaintenance/about-the-em-warranties-form/field-definitions-em-warranties-form"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/job-resources/equipment-management/setupmaintenance/about-the-em-warranties-form/field-definitions-em-warranties-form"
---

# Field Definitions: EM Warranties Form

The following is a list of field descriptions for the EM
 Warranties form. Many of the descriptions include links to other topics that provide additional information about or related to the topic.

##  Equipment

 Enter the equipment or component that the
 warranty applies to or press F4 to select the equipment from a list.
 Equipment is created and maintained using the [EM Equipment ](/en/vista/vista/job-resources/equipment-management/setupmaintenance/about-the-em-equipment-form) form.

##  Sequence #

 Enter the sequence number of the warranty. This allows you to have several warranties for the same piece of equipment or part.
 Enter an ‘N’, ‘NEW’, or ‘+’ and the system will automatically create a new sequence and assign it the next available number.

##  Manufacturer

 Enter the manufacturer of this equipment or part. This field can be up to 30 characters long.
When creating a new sequence, this field will
 default with the manufacturer of the equipment selected in the Equipment
 field.
Equipment is created and maintained using the [EM Equipment ](/en/vista/vista/job-resources/equipment-management/setupmaintenance/about-the-em-equipment-form)form.

##  Part Code

 Enter the manufacturer’s part code. The part code can be up to 20 characters long.

##  Serial Number

 Enter the serial or VIN number of the equipments. The value in this field can be up to 30 characters long.
When creating a new sequence, this field will
 default with the serial number of the equipment selected in the Equipment
 field.
Equipment is created and maintained using the
 [EM Equipment](/en/vista/vista/job-resources/equipment-management/setupmaintenance/about-the-em-equipment-form) form.

## Part Description

Enter a description of the equipment or part. The description can be up to 60 characters long.
 When creating a new warranty, this field defaults with the description of the material, vendor material, equipment material, or equipment part.

## Warranty Description

Enter a description for this warranty, up to 60 characters. (Example: 3 yrs. or 30,000 miles)

##  AP Company

 Enter the AP company of the vendor (specified below) from which you purchased this equipment.

##  AP Vendor

 Specify the AP vendor from which this equipment or part was purchased.

##  HQ Material

 Enter the HQ material number for this equipment or part, if applicable. If you entered an equipment part in the Part Code field, defaults the HQ material designated for the part code, if applicable.

##  AP Invoice #

The AP Invoice # field on the EM Warranties form, Info tab.
 Enter the AP invoice number (reference number) for this equipment or part.

##  Date Purchased

 Enter the date that the part or equipment was purchased.
When creating a new warranty, this field will
 default with the purchase date of the equipment selected in the Equipment
 field.
The purchase date of equipment is set up using
 the Date
 field on the Ownership tab of the [EM Equipment ](/en/vista/vista/job-resources/equipment-management/setupmaintenance/about-the-em-equipment-form)
 form.

##  Status

- Active – Select this option to indicate that this warrant is currently active.

- Inactive – Select this option to indicate that this warranty is inactive.

##  Date

 This field is only accessible if the warranty status is ‘Inactive’.
 Specify the date on which this warranty became inactive.

##  Date Installed

 Specify the date this part was installed in/on the primary equipment.

##  Miles At Install

The Miles at Install field on the EM Warranties form, Info tab.
 Specify the equipment's mileage at the time this part was installed.
This field initially defaults the miles specified in the Odometer: Reading field in EM Equipment, Meters tab. May be overridden if needed.
Note: If you override the default with a lesser value, the system presents a warning that the new value is less than the default value; however, it does allow you to keep the override value.

##  Hours At Install

The Hours at Install field on the EM Warranties form, Info tab.
 Specify the number of hours logged to the equipment at the time this part was installed.
 This field initially defaults the hours from the Hour Meter: Reading field in EM Equipment, Meters tab. May be overridden if needed.
Note: If you override the default with a lesser value, the system presents a warning that the new value is less than the default value; however, it does allow you to keep the override value.

##  Installed By

 Enter the name of the person who installed this part.

##  Hours

 If applicable, indicate the number of hours included in the warranty period.

##  Miles

 If applicable, indicate the number of miles included in the warranty period.

##  Warranty UM

 Specify the applicable time unit for this warranty.

##  Period

 Enter the number of days, months, or years (depending on Warranty UM) in the warranty period, or leave blank to have the system calculate the period based on the Start Date and Expiration Date.

##  Start Date

 Enter the starting date for this warranty. Initially defaults the warranty’s Date Purchased or Date Installed, depending on how you set the Default Warranty Start Date in EM Company Parameters. If the Default Warranty Start Date is left blank, this field defaults as null.
 This date is used in conjunction with the Warranty UM and the Expiration Date to determine the warranty period.

##  Expiration Date

 Enter the expiration date for this warranty. Initially defaults a date based on the Warranty UM, Period, and Start Date. Overriding this date will recalculate the warranty period.
