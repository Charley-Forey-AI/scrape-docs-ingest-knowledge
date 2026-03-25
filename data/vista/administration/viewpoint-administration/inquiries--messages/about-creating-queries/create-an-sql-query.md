---
title: "Create an SQL Query | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/administration/viewpoint-administration/inquiries--messages/about-creating-queries/create-an-sql-query"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/administration/viewpoint-administration/inquiries--messages/about-creating-queries/create-an-sql-query"
---

# Create an SQL Query

These steps provide a basic overview of query construction,
 but do not go into detail.
To create a SQL type query:

1. Enter a name for the
 query in the
 Query Name
 field.

1. Enter a title for the
 query in the
 Title
 field.

1. Enter a description for
 the query in the
 Description
 field.

1. Select
 SQL
 in the
 Type
 field.

1. To make the query
 available to be assigned to a Work Center, select the Assignable in
 Work Center checkbox.

1. Enter the query in the

 Query Text
 field, including the Select, From, and Where clauses. Note: The Select clause identifies the
 information that you want to return from the database. For example, you
 might enter Select Name, Address, City, Zip to query for a name, address,
 city, and zip code. The Where clause filters the information returned by the
 query. When creating a Where clause, specify the primary table that
 information is being requested from. If you are using multiple tables in the
 query, you must define the “joins.” Joins identify how the tables are
 linked; that is, the unique set of values that exist in both tables. After
 identifying the tables, specify how the system filters the data.
Note: Using the address example from above,
 you may want to pull name and address information from the HQ Company Setup
 (HQCO) table. Additionally, you may want to filter for a specific company.
 To do this, the WHERE clause would look like this: FROM HQCO WHERE HQCO=1.
 This clause has the query pull records from HQCO for Company 1. No joins
 exist in this example.

1. Click the
 Update Columns
 button. All specified database columns now display on the Columns
 tab. Note: Using the example from step 5, the
 following columns would display on the Columns tab: Name, Address, City, and
 Zip.

1. Use the Columns tab to
 define how the columns should display in the Work Center. Press F1
 in any of the fields on this tab for more information.

1. Add parameters to
 restrict the records that the query returns. See [Restricting Queries with Parameters](/en/vista/vista/administration/viewpoint-administration/inquiries--messages/restricting-queries-with-parameters).

1. Associate the query with
 specific Work Center templates. See [About Associating Queries with Work Center Templates](/en/vista/vista/administration/viewpoint-administration/inquiries--messages/about-associating-queries-with-work-center-templates).

1. Save the query.

1. If you want to link the
 queries so that users can drill-through them on a Work Center, create an inquiry
 using the Links tab. See [Creating Inquiries](/en/vista/vista/administration/viewpoint-administration/inquiries--messages/creating-inquiries).

1. Set security for the
 query using the [About the VA Inquiry Security Form](/en/vista/vista/administration/viewpoint-administration/inquiries--messages/about-the-va-inquiry-security-form) form.
