---
title: "Field Definitions: SM Customer Site Attch Types Form | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/service-management/service-management-setup/service-management-setup-forms/sm-customer--site-attch-types-form/field-definitions-sm-customer-site-attch-types-form"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/service-management/service-management-setup/service-management-setup-forms/sm-customer--site-attch-types-form/field-definitions-sm-customer-site-attch-types-form"
---

# Field Definitions: SM Customer Site Attch Types Form

The following is a list of field descriptions for the SM
 Customer Site Attch Types form. Many of the descriptions include links to other topics that provide additional information about or related to the topic.

## Attch Type ID

The Attch Type ID field on the SM Customer & Site Attch Types form.
Enter the attachment type ID or press F4 to select from a list of valid IDs (set up in DM Attachment Types). When delivering invoices to a customer or service site, the system will include all attachments with this ID.
Note: If you assign attachment types to both a customer and its service sites, the system will include only attachments that match the attachment types specific to the customer or service site. For example, if you deliver invoices to the service site only, but you have assigned attachment types to both the service site and its associated customer, the service site will only receive attachments matching their attachment types. They will not also receive attachments matching the attachment types assigned to the customer.

Related concepts

- [SM Customer & Site Attch Types Form](/en/vista/vista/service-management/service-management-setup/service-management-setup-forms/sm-customer--site-attch-types-form)

- [SM Customers Form](/en/vista/vista/service-management/service-management-setup/service-management-setup-forms/sm-customers-form)

- [SM Service Sites Form](/en/vista/vista/service-management/service-management-setup/service-management-setup-forms/sm-service-sites-form)

- [DM Attachment Types Form](/en/vista/vista/system-tools/document-management/dm-setup-and-maintenance/set-up-document-management/dm-attachment-types-form)

Related tasks

- [Assign Attachment Types to a Customer / Service Site](/en/vista/vista/service-management/service-management-setup/set-up-an-sm-customer/assign-attachment-types-to-a-customer--service-site)

## Attch Source

The Attch Source drop-down on the SM Customer & Site Attch Types form.
From the drop-down, select the source for the attachment ID.


- A - All

- W - Work Order

- O - Work Order Scope

- D - Work Completed

- T - Trip

- C - Customer

- S - Service Site

- G - Agreement

- V - Agreement Service

- P - Purchase Order

- I - AP Invoice

- Q - Work Order Quote

When delivering invoices to a customer or service site, the system uses the attachment ID and source to determine what attachments to include in the email. For example, say you have attached documents with Attch ID 1000 to a work order, a work completed line, and a trip. If you specify here that you want to include only documents with Attch ID 1000 and a Source of Work Order, the system will include only the attachments with this ID and Source when delivering invoices to the customer or service site.

Note: If you assign attachment types/sources to both a customer and its service sites, the system will include only attachments that match the attachment type/sources specific to the customer or service site. For example, if you deliver invoices to the service site only, but you have assigned attachment types/sources to both the service site and its associated customer, the service site will only receive attachments matching their attachment types and sources. They will not also receive attachments matching the attachment types/sources assigned to the customer.

Related concepts

- [SM Customer & Site Attch Types Form](/en/vista/vista/service-management/service-management-setup/service-management-setup-forms/sm-customer--site-attch-types-form)

- [SM Customers Form](/en/vista/vista/service-management/service-management-setup/service-management-setup-forms/sm-customers-form)

- [SM Service Sites Form](/en/vista/vista/service-management/service-management-setup/service-management-setup-forms/sm-service-sites-form)

- [DM Attachment Types Form](/en/vista/vista/system-tools/document-management/dm-setup-and-maintenance/set-up-document-management/dm-attachment-types-form)

Related tasks

- [Assign Attachment Types to a Customer / Service Site](/en/vista/vista/service-management/service-management-setup/set-up-an-sm-customer/assign-attachment-types-to-a-customer--service-site)
