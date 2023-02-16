import pandas as panda
import logging




logging.basicConfig(
    level=logging.DEBUG,
    filename="log_main.log",
    filemode="w",
    format="%(asctime)s - %(levelname)s - %(message)s"
)


def run():

    data_2014 = panda.read_excel(r"data\Verbrauch_2014.xlsx", index_col=0)
    data_2015 = panda.read_excel(r"data\Verbrauch_2015.xlsx", index_col=0)
    data_2016 = panda.read_excel(r"data\Verbrauch_2016.xlsx", index_col=0)
    data_2017 = panda.read_excel(r"data\Verbrauch_2017.xlsx", index_col=0)
    data_2018 = panda.read_excel(r"data\Verbrauch_2018.xlsx", index_col=0)
    data_2019 = panda.read_excel(r"data\Verbrauch_2019.xlsx", index_col=0)
    logging.info("The outflow data are properly loaded into the system.")


    data = list()
    data.append(data_2014)
    data.append(data_2015)
    data.append(data_2016)
    data.append(data_2017)
    data.append(data_2018)
    data.append(data_2019)

    data_2014_df_verbrauch_max = data_2014['Verbrauch'].max()
    data_2015_df_verbrauch_max = data_2015['Verbrauch'].max()
    data_2016_df_verbrauch_max = data_2016['Verbrauch'].max()
    data_2017_df_verbrauch_max = data_2017['Verbrauch'].max()
    data_2018_df_verbrauch_max = data_2018['Verbrauch'].max()
    data_2019_df_verbrauch_max = data_2019['Verbrauch'].max()

    my_data = list()
    my_data.append(data_2014_df_verbrauch_max)
    my_data.append(data_2015_df_verbrauch_max)
    my_data.append(data_2016_df_verbrauch_max)
    my_data.append(data_2017_df_verbrauch_max)
    my_data.append(data_2018_df_verbrauch_max)
    my_data.append(data_2019_df_verbrauch_max)

    qdmax= max(my_data)
    logging.info(f"The max. amount of outflow is {qdmax}.")

    criteria_1 = 0.5 * qdmax
    print(f"{criteria_1=}")
    logging.info(f"The category 1 is {criteria_1}.")


if __name__ == '__main__':
    run()

