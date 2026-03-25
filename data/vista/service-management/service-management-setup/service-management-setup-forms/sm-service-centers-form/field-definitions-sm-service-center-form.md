---
title: "Field Definitions: SM Service Center Form | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/service-management/service-management-setup/service-management-setup-forms/sm-service-centers-form/field-definitions-sm-service-center-form"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/service-management/service-management-setup/service-management-setup-forms/sm-service-centers-form/field-definitions-sm-service-center-form"
---

# Field Definitions: SM Service Center Form

The following is a list of field descriptions for the SM
 Service Center form. Many of the descriptions include links to other topics that provide additional information about or related to the topic.

## Service Center

Enter a code, up to 10 characters, that identifies this service center.

## Description

Enter a description of this service center, up to 60 characters.

## Address

Enter the address for this service center, up to 60 characters.
If you have Internet access, you can click the
 Map button () to view the address using your
 default map site (Options > User
 Options). If you did not specify a country, the system uses the Default Country
 defined in HQ Company Setup.

## City

Enter the address city for this service center, up to 30 characters.
If you have Internet access, you can click the
 Map button () to view the address using your
 default map site (Options > User
 Options). If you did not specify a country, the system uses the Default Country
 defined in HQ Company Setup.

## State

Enter a valid state (as defined in HQ States)
 for this service center. The system validates the state based on the Default Country
 specified in HQ Company Setup for the active company. If not valid, an error displays, but
 entry is allowed. You must then enter a valid country for this state in the Country
 field.
If you have Internet access, you can click the
 Map button () to view the
 address using your default map site (Options > User
 Options). If you did not specify a country, the system uses the Default Country
 defined in HQ Company Setup.

## Zip Code

Enter the zip code, up to 10 characters.
If you have Internet access, you can click the
 Map button () to view the
 address using your default map site (Options > User
 Options). If you did not specify a country, the system uses the Default Country
 defined in HQ Company Setup.

## Country

Enter the 2-character country code. Entry in
 this field is required when the address exists outside the Default Country
 specified in HQ Company Parameters for the active company. Country must be valid for the
 specified state (e.g. state, province, territory, etc.) as defined in HQ States.
If you have Internet access, you can click the
 Map button () to view the
 address using your default map site (Options > User
 Options). If you did not specify a country, the system uses the Default Country
 defined in HQ Company Setup.

## Add'l Address

Use this field to enter additional mailing
 address information for this service center. For example, if this center receives mail at a
 P.O. Box, then you might enter the P.O. Box in the Address field above, and use this field
 to enter the street address.

## Phone

Enter the phone number for this service center, up to 20 characters.

## Fax

Enter the fax number for this service center, up to 20 characters.

## Email

Enter the email address for this service
 center.
Note: Clicking the Send button () will automatically open up Microsoft Outlook and set up an outgoing message for you using the email address specified in this field.

## Tax Code

Enter the tax code (from HQ Tax Codes) for this service center. This tax code will be used to calculate tax amounts when entering work completed on a work order that references this service center.
Note: The tax code entered here will only be used if the
 Sale
 Location is set to Service Center for the work order scope.
Leave this field blank if taxes will not be applied to work orders for this service center or if you want tax codes to be entered manually when entering work completed for a work order.

## Use
 Tax Code (Y/N)

Use Tax Code checkbox on the SM Service Center form, Info tab.
Select this checkbox in order to enter a tax code to use for Use tax.
 You
 will only need to enter a tax code into the Use Tax Code field if the Use tax code
 differs from the Sales tax code for this service site.
If you do not pay Use tax or if you use the same tax code for Sales and Use tax, leave this checkbox unselected and the field blank.

## Use Tax Code

Use Tax field on the SM Service Center form, Info tab.
Select
 the Use Tax
 Code checkbox and enter the Use tax code for this service center or press
 F4
 to select from a list of valid tax codes. You will only need to enter a tax code here if
 the Use tax code differs from the Sales tax code for this service center.
The system will default this tax code for material-related lines with a tax type of Use, and where the Tax Source for the agreement service, work order quote, or work order is Service Center.
Note: Material-related lines include: inventory work completed lines, purchase work complete lines that specify a material or a material SM cost type, miscellaneous work complete lines that specify a material SM cost type, required material lines, and required miscellaneous lines specifying a material SM cost type.

## Department

Enter the department (from SM Departments) to use for determining the GL accounts to update when capturing work completed on a work order that references this service center.
Note: You can override the department assigned to a service center by division. If you define overrides by division, the system will only use the department assigned here if no division is specified on the work order scope or if no department is assigned to the division specified on a work order scope.

## Reviewer

Enter a reviewer ID in this field to enable
 that user to mark work orders as ready to bill.
Press F4 in the Reviewer field
 for a list of active reviewers from which to choose. Press F5 to access
 the HQ Reviewers form.

## Active

Check this box to activate this service center. Once activated, it will be available for selection when assigning service centers to service sites (in SM Service Sites) and/or work orders (in SM Work Orders), and will be included in service site lookups.
Uncheck this box to deactivate this service center. Service center will not be available for selection when assigning service centers to service sites or work orders, and will not be included in service site lookups.
