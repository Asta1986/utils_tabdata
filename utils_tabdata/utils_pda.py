from pandas import DataFrame, ExcelWriter


class UtilsPDA:
    @staticmethod
    def dframes_to_excel_sheets(data_frames, sheet_names, file_name):
        """Creates an excel file with the contents of a data frame per sheet.
        Precondition: data_frames and sheet_names parameters have the same length.
        """
        try:
            with ExcelWriter(file_name + ".xlsx") as writer:
                ct = 0
                for df in data_frames:
                    df.to_excel(writer, sheet_name=sheet_names[ct], index=False)
                    ct += 1
        except IOError:
            print("File {} could not be created.".format(file_name))

    @staticmethod
    def print_numtable(table):
        """Prints the received table (2D array) with column and row numbers
        and fixed column width (up to 46 characters per cell).
        """
        print(DataFrame(table))
