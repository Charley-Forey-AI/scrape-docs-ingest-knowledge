---
title: "Field Definitions: EM Work Order Parts Posting Form | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/job-resources/equipment-management/work-orders/about-the-em-work-order-parts-posting-form/field-definitions-em-work-order-parts-posting-form"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/job-resources/equipment-management/work-orders/about-the-em-work-order-parts-posting-form/field-definitions-em-work-order-parts-posting-form"
---

# Field Definitions: EM Work Order Parts Posting Form

The following is a list of field descriptions for the EM Work
 Order Parts Posting form. Many of the descriptions include links to other topics that provide additional information about or related to the topic.

##  Seq#

 Enter the sequence number of an existing entry or enter ‘N’, ‘New’, or ‘+’ to add a new sequence. The system will automatically assign the next available sequence number.

## Action

The Action drop-down on multiple forms throughout Vista.
When entering new records, this field defaults to A (Add) and cannot be accessed.
For existing records, select the action for this entry.

- C-Change - Use this action to make changes to records that have already been processed.

- D-Delete - Use this action to delete this record from all related module files. (The delete functions in the toolbar and Records menu only delete the entry from the batch.

##  Date

 Enter the posting date for this work order. Initially defaults the current date.

##  Work Order

 Specify the work order (from EM Work Orders) for which to post parts.

##  WO Item

 Specify the work order item for which to post parts.

##  Cost Code

 This field is only accessible if you have checked the Allow Cost Code Change option in EM Company Parameters (Work Order tab).
 Enter the cost code for this parts entry. Initially defaults the cost code assigned to the work order (in EM Work Order Edit).

##  Cost Type

 Enter the cost type for this parts entry. Initially defaults the Parts Cost Type specified in EM Company Parameters (Work Orders tab).

##  IN Co#

 If part is a stocked material, specify the IN company (set up in IN Company Parameters) supplying the part. If you initialized parts, defaults the IN Co specified for the work order item/part in EM Work Order Edit.

##  Inv Loc

 If part is a stocked material, specify the IN
 location (set up in IN Locations) supplying the part. If you initialized parts, defaults
 the IN Location specified for the work order item/part in EM Work Order Edit.

##  Part Code

 This field initially defaults the part code set up for the work order item. If no parts are set up on the work order, specify the required part for completing this work order item.
 If you are validating parts (option in EM Company Parameters, Parts tab), you must enter a valid HQ material, vendor part, or an equipment part cross-referenced to a valid HQ material. (If the part code is referenced to an HQ material, the program will use the HQ material number and validate the unit of measure from either HQ Materials or from IN Location.)
 If not validating parts, and you have not
 specified an Inventory location in the Inv Loc field, you may specify any part
 code. If you specified an IN location (stocked part), you can enter only parts that have
 been set up for that location (in IN Location Materials), regardless of how the Validate
 Parts option is set.
Note: Once you enter a part code in this field, the Last Used Date of Part field displays in the header area of this form if you selected the ‘Display last used date for parts in AP/PO/EM’ checkbox in EM Company Parameters.

## Description

Defaults the description of the part as defined in HQ Materials. May be overridden. Up to 60 characters allowed.

##  Parts Status

 Enter the status (from EM Work Order Parts Status) for this work order part. If you initialized parts (EM Work Order Parts Init), defaults the Change to Parts Status Code specified during initialization. May be overridden.

##  Serial No.

 Enter the serial number for the part, up to 20 characters, if applicable.

##  Tax Code

 This field is only accessible if you have checked the ‘Use Tax on Materials’ option in EM Company Parameters (Parts tab).
 If applicable, specify the tax code for this work order item/part.
Note: Use tax amount will not display on the screen, since the calculation only occurs when you post the batch.

##  Units

 Specify the quantity of this part used to complete work order item. Although a 'quantity needed' is generally specified when the work order is set up, this field defaults 0.00, as the quantity needed is not necessarily the quantity actually used.

##  UM

 Defaults the unit of measure specified for the part in EM Work Order Edit. May be overridden.

##  Unit Price

 Specify the unit price for this part. Initially defaults a unit price as follows:

- If a stocked part, unit price defaults based on the Pricing Option specified for Equip Sales in IN Company Parameters. For example, if the Pricing Option is 'Average Cost plus Markup', default will be the Average Unit Cost for the material/location (IN Location Materials), plus the Markup/Discount Rate for Equipment (also IN Location Materials).

- If a non-stocked part, default will be the Std Unit Price specified for the part in HQ Materials.

- If a non-valid part and the Validate Parts option (in EM Company Parameters) is N (unchecked), unit price defaults as null.

 Once unit price is established, the total amount for the work order item (units x unit price) displays in the Total field (far right).

##  Tax Basis

 If you specified a tax code for this parts entry, the tax basis defaults an amount equal to the Total (far right). If the tax basis amount differs from the Total, enter that amount here.

##  Current Odometer

 Enter the current odometer reading for the main equipment at the time this part was installed. Entry in this field will update the equipment’s odometer reading and date in EM Equipment.

##  Current Hours

 Enter the current hour reading for the main equipment at the time this part was installed. Entry in this field will update the equipment’s hour meter reading and date in EM Equipment
