---
title: "Use the Invoice Delivery Feature | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/service-management/sm-invoices/about-previewing-printing-andor-delivering-invoices/use-the-invoice-delivery-feature"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/service-management/sm-invoices/about-previewing-printing-andor-delivering-invoices/use-the-invoice-delivery-feature"
---

# Use the Invoice Delivery Feature

The invoice delivery feature of Service Management allows you to deliver work order and agreement invoices to a specified list of recipients.

You can use this feature for recipients who are responsible for payment of the invoice, as well as for those who only receive a copy of the invoice for informational purposes.Once you post an invoice in SM Invoice Review (work order invoices) or SM Agreement Invoice Review (agreement invoices), the system enables the Recipients tab in the respective form, allowing you to modify the delivery information for the default recipient (as defined in SM Customers), as well as add new recipients.
 If you have attachments you want included with an invoice (email delivery only), you can add attachments or select existing attachments using the Attachments tab.
Note: The system determines what attachments to display on the Attachments grid based on the attachment types/sources defined for the customer and/or service site (in SM Customer & Site Attch Types) and how you set the how Customer/Site Attachments in Invoicing checkbox in SM Company Parameters. For more information, see [Show Customer/Site Attachments in Invoicing](/en/vista/vista/service-management/service-management-setup/service-management-setup-forms/sm-company-parameters-form/field-definitions-sm-company-parameters-form#concept-ef98d82c-a321-4e15-baba-6f8903712c86--en).

When you ready to deliver the invoice, click the Deliver button. The system cycles through each recipient in the list, printing or emailing the invoice (depending on their selected Delivery Method). For recipients with the Email delivery method, the system generates an email using the information set up on the Email Settings tab in SM Company Parameters and the email address specified for the recipient, and adds any attachments you selected to include. For recipients with the Print delivery method, you can print the invoice for postal delivery.
The following links provide instructions to setting up and using the invoice delivery feature. Click the hyperlinks on applicable steps to get more information on completing the step. These links will take you to topics that give you detailed information on completing that step.

1.  Set up Service Management to use the Invoice Delivery feature.

1. In AR Customers, verify that you have set up Mailing and Email addresses for each customer that will be defined as a recipient on SM invoices (used when the Deliver To method is AR Customer).

1. In SM Company Parameters, [set up the email parameters](/en/vista/vista/service-management/service-management-setup/set-up-an-sm-company/define-email-settings-for-invoice-delivery) to use when delivering invoices via email.

1. In SM Customers, [set up the invoice delivery options](/en/vista/vista/service-management/service-management-setup/set-up-an-sm-customer/set-up-billing-information-for-a-customer) for each applicable customer.

1. In SM Service Sites, [set up the mailing and billing email addresses](/en/vista/vista/service-management/service-management-setup/about-service-sites/set-up-a-customer-service-site) for each service site that will be defined as a recipient on SM invoices (used when the Deliver To method is Service Site in SM Customers).

1. Generate and process invoices.For work order invoices, see [Generate & Process Work Order Invoices](/en/vista/vista/service-management/sm-invoices/generate--process-work-order-invoices).For agreement invoices, see [Generate & Process Agreement Billings](/en/vista/vista/service-management/sm-invoices/generate--process-agreement-billings).

1. [Modify recipient list](/en/vista/vista/service-management/sm-invoices/about-previewing-printing-andor-delivering-invoices/use-the-invoice-delivery-feature/edit-the-recipients-list-for-sm-invoices) for each invoice in SM Invoice Review (work order invoices) or SM Agreement Invoice Review (agreement invoices).

1. If applicable, [add/select attachments to include with the invoice](/en/vista/vista/service-management/sm-invoices/about-previewing-printing-andor-delivering-invoices/use-the-invoice-delivery-feature/addselect-attachments-for-sm-invoice-delivery) (email delivery only).You can [review invoice attachments](/en/vista/vista/service-management/sm-invoices/about-previewing-printing-andor-delivering-invoices/use-the-invoice-delivery-feature/review-sm-invoice-attachments) if needed.

1.  Deliver each invoice by clicking the Deliver button (at the bottom of the invoice form).

Related information

- [SM Invoices](/en/vista/vista/service-management/sm-invoices)

- [Generate & Process Work Order Invoices](/en/vista/vista/service-management/sm-invoices/generate--process-work-order-invoices)

- [Use the Invoice Delivery Feature](/en/vista/vista/service-management/sm-invoices/about-previewing-printing-andor-delivering-invoices/use-the-invoice-delivery-feature)
