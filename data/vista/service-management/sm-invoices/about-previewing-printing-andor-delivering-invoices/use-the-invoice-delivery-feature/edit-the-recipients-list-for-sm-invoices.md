---
title: "Edit the Recipients List for SM Invoices | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/service-management/sm-invoices/about-previewing-printing-andor-delivering-invoices/use-the-invoice-delivery-feature/edit-the-recipients-list-for-sm-invoices"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/service-management/sm-invoices/about-previewing-printing-andor-delivering-invoices/use-the-invoice-delivery-feature/edit-the-recipients-list-for-sm-invoices"
---

# Edit the Recipients List for SM
 Invoices

You can add additional recipients, delete recipients,
 and edit the delivery information for existing recipients as needed before
 delivering invoices (work order or agreement).
You must first process an invoice before you can
 edit the recipients list. Once an invoice is processed (that is, sent to AR
 by posting a batch), the Recipients tab is enabled, allowing you to add,
 modify, or delete recipients.
 When you
 generate invoices for a customer work order (via SM Work Orders or SM Work
 Order Billing) or an agreement work order (via SM Agreement Billings Due),
 the system creates a Recipient list for each invoice based on the delivery
 options defined for the customer in SM Customers. Initially, the list will
 contain the single recipient specified for the customer; however, you can
 add additional recipients, delete recipients, and edit the delivery
 information for existing recipients as neededTo edit
 an invoice's recipients list:

1. If you
 are not already in the related invoice form (SM Invoice
 Review or SM Agreement Invoice Review), open the related
 invoice form as follows:

- Double-click on the
 invoice from the Invoice tab in SM Customers, SM
 Service Sites, SM Work Orders (work order invoices),
 or SM Agreements (agreement invoices).

- Open SM Invoices, select the Invoiced radio button,
 and use Search criteria to find the invoice. Then
 double-click on the invoice in the Invoices
 grid.

1. Click on
 the Recipients tab.

1. To add a
 new recipient:

1. In the Seq
 field, enter N
 or +. The system auto-generates the
 sequence number for you.

1. If this invoice serves as the bill for this
 recipient, select the Bill checkbox.

1. In the Delivery
 Method field, select P-Print or E-Email.

1. In the Delivery
 To field, select A-AR
 Customer, O-Other, S-Service
 Site.

1. In the Name field, enter the name of the
 individual or company to whom you will be mailing
 or emailing the invoice, or accept the defaulted
 name (AR Customer or Service Site recipients
 only).

1. If the delivery method is
 E-Mail, use the Email field to enter the recipient's
 email address or accept the defaulted email
 address (AR Customer or Service Site recipients
 only).Note: You can enter multiple email addresses if
 applicable; however, you must separate them with a
 semi-colon (for example, jane.doe@email.com;
 johnd@email.com; joe.smith@email.com). The system
 will send an email to each address specified
 here.

1. If the delivery method is
 P-Print, use the Address
 fields to enter the recipient's mailing address or
 accept the defaulted address (AR Customer or
 Service Site recipients only).

1. Save the record.

1. To edit
 an existing recipient:

1. Select the recipient
 to edit.

1. Change the Delivery
 Method, Delivery
 To, Name, Email, and/or Address fields as needed.Note: You can enter multiple email addresses if
 applicable; however, you must separate them with a
 semi-colon (for example, jane.doe@email.com;
 johnd@email.com; joe.smith@email.com). The system
 will send an email to each address specified
 here.

1. Save the
 record.

1. To
 delete an existing recipient:

1. Select the recipient to delete.

1.  Click Delete
 Record ().


Once you are satisfied with the modifications to
 your recipient list, you can deliver the invoice to the recipients by
 clicking the Deliver button. The system delivers the invoice to each
 recipient based on their delivery information, and then updates the Delivery
 tab with the recipient information.Note: The system does not retain modifications to the Recipients
 list. Once you close the SM Invoice Review form, the system
 deletes any recipients you added and resets the delivery
 information for the default recipient to the original
 settings (from SM Customers). If you deleted the default
 recipient, it will be re-added to the list.

Related information

- [Set Up Billing Information for a Customer](/en/vista/vista/service-management/service-management-setup/set-up-an-sm-customer/set-up-billing-information-for-a-customer)
