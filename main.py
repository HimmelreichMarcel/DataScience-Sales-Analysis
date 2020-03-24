import Analysis as analysis
import os


def main():
    path = "./Data/"
    files = [file for file in os.listdir(path) if not file.startswith('.')]  # Ignore hidden files

    #preprocess Data
    dataframe = analysis.MergeData(files, path)
    dataframe = analysis.CleanData(dataframe)
    dataframe = analysis.PreprocessData(dataframe)

    #perform analysis
    analysis.GetBestMonth(dataframe)
    analysis.MostSoldCity(dataframe)
    analysis.AdTime(dataframe)


if __name__ == "__main__":
    main()


