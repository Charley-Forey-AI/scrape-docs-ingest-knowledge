---
title: "Field Definitions: SM Service Site Form | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/service-management/service-management-setup/service-management-setup-forms/sm-service-sites-form/field-definitions-sm-service-site-form"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/service-management/service-management-setup/service-management-setup-forms/sm-service-sites-form/field-definitions-sm-service-site-form"
---

# Field Definitions: SM Service Site Form

The following is a list of field descriptions for the SM
 Service Site form. Many of the descriptions include links to other topics that provide additional information about or related to the topic.

## Service Site

Enter the service site to set up (e.g. an abbreviated name or numeric code to represent the service site). Up to 20 characters allowed.

## Type

Enter the service site type.

- C-Customer - Select this option if this is a customer service site (i.e. is linked to an SM customer).

- J-Job - Select this option if this is a job service site (i.e. is linked to a JC job).

## Customer

Required.
This field is only displayed and enabled when
 the service site Type is C-Customer.
Enter the customer for this service site.
 Press F4 for a list of valid SM customers.
Note: If the customer you wish to specify is not set up as an SM customer, you can press the F5 key from this field to access the SM Customers form. Then [set up the customer](/en/vista/vista/service-management/service-management-setup/set-up-an-sm-customer), exit the form to return to this field, and enter the new customer.

## JC Co

Required.
This field is only displayed and enabled when
 the service site Type is J-Job.
Enter the Job Cost company for the job
 associated with this service site. Press F4 for a list of valid Job Cost
 companies.
This field initially defaults the JC Co defined for the SM company in SM Company Parameters.

## Job

Required.
This field is only displayed and enabled when
 the service site Type is J-Job.
Enter the job (set up in JC Jobs) to which
 this service site is associated. Must be a valid job for the JC Co specified above. Press
 F4
 for a list of valid jobs.

-  If the job is not set up in JC Jobs, you can press
 F5 from this field to access the JC Jobs form. Once you set up the job and exit the
 Job Master form, you can enter the new job here.

- You can set up this service site for a soft or
 hard-closed job; the system will allow you to save the record. However, if you do not
 allow posting to closed jobs (i.e. the Allow Posting to Hard-Closed Jobs
 and/or Allow
 Posting to Soft-Closed Jobs boxes are unchecked in JC Company
 Parameters), you will be unable to enter work orders or work completed for the
 service site.

## Non-Billable

Check this box to have work orders created for this service site default as 'non-billable'. Work order scopes added to work orders for this service site will automatically default a
 Price Method
 of N-Non-Billable. May be overridden.
Leave this box unchecked to have work orders created for this service site default as 'billable'. Work order scopes added to work orders for this service site will automatically default a
 Price Method
 of T-Time and Material. May be overridden.
The enabling/disabling and default behavior for this checkbox is as follows:

- If this is a customer service site and the
 Non-Billable
 checkbox in SM Customers is selected for the customer, this field defaults as selected and is disabled.

 If the
 Non-Billable
 checkbox is not selected for the customer, this field defaults as unselected and is enabled.

- If this is a job service site and the
 Costing Method
 drop-down for the service site is set to Markup, this field defaults as unselected and is disabled.

If the
 Costing Method
 drop-down is set to Actual Cost, this field defaults as unselected and is enabled.

## Active

Check this box to activate this service site. Once activated, it will be available for selection when entering work orders (in SM Work Orders), and will be included in service site lookups.
Uncheck this box to deactivate this service site. Service site will not be available for selection when entering work orders (in SM Work Orders), and will not be included in service site lookups.

## Costing Method

Required.
This field is only displayed and enabled when the
 service site Type is J-Job.
Specify how costs will be sent to Job Cost for work completed on a job work order.

- Actual Cost (Default) - Select this option to send actual costs to Job Cost. When capturing work completed, the system sets the Billable amount equal to the Actual Cost amount and sends the Billable amount to Job Cost.

