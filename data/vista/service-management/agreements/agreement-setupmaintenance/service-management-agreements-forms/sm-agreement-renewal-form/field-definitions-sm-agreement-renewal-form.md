---
title: "Field Definitions: SM Agreement Renewal Form | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/service-management/agreements/agreement-setupmaintenance/service-management-agreements-forms/sm-agreement-renewal-form/field-definitions-sm-agreement-renewal-form"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/service-management/agreements/agreement-setupmaintenance/service-management-agreements-forms/sm-agreement-renewal-form/field-definitions-sm-agreement-renewal-form"
---

# Field Definitions: SM Agreement Renewal Form

The following is a list of field descriptions for the SM
 Agreement Renewal form. Many of the descriptions include links to other topics that provide additional information about or related to the topic.

## Type

Enter the agreement type by which to filter
 agreements or press F4 to select from a list of valid agreement types.
Leave this field blank if not filtering by agreement type. The system will display all agreements meeting all filter criteria, regardless of agreement type.

## Customer

Enter the customer by which to filter
 agreements or press F4 to select from a list of valid SM Customers.
Leave this field blank if not filtering by customer. The system will display agreements meeting all filter criteria, regardless of customer.

## Service Center

Service Center field in the header of the SM Agreement Renewal form.
Enter the service center by which to filter agreements or press F4 to select from a list of valid service centers.
Leave blank if not filtering by agreement type.

## Division

Division field in the header of the SM Agreement Renewal form.
Enter the division by which to filter agreements or press F4 to select from a list of valid divisions.

Leave blank if not filtering by agreement type.

## Only Show Agreements with Auto Renew

Select this checkbox to show only those agreements with a Renew Through date specified in SM Agreements.
Leave this checkbox unselected to display all agreements meeting the filter criteria, regardless of whether a Renew Through date is specified in SM Agreements.

## Expiring Within ___ Days

This field only displays when you select the
 Expiring option in the Grid Shown field.
Enter the number of days before expiration by which to filter agreements. Only agreements that will expire within the specified number of days (from today) that meet all other filter criteria will be included in the grid.
Leave this field blank to show all expiring agreements, regardless of Expiration Date.

## Grid Shown

Select the agreements to show in the grid.

- Expiring - Select this option to show Expiring agreements. The Grid tab will display a list of expiring agreements meeting the specified filter criteria.

- Renewals - Select this option to show agreement renewals. The Grid tab will display a list of agreements meeting the specified filter criteria for which you have created a renewal.

## Markup Percent to Apply

This field only displays when you select the
 Renewals option in the Grid Shown field.
Enter the markup percent to apply to
 agreements selected for renewal (i.e. those agreements for which you have selected the
 Included checkbox). For example, to mark up agreement pricing by 15%,
 enter 15.00.
 To apply the markup percent, click the Apply
 to Included button. The system will update this value to the % Markup column
 for all agreements with the Included checkbox selected.

## Included

For expiring agreements (Grid Shown
 filter is set to Expiring), select this checkbox to include this agreement when creating
 renewals. Leave unselected if you are not ready to create a renewal for this agreement.
For agreement renewals (Grid Shown
 filter is set to Renewals), select this checkbox to include this agreement when activating
 renewals. Leave unselected if you are not ready to activate this agreement renewal.

## % Markup

Enabled for agreement renewals only.
 Enter the percent by which to mark up the price for this agreement. The system will automatically update the New Price based on the Previous Price and this percentage.
Note: The system disables this field for agreements where
 the Previous
 Price is blank or 0.00.

## New Price

Enter the new price for this agreement.

## % Markup

Enabled for agreement renewals only.
Enter the percent by which to mark up the price for this agreement service. The system will automatically update the New Price based on the Previous Price and this percentage.
Note: The system disables this field for agreement services where the Previous Price is blank or 0.00.

## New Price

Enabled for agreement renewals only, where Pricing Method is Periodic or Time of Service.
This field defaults a value based on the Previous Price and the % Markup. Accept the default or enter the new price. Overriding the default will cause the % Markup to be recalculated.
Note: The system disables this field for agreement services where the Previous Price is blank or 0.00.
