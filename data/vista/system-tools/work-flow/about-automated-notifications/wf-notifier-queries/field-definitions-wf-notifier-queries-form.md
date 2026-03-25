---
title: "Field Definitions: WF Notifier Queries Form | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/system-tools/work-flow/about-automated-notifications/wf-notifier-queries/field-definitions-wf-notifier-queries-form"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/system-tools/work-flow/about-automated-notifications/wf-notifier-queries/field-definitions-wf-notifier-queries-form"
---

# Field Definitions: WF Notifier Queries Form

The following is a list of field descriptions for the WF
 Notifier Queries form. Many of the descriptions include links to other topics that provide additional information about or related to the topic.

## Query Name

Enter a name for the query. The query name is
 used to select the Notifier Query in the Query field on the Info tab of [WF Notifier Job Manager ](/en/vista/vista/system-tools/work-flow/about-automated-notifications/wf-notifier-job-manager). The query name must be
 unique.
To select an existing query, press F4 to select
 one from a list.

## Title

Enter a title of the query. The title can be up to 255 characters long.

##  Event Query

 Select this checkbox if the query is event driven.
For more information about even-driven queries, see [About Event-Driven Queries](/en/vista/vista/system-tools/work-flow/about-automated-notifications/about-event-driven-queries).

## Description

Enter a description of the query. The description can be up to 255 characters long.
Generally the description should describe the function that the query performs. For example, if a query notifies you when a vehicle's license expires, your query description might be "This procedure will return 1 row for each piece of equipment whose license is either expired, or will expire, within the next 30 days."

## Select Clause

Enter the SELECT clause in this field. The text in this field can be up to 8,000 characters long.
 Click the Format Query
 button to format the select clause. Formatting adds brackets where necessary to identify
 query parameters (email fields).
If there is a similar SELECT clause in an
 existing query, for example a standard query, you can copy the SELECT clause from that
 query and then paste it into this field.
Enter the following text in the SELECT Clause
 field if you want to create a Notifier Query that generates a list of employees with a
 birthday in the current month.
Select Name as [Name], Address as [Address],
 Zip as [Zip]
Click [here](/en/vista/vista/system-tools/work-flow/about-automated-notifications/wf-notifier-queries/field-definitions-wf-notifier-queries-form#ID-0004dd83--en)
 for information on what should be entered in the FROM WHERE Clause field to complete this
 query.

## From Where Clause

Enter the FROM and WHERE clauses in this field. The text in this field can be up to 8,000 characters long.
Important: If you are using datatype security, you cannot use views; you can only use tables. Click [here](/en/vista/vista/administration/viewpoint-administration/application-security/data-record-and-content-security/datatype-security/securing-datatypes) for information about setting up datatype security.
 When creating a FROM and WHERE clause, you
 must specify the primary table/view that information is being requested from. If you are
 using multiple tables in the query, you must define the “joins.” Joins identify how the
 tables are associated; that is, the unique set of values that exist in both tables. After
 identifying the tables to use, you must specify how the system filters the returned data.
 Select Options > Viewpoint
 Views to open the [WF Notifier Viewpoint Tables ](/en/vista/vista/system-tools/work-flow/about-automated-notifications/wf-notifier-viewpoint-tables) form. This form displays a
 list of views and the fields associated with them.
If there is a similar FROM and WHERE clause in
 an existing query, for example a standard query, you can copy the FROM and WHERE clause
 from that query and then paste it into this field.

### Example

Enter the following text in the FROMWHERE
 Clause field if you want to create a Notifier Query that generates a list
 of employees with a birthday in the current month.
FROM HQCO
WHERE HQCo > @company
@company is a local variable that will be
 used to filter the results by HR company. You need to create an entry for this local
 variable on the Query Parameters tab on this form once you have saved the query. When
 the Notifier Query is associated with a Notifier Job, you will be able to define the
 value of this variable using the Parameters tab on the [WF Notifier Job Manager ](/en/vista/vista/system-tools/work-flow/about-automated-notifications/wf-notifier-job-manager) form.
Click [here](/en/vista/vista/system-tools/work-flow/about-automated-notifications/wf-notifier-queries/field-definitions-wf-notifier-queries-form#ID-0004dd72--en)
 for information on what should have been entered in the SELECT
 Clause field in this example.

## Parameter

Enter any local variables that you used in the
 SQL query entered in the SELECT Clause and FROM WHERE
 Clause fields on the Info tab.
For example if you used an @company or @days
 local variable in the WHERE clause of your SQL statement, create an entry for each of those
 entries on the Query Parameters tab. When the Notifier Query is associated with a Notifier
 Job, you can use the Parameters tab on the [WF Notifier Job Manager ](/en/vista/vista/system-tools/work-flow/about-automated-notifications/wf-notifier-job-manager) form to set the value of those
 parameters.

## Description

Enter a description of the parameter. The description can be up to 255 characters long.
The description should indicate the expected entry type for the parameter. For example, if your query sends a notification when a vehicle's license expires, and the parameter is Days, the description might prompt to specify the number of days before the vehicle's license expires that a warning should be given.