- Markup - Select this option to send revenue (cost plus markup) as cost to Job Cost. When capturing work completed, the system calculates the Billable amount based on the rate template assigned to the work order scope, and sends this amount as cost to JC.
Note:

- You will typically use this method if you want the amount you charge the customer to be sent to the job as costs.

- Using this method does not affect the Cost amounts for the work completed entry.

 The cost method defined here will default automatically on any work orders created for this job service site; however, you can override the cost method as applicable.

## Site Description

Enter a description of this service site. Up to 60 characters allowed.

## Address

The
 address fields initially default the Mailing Address from AR Customers (if a customer
 service site) or the Ship Address from JC Jobs (if a job service site).
 You may override the address as needed:

- Address- Enter the street address for this service site.

- City - Enter the city.

- State - Enter a valid state (as defined in HQ
 States). The system validates the state based on the Default Country specified in HQ
 Company Setup for the active company. If not valid, an error displays, but entry is
 allowed. You must then enter a valid country for this state in the Country
 field.

- Zip Code - Enter the zip code or postal code, up to 12 digits.

- Country - Enter the 2-character country code. Entry in this field is required when the address exists outside the Default Country specified in HQ Company Parameters for the active company. Country must be valid for the specified state (e.g. state, province, territory, etc.) as defined in HQ States.

- Add'l Address - Enter additional address information
 for this service site (e.g. suite number, apartment, etc.). If this site receives
 mail at a PO Box, then you might enter the PO Box in the Address
 field above, and use this field to enter the street address.

Note: Once you save the service site, changes to the service site customer will not affect the address. You can change the address as needed if changes to the customer make it necessary to do so.
If you have Internet access, you can click the
 Map button () to view the
 address using your default map site (Options > User
 Options). If you did not specify a country, the system uses the Default Country
 defined in HQ Company Setup.

## Phone

Enter the phone number for this service site. Up to 20 characters allowed.

## Billing Email

The Billing Email field on the SM Service Site form.
Enter the billing email address for this
 service site.
You can enter multiple email addresses if applicable; however, you must separate them with
 a semi-colon. For example, jane.doe@email.com; johnd@email.com;
 joe.smith@email.com.
If you selected Service
 Site as the Deliver To recipient for this site's
 customer (in SM Customers), the system will send an email to each email address specified
 here. You may override the email address on the Recipients tab of SM
 Invoice Review.

## Default Service Center

Required.
Enter the default service center (set up in SM Service Centers) for this service site. This service center will default when entering work orders for this customer/service site.
Note: If you have not set up the service center that will service this site, you can press the F5 key from this field to access the SM Service Centers form. Then [set up the service center](/en/vista/vista/service-management/service-management-setup/set-up-a-service-center), exit the form to return to this field, and enter the new service center.

## Default Contact

Enter the default contact for this service
 site, if applicable. Press F4 for a list of valid contacts.
Note: The contact specified here will be set up automatically as a site contact on the Contacts tab.

## Rate Template

Enter the rate template ([set up in SM Rate Templates](/en/vista/vista/service-management/service-management-setup/about-rate-templates-and-override-rates/set-up-a-rate-template)) for this service site. This template is used to
 determine equipment markups, labor rates, and material markups/discounts when creating work
 orders referencing this service site.
Work order scopes automatically default the rate template specified for a service site
 (does not apply to Actual Cost job work orders). If you do not specify a rate template for
 the service site, the rate template on the work order defaults as follows:

- If a customer work order, the system defaults the rate template specified for the
 customer (in SM Customers) or as blank if no rate template is specified for the
 customer.

- If a job work order, the system defaults the rate template as blank.

Note: If this service site was created from a call record (in SM Call
 Handler), this field defaults the rate template specified on the service call record.
 You can override as needed.

Note: If you convert a job site to a customer site, assign a rate template, and then
 revert the customer site back to a job site, the system retains the rate template
 designation.

## Tax Code

Enter the tax code (from HQ Tax Codes) for this service site. This tax code will be used to calculate tax amounts when entering work completed on a work order that references this service site.
Note: The tax code entered here will only be used if the
 Sale
 Location is set to Service Site for the work order scope.
