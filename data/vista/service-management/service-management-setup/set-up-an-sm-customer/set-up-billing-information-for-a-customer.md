---
title: "Set Up Billing Information for a Customer | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/service-management/service-management-setup/set-up-an-sm-customer/set-up-billing-information-for-a-customer"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/service-management/service-management-setup/set-up-an-sm-customer/set-up-billing-information-for-a-customer"
---

# Set Up Billing Information for a
 Customer

For each customer you set up in SM Customers, you must set up
 billing information to indicate who will receive work order invoices and/or agreement
 invoices for that customer, as well as what delivery method to use.
When you generate work order invoices (in SM Work
 Orders or SM Work Order Billing) or agreement invoices (in SM Agreement Billings
 Due), the system generates a recipient list (in SM Invoice Review or SM Agreement
 Invoice Review, respectively) based on what you set up here. You can modify the
 recipient list as needed for each invoice you generate. This includes adding
 additional recipients, deleting recipients, or modifying the mailing address and/or
 email address as needed.

1. Open the SM Customers
 form and select the desired customer.

1. Define the Work Order Invoice Settings as
 follows:

1. From the Invoice Grouping drop-down, indicate
 how to generate invoices when billing multiple work orders for to this
 customer in SM Work Order Billing. For more information about each
 option, see the [F1](/en/vista/vista/service-management/service-management-setup/service-management-setup-forms/sm-customers-form/field-definitions-sm-customer-form#ID-00042c10--en)
 help.

- C-One per CustomerNote: Do not select this option if you will be
 delivering invoices to a service site.

- S-One per service site

- W-One per work order

- P-One per work order scope

1. To group work order scopes with the same customer PO on the same
 invoice, select the PO Override check
 box. Selecting this checkbox overrides the Invoice
 Grouping setting.

1. From the Invoice
 Summary Level drop-down, indicate how to summary invoice
 detail on work order invoices for this customer. For more information
 about each option, see the [F1](/en/vista/vista/service-management/service-management-setup/service-management-setup-forms/sm-customers-form/field-definitions-sm-customer-form#ID-00042c41--en) help.

- L-Line Type

- C-Cost Type

- T-Transaction

1. (Optional) Click the WO
 Invoice Desc of Work Options button to launch the SM WO
 Inv Desc Cust Options form, which allows you to specify fields to be
 included in the Description of Work field for SM work order invoices.


1. If you are using a custom report for work order invoices for this customer, enter the
 custom report in the Custom Invoice Report field or press F4 to select from a list of valid custom reports.

1. In the Deliver To field, indicate the recipient
 for work order invoices:

- AR Customer

- Service Site

- Other

1. From the Delivery Method
 drop-down, select P-Print to print
 invoices for postal mailing or E-Email to send
 invoices via email.

1. If you selected Other as the Deliver To
 recipient, use the Email,
 Name, and Address
 fields to enter the recipients email address, name, and billing
 address.Note: When entering the email address, you can enter multiple email
 addresses if applicable; however, you must separate them with a
 semi-colon (for example, jane.doe@email.com; johnd@email.com;
 joe.smith@email.com). The system sends an email to each address
 specified here.

1. Define the Agreement Invoice Settings as
 follows:

1. If you are using a custom report for
 agreement invoices for this customer, enter the custom report in the Custom Invoice Report
 field or press F4 to select from a
 list of valid custom reports.

1. To use the same delivery options defined
 for work order invoices, select the Use Work Order Invoice
 Settings checkbox and save the record.

1. If you did not select the Use Work Order Invoice Settings checkbox, do the
 following:

- In the Deliver To field, select
 AR Customer or
 Other as the recipient for agreement
 invoices.

- From the Delivery Method drop-down,
 select P-Print to
 print invoices for postal mailing or E-Email to send invoices via email.

- If you selected Other as the Deliver To
 recipient, use the Email,
 Name, and
 Address fields to enter the
 recipients email address, name, and billing address.Note: When
 enering the email address, you can enter multiple email
 addresses if applicable; however, you must separate them
 with a semi-colon (for example, jane.doe@email.com;
 johnd@email.com; joe.smith@email.com). The system will send
 an email to each address specified here.

The system uses the information defined here to create the
 recipient list on the invoice. Once you post an invoice, you can modify the recipient
 information as needed. This includes changing the delivery method, delivery information,
 or adding/deleting recipients.

Related concepts

- [About Invoice Grouping](/en/vista/vista/service-management/service-management-setup/set-up-an-sm-customer/about-invoice-grouping)

Related information

- [Edit the Recipients List for SM Invoices](/en/vista/vista/service-management/sm-invoices/about-previewing-printing-andor-delivering-invoices/use-the-invoice-delivery-feature/edit-the-recipients-list-for-sm-invoices)
