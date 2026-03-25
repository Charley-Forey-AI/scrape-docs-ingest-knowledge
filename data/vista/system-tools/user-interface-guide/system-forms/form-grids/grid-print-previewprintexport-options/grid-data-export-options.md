---
title: "Grid Data Export Options | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/system-tools/user-interface-guide/system-forms/form-grids/grid-print-previewprintexport-options/grid-data-export-options"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/system-tools/user-interface-guide/system-forms/form-grids/grid-print-previewprintexport-options/grid-data-export-options"
---

# Grid Data Export Options

Most forms in the system have a Grid tab. It is used for
 viewing, entering, or editing records in a spreadsheet format. You have multiple options
 when exporting data from a grid.
Export Option Description
Header Text/HeightUse this field to enter the text you want displayed in the header of
 the document (above the grid). Initially defaults the form name
 (e.g. AP Vendor Compliance), which may be overridden. Headings are
 set to default center alignment (indicated by the ‘\t’ before the
 form name); however, you can change the alignment to left or right
 if desired. For left alignment, simply remove the alignment code
 (\t). For right alignment, enter a second alignment code before the
 form name (e.g. \t \t AP Vendor Compliance). Note: The Height
 setting controls the height of the row, which determines how far
 above the grid the heading will display. Although you can enter
 any number 0-100, you must enter a minimum height of 15 in order
 for the heading to display.

Footer Text/ HeightUse this field to enter the text you want displayed in the footer of
 the document (below the grid). Initially set to default page number
 and total pages (\p of \P), which will be rendered as ‘# of #’ (e.g.
 1 of 10, 2 of 10, etc.) Default may be overridden. Footers are also
 set for center alignment, which may be overridden. For left
 alignment, simply remove the alignment code (\t). For right
 alignment, enter a second alignment code before the paging codes
 (e.g. \t \t \p of \P).Note: The Height setting controls the height
 of the row, which determines how far below the grid the footer
 will display. Although you can enter any number 0-100, you will
 need to enter a minimum height of 10 in order for the footer to
 display.

Row HeightThis option controls the height of the rows in the grid.

- Stretch to Fit – Select this option to
 stretch the row height to fit all data.

- Fixed – Select this option to use the grid’s row height.

- Stretch up to Value – Select this option to stretch the row
 height to no greater than the value specified to the right.


Wrap text in columnsThis option controls whether or not the text in each cell is wrapped.
 Used in conjunction with the Row Height option above.

- Wrap All Text – Select this option to
 always wrap the text in a cell. Will only wrap text if you
 select the Stretch to Fit or Stretch Up To Value option
 above.

- Do Not Wrap Text – Select this option to
 never wrap the text in a cell.

- Wrap Like Columns – Select this option to use the column’s
 wrap property to wrap text.

Horizontal Page Break

- Fit Columns On One Page – Select this option
 to fit all columns on one page. Be aware that if there are more
 columns than can easily fit on the page, the columns will be
 compacted and may not be readable.

- Clip columns in page – Select this option if
 the far right column should be clipped if it does not fit on the
 page.

- Break On Splits – Select this option to
 place a break on a new split or on any column that does not fit
 on the page. Break will occur before the splitter or before the
 column.

- Break On Any Column – Select this option to place a break on any
 column that does not fit on the page. Break will occur before
 the column.

Stretch to Page Width

- Stretch All Columns – Select this option to
 extend (stretch) all columns proportionally to fit the page.

- Do Not Stretch – Select this option if you
 do not want columns stretched to fit the page. If the grid is
 smaller than the width of the page, empty space will print on
 the right side.

- Stretch Last Column – Select this option to extend the last
 column in a grid to fit the page.

Repeat Grid HeaderCheck this option to print the grid header at the top of each page.
 Leave unchecked to print the grid header on the top of the first
 page only.

Repeat Split HeadersCheck this option to print split captions at the top of each page
 below the grid header and above the column headings (if applicable).
 Leave unchecked if split captions should print on the first page only.
 (This feature is not currently used in the software.)
Repeat Column HeadersCheck this option to print column headers on each page. Leave
 unchecked to print column headings on first page only.
Repeat Column FootersCheck this option to print column footers at the bottom of each page.
 Leave unchecked to print column footers on the last page only. (This
 feature is not currently used in the software.)
Print Horizontal SplitsCheck this option to print/preview horizontal splits. All columns
 after the split will be printed. Leave unchecked if you do not want to
 print/preview horizontal splits. Only the columns before the split will
 be printed.
One Form Per PageCheck this option to print one record per page. Leave unchecked to
 print multiple records on one page. (This feature is not currently used
 in the software.)
Use Grid ColorsSelect this option to print grid colors (e.g. gray/white). Leave
 unchecked to print grid in white only.
Show ProgressSelect this option to show the progress indicator when printing grid
 to preview form or printer. Leave unchecked if you do not want to see
 the progress indicator.

Related information

- [Grid Print Preview/Print/Export Options](/en/vista/vista/system-tools/user-interface-guide/system-forms/form-grids/grid-print-previewprintexport-options)

- [Print Grid Data](/en/vista/vista/system-tools/user-interface-guide/system-forms/form-grids/grid-print-previewprintexport-options/print-grid-data)

- [Export Grid Data](/en/vista/vista/system-tools/user-interface-guide/system-forms/form-grids/grid-print-previewprintexport-options/export-grid-data)
