import Analysis as analysis
import os


def main():
    path = "./Data/"
    files = [file for file in os.listdir(path) if not file.startswith('.')]  # Ignore hidden files

    #preprocess Data
    dataframe = analysis.merge_data(files, path)
    dataframe = analysis.clean_data(dataframe)
    dataframe = analysis.preprocess_data(dataframe)

    #perform analysis
    analysis.get_best_month(dataframe, path)
    analysis.most_sold_city(dataframe, path)
    analysis.ad_time(dataframe, path)


if __name__ == "__main__":
    main()