Leave this field blank if taxes will not be applied to work orders for this service site or if you want tax codes to be entered manually when entering work completed for a work order.

## Use
 Tax Code (Y/N)

Use Tax Code checkbox on the SM Service Sites form, Info tab.
Select this checkbox in order to enter a tax code to use for Use tax.
 You
 will only need to enter a tax code into the Use Tax Code field if the Use tax code
 differs from the Sales tax code for this service site.
If you do not pay Use tax or if you use the same tax code for Sales and Use tax, leave this checkbox unselected and the field blank.

## Use Tax Code

The Use Tax field on the SM Service Sites form, Info tab.
Select the Use Tax Code checkbox and enter the Use tax code for this service site or press
 F4 to select from a list of valid tax codes. You will only need to enter a tax code here if
 the Use tax code differs from the Sales tax code for this service site.
The system will default this tax code for material-related lines with a tax type of Use, and where the Tax Source for the agreement service, work order quote, or work order is Service Site.
Note: Material-related lines include: inventory work completed lines, purchase work complete lines that specify a material or a material SM cost type, miscellaneous work complete lines that specify a material SM cost type, required material lines, and required miscellaneous lines specifying a material SM cost type.

## Primary Technician

Enter the primary technician for this service site. This will generally be the technician preferred by the service site or the technician most qualified to handle service calls for the service site.
Note: Must be flagged as "Active" in PR Employees. If you enter a technician that is flagged as "inactive" in PR Employees, a warning displays and you will be unable to save the record.

## Reviewer

Enter a reviewer ID in this field to enable that user to mark work orders as ready to bill.
Press F4 in the Reviewer field
 for a list of active reviewers from which to choose. Press F5 to access
 the HQ Reviewers form.

## Customer PO Override

For Customer Service Sites only.
Select the PO setting for this service site. This setting overrides the PO setting defined for this site's customer (in SM Customers).

- Blank (default) - No override.

- N - Not Required. This customer site does not require a PO number on work orders for services performed.

- R - Required. This customer site requires a PO number (provided by them) on service work orders. If a PO number is not entered when adding a work order (in SM Work Orders), the system will display a warning; but will allow the work order to be saved. The system will also display a warning when billing for work completed if you have not assigned a PO to the associated work order scope; however, invoice will be created and can be processed.

Note: When adding work order scopes, the system will first check the site level setting to determine whether a PO is required. If the site setting is null (blank), the system will then use the customer setting to determine whether a PO is required.

## Custom Invoice Report

For Customer Service Sites only.
Enter the custom report to use for printing work order invoices for this service site. Leave blank to use the custom invoice report specified for this service site's customer.
Note: If no custom invoice report is specified for the
 service site or customer, the system will automatically use the Default WO Invoice
 Report specified in SM Company Parameters.

## Invoice Grouping

For Customer Service Sites only.
Specify how you want invoices generated (via SM Work Order Billing) for work orders posted to this service site. The setting specified here overrides the Invoice Grouping setting at the customer level.

- S - One per service site — Select this option to print a separate invoice per service site; all work orders posted to the same service site will be grouped together on the same invoice.

- W - One per work order— Select this option to print a separate invoice per work order.

- P - One per work order scope — Select this option to print a separate invoice per work order scope.

- If the Bill To settings differ by work order scope, this will affect how the system generates invoices, regardless of the option selected here. For more information, see [About Invoice Grouping](/en/vista/vista/service-management/service-management-setup/set-up-an-sm-customer/about-invoice-grouping).

- The invoice grouping feature is not used when generating single invoices (in SM Work Orders).

## PO Override

PO Override drop-down on the SM Service Sites form, Info tab.
This field defaults to blank for all new service sites, whether added via SM Service Sites or SM Call Handler.

- Blank - Do not override the PO Override setting defined for the customer in SM Customers.

