---
title: "Field Definitions: IN Physical Count Worksheet Form | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/job-resources/inventory/monthly-reconciliation/in-physical-count-worksheet-form/field-definitions-in-physical-count-worksheet-form"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/job-resources/inventory/monthly-reconciliation/in-physical-count-worksheet-form/field-definitions-in-physical-count-worksheet-form"
---

# Field Definitions: IN Physical Count Worksheet Form

The following is a list of field descriptions for the IN
 Physical Count Worksheet form. Many of the descriptions include links to other topics that provide additional information about or related to the topic.

##  Location

 Enter the location (from IN Locations) for which to create/display a
 worksheet. All materials already set up on the worksheet will display.

##  Material

 If the worksheet was initialized, all materials set up for the specified location are displayed. Materials may be deleted or added to the worksheet.
 If adding a material to the worksheet, it must be active and set up for the location in IN Location Materials. In addition, the material cannot already exist on the current worksheet, nor can it exist on another user’s worksheet for the same location. Pressing F4 displays a list of valid materials for the specified location that are not already on the current worksheet or a worksheet for another user.

##  Physical Location

 Displays only if ‘Show Physical Location’ option checked (Options menu).
 Defaults the physical location specified for the material (IN Location Materials), if applicable. You may override the default, if necessary or if left blank, enter a physical location, up to 30 characters.

##  Physical Count

 Enter the number of units for the specified material, as determined by a physical count at the specified location.

## Count Date

For initialized worksheets, defaults the count date specified during initialization; may be overridden.
If a date was not specified, or if this is a new entry, specify the date to be recorded as the count date for this material.
Date Field Shortcut
T or t
Set the date to the current date.

MMDD
Four digit month and day
Enter a four digit month and date (MMDD) and the system will automatically add the current year.

+
The system will automatically set the date to tomorrow.

+5
The system will automatically set the date to 5 days in the future.
You can actually enter any value after the +, for
 example you can enter +7 to set the date to next week.

-
The system will automatically set the date to the previous day.

-5
The system will automatically set the date to 5 days in the past.
Just like with +, you can enter any value after the
 -, for example you can enter -7 to set the date to the
 previous week.

##  Counted By

 Enter the name of the person who conducted the physical count, up to 20 characters. This is not a validated field.

##  System Count

 This display only field shows the material’s current quantity on hand.
 System count quantities are determined by ‘on hand’ quantities (IN Materials) minus any “ins” and “outs” from INDT (Inventory Detail) with an Actual Date equal to or greater than the Count Date (On Hand – [Units In + Units Out]). The only exceptions are ‘same day’ adjustments with a source of ‘IN Adj’—these quantities will be included in the system count.
Note: The system count will be incorrect if unposted PO Receipts, AP Invoice, IN Transfer, IN Production, IN Adjustments, or MS Ticket batches exist with entries for this material that are dated prior to the specified Count Date.

##  Adj Units

 Defaults an amount based on the physical count and the system count (previous field). If a system count was not initiated, this field defaults to null. The value displays as positive if the adjustment will increase the system count or negative if the adjustment will decrease the system count.

##  Unit Cost

 This field defaults a unit cost for the material based on the Cost Method
 for the location (IN Locations) or category (IN Location Category Override). The field may
 only be overridden if the Allow Unit Cost Overrides checkbox is selected in IN Company
 Parameters.

##  ECM

 Indicates what quantity the unit cost represents. This can only be overridden if the Allow Unit Cost Overrides option is checked (IN Company Parameters).

- E – Per Each

- C – Per Hundred

- M – Per Thousand

##  Ready

 Check this box if this material’s counts have been established and it is ready to be added to the adjustment batch.
Note: This flag can be set for all materials on the worksheet by selecting File > Set Ready Flag and clicking Yes on the displayed dialog box.

##  Memo

 Use this field to record notes about this material, up to 30 characters. This memo will be used as the transaction description for the adjustment entry.
