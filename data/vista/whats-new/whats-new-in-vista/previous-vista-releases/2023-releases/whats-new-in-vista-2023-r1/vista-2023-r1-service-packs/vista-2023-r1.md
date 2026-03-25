---
title: "Vista 2023 R1.03 | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/whats-new/whats-new-in-vista/previous-vista-releases/2023-releases/whats-new-in-vista-2023-r1/vista-2023-r1-service-packs/vista-2023-r1.03"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/whats-new/whats-new-in-vista/previous-vista-releases/2023-releases/whats-new-in-vista-2023-r1/vista-2023-r1-service-packs/vista-2023-r1.03"
---

# Vista 2023 R1.03

This release contains an update to the Canadian Bonus Tax routine, updates to the JB Invoice Delivery feature, and defect fixes that apply to all geographies.

## Canadian Bonus Tax

Updated the Canadian Bonus Tax routine to meet the new CRA requirements, as defined in the T4127 (117th Edition) document. Changes are effective as of 1/1/2023.

## Updates to JB Invoice Delivery

Several updates were made for the JB Invoice Delivery feature released in Vista 2023 R1. These updates are as follows:

- JC Contracts - Added a JB Delivery History tab to show the delivery history of Progress and T&M invoices for the selected contract. Information shown on this tab includes the delivery ID, bill month, bill number, the date the invoice was sent (delivered), delivery method, delivery status (Delivered or Failed), and the recipient, as well as the recipient's email and/or address information (depending on the delivery method).

- JB Contract Info - Added a JB Delivery History tab to show the delivery history of Progress and T&M invoices for the selected contract. Information shown includes the delivery ID, bill month, bill number, the date the invoice was sent (delivered), delivery method, delivery status (Delivered or Failed), and the recipient, as well as the recipient's email and/or address information (depending on the delivery method).

- JB Invoice Delivery (JBEmail) - The Deliver button (below the grid) is now disabled until you select one or more invoices for delivery in the grid (that is, the Select checkbox is selected for one or more invoices).

- JB Invoice Delivery (JBEmailDelivery) - This secondary form, accessed by selecting the Deliver button from the JB Invoice Delivery (JBEmail) form, has been renamed to "JB Invoice Delivery - Send" to better clarify its purpose.

## New Division Filter Tag for Custom Dispatch Board Queries

​If you create custom queries for your Service Management Dispatch board (via [VA Inquiries](/en/vista/vista/administration/viewpoint-administration/inquiries--messages/va-inquiries-form)) and filter work orders by Division, the system now supports a new WHERE clause tag: {{FilterByDivisionWhere}}.
When you run a query with this tag, the system replaces the tag with the following, " AND Division= 'SomeDivision' ", where 'SomeDivision' is the division on the work order scope (if one exists) or blank (if no division exists).
For information about creating queries, see [About Creating Queries](/en/vista/vista/administration/viewpoint-administration/inquiries--messages/about-creating-queries).

## Changes to Security Permissions for Active Directory Users

For an active directory (AD) user to show up as a systems user in the F4 lookup on the VA User Profile form, the service account running the Vista Application Services must have permission to enumerate AD groups. Typically, application services run as the Network Service account, which has sufficient permissions on most systems.

## Check Issue Status

To see a list of defects fixed in this version, go to the [Track Cases/Issues page](https://support.viewpoint.com/s/browse-cases-and-issues) of the Viewpoint Customer Portal. Use the filter options to select your product and module. In the Fixed in Version field, select this version, then select Apply Filters.
