---
title: "SM Customer & Site Attch Types Form | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/service-management/service-management-setup/service-management-setup-forms/sm-customer--site-attch-types-form"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/service-management/service-management-setup/service-management-setup-forms/sm-customer--site-attch-types-form"
---

# SM Customer & Site Attch Types Form

Use the SM Customer & Site Attch Types form to specify the types of attachments to include when delivering work order invoices to a customer or service site.
Access this form by clicking Include Attachments in the SM Customer or SM Service Sites forms.
You can assign as many attachment types as needed to a customer and/or service site. In addition to the attachment types that are associated with work orders (such as copies of work orders, site pictures, etc.), you can also specify to include attachments from other related records.

 The Attch Source field allows you to indicate what attachments from related records to include in emails. For example, you may have an AP Invoice attached to the agreement associated with a work order. In this case, you would set up an Attch Type ID of 4 (AP Invoice) and then set the Attch Source to G - Agreement.
 Once you process an invoice, the system determines what attachments to display on the Attachments tab in the invoice form (SM Invoice Review or SM Agreement Invoice Review) based on the setup in this form and the Show Customer/Site Attachments in Invoicing checkbox in SM Company Parameters.

- If the Show Customer/Site Attachments in Invoicing checkbox is selected, the Attachments tab displays all attachments associated with the customer and/or service site that match the attachment types/sources defined for the customer and/or service site. You can then select which attachments to include when delivering the invoice (via email).

- If the Show Customer/Site Attachments in Invoicing checkbox is not selected, the system uses the Deliver To option specified for the recipient (the Recipients tab on the invoice form) to determine what attachments to display on the Attachments tab. For example, if the Deliver To option is AR Customer, the Attachment tab will display all attachments matching the attachment types/sources for the customer. You can then select which attachments to include during invoice delivery.

Note: Once you set up your attachment type IDs, a message displays to the right of the Include Attachments button indicating attachments are included.
 For more information about this form, click the link below.
[Assign Attachment Types to a Customer / Service Site](/en/vista/vista/service-management/service-management-setup/set-up-an-sm-customer/assign-attachment-types-to-a-customer--service-site)

Related information

- [SM Customers Form](/en/vista/vista/service-management/service-management-setup/service-management-setup-forms/sm-customers-form)

- [SM Service Sites Form](/en/vista/vista/service-management/service-management-setup/service-management-setup-forms/sm-service-sites-form)
