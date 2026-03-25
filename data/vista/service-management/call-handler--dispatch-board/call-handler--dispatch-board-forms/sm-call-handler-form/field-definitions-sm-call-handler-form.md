---
title: "Field Definitions: SM Call Handler Form | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/service-management/call-handler--dispatch-board/call-handler--dispatch-board-forms/sm-call-handler-form/field-definitions-sm-call-handler-form"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/service-management/call-handler--dispatch-board/call-handler--dispatch-board-forms/sm-call-handler-form/field-definitions-sm-call-handler-form"
---

# Field Definitions: SM Call Handler Form

The following is a list of field descriptions for the SM Call
 Handler form. Many of the descriptions include links to other topics that provide additional information about or related to the topic.

## Call ID

The Call ID field on the SM Call Handler form, Info tab.
Enter N, New, or + to start a new
 service call record. The system will auto-generate the next available
 number.

## Search

The Search field on the SM Call Handler form, Info tab.
Use this box to search for an existing customer or service site. If you already know the customer number or service site code, leave this field blank and enter the customer and/or service site below.

1. Enter any number of characters or words of the customer or service site name, address, or phone number. The more characters/words you enter, the more refined the search will be.Note: The system searches each word separately and shows only those records containing all of the entered words. For example, if you enter construction 97221, the search will return a list of records that include the word "construction" and the number "97221".

1.  Press Return.
 If only one customer/service site match is found, the system will populate the call
 record with that customer/service site.If more than one match is found, the
 SM Customer Search Results window displays, showing a list of customers and
 service sites based on your character/word entry. Choose the desired
 customer/service site from the search results list and click Select.
Note: You can add or change keywords in the
 Search field (of the SM Customer Search Results window) to produce
 refined or different search results.
Once you select the customer/service
 site, the system automatically populates the customer number, name, rate template,
 and service site fields accordingly; this information cannot be changed.

## New Customer

The New Customer checkbox on the SM Call Handler form, Info tab.
Select this checkbox if this service call is for a new customer.
Do not select this checkbox if this service call is for an existing customer.
Note: If you select this checkbox and then enter an existing customer or service site, the system will automatically clear the checkbox.

## Customer

The Customer field on the SM Call Handler form, Info tab.
Required.

### Existing Customer

Enter the customer number or press F4 to select from a list of valid SM Customers.
Note: Once you enter the customer number, the system displays any applicable customer alerts (in red) above the tabs. For more information about alerts, see [Customer / Site Alerts](/en/vista/vista/service-management/call-handler--dispatch-board/call-handler--dispatch-board-forms/sm-call-handler-form).In addition, if the customer is inactive, a warning displays. The system allows you to save the call handler record, but you must set the customer to Active (in SM Customers) in order to create the work order.


### New Customer

Applies only when New Customer checkbox is selected.
To use your own numbering scheme, enter a unique number, up to 6 digits.
To auto-generate a number, leave the field blank. The system will generate a customer number when you create the work order using the next available AR Customer number.
Note: You can also enter N, New, or n to immediately generate a number. However, because the customer is not added to AR Customers and SM Customers until you click the Create Work Order button, it is possible that the number generated here may no longer be available when the customer is created. In which case, the system will assign the first unused number found.

## Customer Name

The Customer Name field on the SM Call Handler form, Info tab.
This field is only enabled when the New Customer
 checkbox is selected.
Enter the customer's name, up to 60 characters.
For existing customers, this field displays the customer name as defined in AR Customers.
Note: Entry in this field is not required when initially entering a service call for a new customer. However, you must enter the customer name prior to creating the work order.

## Rate Template

The Rate Template field on the SM Call Handler form, Info tab.
This field is only enabled when the New Customer
 checkbox is selected.
Enter the rate template to use for this
 customer or press F4 to select from a list of valid rate templates. The template specified here becomes the default template for the work order generated from this call.
For existing customers, this field displays the rate template designated for the customer in SM Customers or blank if no rate template is specified.
Note: If you specify a new customer and/or a new service site for this call record, the system automatically defaults this rate template for the new customer (in SM Customers) and/or service site (in SM Service Sites) created when you generate the work order.

## New Site

