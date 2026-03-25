---
title: "Service Management Features | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/whats-new/whats-new-in-vista/previous-vista-releases/2021-releases/whats-new-in-vista-2021-r2/service-management/service-management-features"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/whats-new/whats-new-in-vista/previous-vista-releases/2021-releases/whats-new-in-vista-2021-r2/service-management/service-management-features"
---

# Service Management Features

Vista 2021 R2 delivers on user-requested Service Management enhancements, fixes, and other improvements.

## Added Division and Agreement to SM Call Handler

You can now designate a Division and/or Agreement when entering service calls in SM Call Handler, and the system automatically includes these fields when you generate the work order. This eliminates the need to open up the work order and manually enter the information.
To implement this functionality, the following fields were added to the Info tab of the SM Call Handler form:

-  Division - Use to enter the service center division for the work order. F4 from this field will show only those Divisions valid for the service center specified on the service call.

-  Agreement / Rev - The Agreement field is enabled only if the service call is for an existing customer. F4 from this field shows only agreements associated with the specified customer. The Rev field is display only and shows the current revision number of the specified agreement.

## Default Rate Template for New Customers / Service Sites

When you enter a call in SM Call Handler for a new customer and/or service site, if you specify a rate template on the call record, the system now automatically defaults the rate template for the new customer and/or service site created when you generate the work order. You can override the default for the customer in SM Customers or the service site in SM Service Sites as needed.

## Separate Invoice Delivery Options for Agreement Invoices

You now have the ability to set up invoice delivery options for agreement invoices that differ from those set up for work order invoices.
To enable this new functionality, the SM Customers form was updated as follows:

- Created a new Billing tab with group boxes for Work Order Invoice Settings and Agreement Invoice Settings.

- Moved the existing invoice delivery settings from the Info tab to the new Work Order Invoice Settings group box on the Billing tab. Fields moved are as follows:

- Invoice Grouping

- PO Override

- Invoice Summary Level

- WO Invoice Desc of Work Options

- Custom Invoice Report

- Deliver To

- Delivery Method

- Email

- Name

- Address (Address, City, State, Postal Code, Country, and Add'l Address)

- Added several new fields to the Agreement Invoice Settings group box on the Billing tab. These new fields are as follows:

- Use Work Order Invoice Settings - If you select this checkbox, the system disables the remaining agreement invoice delivery fields (except the Custom Invoice Report field) and uses the work order invoice settings for delivering agreement invoices.

- Custom Invoice Report - Use to specify a custom report to use for agreement invoices. This report is used even if you elect to use the work order invoice settings. If left blank, the system uses the invoice report defined for agreements in SM Company Parameters or the standard SM Agreement Invoice report if no report is defined in SM Company Parameters.

- Deliver To - Use to specify the invoice recipient: AR Customer or Other..

- Delivery Method - Use to specify whether printing or emailing invoices.

- Email, Name, and Address - These fields are enabled only if you select Other as the 'deliver to' option. Use to enter the third-party recipient's name, email, and billing address.

For more information about work order and agreement invoice settings, see [Set Up Billing Information for a
 Customer](/en/vista/vista/service-management/service-management-setup/set-up-an-sm-customer/set-up-billing-information-for-a-customer).

## Support Agreement, Revision, and Term Notes and Attachments

You can now enter notes and add attachments at the agreement, revision, and term levels in SM Agreements.
Changes made to enable this functionality include the following:

- Agreement Notes - A new Agreement Notes tab was added to the SM Agreements form. Double-clicking in the Agreement Notes grid accesses the new SM Agreement Notes form. You can add notes for an agreement using this new form or via the Agreement Notes tab. Agreement notes apply to the agreement as a whole, so you can view, add, or modify notes from any revision of the agreement.
You can add attachments to agreement notes in the SM Agreement Notes form or the Agreement Notes tab in SM Agreements. These attachments are accessible and editable from all revisions of the agreement.

- Revision Notes - With this release, the Notes tab in SM Agreements was changed to Revision Notes. Notes entered on this tab are specific to the selected revision and are not visible from any other revision on the agreement. However, if notes exist for an active revision and you create an amendment, the notes for that revision are copied to the new (amendment) revision.
You can add attachments for a revision using the Revision Notes tab or via the agreement header or Info tabs. Attachments are specific to the revision and are not accessible from any other revision. In addition, revision attachments are not copied when creating an amendment or renewal from an active revision.

- Term Notes - A new Term Notes tab was added to the SM Agreements form. Double-clicking in the Term Notes grid accesses the new SM Agreement Term form. You can add term notes using this new form or via the Term Notes tab. Term notes are specific to an agreement term and can only be edited when focus is on the term record in the Term Notes tab or the SM Agreement Term form.
You can add attachments for an agreement term via the Term Notes tab in SM Agreements or the SM Agreement Term form. These attachments apply to all revisions associated with the agreement term and are only accessible when focus is on the term record on the Term Notes tab or via SM Agreement Term.

For more information about agreement, revision, and term-level notes and attachments, see [About Agreement Notes / Attachments](/en/vista/vista/service-management/agreements/agreement-setupmaintenance/about-agreement-notes--attachments).

## Margin Added for Flat Price Quote Scopes

You now have the ability to specify a margin for Flat Price work order quote scopes.
 A new Margin field was added to the scopes section of the SM Work Order Quotes form. This field only displays for flat price scopes if you are using the 'as costs incurred' method of revenue recognition (set in SM Company Parameters). Entry in this field is required.
When you generate a work order from a quote, the specified Margin is updated to the corresponding work order scope, which is then used during the revenue recognition process (in SM Revenue Recognition) to determine the revenue to recognize.

## Check Issue Status

To see a list of defects fixed in this version, go to the [Track Cases/Issues page](https://support.viewpoint.com/s/browse-cases-and-issues) of the Viewpoint Customer Portal. Use the filter options to select your product and module. In the Fixed in Version field, select this version, then select Apply Filters.
