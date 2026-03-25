---
title: "Field Definitions: SM Customer Form | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/service-management/service-management-setup/service-management-setup-forms/sm-customers-form/field-definitions-sm-customer-form"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/service-management/service-management-setup/service-management-setup-forms/sm-customers-form/field-definitions-sm-customer-form"
---

# Field Definitions: SM Customer Form

The following is a list of field descriptions for the SM
 Customer form. Many of the descriptions include links to other topics that provide additional information about or related to the topic.

## Customer

The Customer field on the SM Customers form.
Enter the number of the AR customer that you are setting up as a Service Management customer. Press F4 for a list of valid AR customers.
Note: Customer must already exist in AR Customers in order to add them here. If the customer does not exist in AR Customers, you can press F5 from this field to access AR Customers and set them up. Once set up in AR Customers, you can add them here.

## Non-Billable

The Non-Billable checkbox on the SM Customers form, Info tab.
Select this checkbox to have work orders created for
 this customer default as 'non-billable' (that is, have the Price Method default as Non-Billable for
 all work order scopes added to a work order). You may override the price method on the work order as needed.
Leave this box unselected to have work orders
 created for this customer default as 'billable'. Work order scopes added to work orders for
 this customer will automatically default a Price Method of T-Time and Material. You may override the price method on the work order as needed.
Note: The setting of this checkbox determines the default setting for all services added for the customer as follows:

-  If selected, the Non-Billable checkbox in SM Service Sites defaults as selected
 and is disabled for all service sites added for the customer.

- If not selected, the Non-Billable checkbox in SM Service Sites defaults as
 unselected and is enabled for all service sites added for the customer.

## Alternate Bill To

The Alternate Bill To checkbox on the SM Customers form, Info tab.
Select this checkbox to bill work orders associated with this customer to a different AR customer. Use the text box to the right of this field to enter the customer to bill.
Leave this checkbox unselected to bill work orders directly to this SM customer.

## Bill To

The Bill To field (unlabeled) on the SM Customers form, Info tab.
This field is enabled only when the Alternate Bill
 To checkbox is selected.
Specify the AR customer to bill for services received by this SM customer.

## Rate Template

The Rate Template field on the SM Customers form, Info tab.

Enter the rate template (set up in SM Rate
 Templates) for this SM customer. This template is used to determine equipment markups,
 labor rates, and material markups/discounts when creating work orders for this
 customer.
Note: Work orders will only default the rate template
 specified here if no rate template is specified for the service site referenced on the
 work order. If you leave this field blank, you will be required to manually enter the
 rate template on the work order before you can enter work completed items.

Note: If this customer was created from a call record (in SM Call
 Handler), this field defaults the rate template specified on the service call record.
 You can override as needed.

## Customer PO Setting

The Customer PO Setting drop-down on the SM Customers form, Info tab.
Required.
Select the PO requirements setting for this customer.

- N - Not Required (default). This customer does not require a PO number on work orders for services performed.

- R - Required. This customer requires a PO number (provided by them) on service work orders. If a PO number is not entered when adding a work order (in SM Work Orders), the system displays a warning but allows you to save the work order. The system also displays a warning when billing for work completed if you have not assigned a PO to the associated work order scope; however, the invoice is created and can be processed.

Note: You can also override this setting at the customer site level. When adding work order scopes, the system first checks the site level setting to determine whether a PO is required. If the site setting is null, the system then uses the customer setting to determine whether a PO is required.

## Primary Technician

The Primary Technician field on the SM Customers form, Info tab.
Enter the primary technician for this customer. This will generally be the technician preferred by the customer or the technician most qualified to handle service calls for the customer.
Note: Must be flagged as "Active" in PR Employees. If you enter a technician that is flagged as "inactive" in PR Employees, a warning displays and you will be unable to save the record.

## Reviewer

The Reviewer field on the SM Customers form, Info tab.
Enter a reviewer ID in this field to enable that user to mark work orders as ready to bill.
Press F4 in the Reviewer field
 for a list of active reviewers from which to choose. Press F5 to access
 the HQ Reviewers form.

## Active

