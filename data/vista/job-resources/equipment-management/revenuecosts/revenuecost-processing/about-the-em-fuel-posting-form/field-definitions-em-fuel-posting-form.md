---
title: "Field Definitions: EM Fuel Posting Form | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/job-resources/equipment-management/revenuecosts/revenuecost-processing/about-the-em-fuel-posting-form/field-definitions-em-fuel-posting-form"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/job-resources/equipment-management/revenuecosts/revenuecost-processing/about-the-em-fuel-posting-form/field-definitions-em-fuel-posting-form"
---

# Field Definitions: EM Fuel Posting Form

The following is a list of field descriptions for the EM Fuel
 Posting form. Many of the descriptions include links to other topics that provide additional information about or related to the topic.

## Seq

The Seq # field on the EM Fuel Posting form.
 Enter the sequence number of an existing entry or enter ‘N’, ‘New’, or ‘+’ to add a new sequence. The system will automatically assign the next available sequence number.

Related information

- [Enter Fuel Usage Manually](/en/vista/vista/job-resources/equipment-management/revenuecosts/revenuecost-processing/enter-fuel-usage-manually)

- [About the EM Fuel Posting Form](/en/vista/vista/job-resources/equipment-management/revenuecosts/revenuecost-processing/about-the-em-fuel-posting-form)

## Action

The Action drop-down on multiple forms throughout Vista.
When entering new records, this field defaults to A (Add) and cannot be accessed.
For existing records, select the action for this entry.

- C-Change - Use this action to make changes to records that have already been processed.

- D-Delete - Use this action to delete this record from all related module files. (The delete functions in the toolbar and Records menu only delete the entry from the batch.

## Equipment

The
 Equipment field on the EM Fuel Posting form.
Required.
Enter an equipment code or press F4 to select
 one from a list. You can only select equipment that is set up to use fuel.
Equipment is created and maintained using the
 [EM Equipment ](/en/vista/vista/job-resources/equipment-management/setupmaintenance/about-the-em-equipment-form) form. Equipment is set up to use fuel when
 the Diesel, Gas, or Other box on
 the Additional Information tab of the EM Equipment form is checked.

Related information

- [Enter Fuel Usage Manually](/en/vista/vista/job-resources/equipment-management/revenuecosts/revenuecost-processing/enter-fuel-usage-manually)

- [About the EM Fuel Posting Form](/en/vista/vista/job-resources/equipment-management/revenuecosts/revenuecost-processing/about-the-em-fuel-posting-form)

## EM Cost Code

The EM Cost Code field on the EM Fuel Posting form.
Required.
Enter the cost code for this fuel usage transaction. Initially defaults the fuel cost code specified for the equipment in EM Equipment or, if none assigned at the equipment level, the default fuel cost code specified in EM Company Parameters.

Related information

- [Enter Fuel Usage Manually](/en/vista/vista/job-resources/equipment-management/revenuecosts/revenuecost-processing/enter-fuel-usage-manually)

- [About the EM Fuel Posting Form](/en/vista/vista/job-resources/equipment-management/revenuecosts/revenuecost-processing/about-the-em-fuel-posting-form)

## EM Cost Type

The EM Cost Type field on the EM Fuel Posting form.
Required.
Enter the cost type for this fuel usage transaction. Initially defaults the fuel cost type specified for the equipment in EM Equipment or, if none assigned at the equipment level, the default fuel cost type specified in EM Company Parameters.

Related information

- [Enter Fuel Usage Manually](/en/vista/vista/job-resources/equipment-management/revenuecosts/revenuecost-processing/enter-fuel-usage-manually)

- [About the EM Fuel Posting Form](/en/vista/vista/job-resources/equipment-management/revenuecosts/revenuecost-processing/about-the-em-fuel-posting-form)

## Usage Date

The Usage Date field on the EM Fuel Posting form.
 Required.
 Enter the posting date for this fuel usage transaction. Initially defaults the current date (new batch) or date from previously accessed transaction). This date will update the equipment's Last Fuel Date (in EM Equipment). Additionally, it may update the equipment's odometer and/or hour meter reading dates depending on the update option selected for fuel posting in EM Company Parameters.

Related information

- [Enter Fuel Usage Manually](/en/vista/vista/job-resources/equipment-management/revenuecosts/revenuecost-processing/enter-fuel-usage-manually)

- [About the EM Fuel Posting Form](/en/vista/vista/job-resources/equipment-management/revenuecosts/revenuecost-processing/about-the-em-fuel-posting-form)

##  IN Co

