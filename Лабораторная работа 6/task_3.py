OUTPUT_FILE = "output.csv"

headers_list = ['longitude', 'latitude', 'housing_median_age', 'total_rooms', 'total_bedrooms', 'population',
                'households', 'median_income', 'median_house_value']
data = [
    ['-122.050000', '37.370000', '27.000000', '3885.000000', '661.000000', '1537.000000', '606.000000', '6.608500',
     '344700.000000'],
    ['-118.300000', '34.260000', '43.000000', '1510.000000', '310.000000', '809.000000', '277.000000', '3.599000',
     '176500.000000'],
    ['-117.810000', '33.780000', '27.000000', '3589.000000', '507.000000', '1484.000000', '495.000000', '5.793400',
     '270500.000000'],
    ['-118.360000', '33.820000', '28.000000', '67.000000', '15.000000', '49.000000', '11.000000', '6.135900',
     '330000.000000'],
]


def to_csv_file(FILE_OUTPUT, list_headers, rows, delimiter=",", new_line="\n"):
    with open(FILE_OUTPUT, "w") as file_rows:
        file_rows.write(delimiter.join(list_headers) + new_line)
        for rows in data:
            file_rows.write(delimiter.join(rows) + new_line)
    with open(FILE_OUTPUT) as file_line:
        for line in file_line:
            print(line, end="")
    return


to_csv_file(OUTPUT_FILE, headers_list, data)