The New Site checkbox on the SM Call Handler form, Info tab.
Select this checkbox if this service call is for a new service site (applies to new or existing customers).
Do not select this checkbox if this service call is for an existing service site (existing customers only).
Note: If you select this checkbox and then enter an
 existing service site, the system will automatically clear this checkbox. If you also
 selected the New
 Customer checkbox, the system will automatically populate the Customer field
 as applicable and clear the New Customer checkbox.

## Site ID

The Site ID field on the SM Call Handler form, Info tab.

### Existing Service Site

Enter the service site or press F4 to select from a list of valid service sites for the specified customer (existing customers only).
Note: Once you enter the service site, the system displays any applicable site alerts (in red) above the tabs. For more information about alerts, see [Customer / Site Alerts](/en/vista/vista/service-management/call-handler--dispatch-board/call-handler--dispatch-board-forms/sm-call-handler-form).In addition, if the service site is inactive, a warning displays. The system allows you to save the call handler record, but you must set the service site to Active (in SM Service Sites) in order to create the work order.


### New Service Site

Applies only when New Site checkbox is selected.
To enter your own site code (alpha or numeric), enter the service site ID, up to 20 characters.
If you selected the Auto-Number: Service Sites checkbox in SM Company Parameters, you can leave this field blank to have the system auto-generate a site ID (numeric only). If you did not select the Auto-Number: Service Sites checkbox, you will need to manually enter a site code.
Note: You can also enter N, New, or n to immediately generate a site ID. However, because the service site is not created until you click the Create Work Order button, it is possible that the number generated here may no longer be available when the service site is created. In this case, the system will assign the first unused number found.

## Site Description

The Site Description field on the SM Call Handler form, Info tab.
Enabled only when the New Site
 checkbox is selected.
Enter a description of the new service site. Up to 60 characters allowed.

## Address

The Address fields on the SM Call Handler form, Info tab.
The address fields are enabled only when the
 New
 Site checkbox is selected.
Enter the customer's address information in the following fields:

- Address- Enter the customer's street address.

- Add'l Address - Enter additional address information for
 this customer (e.g. suite number, apartment, etc.). If the customer receives their
 mail at a P.O. Box, then you might enter the P.O. Box in the Address 1
 field above, and use this field to enter the street address.

- City - Enter the city.

- State - Enter a valid state (as defined in HQ
 States). The system validates the state based on the Default Country specified in HQ
 Company Setup for the active company. If not valid, an error displays, but entry is
 allowed. You must then enter a valid country for this state in the Country
 field.

- Zip Code - Enter the zip/postal code, up to 12 digits.

- Country - Enter the country code or press F4 to
 select from a list of valid country codes. Entry in this field is required when the
 address exists outside the Default Country specified in HQ Company Parameters for the
 active company. Country must be valid for the specified state (e.g. state, province,
 territory, etc.) as defined in HQ States.

If this service call is for a new customer, the this address information will default as the Mailing Address and Billing Address for the customer in AR Customers. In addition, it will default as the address for the new service site in SM Service Sites.
Note: If you have Internet access, you can click the Map button for direct access to the default map site for your login (as defined in User Options, Main Menu). Map will default the approximate location of the specified country and address. If a country is not specified, attempts to locate address based on Default Country specified in HQ Company Setup.

## Center

The Center field on the SM Call Handler form, Info tab.
Enter the service center that will handle the
 service call or press F4 to select from a list of valid service
 centers. If the call is for an existing service site, this field defaults the service
 center assigned to the service site (in SM Service Sites). If the call is for a new service
 site, this field defaults as blank.

## Contact: Name

The Contact Name field on the SM Call Handler form, Info tab.
Enter the contact name for the specified
 service site, up to 60 characters or press F4 to select from a list of valid site,
 customer, or HQ contacts.
Note: You can also set up a contact on-the-fly by pressing F5 to access the HQ Contacts form. Once you have [set up the contact](/en/vista/vista/administration/headquarters/company-setup/set-up-hq-contacts) and returned to this form, you can enter the new contact here. Be aware that setting up a new contact in HQ Contacts and assigning them here does not automatically set them up as a customer contact (in SM Customers) or a site contact (in SM Service Sites).

