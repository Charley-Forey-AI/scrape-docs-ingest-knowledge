---
title: "Validation | Trimble Help"
source_url: "https://help.trimble.com/en/spectrum/spectrum/equipment/equipment-control/spectrum-menus/maintenance-overview/validation"
fetched_at: "2026-04-03T20:47:47.926179+00:00"
menu_path: "/en/spectrum/spectrum/equipment/equipment-control/spectrum-menus/maintenance-overview/validation"
---

# Validation

Use this section to set up the validation controls for this statistic code. The fields that display here depend on the selection made in the Result format section.

- If the Result format is set to Alpha-numeric, then a Validate alpha-numeric entries checkbox displays, and if this checkbox is selected, the Valid Results button is enabled. The Valid Results window displays a Alpha result column and a Test result column, and these entries are used in the Examination entry field for alpha-numeric statistic readings and tests in the Equipment - Statistics Entry window.

- If the Result format is set to Date, then the Validate minimum/maximum processing dates checkbox displays. When selected, the Examination entry field in the Equipment - Statistics Entry window will verify that the date entered is within the minimum/maximum date range, and dates outside the range will yield a "Fail" test result.

- If the Result format is set to either Numeric or Percentage, then the following fields display:

- Standard norm: Enter the standard value for this statistic code (for example, the standard tire PSI number). This entry will be used for comparison purposes, and will validate and display based on the mask entered above.

- Standard minimum: Enter the default minimum value for this statistic code. This entry will be used for comparison purposes, and numbers below this value will result in a "Fail" test result.

- Standard maximum: Enter the default maximum value for this statistic code. This entry will be used for comparison purposes, and numbers above this value will result in a "Fail" test result.
