---
title: "About the MS Company Parameters Form | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/job-resources/material-sales/setupmaintenance/about-the-ms-company-parameters-form"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/job-resources/material-sales/setupmaintenance/about-the-ms-company-parameters-form"
---

# About the MS Company Parameters Form

Use this form to set up various control options for Material
 Sales (MS) processing in a company.
You must define these options before processing in MS. It is important that you take time to understand the effects of all choices for each setup option. The options you select will affect which MS forms you will use, how the forms work, and how MS affects other modules. It is suggested that you restrict this company setup form so only the system administrator has access to it.

## About Setting Up Material Sales

As with most of the modules, MS interacts with several modules,
 requiring that specific information be set up before using it. In some cases, the
 system uses this information to validate specific entries in MS, such as customers
 (AR Customers) and/or jobs (JC Jobs) who you sell materials to. The following is a
 brief description of data required to implement Material Sales processing:

- Headquarters (HQ)– Companies
 must be set up in HQ Company Setup before you can set it up in MS
 Company Parameters. Additionally, you must set up the material
 categories (HQ Material Categories) and materials (HQ Materials) for use
 throughout Material Sales.

- Inventory (IN) – The
 Inventory module must be in use before you can use Material Sales.
 Material Sales and Inventory must share the same company number (i.e.
 materials sold from MS CO#1 must be stocked in IN CO#1). Set up shared
 companies in IN Company Parameters before doing so in MS. All materials
 sold through MS come from locations set up in IN Locations, whether they
 are stocked materials or not. Additionally, many of the defaults in MS
 for material unit prices, tax codes, and GL accounts for hauling accrual
 and income are set up in Inventory. (Defaults may be overridden when
 processing in Material Sales.)

- Accounts Payable (AP) –
 Material vendors and outside haulers used to haul materials sold through
 MS must be set up in the AP Vendors.

Once defined, changes are usually rare
 to setup options. Because changing an option may affect processing or stored
 information, make changes carefully. If you want to change an option but are unsure
 of its effect on existing data, contact Viewpoint Support.

## Default Surcharge Group

If you will be implementing surcharges in MS, you can assign a default surcharge
 group for each applicable MS company. Although surcharge groups can be assigned at
 the quote level, assigning a surcharge group here will ensure that every ticket will
 be assessed surcharges, regardless of whether a quote is referenced. During ticket
 entry, the system will assess surcharges based on the surcharge group assigned to
 the quote. However, if no surcharge group is assigned to the quote and quote is
 flagged to apply surcharges, if no quote exists for the purchaser, the system will
 then use the surcharge group assigned here to assess the surcharges.

## About Setting Ticket and Haul Sheet Entry Options

If there are certain types of information that you typically do not track when
 posting material sales tickets or hauler time sheets, use the Remove From
 Ticket Entry and Remove From Haul Sheet Entry
 options in MS Company Parameters to control which fields display on the screen.
 For each field listed, indicate whether you want the field removed from the
 specified form (MS Ticket Entry or MS Hauler Time Sheet Entry). When you select a
 checkbox, the system removes the corresponding field(s) from the form, but they
 will still be available for reporting purposes. If you elect to remove tax fields
 and discount fields from either form, be aware that the system still calculates
 taxes and discounts where applicable. Although you cannot see the calculations, they
 will be stored in the appropriate file and processed normally.
If you want specific fields to display
 on the form, but want to skip input for, use the F3 Properties window.
Note: To restrict input in MS Ticket Entry, select
 Options > Ticket
 Entry Options and select all fields you want skipped for input, rather than using
 the F3 Properties window to do each field manually.

## About Tracking Changes to this Form

The HQ Master Audit (HQMA) table contains a list of changes to records in the
 application. For example, if you change a setting on a company parameters form, a
 new entry is created in the HQMA table so that there is a record of the change. See
 [About Viewing the Master Audit Log](/en/vista/vista/administration/viewpoint-administration/setup-and-maintenance/maintenance/view-the-audit-log) for more
 information about viewing information in the HQMA table.

## Quote Numbers and Invoice Numbers

You can enter quote numbers manually or have the system generate them
 automatically.
If you always use numeric quote numbers,
 you can check the Auto-Generate Quote #'s box in MS
 Company Parameters to have quote numbers assigned automatically during quote entry.
 When N, New, or + is
 entered for a new quote, the system generates a sequential number based on the
 Last
 Used Quote # specified in the company file, and also updates the
 Last
 Used Quote # with the new number. If you use both numeric and
 alphanumeric quote numbers, use manual entry.
The system assigns invoice numbers
 automatically. However, number assignment is determined by how you set the
 Use
 Invoice #'s from option in MS Company Parameters (Invoices tab).
 Select MS to have Material Sales invoices use their own numbering scheme
 or AR to have them share invoice numbers with AR. Regardless of which
 option you select, the system will assign invoice numbers sequentially based on the
 Last
 Used MS Invoice # specified in either MS Company Parameters or AR
 Company Parameters.

Related information

- [Company Setup Options for Ticket Entry](/en/vista/vista/job-resources/material-sales/ticketsmaterialshaul/tickets/company-setup-options-for-ticket-entry)
