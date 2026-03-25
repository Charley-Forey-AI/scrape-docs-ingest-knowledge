---
title: "Field Definitions: EM Equipment Parts Form | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/job-resources/equipment-management/setupmaintenance/about-the-em-equipment-parts-form/field-definitions-em-equipment-parts-form"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/job-resources/equipment-management/setupmaintenance/about-the-em-equipment-parts-form/field-definitions-em-equipment-parts-form"
---

# Field Definitions: EM Equipment Parts Form

The following is a list of field descriptions for the EM
 Equipment Parts form. Many of the descriptions include links to other topics that provide additional information about or related to the topic.

##  Equipment

 Enter the equipment (from EM Equipment) for which you are setting up parts.

## Part Number

Enter the part number, up to 30 characters. Typically used to enter the manufacturer’s part code; however, you can enter a valid HQ material number if desired.
Note: It is important to note that entering a valid HQ
 material number here does not automatically make the part valid. You will need to associate
 the part with the HQ material number in the HQ Material field below.

## HQ Material

Required if Validate
 Parts/Materials box is checked in EM Company Parameters.
Enter a valid HQ material number for the specified part number. Press F4 to show a list of valid HQ Materials, Equipment Materials, or Vendor Materials. Leave blank if not cross-referencing to an HQ material.
Note: If you have specified to validate parts/materials, parts cross-referenced to a valid HQ material will be required when entering parts on work orders or cost adjustment transactions.

## Description

Enter a description of this part, up to 60 characters. If you entered a HQ material number in the previous field, this field defaults to the HQ Material description.

## Quantity

Specify the quantity of this part needed for the specified piece of equipment or leave blank if no designated quantity. Up to 12 digits allowed (###,###,##0.000).
Note: This field allows up to 3 decimals and will not round to the highest whole number when fractional amounts are entered (e.g. 5.25 will not round to 5.00).

##  U/M

 Specify the unit of measure (from HQ Units of Measure) for this part.

##  Memo

The Memo field on the EM Equipment Parts form.
 Use this field to enter miscellaneous information about this part, up to 30 characters.
