---
title: "Field Definitions: HR Company Assets Form | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/hr-and-payroll/human-resources/setupmaintenance/about-the-hr-company-assets-form/field-definitions-hr-company-assets-form"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/hr-and-payroll/human-resources/setupmaintenance/about-the-hr-company-assets-form/field-definitions-hr-company-assets-form"
---

# Field Definitions: HR Company Assets Form

The following is a list of field descriptions for the HR
 Company Assets form. Many of the descriptions include links to other topics that provide additional information about or related to the topic.

##  Asset

 Enter a unique asset code, up to 20 characters, for this item.

##  Category

 Optional.
 Enter the category for this asset, up to 20 characters. The category assigned here will be used by reports to group assets by category.
Note: This is a non-validated field; therefore, you should
 use the naming scheme and usage rules defined by your company.

##  Description

 Enter a description of this item, up to 60 characters.

##  Unassigned Loc

 Specify where this asset is stored when it is not assigned to a resource (e.g. bin, drawer, shelf, etc.). Up to 60 characters allowed.

##  Manufacturer

 Specify the manufacturer of this asset, up to 60 characters.

##  Model Year

 Enter the year this asset was manufactured. Up to 4 digits allowed.

##  Model Number

 Enter this asset's model number, up to 60 characters.

##  ID Number

 Enter this asset's identification number (e.g. serial number, VIN#, account number, etc.). Up to 60 characters allowed.

##  Phone Number

 If this asset is a mobile (cell) phone, enter the phone number. Up to 20 characters allowed.

##  Purchase Date

 Enter the date this asset was purchased.

##  Value

 Enter the dollar value (book or estimated) of this asset. Up to 10 digits and 2 decimals.

##  License Number

 Enter the license number (or plate number) of this asset, if applicable. Up to 20 characters allowed.

##  Expire Date

 Enter the expiration date of this asset's license.

##  Lic State

 Enter the state in which this license was issued.

##  Warranty

 Enter the warranty information for this asset, up to 60 characters.

##  Warr Expire Date

 Enter the warranty's expiration date.

## Status

 Specify the status of this asset.

- 0-Available – Asset is currently available for assignment. Assets will be flagged with this status automatically whenever they are 'checked in' by a resource.

- 1-Unavailable – Asset is currently
 unavailable (e.g. checked out for use or repairs). Assets will be flagged with this
 status automatically when they are checked out by a resource, or when they are
 checked in, but have been flagged as 'Make Unavailable'.

- 2-Disposed – Asset has been disposed of. This is the only status that must be set manually.

##  Status Memo

 Enter any notes regarding this asset's current status, if applicable. Up to 60 characters allowed.

##  Assigned To

 Display only, showing the resource to which the asset is currently assigned, when the asset was assigned (i.e. checked out), and the 'out memo', if applicable.
 If the asset has been checked in, will show the resource to which the asset was 'last assigned', when it was checked out by that resource, when the asset was returned (checked in), and the 'in memo', if applicable.

##  History: HRRef

 Display only, the resource to which the asset is currently (or was) assigned.

## History: Date Out

The Date Out field on the HR Company Assets form, History tab.
Displays the date this asset was checked out by the assigned resource. May be overridden as long as the new checkout date falls after the resource's check-in date.
Enter the date this asset was checked out by this resource.

##  History: Memo Out

 Displays the memo entered when checking out this asset for the specified resource. May be overridden. Up to 60 characters allowed.

##  History: Date In

 Displays the date this asset was checked in by the assigned resource. May be overridden as long as the new check-in date falls after the resource's checkout date, and on or before the next checkout date if the asset has already been reassigned to another resource.
 If you are checking in this asset, enter the date the asset was checked in by this resource.

##  History: Memo In

 Displays the 'in memo' entered for this asset when checked in by the assigned resource. May be overridden. Up to 60 characters allowed.
 If you are checking in this asset, enter any notes regarding this asset and/or resource, up to 60 characters (e.g. asset's condition, any accessories returned with it, etc.).
