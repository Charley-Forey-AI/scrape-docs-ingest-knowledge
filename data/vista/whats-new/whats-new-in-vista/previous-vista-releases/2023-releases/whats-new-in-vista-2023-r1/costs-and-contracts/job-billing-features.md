---
title: "Job Billing Features | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/whats-new/whats-new-in-vista/previous-vista-releases/2023-releases/whats-new-in-vista-2023-r1/costs-and-contracts/job-billing-features"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/whats-new/whats-new-in-vista/previous-vista-releases/2023-releases/whats-new-in-vista-2023-r1/costs-and-contracts/job-billing-features"
---

# Job Billing Features

Vista 2023 R1 delivers on user-requested Job Billing enhancements, fixes, and other improvements.

## New Invoice Delivery Feature

You now have the ability to auto-deliver Progress and T&M invoices to selected recipients via email. If you prefer, you also have the option to have the system auto-print invoices so that you can send them to recipients via postal service.
The invoice delivery functionality was implemented as follows:
JB Company ParametersAdded two new fields for specifying the invoice format to use when delivering Progress and T&M invoices:

- Progress Bills Invoice Format

- T&M Bills Invoice Format

You can assign custom or standard invoice reports, and the system will use these reports for all billing invoices delivered using the Invoice Delivery feature.
 You can override these invoice formats at the customer level (in AR Customers) and/or contract level (in JC Contracts) if the customer or contract requires a different invoice format than the ones specified at the company level.
Entry in these fields is not required; however, if there is not at least one invoice format specified for a given delivery at the company, customer, or contract level, the system will be unable to successfully complete the invoice delivery.
An Email Settings tab was also added to the JB Company Parameters form. This tab allows you to define the email parameters to use for invoices delivered via email.
For more information about getting set up for invoice delivery, see [Set Invoice Delivery Options](/en/vista/vista/costs-and-contracts/job-billing/setup-and-maintenance-of-job-billing/set-up-job-billing/set-invoice-delivery-options).
AR CustomersIf you have customers that require a different invoice format for Progress and T&M invoices than what you have specified for a Job Billing company, you can assign the format you wish to use for each applicable customer in AR Customers. For more information, see the [Accounts Receivable](/en/vista/vista/whats-new/whats-new-in-vista/previous-vista-releases/2023-releases/whats-new-in-vista-2023-r1/accounting/accounts-receivable-features) release notes.JC Contract Recipients DetailA new JC Contract Recipients Detail form was added for setting up recipients by contract for invoice delivery. For more information, see [Recipient / Invoice Format Setup for JB Invoice Delivery](/en/vista/vista/whats-new/whats-new-in-vista/previous-vista-releases/2023-releases/whats-new-in-vista-2023-r1/costs-and-contracts/job-cost-features#concept-409--en__SetContractRecipients) in the Job Cost release notes.JB Bill InitializationIf you have set up recipients for invoice delivery (in JC Contract Recipients Detail), the initialization process will now automatically add the recipients to the Recipients tab in the related billing form (JB Progress Billing or JB T&M Bill Edit). You then can modify, add, or delete recipients as needed for each billing.JB T&M Bill Edit / JB Progress BillingAdded Recipients and Delivery tabs to both the Progress and T&M billing forms.

- Recipients - This new tab automatically defaults the recipients defined for a contract in the JC Contract Recipients Detail form, regardless of whether you manually add a billing or generate one via the JB Bill Initialization form. You can edit the delivery information as needed for each default recipient, add new recipients, or delete recipients. The delivery method defined for each recipient determines whether invoices will be sent to the recipient via email or printed and mailed via the postal service.

- Delivery - This new display-only tab tracks the delivery history for invoices delivered via the JB Invoice Delivery form. Once an invoice is delivered, this tab shows the delivery ID, when the invoice was sent, the delivery status, who the invoice was sent to, and the email used to deliver the invoice.

JB Invoice DeliveryYou can now search for, select, and send multiple invoices to recipients at one time using JB Invoice Delivery. With the new JB Invoice Delivery form, filter and choose the invoices you want to deliver, then edit recipients and deliver invoices through the JB Invoice Delivery sub-form.
Note: The JB invoice delivery feature does not currently include attachments. If you have attachments that you want included when delivering invoices to recipients, use the Billing Compiler in Financial Controls. For more information, see [Billing Compiler](https://apim.viewpointplatform.com/help/v1/contents/urn:contentId:FC_000012:FC:FC).

To learn more about JB invoice delivery, see [Deliver JB Invoices](/en/vista/vista/costs-and-contracts/job-billing/billing/invoicing/deliver-jb-invoices).
JB Move Bill MonthWhen moving billings from one month to another, the move process will now include the recipients defined for the bill.

## Check Issue Status

To see a list of defects fixed in this version, go to the [Track Cases/Issues page](https://support.viewpoint.com/s/browse-cases-and-issues) of the Viewpoint Customer Portal. Use the filter options to select your product and module. In the Fixed in Version field, select this version, then select Apply Filters.