The IN Co field on the EM Fuel Posting form.
 Specify the IN company that supplied the fuel for this equipment. Initially defaults the IN Co specified in EM Company Parameters for the active company.

Related information

- [Enter Fuel Usage Manually](/en/vista/vista/job-resources/equipment-management/revenuecosts/revenuecost-processing/enter-fuel-usage-manually)

- [About the EM Fuel Posting Form](/en/vista/vista/job-resources/equipment-management/revenuecosts/revenuecost-processing/about-the-em-fuel-posting-form)

## IN Location

The IN Location field on the EM Fuel Posting form.
 If applicable, specify the inventory location
 (from IN Locations) that provided the fuel for this equipment.

Related information

- [Enter Fuel Usage Manually](/en/vista/vista/job-resources/equipment-management/revenuecosts/revenuecost-processing/enter-fuel-usage-manually)

- [About the EM Fuel Posting Form](/en/vista/vista/job-resources/equipment-management/revenuecosts/revenuecost-processing/about-the-em-fuel-posting-form)

## Fuel Matl Code

The
 Fuel Matl Code field on the EM Fuel Posting form.
This field is only required if an IN module
 company is entered in the IN Co field.
Specify the fuel material code for this equipment. Initially defaults the fuel part code specified for the equipment in EM Equipment.
If you checked the Validate
 Parts/Materials box in EM Company Parameters, you must enter a fuel code
 that is set up in HQ Materials, PO Vendor Materials, or EM Equipment Parts (with a HQ
 material cross-reference). If a part code references a valid HQ material, the system uses
 the HQ material number and validates the UM from either HQ Materials or from IN Location.)
If you are not validating parts, you can enter
 any part code, as long as you have not specified an Inventory location. If you did specify
 an Inventory location, you must enter a material that is valid for the location, regardless
 of how you set the Validate Parts/Materials checkbox.
Note: If the usage units entered for this transaction should
 update the Fuel
 Used reading for the equipment in EM Equipment, the material specified here
 must match the fuel material code specified for the equipment (in EM Equipment, Add'l Info
 tab).

Related information

- [Enter Fuel Usage Manually](/en/vista/vista/job-resources/equipment-management/revenuecosts/revenuecost-processing/enter-fuel-usage-manually)

- [About the EM Fuel Posting Form](/en/vista/vista/job-resources/equipment-management/revenuecosts/revenuecost-processing/about-the-em-fuel-posting-form)

## UM

The UM field on the EM Fuel Posting form.
 Specify the unit of measure. Initially defaults the unit of measure assigned to the fuel material code in HQ Materials.

Related information

- [Enter Fuel Usage Manually](/en/vista/vista/job-resources/equipment-management/revenuecosts/revenuecost-processing/enter-fuel-usage-manually)

- [About the EM Fuel Posting Form](/en/vista/vista/job-resources/equipment-management/revenuecosts/revenuecost-processing/about-the-em-fuel-posting-form)

## Tax Code

The Tax
 Code field on the EM Fuel Posting form.
This field is only enabled if the Use Tax on
 Materials box is checked in EM Company Parameters (Parts tab).
Enter the tax code, if applicable, for this
 fuel usage transaction. If the material is taxable (flag in HQ Materials) and you specified
 an IN Co/Location, the tax code defaults from IN Locations. Otherwise, defaults as null.
The tax code specified here is for informational purposes only (e.g. for reporting); no taxes are calculated, as the fuel price usually includes tax.

Related information

- [Enter Fuel Usage Manually](/en/vista/vista/job-resources/equipment-management/revenuecosts/revenuecost-processing/enter-fuel-usage-manually)

- [About the EM Fuel Posting Form](/en/vista/vista/job-resources/equipment-management/revenuecosts/revenuecost-processing/about-the-em-fuel-posting-form)

## Units

The
 Units field on the EM Fuel Posting form.
Enter the units of fuel used by this piece of
 equipment. This field will update the Fuel Used field in EM Equipment; however,
 the update will only occur if the material code specified for this usage transaction
 matches the fuel material code specified for the equipment in EM Equipment (Add'l Info
 tab).

Related information

- [Enter Fuel Usage Manually](/en/vista/vista/job-resources/equipment-management/revenuecosts/revenuecost-processing/enter-fuel-usage-manually)

- [About the EM Fuel Posting Form](/en/vista/vista/job-resources/equipment-management/revenuecosts/revenuecost-processing/about-the-em-fuel-posting-form)

## Unit Price