The Active checkbox on the SM Customers form, Info tab.
Select this checkbox to activate this SM customer. Once activated, this customer will be available for assignment to service sites (in SM Service Sites) and included in SM customer lookups.
Clear this checkbox to deactivate this SM customer. Customer will not be available for assignment to service sites and will not be included in SM customer lookups.
Note: The active status defined here does not affect the active status of the customer in AR Customers.

## WO Invoices: Invoice Grouping

The Invoice Grouping drop-down on the SM Customers form, Billing tab, Work Order Invoice Settings section.
Specify how you want invoices generated (via SM Work Order Billing) when billing multiple work orders for to this customer.

- C - One per customer (default) — Select this option to group all billable work orders on a single invoice for this customer.

- S - One per service site — Select this option to print a separate invoice per service site; all work orders posted to the same service site will be grouped together on the same invoice.

- W - One per work order— Select this option to print a separate invoice per work order.

 The option selected here determines the options available for selection in the Deliver To field below. See the [F1](/en/vista/vista/service-management/service-management-setup/service-management-setup-forms/sm-customers-form/field-definitions-sm-customer-form#ID-00042c5a--en) help for more information. You may override this setting at the service site level in SM Service Sites.
Note: If the Bill To and Custom Invoice Report settings differ for a work order, this will affect how the system generates invoices, regardless of the option selected here. For more information, see [About Invoice Grouping](/en/vista/vista/service-management/service-management-setup/set-up-an-sm-customer/about-invoice-grouping)

## WO Invoices: PO Override

The PO Override checkbox on the SM Customers form, Billing tab, Work Order Invoice Settings section.
This checkbox defaults as unselected for all new customers, whether added via SM Customers or via SM Call Handler.
Select this checkbox to group work order scopes that are assigned the same customer PO number together on the same invoice, regardless of how the Invoice Grouping option is set. This only applies if this customer is designated as the "bill to" customer on the work order scope.
If this checkbox is not selected, the system uses the Invoice Grouping option to determine how invoices are generated.
Note: You can override this setting by service site in SM Service Sites.

## WO Invoices: Invoice Summary Level

The Invoice Summary Level drop-down on the SM Customers form, Billing tab, Work Order Settings section.
Specify how to summarize invoice detail (work completed lines) for this customer.

- L-Line — Select this option to summarize invoice detail at the line level. For each scope on a work order, the system will summarize all work completed lines of the same type (Labor, Equip, Material, and Misc) and print the totals in their respective columns on the invoice.

- C-Cost Type — Select this option to summarize invoice detail at the cost type level. For each scope on a work order, the system will summarize all work completed lines referencing the same cost type and print a single line for that cost type on the invoice. Totals for work completed lines with no cost type assigned will print first, under the heading of "***NO COST TYPE***".Note: You will typically only use this option if you assign cost types to work completed lines.

- T-Transaction — Select this option to summarize invoice detail at the transaction level. For each scope on a work order, the system will print a separate line for each work completed line referencing that scope.

Note: You can override the invoice summary level by invoice in SM Invoice Review.

## WO Invoices: Custom Invoice Report

The Custom Invoice Report field on the SM Customers form, Billing tab, Work Order Invoice Settings section.
Enter the identification number of the custom invoice report to use for previewing/printing work order invoices for this customer. Press F4 for a list of valid custom reports.
Note: If you select the Use Work Order Invoice Settings checkbox (in the Agreement Invoice Settings section), agreement invoices will use the report specified here to preview/print agreement invoices as well.

If this field is blank, the system will use the Default WO Invoice Report specified in SM Company Parameters or the standard SM Invoice report (if no default report is specified for the SM company).

## WO Invoices: Deliver To

The Deliver To field on the SM Customers form, Billing tab, Work Order Invoice Settings section.
Specify where to deliver invoices for this SM customer.

- AR Customer - Select this option to send all work order invoices to the AR customer using the billing address or email address defined in AR Customers.

- Service Site (disabled if Invoice Group is C - One per customer) - Select this option to send work order invoices to the service site using the address or billing email defined in SM Service Sites.

- Other (disabled if Invoice Group is C - One per customer) - Select this option to send work order invoices to a recipient other than the AR customer or service site. Use the Email, Name, and Address fields below to enter the recipient's name and delivery information.

Note: If you selected the Use Work Order Invoice Settings checkbox (in the Agreement Invoice Settings section), the system uses the option selected here to determine the recipient for agreement invoices for this customer.

Note: The setting defined here is used in conjunction with the Show Customer/Site Attachments in Invoicing checkbox in SM Company Parameters to determine how attachments are handled for invoices. For more information, see [Show Customer/Site Attachments in Invoicing](/en/vista/vista/service-management/service-management-setup/service-management-setup-forms/sm-company-parameters-form/field-definitions-sm-company-parameters-form#concept-ef98d82c-a321-4e15-baba-6f8903712c86--en).

## WO Invoices: Delivery Method

The Delivery Method drop-down on the SM Customers form, Billing tab, Work Order Invoice Settings section.
Select the invoice delivery method for this customer.
The billing address used depends on the recipient option you selected in the Deliver To field above.

- P-Print — Select this option to print invoices for delivery via postal mail.

- E-Email — Select this option to
 deliver invoices via email. The system uses the email address defined for the
 customer in AR Customers, the service site in SM Service Sites, or the email
 field below (if you select Other as the Deliver To
 recipient).

Note: If you selected the Use Work Order Invoice Settings checkbox (in the Agreement Invoice Settings section), the system uses the name entered here as the recipient for agreement invoices for this customer.

## WO Invoices: Email

The Email field on the SM Customers form, Billing tab, Work Order Invoice Settings section.
This field is enabled only when you select the Other radio button in the Deliver To field (above).
Required.
Enter the email address for delivering invoices for this contact.
 You can enter multiple email addresses if applicable; however, you must separate them with a semi-colon. For example, jane.doe@email.com; johnd@email.com; joe.smith@email.com. The system will send an email to each email address specified here.Note: You may override the email address(es), if needed, on the Recipients tab of the invoice (in SM Invoice Review or SM Agreement Invoice Review).

Note: If you selected the Use Work Order Invoice Settings checkbox (in the Agreement Invoice Settings section), the system uses the email entered here for delivering agreement invoices for this customer.

## WO Invoices: Name

The Name field on the SM Customers form, Billing tab, Work Order Invoice Settings section.
This field is enabled only when you select the Other option in the Deliver To field for work order invoices.
Required.
Enter the name of the individual or company to whom you will be mailing or emailing work order invoices for this customer.
Note: If you selected the Use Work Order Invoice Settings checkbox (in the Agreement Invoice Settings section), the system uses the name entered here as the recipient for agreement invoices for this customer.

## WO Invoices: Address

The billing address fields on the SM Customers form, Billing tab, Work Order Invoice Settings section.

The billing address fields are enabled only when you select the Other radio button in the Deliver To field.
Required.
Enter the billing address to use for this customer in the following fields:

- Address- Enter the customer's street address.

- City - Enter the city.

- State - Enter a valid state (as defined in HQ States). The system validates the state based on the Default Country specified in HQ Company Setup for the active company. If not valid, an error displays, but entry is allowed. You must then enter a valid country for this state in the Country field.

- Postal Code - Enter the zip code or postal code, up to 12 digits.

- Country - Enter the 2-character country code. Entry in this field is required when the address exists outside the Default Country specified in HQ Company Parameters for the active company. Country must be valid for the specified state (e.g. state, province, territory, etc.) as defined in HQ States.

- Add'l Address - Enter additional address information for this customer (e.g. suite number, apartment, etc.). If the customer receives their mail at a PO Box, then you might enter the PO Box in the Address field above, and use this field to enter the street address.

If you have Internet access, you can click the Map button () to view the address using your default map site (Options > User Options). If you did not specify a country, the system uses the Default Country defined in HQ Company Setup.
Note: If you selected the Use Work Order Invoice Settings checkbox (in the Agreement Invoice Settings section), the system uses the name entered here as the recipient for agreement invoices for this customer.

## Agreement Invoices: Use Work Order Invoice Settings

The Use Work Order Invoice Settings checkbox on the SM Customers form, Billing tab, Agreement Invoice Settings section.
Select this checkbox to use the work order invoice delivery settings for agreement invoices. Once selected, all fields in the Agreement Invoice Settings section are disabled except this checkbox and the Custom Invoice Report field. When delivering agreement invoices, the system uses the work order invoice settings to determine the delivery method and recipient.
Leave this checkbox unselected to define separate invoice delivery settings for agreement invoices. When delivering agreement invoices, the system uses the agreement invoice settings to determine the delivery method and recipient.

## Agreement Invoices: Custom Invoice Report

The Custom Invoice Report field on the SM Customers form, Billing tab, Agreement Invoice Settings section.
Enter the identification number of the invoice report to use for previewing/printing agreement invoices for this customer. Press F4 for a list of valid custom reports.
If this field is blank, the system uses the Def Agreement Inv Report specified in SM Company Parameters or the standard SM Agreement Invoice report if no default report is specified for the SM company.

## Agreement Invoices: Deliver To

The Deliver To field on the SM Customers form, Billing tab, Agreement Invoice Settings section.
This field is enabled only when the Use Work Order Invoice Settings checkbox is unselected.
Specify to whom agreement invoices for this SM customer should be delivered.

- AR Customer - Select this option to send all agreement invoices to the AR customer using the billing address or email address defined in AR Customers.

- Other - Select this option to send agreement invoices to a recipient other than the AR customer. Use the Email, Name, and Address fields below to enter the recipient's name and delivery information.

## Agreement Invoices: Delivery Method

The Delivery Method drop-down on the SM Customers form, Billing tab, Agreement Invoice Settings section.
Select the delivery method for agreement invoices for this customer.

- P-Print — Select this option to print agreement invoices for delivery via postal mail.

- E-Email — Select this option to deliver agreement invoices via email. The
 system uses the email address defined for the customer in AR Customers or
 the email field below (if you select Other as the
 Deliver To recipient).

Note: The billing address or email address used depends on the Deliver To option you selected for agreement invoices.

## Agreement Invoices: Email

The Email field on the SM Customers form, Billing tab, Agreement Invoice Settings section.
This field is enabled only when you select the Other option in the Deliver To field for agreement invoices.
Required.
Enter the billing email address for delivering agreement invoices for this customer.
You may enter multiple email addresses if applicable, making sure to separate them with a semi-colon (for example, jane.doe@email.com;johnd@email.com; etc.). The system sends an email to each email address specified here.
Note: You may override the email address(es), if needed, on the Recipients tab of the invoice (in SM Agreement Invoice Review).

## Agreement Invoices: Name

The Name field on the SM Customers form, Billing tab, Agreement Invoice Settings section.
This field is enabled only when you select the Other option in the Deliver To field for agreement invoices.
Required.
Enter the name of the individual or company to whom you will be mailing or emailing invoices for this customer.

## Agreement Invoices: Address

The Billing Address fields on the SM Customers form, Billing tab, Agreement Invoice Settings section.
The billing address fields are enabled only when you select the Other radio button in the Deliver To field for agreement invoices.
Required.
Use the Address, City, State, Postal Code, Country, and Add'l Address fields to enter the billing address to use when delivering agreement invoices for this customer.
If you have Internet access, clicking the Map button () locates the address using the default map site specified in the User Options form (accessed from the main menu by selecting Options > User Options). If you do not specify a country, the system uses the Default Country defined in HQ Company Setup.

## Work Order

The Work Order field on the SM Customers form, Work Orders tab.
Display only, the number assigned (by the system) to this work order. Cannot be changed.

## Service Site

The Service Site field on the SM Customers form, Work Orders tab.
Display only, the service site (set up in SM Service Sites) for this work order.
Note: Changes to this field can only be made via SM Work Orders. Just double-click on the desired record in the grid to open the work order. Once you make the necessary changes, save the record and exit SM Work Orders to return to this form. Then click the Refresh button (in the toolbar) to update the changes to this grid.
Note: You can only make changes to this field if the WO Status is Open.

## Description

The Description field on the SM Customers form, Work Orders tab.
Display only, the description of this work order.
Note: Changes to this field can only be made via SM Work
 Orders. Double-click on the desired record in the grid to open the work order. Once you
 make the necessary changes, save the record and exit SM Work Orders to return to this form.
 Then click the Refresh button (in the toolbar) to update the changes to this grid.
Note: You can only make changes to this field if the
 WO
 Status is Open.

## Date Requested

The Date Requested field on the SM Customers form, Work Orders tab.
Display only, the date the service associated with this work order was requested (typically the day the service call was received).
Note: Changes to this field can only be made via SM Work
 Orders. Double-click on the desired record in the grid to open the work order. Once you
 make the necessary changes, save the record and exit SM Work Orders to return to this form.
 Then click the Refresh button (in the toolbar) to update the changes to this grid.
Note: You can only make changes to this field if the
 WO
 Status is Open.

## Requested Time

The Requested Time field on the SM Customers form, Work Orders tab.
Display only, the time (in 24-hour format) the service associated with this work order was requested.
Note: Changes to this field can only be made via SM Work Orders. Just double-click on the desired record in the grid to open the work order. Once you make the necessary changes, save the record and exit SM Work Orders to return to this form. Then click the Refresh button (in the toolbar) to update the changes to this grid.
Note: You can only make changes to this field if the WO Status is Open.

## Requested By

The Requested By field on the SM Customers form, Work Orders tab.
Display only, the name of the person requesting the service associated with this work order.
Note: Changes to this field can only be made via SM Work
 Orders. Just double-click on the desired record in the grid to open the work order. Once
 you make the necessary changes, save the record and exit SM Work Orders to return to this
 form. Then click the Refresh button (in the toolbar) to update the changes to this
 grid.
Note: You can only make changes to this field if the
 WO
 Status is Open.

## Contact Name

The Contact Name field on the SM Customers form, Work Orders tab.
Display only, the name of the contact specified for this work order.
Note: Changes to this field can only be made via SM Work
 Orders. Just double-click on the desired record in the grid to open the work order. Once
 you make the necessary changes, save the record and exit SM Work Orders to return to this
 form. Then click the Refresh button (in the toolbar) to update the changes to this
 grid.
Note: You can only make changes to this field if the
 WO
 Status is Open.

## Contact Phone

The Contact Phone field on the SM Customers form, Work Orders tab.
Display only, the phone number of the contact specified in the Contact Name field.
Note: Changes to this field can only be made via SM Work
 Orders. Double-click on the desired record in the grid to open the work order. Once you
 make the necessary changes, save the record and exit SM Work Orders to return to this form.
 Then click the Refresh button (in the toolbar) to update the changes to this grid.
Note: You can only make changes to this field if the
 WO
 Status is Open.

## Service Center

The Service Center field on the SM Customers form, Work Orders tab.
Display only, the service center (set up in SM Service Centers) assigned to perform the requested service for this work order.
Note: Changes to this field can only be made via SM Work Orders. Just double-click on the desired record in the grid to open the work order. Once you make the necessary changes, save the record and exit SM Work Orders to return to this form. Then click the Refresh button (in the toolbar) to update the changes to this grid.
Note: You can only make changes to this field if the WO Status is Open and you have not entered work completed for the work order.

## Contact Seq

The Contact Seq field on the SM Customers form, Contacts tab.
Enter the sequence number of the contact (set up in HQ Contacts) to assign to this customer. The system automatically displays the customer name and contact info (phone, cell, fax, and email address); however, information is display only and cannot be edited. Any changes to the contact information should be made directly in HQ Contacts.
Note: If this is a new contact, you can press F5 to access HQ Contacts and set up the new contact. Once you save the contact record, you are returned to this field and can add the contact.

## Include Trip Close Email

The Include Trip Close Email checkbox on the SM Customers form, Contacts tab.
Select this checkbox if this contact should receive an email when a trip to
 any service site for this customer is completed. When you close a trip in Vista Field
 Service for a work order
 associated this customer, any contact with this checkbox selected receives an email
 indicating the trip was closed.
Leave this checkbox unselected if this contact should not receive emails when trips for work orders associated with this customer are completed.
For more information about closing trips in Vista Field Service, see [Close a Trip in Field
 Service](https://help.viewpoint.com/vista-field-service/vista-field-service/vista-field-service/vista-field-service/work-order-dashboard/close-a-trip-in-field-service).
