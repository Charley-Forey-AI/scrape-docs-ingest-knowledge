---
title: "More Invoice Information - Field Descriptions | Trimble Help"
source_url: "https://help.trimble.com/en/spectrum/spectrum/materials/order-processing/spectrum-menus/data-entry-overview/sales-order-entry/sales-order-entry---grid-field-descriptions/more-invoice-information/more-invoice-information---field-descriptions"
fetched_at: "2026-04-03T20:05:26.860879+00:00"
menu_path: "/en/spectrum/spectrum/materials/order-processing/spectrum-menus/data-entry-overview/sales-order-entry/sales-order-entry---grid-field-descriptions/more-invoice-information/more-invoice-information---field-descriptions"
---

# More Invoice Information - Field Descriptions

Use the table below for reference when completing the fields on this screen.
Fields
Descriptions

Communication

Reference
Enter any reference information, if desired. This information typically is for internal use only.

Remark
Any comments entered in this field will appear on the printed invoice. Double-click to select from a list of available messages.

Terms and conditions

F.O.B. location
Enter the free-on-board description.

Ship via
Enter the quote carrier information, '*' and a valid carrier code, or select from a list of available carrier codes.

Shipping terms
Enter the shipping terms (up to 25 characters), type an asterisk (*) and a valid terms code for partial search, or select from a list of available terms codes.

Payment terms
Enter a valid terms code, or press Enter for the customer terms default.

Other settings

Default warehouse
Enter the default warehouse from which the item will be shipped. Warehouse codes may be up to 10 characters long.

A/R G/L account
The Accounts Receivable General Ledger account code will default from the Order Processing Installation screen, but can be overwritten in the entry screen. The cursor initially jumps past this field, but you can arrow back to access the field. If the G/L account code specified in the Order Processing Installation screen is blank or invalid, Spectrum will require entry in this field.

Quoted hauler
Enter the hauler code that was used on this invoice, if any, or select from a list of available hauler codes.

Salespeople

Commission
The commission percentage for each salesperson displays. Enter an alternate percentage, or press Enter to accept default.

Distribution
The distribution percentage is the percentage of the commission paid to each salesperson. Press Enter to accept this default. Otherwise, enter a new percentage amount.
Three fields are available since a commission can be split into three portions. The distribution percentage defaults to 100% but can be overridden with any percentage between .01 to 100%. For example, if the commission on an order is 10%, but it is divided evenly between two salespersons, the commission percentage for each is 10% and their distribution is 50%.

Billing address

Print alternate address?
Select this checkbox if you would like to apply an alternate billing address to the selected quote, order, or invoice.
 If this checkbox is selected, the Bill-to code field must be completed.

Bill-to code
Enter the alternate bill-to code that you want to apply to the selected quote, order, or invoice or select from a list of available bill-to codes. This field must be completed if the Print alternate address on invoice checkbox is selected.

Ship-to address

Entry method
Enter a ship-to code to indicate where the ordered items are to be shipped, or select from a list of available ship-to codes. Entry method codes are as follows:

- C: To use the customer's billing address line-by-line. The information displays in the ship-to, name, addr 1, addr 2, city, state, zip, and contact fields. The information may not be changed.

- S: To use the Ship-to address. A ship-to code will be required.

- I: To Input the ship-to address information directly.
1-999: If ship-to addresses were defined for this customer in the Customer Ship-to Addresses, enter the number of the ship-to address to which this order is to be sent or select from a list of available ship-to address.

Ship-to code
This field is required when the Entry method is 'Ship-to'. Select from a list of available codes.

Name, Address, Contact
Enter the name of the company or person to whom this invoice is to be delivered, along with the mailing address.

Weight
If Inventory Control is installed, the total weight of all items invoiced displays. No entry is allowed. If Inventory Control is not installed, this field remains blank.