The Unit Price field on the EM Fuel Posting form.
Enter the unit price for the fuel material code specified above. This field initially defaults as follows:

- If you did not enter an IN Co and Location above,
 this field defaults the standard unit price defined for the material in HQ Materials.

- If you did enter an IN Co and Location, this field
 defaults a unit price from IN Location Materials based on the Pricing Option
 specified for Equipment Sales in IN Company Parameters (Add'l Info tab).

 For
 example, if the Pricing Option for Equipment Sales in IN Company Parameters is Average Cost plus markup, the system
 calculates the unit price using the Avg Unit Cost for the location/material on the
 Costs/Qtys tab in IN Location Materials, along with markup rate specified for Equipment in
 the Markup/Discount Rates section of the Costs/Qtys tab.

Related information

- [Enter Fuel Usage Manually](/en/vista/vista/job-resources/equipment-management/revenuecosts/revenuecost-processing/enter-fuel-usage-manually)

- [About the EM Fuel Posting Form](/en/vista/vista/job-resources/equipment-management/revenuecosts/revenuecost-processing/about-the-em-fuel-posting-form)

## Trans Acct

The Trans Acct field on the EM Fuel Posting form.
 Required.
 Initially defaults the cost code GL account (specified for the equipment's department) or the cost type GL account (if no override GL account is set up for the cost code). If you allow overrides to GL accounts (flag in EM Company Parameters), you may override the default. Otherwise, this field is disabled.

Related information

- [Enter Fuel Usage Manually](/en/vista/vista/job-resources/equipment-management/revenuecosts/revenuecost-processing/enter-fuel-usage-manually)

- [About the EM Fuel Posting Form](/en/vista/vista/job-resources/equipment-management/revenuecosts/revenuecost-processing/about-the-em-fuel-posting-form)

## Offset Acct

The
 Offset Acct field on the EM Fuel Posting form.
Specify the GL account (from GL Chart of
 Accounts) to credit for this adjustment transaction. This account must have a sub ledger
 code of blank (null).
This field initially defaults as follows:

-  If you specified a non-stocked material for this adjustment, defaults the Non-Stocked GL Account designated for the material in HQ Material Categories.

-  If you specified a stocked material, defaults the
 Equipment Sales account designated for the specified location in IN Locations.

- If posting miscellaneous parts/materials (not set up
 in HQ) and you are not validating materials (Validate Parts/Materials box is
 unchecked), defaults the Misc Parts GL Acct specified in EM Company Parameters.

- This account offsets the transaction account specified in the previous field. You will only need to enter an account here if you are posting additional costs or making an accrual or reversal entry for this transaction.

- If you specified an IN Co/IN Location for this
 transaction, this field is only accessible if you have checked the Allow GL Account
 Overrides box in IN Company Parameters. If no IN Co/Location
 specified, this field is always accessible.

Related information

- [Enter Fuel Usage Manually](/en/vista/vista/job-resources/equipment-management/revenuecosts/revenuecost-processing/enter-fuel-usage-manually)

- [About the EM Fuel Posting Form](/en/vista/vista/job-resources/equipment-management/revenuecosts/revenuecost-processing/about-the-em-fuel-posting-form)

## New Odo

The New Odo field on the EM Fuel Posting form.
 Enter the equipment’s odometer reading at the time of refueling. Once entered, the difference between the current reading and the previous reading is calculated and displayed in the Difference field in the informational display above.
Reading entered here will update the odometer reading in EM Equipment (based on the update option for fuel posting in EM Company Parameters).

Related information

- [Enter Fuel Usage Manually](/en/vista/vista/job-resources/equipment-management/revenuecosts/revenuecost-processing/enter-fuel-usage-manually)

- [About the EM Fuel Posting Form](/en/vista/vista/job-resources/equipment-management/revenuecosts/revenuecost-processing/about-the-em-fuel-posting-form)

## New Hours

The New Hours field on the EM Fuel Posting form.
 Enter the equipment’s current hour meter reading at the time of refueling. Once entered, the difference between the current reading and the previous reading is calculated and displayed in the Difference field in the informational display above.
The reading entered here will update the hour meter reading in EM Equipment (based on the update option for fuel posting in EM Company Parameters).

Related information

- [Enter Fuel Usage Manually](/en/vista/vista/job-resources/equipment-management/revenuecosts/revenuecost-processing/enter-fuel-usage-manually)

- [About the EM Fuel Posting Form](/en/vista/vista/job-resources/equipment-management/revenuecosts/revenuecost-processing/about-the-em-fuel-posting-form)
