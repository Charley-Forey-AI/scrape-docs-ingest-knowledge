---
title: "Assign Attachment Types to a Customer / Service Site | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/service-management/service-management-setup/set-up-an-sm-customer/assign-attachment-types-to-a-customer--service-site"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/service-management/service-management-setup/set-up-an-sm-customer/assign-attachment-types-to-a-customer--service-site"
---

# Assign Attachment Types to a Customer / Service Site

You can assign attachment types to a customer and/or service site to designate what attachments are included when delivering invoices to the customer or service site.
Before you can assign attachment types to a customer or service site, you must [set up the appropriate types](/en/vista/vista/system-tools/document-management/dm-setup-and-maintenance/set-up-document-management/set-up-attachment-types) in DM Attachment Types.
You can set up attachment types for both a customer and its service sites. The system uses the attachment types/sources, along with the Show Customer/Site Attachments in Invoicing checkbox in SM Company Parameters to determine which customer and/or service site attachments will be available for inclusion when delivering invoices. For more information, see [Show Customer/Site Attachments in Invoicing](/en/vista/vista/service-management/service-management-setup/service-management-setup-forms/sm-company-parameters-form/field-definitions-sm-company-parameters-form#concept-ef98d82c-a321-4e15-baba-6f8903712c86--en).

1. For customers, open SM Customers and select the customer to which you are assigning attachment types.For service sites, open SM Service Sites and select the service site to which you are assigning attachment types.

1. Click Include Attachments. The SM Customer & Site Attch Types form displays.

1. In the Attch Type ID field, enter the attachment type ID or press F4 to select from a list of valid attachment type IDs.Note: The system automatically displays the attachment name, months to retain, and status. These fields are disabled and can only be edited in DM Attachment Types.

1. In the Attch Source field, select the source for the attachment ID. The system uses this source, along with the attachment ID to determine what attachments to include when sending invoices to customers and/or service sites. For more information, see the [Attch Source](/en/vista/vista/service-management/service-management-setup/service-management-setup-forms/sm-customer--site-attch-types-form/field-definitions-sm-customer-site-attch-types-form#concept-14--en) F1 help.

1. Save the record.

1. Repeat as necessary.

Related information

- [SM Customer & Site Attch Types Form](/en/vista/vista/service-management/service-management-setup/service-management-setup-forms/sm-customer--site-attch-types-form)

- [SM Customers Form](/en/vista/vista/service-management/service-management-setup/service-management-setup-forms/sm-customers-form)

- [SM Service Sites Form](/en/vista/vista/service-management/service-management-setup/service-management-setup-forms/sm-service-sites-form)

- [DM Attachment Types Form](/en/vista/vista/system-tools/document-management/dm-setup-and-maintenance/set-up-document-management/dm-attachment-types-form)