- Yes - Select this option to always group work order scopes associated with
 this service site and having the same customer PO number and same bill to customer
 together on the same invoice, regardless of how you set the PO
 Override checkbox for the customer.

- No - Select this option if you do not want scopes for this service site
 grouped together on the same invoice when they have the same customer PO number,
 regardless of how you set the PO Override checkbox for the
 customer. Instead, use the Invoice Grouping option selected
 for the service site to determine how invoices are generated.

## Alternate Bill To

For Customer Service Sites only.
Check this box to bill work orders associated
 with this service site to an AR customer other than the customer designated in the
 Owner field above. Then enter the 'bill to' customer in the field to the
 right.
Leave this box unchecked if work orders will
 be billed to the Owner specified above for this service site.

## Bill To

For Customer Service Sites only.
This field is enabled only when the Alternate Bill
 To box (left) is checked.
Specify the AR customer to bill for services
 received by the customer specified in the Owner field above.

## PR Local Code

Enter the local code that identifies the city, county, or other taxing district in which this service site is located. Press F4 for a list of valid local codes (defined in PR Local Codes).
The local code specified here will be used as the default local code when entering work orders for this service site (in SM Work Orders). Default may be overridden.

## Insurance Code

 Enter a valid insurance code for this service
 site. Press F4 for a list of valid insurance codes (set up in HQ Insurance Codes).
 This code will be used as the default insurance code when entering work orders for this service site (in SM Work Orders). Default may be overridden at the work order scope level.

## Craft Template

For Customer service sites only.
Enter the default craft template for this
 service site or press F4 to select from a list of valid craft
 templates (set up in PR Templates) for the PR Co associated with this SM Company.
The template specified here will default as the craft template for all work orders created for this service site. Additionally, the system will use this template to determine craft/class pay rate defaults in PR Timecard Entry for labor hours posted to work orders for the service site.

## Certified Payroll

Check
 this box to default the Certified Payroll box as checked for all
 work orders set up (in SM Work Orders) for this service site. Default may be overridden at
 the work order level.
Leave this box unchecked to default the
 Certified
 Payroll box as unchecked for all work orders set up (in SM Work Orders) for
 this service site. Default may be overridden at the work order level.
Note: This flag applies to customer service sites/work
 orders only. Job sites/work orders will follow the Certified Payroll setting defined for
 the job in JC Jobs (PR Info tab).

## Contact Seq

Enter the sequence number of the contact (set up in HQ Contacts) to assign to this service site. The system automatically displays the contact's name and info (phone, cell, fax, and email address); however, information is display only and cannot be edited. Any changes to the contact information should be made directly in HQ Contacts.
Note: If you entered a Default Contact for this service site
 (Info tab), that contact will be added automatically to this grid (and will display with
 the Default
 Contact box checked).

## Include Trip Close Email

The Include Trip Close Email checkbox on the SM Service Sites form, Contacts tab.
Select this checkbox if this contact should receive an email when a trip to the service site is completed. When you close a trip in Vista Field Service for a work order associated this this service site, any contact with this checkbox selected receives an email indicating the trip was closed.
Leave this checkbox unselected if this contact should not receive emails when trips to this service site are completed.
For more information about closing trips in Vista Field Service, see [Close a Trip in
 Field Service](https://help.viewpoint.com/vista-field-service/vista-field-service/vista-field-service/vista-field-service/work-order-dashboard/close-a-trip-in-field-service).

## Field Service - ID for QR Code

The Field Service - ID for QR Code field on the SM Serviceable Items form, Grid tab.
This field displays the QR code ID that was entered for the service item in Vista Field Service. Up to 60 characters allowed.
You can access this field in the following locations in Vista:

- SM Service Sites > Serviceable Items tab

- SM Serviceable Items > Grid tab

QR codes linked to service items allow Vista Field Service technicians to quickly access service item details and work history. For more information about adding QR codes in Vista Field Service, see [About Service Item QR Codes](https://apim.viewpointplatform.com/help/v1/contents/urn:contentId:FS_000014:FS:FS).
