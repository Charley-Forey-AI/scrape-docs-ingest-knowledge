---
title: "Field Definitions: JC Field Ticket Form | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/costs-and-contracts/job-cost/jobs-and-contracts-setup/jc-field-ticket-form/field-definitions-jc-field-ticket-form"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/costs-and-contracts/job-cost/jobs-and-contracts-setup/jc-field-ticket-form/field-definitions-jc-field-ticket-form"
---

# Field Definitions: JC Field Ticket Form

The following is a list of field descriptions for the JC Field
 Ticket form. Many of the descriptions include links to other topics that provide additional information about or related to the topic.

## Contract

The Contract field on the JC Field Ticket form, Info tab.
This field is disabled when accessing this form via the JC Contracts or PM Contracts forms (Field Tickets tab).
Required.
Enter the contract to work with. Press F4 to select from a list of valid contracts.

## Field Ticket

The Field Ticket field on the JC Field Ticket form, Info tab.
Enter N, New, or + to create a new field ticket number. The system assigns the next sequential number based on the Next Field Ticket number in JC Company Parameters or, if you did not specify a value in the Next Field Ticket field, the highest ticket number in the system.
Once set up here, you can associate this field ticket number with related costs, such as timecards, equipment usage, AP invoices / unapproved invoices, material usage, and purchase orders.

## Description

The Description field on the JC Field Ticket form, Info tab.
Enter a description for this field ticket. Up to 255 characters allowed.

## Ordered By

The Ordered By field on the JC Field Tickets form, Info tab.
Enter the name of the person who ordered/called in this ticket.

## Customer PO

The Customer PO field on the JC Field Ticket form, Info tab.
Enter the customer PO number associated with this field ticket (if applicable)
 or press F4 to select from a list of valid customer POs for the contract.Note: Before you can assign a customer PO to a field ticket, you
 must first set up it up on the Customer PO tab in the JC Contracts form.

## Owner Job No

The Owner Job No field on the JC Field Ticket form, Info tab.
Enter the owner's job number. This number is provided by the customer and will either be the customer's job number or AFE (Authority for Expenditure) number.

## Address

The address fields on the JC Field Ticket form, Info tab.
Enter the address information for this field ticket:

- Address - Enter the street address. This will be either the job site address or the customer's address.

- City - Enter the city.

- State - Enter the state or press F4 for a list of valid states.
The system validates the state based on the Default Country specified in HQ Company Setup for the active company. If not valid, an error displays, but entry is allowed. You must then enter a valid country for this state in the Country field.

- Zip Code - Enter the zip/postal code, up to 12 digits.

- Country - Enter the country code or press F4 to select from a list of valid country codes.
 Entry in this field is required when the address exists outside the Default Country specified in HQ Company Setup for the active company.

## Contact

The Contact field on the JC Field Ticket form, Info tab.
Enter the name of the person to contact regarding this field ticket.

## Phone

The Phone field on the JC Field Ticket form, Info tab.
Enter the contact's phone number.

## Status

The Status field on the JC Field Ticket form, Info tab.
Specify the current status of this field ticket.

- O-Open - This status is applied when you create a field ticket in either this form or in Field Management. You can only post costs to field tickets with this status; therefore, you should not change from this status until you are ready to close and/or approve this field ticket for billing.

- C-Closed - Select this status when you are ready to close this field ticket and submit it for approval.Note: You cannot change the status of a field ticket to Closed or Approved if the field ticket is referenced in any open batches (such as PR Timecard, EM Usage, etc.).

- A-Approved - Select this status when the field ticket is approved for billing.

- Rejected - Select this status if the field ticket was not approved for billing.

- B-Billed - This status is applied automatically when you create a billing for the contract/job associated with the field ticket (via JB Bill Initialization or JB T&M Bill Edit). In addition, the system populates the Bill Month and Bill Number fields, which cannot be changed.Note: You cannot manually change a field ticket to or from the Billed status.

## Bill Month

The Bill Month field on the JC Field Ticket form, Info tab.
This field is disabled, but is populated automatically with the bill month once you create a bill for the contract/job associated with this field ticket in JB Bill Initialization or JB T&M Bill Edit.

## Bill Number

The Bill Number field on the JC Field Ticket form, Info tab.
This field is disabled, but is populated automatically with the bill number once you create a bill for the contract/job associated with this field ticket in JB Bill Initialization or JB T&M Bill Edit.

## Bill Invoice

The Bill Invoice field on the JC Field Ticket form, Info tab.
This field is disabled, but is populated automatically with the bill invoice number once you create a bill for the contract/job associated with this field ticket in JB Bill Initialization or JB T&M Bill Edit.

## Ticket Approved By

The Ticket Approved By field on the JC Field Ticket form, Info tab.
Display only, the name of the person (login name) who approved this field ticket.
This field is populated once the field ticket is approved in Field Management (via the Field Ticket Dashboard).

## Ticket Date Approved

The Ticket Date Approved field on the JC Field Ticket form, Info tab.
Display only, the date this ticket was approved.
This field is populated once the field ticket is approved in Field Management (via the Field Ticket Dashboard).

## Billing Approved By

The Billing Approved By field on the JC Field Ticket form, Info tab.
Display only, the name of the person who approved this field ticket for billing.
This field is populated once the field ticket is approved for billing in JC Field Ticket (that is, the Status field is set to A-Approved).

## Billing Date Approved

The Billing Date Approved field on the JC Field Ticket form, Info tab.
Display only, the billing approval date for this field ticket.
This field is populated once the field ticket is approved in JC Field Ticket (that is, the Status field is set to A-Approved).
