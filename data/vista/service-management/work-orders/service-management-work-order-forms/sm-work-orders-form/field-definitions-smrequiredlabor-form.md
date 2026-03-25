---
title: "Field Definitions: SMRequiredLabor Form | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/service-management/work-orders/service-management-work-order-forms/sm-work-orders-form/field-definitions-smrequiredlabor-form"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/service-management/work-orders/service-management-work-order-forms/sm-work-orders-form/field-definitions-smrequiredlabor-form"
---

# Field Definitions: SMRequiredLabor Form

The following is a list of field descriptions for the
 SMRequiredLabor form. Many of the descriptions include links to other topics that provide additional information about or related to the topic.

## Labor: Seq

Enter N, New, or +. The system will auto-generate a
 sequence number for the requirements entry.
Note: For class maintenance tasks, agreement services, work order quotes, or work orders defaulting requirement records from a standard task (assigned on the Tasks tab), this field cannot be edited. However, you can add new requirement records.

## Labor: Task

Enter the task associated with this
 requirements entry or leave blank if this requirements entry is not related to a task.
 Press F4 for a list of valid tasks (those set up on the Tasks tab).
Note: For class maintenance tasks, agreement services, work order quotes, or work orders defaulting requirement records from a standard task (assigned on the Tasks tab), this field cannot be edited.

## Labor: Technician

Enter the technician for this labor
 requirements entry (typically the technician who will be scheduled to perform the work).
 Press F4 for a list of valid technicians for the active SM company.
Note: For labor requirements auto-populated from a standard task (assigned on the Tasks tab), this field defaults as blank. If you enter a technician for a PR company that differs from the PR company associated with the line's defaulted craft/class, the craft/class values will either be replaced by the craft/class defined for the technician in PR Employees or set to blank if no craft/class is defined for the technician. Default may be overridden.

## Labor: Craft

Required if entering a craft class in the
 Class field.
Enter the craft for this labor requirements entry or leave blank if a specific craft is not required. Press F4 for a list of valid crafts.
Note: Class Maintenance, Agreement Services, Work Order Quotes, and Work Orders only:
Note: For requirement entries auto-populated from a standard task (assigned on the Tasks tab), this field will automatically default as defined for the requirements record in SM Standard Tasks (if applicable). Default may be overridden.

## Labor: Class

Enter the craft class for this labor
 requirements entry. Press F4 for a list of valid craft classes.
Leave this field blank if you did not specify
 a craft in the Craft field.
Note: Class Maintenance, Agreement Services, Work Order Quotes, and Work Orders only:
Note: For requirement entries auto-populated from a standard task (assigned on the Tasks tab), this field will automatically default as defined for the requirements record in SM Standard Tasks (if applicable). Default may be overridden.

## Labor: Qty

Enter the labor quantity for this labor requirements entry. This will typically be the number of hours you estimate it will take to complete the work.
Note: Class Maintenance, Agreement Services, Work Order Quotes, and Work Orders only:
Note: For requirement entries auto-populated from a standard task (assigned on the Tasks tab), this field will automatically default as defined for the requirements record in SM Standard Tasks (if applicable). Default may be overridden.

## Labor: Cost Rate

Enter the cost rate for this labor requirement. Initially defaults a rate from SM Labor Cost Estimate based on the current date and the information entered for the labor requirement (e.g. PRCo, Technician, Craft, Class, and/or Effective Date). If no matching record is found in SM Labor Cost Estimate, the cost rate defaults as 0.00. For more information, see [Setting Up Labor Cost Rate Estimates](/en/vista/vista/service-management/service-management-setup/set-up-labor-cost-estimates).

## Labor: Cost Total

This field defaults the total cost for this requirements line and cannot be edited.

## Labor: Billing Rate

This field only displays for work order and work order quote scopes with a Time and Materials pricing method and agreement services with a Time of Service, Rate Template pricing method.
Display only, the billing rate for the selected required labor sequence. Defaults the advanced rate defined by technician, craft/class, and/or call type (in SM Advanced Labor Overrides) or the standard rate defined on the template associated with the agreement service, work order quote scope, or work order scope (if no override rates are defined).
The system uses the following hierarchy to determine the billing rates to use for required labor lines.
Technician
PRCo
Craft
Class
Call Type

X

X

X

X
X

X
X

X

X
X
X

X
X
X
X

X
X

X
X
X

X
X
X
X

X
X
X
X
X

Note: Unlike work completed labor lines, required labor lines do not include a pay type. Therefore, overrides set up with a pay type (in SM Advanced Labor Overrides) will be ignored when determining the billing rate for the required labor line. If you have rates set up that normally include a pay type and you want to use those rates for required labor lines, make sure you set up those same combinations without the pay type.

## Labor: Total Billable

This field only displays for work order and work order quote scopes with a Time and Materials pricing method and agreement services with a Time of Service, Rate Template pricing method.
Display only, the total billable for this required labor sequence.

## Labor: Tax Type

Tax Type field on the Labor tab of the following forms: SM Service, SM Work Order Quotes, and SM Work Orders.
This field only displays for work order quotes and customer work orders with a pricing method of T-Time and Material, and for agreement services with a pricing method of T-Time of Service, Rate Template.
If the labor required for the quote, work order, or agreement service is taxable, specify the tax type:

- 1 - Sales

- 3 - VAT

## Labor: Tax Code

Tax Code field on the Labor tab of the following forms: SM Service, SM Work Order Quotes, and SM Work Orders.
This field only displays for work order quotes and customer work orders with a pricing method of T-Time and Material, and for agreement services with a pricing method of T-Time of Service, Rate Template.
Enter the tax code to use for calculating the tax amount for this labor sequence. This field initially defaults the tax code for the Service Site or Service Center, depending on the Tax Source specified for the quote, work order, or agreement service. If no tax code is specified for the service site or service center, defaults as blank.

## Labor: Tax Basis

Tax Basis field on the Labor tab of the following forms: SM Service, SM Work Order Quotes, and SM Work Orders.
This field only displays for work order quotes and customer work orders with a pricing method of T-Time and Material, and for agreement services with a pricing method of T-Time of Service, Rate Template.
Enter the taxable portion of the total amount for this labor sequence or accept the default amount (defaults from Total Billable).
