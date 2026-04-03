---
title: "Common Error Messages | Trimble Help"
source_url: "https://help.trimble.com/en/spectrum/spectrum/equipment/preventive-maintenance/troubleshooting/common-error-messages"
fetched_at: "2026-04-03T18:19:14.179823+00:00"
menu_path: "/en/spectrum/spectrum/equipment/preventive-maintenance/troubleshooting/common-error-messages"
---

# Common Error Messages

The Common Error Messages section is a quick way to find solutions for some of the error messages in Spectrum.

## Error - Equipment Code Entered Is Not Available For Use

If a retired equipment code is entered, this message displays. This error message
 disallows further data entry.
To change the equipment's status, click Equipment Control > Maintenance > Equipment to open the Equipment File Maintenance screen. In
 the Status field, enter a different status code, or press
 F4 to select from a list of valid equipment status codes.

## Error - Outstanding PO items-on-order for this WO. Close not allowed

This message appears when you are trying to close an equipment work order that has an
 open PO on it. Specifically, the system will not allow you to close the work order
 when:

- There are any open purchase orders for this work order.

- The Disallow work
 order to be closed if PO with outstanding quantity due is present
 checkbox on the Preventive Maintenance Installation screen is selected.

Review to make sure that you indeed want to close out this equipment
 work order. To close the work order, either revise the Purchase Order quantities or
 close the PO itself.
