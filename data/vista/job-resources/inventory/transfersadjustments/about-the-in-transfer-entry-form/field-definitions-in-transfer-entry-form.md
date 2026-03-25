---
title: "Field Definitions: IN Transfer Entry Form | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/job-resources/inventory/transfersadjustments/about-the-in-transfer-entry-form/field-definitions-in-transfer-entry-form"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/job-resources/inventory/transfersadjustments/about-the-in-transfer-entry-form/field-definitions-in-transfer-entry-form"
---

# Field Definitions: IN Transfer Entry Form

The following is a list of field descriptions for the IN
 Transfer Entry form. Many of the descriptions include links to other topics that provide additional information about or related to the topic.

##  Seq#

 Enter NEW to create a new entry or enter the batch sequence number of an existing entry you wish to display.

##  Date

 Enter the transfer date for this material. This field defaults to the current date.

##  From Loc

 Specify from which location the material is being transferred.

##  To Loc

 Specify the location to which the material is being transferred.

##  Material

 Specify the material being transferred. This must be an active material set up for both the From and To locations (IN Location Materials).

## Units

Enter the number of units to be transferred. This may be a positive or negative amount, but cannot be 0.00.
If the amount entered here will cause the On Hand quantity to go below 0.00, and the 'Display Warning if Qty On Hand is Negative' checkbox is selected in IN Company Parameters, a warning displays that the transfer will result in a negative ‘On Hand’ quantity at the source location. However, entries can still be posted.

## Unit Cost

This field defaults the current average, last, or standard unit cost for
 the material depending on the Cost Method specified for the ‘From’ location.
Unit Cost may only be overridden if the Allow Unit Cost Overrides option is checked (IN Company Parameters). Override value must be equal to or greater than 0.00.
Note: If Cost Method is Std Unit Cost, and the amount
 entered here is not equal to the Std Unit Cost, the difference will be posted to the
 appropriate Cost Variance account (defined in IN Locations or IN Location Category
 Override).

##  ECM

 Indicates what quantity the unit cost represents. This can only be overridden if the Allow Unit Cost Overrides option is checked (IN Company Parameters).
E – Per Each
C – Per Hundred
M – Per Thousand

##  Memo

 Use this field to enter a description of this transfer, up to 30 characters.
