---
title: "Track License Counts and Usage | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/getting-started/getting-started-with-vista/vista-licensing/track-license-counts-and-usage"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/getting-started/getting-started-with-vista/vista-licensing/track-license-counts-and-usage"
---

# Track License Counts and Usage

Check and monitor license usage in Vista using one or more of the following methods.

## On the VA User License Allocation Report

View your organization's current Vista license information and a comprehensive breakdown of
 user license distribution. You can use this information when reconciling on-demand
 licensing usage. For details, see [VA User License Allocation](/en/vista/vista/reports-catalog/viewpoint-administration-reports/viewpoint-administration-general-reports/va-user-license-allocation).

## On the VA License Usage by Day Report

Assess the licenses in use on the VA License Usage by Day report. For details, see [Assess License Usage](/en/vista/vista/getting-started/getting-started-with-vista/vista-licensing/assess-license-usage).

## On the VA User Profile Form

Open the VA User Profile form and see the [License Type](/en/vista/vista/administration/viewpoint-administration/setup-and-maintenance/user-profile-management/va-user-profile-form/field-definitions-va-user-profile-form#concept-8148--en) for each user in your organization.

## On the VA System Users Report

Use the VA System Users report to inspect user profiles and filter by license status and/or license type.

## With a SQL Query

Identify which forms and reports require an Office license. Use the following SQL query to find active Vista Office licenses:
`select VPUserName, LicenseType, DeactivatedDate, UserAccountTypeID, UserType, ExpiryDate`
`from DDUP`
`where LicenseType = 'Office'`
`and DeactivatedDate is null`
`and UserAccountTypeID = 0`
`and UserType = 0`
`and (ExpiryDate Is Null or ExpiryDate >= GETDATE())`
Note: If you want to find active PM licenses, change the `LicenseType` to `'PM'`.

## With VA License Type Inquiries in Work Center

Add VA License Type inquiries to a Work Center to identify forms requiring an Office license or those available to PM licenses.

- VAFormsOfficeLicenseReqUse this inquiry to identify forms that require an Office license or forms available to PM licenses.

- VAReportsOfficeLicenseReqUse this inquiry to identify reports that require an Office license or reports available to PM licenses.

For more information about setting up inquiries and adding them to a Work Center, see [Creating Inquiries](/en/vista/vista/administration/viewpoint-administration/inquiries--messages/creating-inquiries).

## On the Trimble Construction One Admin Center

If you have access, view or export license data from the Trimble Construction One Admin Center in a consolidated .CSV file report. For details and steps, see [Export License Data](/en/vista/vista/getting-started/getting-started-with-vista/vista-licensing/export-license-data).

Related information

- [Vista Licensing](/en/vista/vista/getting-started/getting-started-with-vista/vista-licensing)