## Contact: Phone

The Contact Phone field on the SM Call Handler form, Info tab.
Enter the phone number of the service site contact specified above. If you specified an existing contact above, this field defaults the phone number defined for the contact in HQ Contacts.

## Caller Name

The Caller Name field on the SM Call Handler form, Info tab.
Enter the caller's name, up to 60 characters.

## Caller Phone

The Caller Phone field on the SM Call Handler form, Info tab.
Enter the caller's phone number.

## Closed

The Closed checkbox on the SM Call Handler form, Info tab.
Select this checkbox to close the service call. Closing a call disables all fields on the form except this checkbox and the Notes tab.
Note: The system automatically sets this box to selected once you create the work order. Although you can deselect this box to enable the Call Information (Caller Name, Caller Phone, and Details), all other fields will remain disabled.
Leave this box unselected to leave the service call open.

## Call Information: Details

The Call Information: Details field on the SM Call Handler form, Info tab.
Enter the details about this service call. Space allowance is virtually unlimited.
The information entered here is informational only; it will not be updated to the work order if one is generated.

## Work Order

The Work Order field on the SM Call Handler form, Info tab.
To use your own numbering scheme, enter a unique number (1-2,147,483,647).
To auto-generate a number, leave the field blank. The system will generate a work order number when you create the work order as follows:

- If a value is specified in the Next Work Order Number field in SM Company Parameters, the system assigns the first unused sequential number after that value.

- If the Next Work Order Number field is blank in SM Company Parameters, the system assigns the next sequential number available based on the highest work order number in the system.

Note: You can also enter N, New, or
 n to
 immediately generate a number. The system assigns a number using one of the two options
 indicated above. However, because the work order is not set up in SM Work Orders until you
 click the Create Work Order button, it is possible that the number generated here may no
 longer be available when the work order is created. In which case, the system assigns
 the next available number found.

## Description

The Description field on the SM Call Handler form, Info tab.
Enter a description of the work order, up to 60 characters. When you create the work order, this will become the work order header description.

## Work Scope

The Work Scope field on the SM Call Handler form, Info tab.
Enter the work scope that represents the work
 to be done for this service call. Press F4 to select from a list of valid work
 scopes.
Leave this field blank if this service call is not associated with an existing work scope.

## New Work Order: Details

The New Work Order: Details field on the SM Call Handler form, Info tab.
Enter a description of the problem or service
 request; space allowance is virtually unlimited. When you create the work order, this
 description will default in the Scope Detail field on the work order
 scope.

## Division

The Division field on the SM Call Handler form, Info tab.
Enter the service center division or press F4 to select from a list of valid service
 center divisions. This will generally be the division that handles the type of work to be done for this service call.

## Agreement

The Agreement field on the SM Call Handler form, Info tab.
This field is enabled only if the customer specified for this service call is an existing customer.
Enter the agreement to which this service call applies, if applicable. Press F4 to select from a list of valid agreements for the specified customer. The agreement's current Rev displays to the right and cannot be changed.

## Priority

The Priority field on the SM Call Handler form, Info tab.
Enter Low, Med, or High to
 represent the priority of the work order. If you entered a work scope above, this field
 will default the priority specified for the work scope (in SM Work Scopes). May be
 overridden as necessary.

## Service Item

The Service Item field on the SM Call Handler form, Info tab.
This field is only enabled if you specified an existing service site for the service call.
Enter the serviceable item to which this
 service call applies or press F4 to select from a list of valid
 serviceable items for the service site.
Leave this field blank if the service call does not apply to a specific serviceable item.

## Call Type

The Call Type field on the SM Call Handler form, Info tab.
Enter the call type (from SM Call Types) for
 the work order. Press F4 for a list of all valid call types or
 call types by service center.

## Due Date

The Due Date field on the SM Call Handler form, Info tab.
Specify the due date for this work order. When you create the work order, the system assigns this date to the work order scope and sets the due date type to 0-By.

## Customer PO

The Customer PO field on the SM Call Handler form, Info tab.
Enter the PO number (provided by the customer) for this work order scope, up to 30 characters.
Leave blank if there is no customer PO associated with this service call.
