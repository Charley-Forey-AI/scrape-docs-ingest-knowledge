---
title: "Grid Filtering Criteria | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/getting-started/getting-started-with-vista/user-interface-guide/system-forms/form-grids/filter-grid-records/grid-filtering-criteria"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/getting-started/getting-started-with-vista/user-interface-guide/system-forms/form-grids/filter-grid-records/grid-filtering-criteria"
---

# Grid Filtering Criteria

Most form in the system have a Grid tab. It is used for
 viewing, entering, or editing records in a spreadsheet format. You can filter records on the
 Grid tab so that you can easily locate a specific record or set of records.
Filtering is based on the order in which you
 enter information. For example, if you enter 11, the only records that will return for
 that column are values beginning with 11 (1100, 112, 1132, etc.), rather than returning
 values that contain 11 (32112, 211, 89113, etc.). The advantage to this type of
 filtering is that it increases the speed in which records are displayed. Additionally,
 results include values that begin with a space. For example, if you enter 11 as the
 filtering criteria, the code _1122 would display.
You can use additional filtering options to
 fine-tune the data returned. You can:

- Enter a specific value and that value (and only that value) will be returned to
 the form.Note: When using this option, the value you enter must be unique. If
 you enter a specific value, but other records begin with that value, the
 system will return those values as well. For example, filtering by Customer,
 with a value of 100 will return records for Customer 100, as well as records
 for customers 1001, 1002, and so forth. Therefore, you may need to filter by
 other criteria (such as the customer's name, rather than the customer's
 number) or enter additional search criteria.

- Use comparison operators (<, >, <>, =, >=, <=). For example,
 if you enter the greater than operator and the desired value (for example,
 >540202), the grid will display a set of records beginning with the first
 record greater than the filter value (540203).

- Use wildcards (% or *). If you enter the % or * wildcard before a value (for
 example, %540 or *540), the search will return records that contain the
 specified value (15402, 33540, 54002, etc.).

Related information

- [Filter Grid Records](/en/vista/vista/getting-started/getting-started-with-vista/user-interface-guide/system-forms/form-grids/filter-grid-records)
