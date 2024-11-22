import argparse
import csv


# Define column mappings from old to new names
COLUMN_MAPPINGS = {
    "Email Address": "email",
    "First Name": "first_name",
    "Last Name": "last_name",
    "Address": "address_line_1",
    "Phone Number": "phone_number_id",
}

# Define the full list of new column names in the desired order
NEW_COLUMNS = [
    "email",
    "first_name",
    "last_name",
    "address_line_1",
    "address_line_2",
    "city",
    "state_province_region",
    "postal_code",
    "country",
    "phone_number_id",
    "external_id",
    "anonymous_id",
]


def remap_csv(input_files, output_file):
    # Open the output CSV file
    with open(output_file, mode="w", newline="", encoding="utf-8") as outfile:
        # Initialize writer with the new column names
        writer = csv.DictWriter(outfile, fieldnames=NEW_COLUMNS)
        writer.writeheader()

        # Process each input CSV file
        for input_file in input_files:
            with open(input_file, mode="r", newline="", encoding="utf-8") as infile:
                reader = csv.DictReader(infile)

                # Process each row in the current input CSV
                for row in reader:
                    # Create a new row with default empty values
                    new_row = {col: "" for col in NEW_COLUMNS}

                    # Map values from the old CSV to the new CSV
                    for old_col, new_col in COLUMN_MAPPINGS.items():
                        new_row[new_col] = row[old_col]

                    # Write the new row to the output CSV
                    writer.writerow(new_row)


def main():
    # Set up argument parser
    parser = argparse.ArgumentParser(
        description="Remap columns in multiple CSV input and combine them into a single output file."
    )
    parser.add_argument("input_files", nargs="+", help="Paths to the input CSV input")
    parser.add_argument("output_file", help="Path to the output CSV file")

    # Parse arguments
    args = parser.parse_args()

    # Call the remap function with the provided file paths
    remap_csv(args.input_files, args.output_file)


if __name__ == "__main__":
    main()
