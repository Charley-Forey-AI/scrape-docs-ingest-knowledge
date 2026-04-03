---
title: "Site Main Properties - Field Descriptions | Trimble Help"
source_url: "https://help.trimble.com/en/spectrum/spectrum/service/work-order/spectrum-menus-overview/sites-menu/site-main-properties/site-main-properties---field-descriptions"
fetched_at: "2026-04-03T18:19:14.179823+00:00"
menu_path: "/en/spectrum/spectrum/service/work-order/spectrum-menus-overview/sites-menu/site-main-properties/site-main-properties---field-descriptions"
---

# Site Main Properties - Field Descriptions

Use the table below for reference when completing the fields on this screen.
Field
Descriptions

Site code
Enter a code to provide a unique
 identifier for this work order job site.
Site address

Name
Enter the name of the site being
 serviced.
Address
Enter the work site address.
Site phone Other phone
Enter the work site's phone number, and
 alternate contact number (if available).
Customer
Enter a valid customer code
 corresponding to this site, indicating the customer for whom the work is to be
 done. The code must have been previously defined in Customer File
 Maintenance. The customer's name will automatically display once
 the code is entered. Note: If this selected
 customer's status is set to Not Used in the Accounts
 Receivable module, entry is not allowed. If the customer's status is set to
 Inactive in the Accounts Receivable module, entry is allowed in this screen,
 however the software will warn you of the customer's status.

Default alternate bill-to address

Print alternate address on work order/invoice?
Select this checkbox to print
 alternate address information for the selected site identification code on work
 orders and invoices; otherwise, leave this checkbox clear. If this checkbox
 is selected, entry is required in the following Bill-to code field.  If this checkbox is selected, then any work orders
 using a site identification code with an alternate bill-to address will
 update this billing information to Accounts Receivable during work order
 transfer.

Bill-to code
Enter the bill-to code to use for the
 selected customer site identification code, or press F4
 on this field to select from a list of available bill-to codes in the
 Alternate Bill-to
 Address window. Alternate bill-to codes can also be added or
 edited from this window.
Name Address
The name and address of the alternate
 bill-to address displays based on the bill-to code selected. Entry is not
 allowed. If the Print alternate address on work order
 / invoice checkbox is not selected and a bill-to code has
 not been entered, then this field will appear blank.

Work order defaults

Lead source
Enter a unique code to identify this
 lead source. Double-click in this field to select from a list of available
 source codes.
Requested tech
If the customer requested a specific
 technician, enter a valid technician code. This information will then display
 on the work order (for informational purposes only – the technician entered
 here will NOT default as the assigned technician on the work order). The code
 must have been previously defined in Technician File
 Maintenance. A search window is available for viewing valid
 technician codes.
Type
Enter a valid work order type. The type
 must have been previously defined in Work Order Type File
 Maintenance. The description will automatically display once the
 code is entered. A search window is available to view valid type codes.
Zone
Enter a valid zone. Zones are used to
 link sites together geographically; this is a feature used extensively in the
 Service Contracts module and for Work Order dispatch. The Zip Code Zone Update
 facilitates setup if service contracts module is present. The zone defaults in
 Add mode based on the address specified on the main screen.
Case type
Select the case type associated with
 the work site or press F4 to search and select from a
 list of available case type codes using the Case Types window. Case types
 can be edited, added, or deleted in the Case Types
 window as needed.
Customer's job
This optional field is used to specify
 customer job specific material pricing on the site's work order.  Enter a unique code in this field to specify a
 customer's job, or press F4 to open the Customer's Jobs window to
 select a customer's job from setup in Inventory Control > Customer Special Price Maintenance. This code will then default into the header of each new work
 order.

Sales tax code
Enter a valid sales tax code for this
 work site; up to 15 characters are allowed. The code must have been previously
 defined in Sales Tax Code Maintenance in
 Accounts Receivable. The description will
 automatically display once the code is entered.
Use tax code
Enter a use tax code for materials for
 both stock or non-stock items. Use tax will be included in the material cost of
 the work order on the Work Order Financial Summary
 page.
Status
Select the work site status from the
 following options:

- Active

- Inactive

- Not used

If Inactive is selected and then an attempt is made to assign a
 new transaction to this work site, the following message displays:
Warning – work site entered has inactive status.
 To continue, click OK and proceed with entering the
 new data.
If Not used is selected and
 then an attempt is made to assign a new transaction to this work site, the
 following message displays:
Error – work site
 entered is not available for use. This error message disallows
 further data entry.

Default note in new work order
Enter any Work Order notes that pertain
 to the work site.
Alert note
Enter any alerts that pertain to the
 work site. Select the Display in work order
 checkbox if you want alert notes to appear on the work order. If this check
 box is selected, the alert will display when the work order is opened. If
 not selected, the alert will not display when the work order is opened, but
 will print on the work order.
Note: Alert notes will always appear in the Service
 Request window, regardless of whether this checkbox is
 selected.

Taxability

Default new work orders for this site to taxable?
Select this checkbox if new work
 orders for the selected site are taxable. This field will
 default to checked if the taxable setting assigned in Customer
 File Maintenance for the specified customer code is set to
 'Yes'.

Labor subject to sales tax?
Select this checkbox if the labor used
 in this job is taxable. When adding a new site this check
 box will default to the setting specified in Work Order
 Installation.

Material subject to sales tax?
Select this checkbox if the material
 used in this job is taxable. When adding a new site, this
 checkbox will default to the setting specified in Work Order
 Installation.

Material subject to use tax?
Select this checkbox if the material
 used is subject to use tax. Note: This option
 will only be available if the material used is not subject to sales
 tax.

Global positioning

Latitude
Enter the GPS latitude and
 longitude settings for the site. When specified, the site location will display
 in the map bar.
Longitude
