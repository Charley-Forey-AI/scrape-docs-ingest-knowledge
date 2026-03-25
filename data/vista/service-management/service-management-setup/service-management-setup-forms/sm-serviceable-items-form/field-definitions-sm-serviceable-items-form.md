---
title: "Field Definitions: SM Serviceable Items Form | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/service-management/service-management-setup/service-management-setup-forms/sm-serviceable-items-form/field-definitions-sm-serviceable-items-form"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/service-management/service-management-setup/service-management-setup-forms/sm-serviceable-items-form/field-definitions-sm-serviceable-items-form"
---

# Field Definitions: SM Serviceable Items Form

The following is a list of field descriptions for the SM
 Serviceable Items form. Many of the descriptions include links to other topics that provide additional information about or related to the topic.

## Serviceable Item

Enter a code (alpha or numeric) to represent the serviceable item. Up to 20 characters allowed.

## Item Description

Enter a description of this serviceable item. This description will display when the serviceable item is referenced on a work order.

## Active

Active field in SM Serviceable Items, Info tab.
Set the active state for the serviceable item.
 Select Active (this checkbox's default) to indicate that the serviceable item is still
 actively used; clear this checkbox to indicate that the serviceable item is no longer in
 service.

## Summary

 Enter a summary of this serviceable item, if applicable. Character allowance is virtually unlimited. You will typically use this field to enter a more detailed description of the serviceable item.

## Class

Required.
Enter the equipment class that applies to this
 serviceable item. Press F4 for a list of valid equipment
 classes.

## Type

Required.
Enter the classification type that applies to
 this serviceable item. Press F4 for a list of valid types for the
 specified equipment class.

## Manufacturer

Enter the manufacturer of this serviceable item. Up to 20 characters allowed.

## Model

Enter the model number of this serviceable item. Up to 60 characters allowed.

## Serial Number

Enter the serial number for this serviceable item, up to 60 characters, for this serviceable item.

## Year Manufactured

Enter the year (in YYYY format) in which this serviceable item was manufactured.

## Location

Enter the location of this serviceable item. This should be the actual physical location of the item (e.g. 3rd Floor, Room 20).

## Labor Warranty

Check this box if a labor warranty exists for this serviceable item.
Leave this box unchecked if no labor warranty exists for this serviceable item.
Note: This field is informational only.

## Labor Warranty: Exp Date

This field is only enabled when the Labor Warranty
 box is checked.
Required.
Enter the expiration date for this serviceable item's labor warranty.
Note: This field is informational only.

## Material Warranty

Check this box if a material warranty exists for this serviceable item.
Leave this box unchecked if no material warranty exists for this serviceable item.
Note: This field is informational only.

## Material Warranty: Exp Date

This field is only enabled when the Material
 Warranty box is checked.
Required.
Enter the expiration date for this serviceable item's material warranty.
Note: This field is informational only.

## Part

Enter a part for the serviceable item, up to 30 characters.
You can use this field to enter a vendor's part number, a part name (e.g. Belt Drive Furnace Blower Motor, 3-Blade Condenser Fan, etc.), or any other identifier for the part.

## Part Type

Required.
Enter the part type (e.g. Furnace Blowers,
 Condenser Fans, etc.). Press F4 for a list of valid part types (as
 defined in SM Part Types).
Note: If you are using the standard tasks feature (SM Standard Tasks) and you assign a standard task to a work order scope for this serviceable item, the system will compare the part type specified here to the part types defined in the task's material requirements to determine the correct material to use when performing the task.

## Material

Required.
Enter the material (from HQ Materials)
 associated with this part. Press F4 to select from a list of valid HQ
 materials.

## Description

Enter a description of the part. Up to 60 characters allowed. This field defaults as follows:

- If you did not associate this part with an HQ material, defaults as null.

- If you associated the part with an HQ material, defaults the material description from HQ Materials. You may override as applicable.

## UM

Enter the unit of measure (from HQ Units of Measure) in which this part is used for the serviceable item. Defaults as follows:

- If you did not associate this part with an HQ material, defaults as null.

- If you associated the part with an HQ material, defaults the standard UM defined for the material in HQ Materials. You may override as applicable; however, must be a valid UM for the material (i.e. any additional UMs defined for the material on the Additional Units of Measure tab in HQ Materials).

## Quantity

Enter the quantity of the part being used on the serviceable item.

## Person Hours

Person Hours field in SM Serviceable Items, Agreements tab.
Enter the override person hours for this serviceable item. The hours entered here will become the Avg Person Hours displayed for the service item on the Work Orders tab in SM Agreements.

## Field Service - ID for QR Code

The Field Service - ID for QR Code field on the SM Serviceable Items form, Grid tab.
This field displays the QR code ID that was entered for the service item in Vista Field Service. Up to 60 characters allowed.
You can access this field in the following locations in Vista:

- SM Service Sites > Serviceable Items tab

- SM Serviceable Items > Grid tab

QR codes linked to service items allow Vista Field Service technicians to quickly access service item details and work history. For more information about adding QR codes in Vista Field Service, see [About Service Item QR Codes](https://apim.viewpointplatform.com/help/v1/contents/urn:contentId:FS_000014:FS:FS).
