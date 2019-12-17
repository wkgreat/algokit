"""
china administrative regions name and codes
"""
import pandas as pd


def all_china_provinces():
    """
    all china provinces code and name
    :return iterator of tuple(prov_code, prov_name)
    """
    df = pd.read_csv('adcodes.csv')
    df = df[["prov_id","prov_name"]]
    df.drop_duplicates(inplace=True)
    for r in df.iterrows():
        yield r[1].to_list()


def all_china_cities(province_code=None, province_name=None):
    """
    all china cities code and name
    :param province_code: filter by province code
    :param province_name: filter by province name, skip it if province code was set
    :return iterator of tuple(prov_code, prov_name, city_code, city_name)
    """
    df = pd.read_csv('adcodes.csv')
    if province_code: df = _filter_by_prov_code(df, province_code)
    elif province_name: df = _filter_by_prov_name(df, province_name)
    df = df[["prov_id","prov_name","city_id","city_name"]]
    df.drop_duplicates(inplace=True)
    for r in df.iterrows():
        yield r[1].to_list()


def all_china_districts(province_code=None, province_name=None, city_code=None, city_name=None):
    """
    all china districts code and name
    :param province_code: filter by province code
    :param province_name: filter by province name, skip it if province code was set
    :param city_code: filter by city code
    :param city_name: filter by city name, skip it if city code was set
    :return iterator of tuple(prov_code, prov_name, city_code, city_name, distinct_code, district_name, phone_code)

    when both province and city parameter are set, must guarantee the city located in the province.
    """
    df = pd.read_csv('adcodes.csv')
    if province_code: df = _filter_by_prov_code(df, province_code)
    elif province_name: df = _filter_by_prov_name(df, province_name)
    if city_code: df = _filter_by_city_code(df, city_code)
    elif city_name: df = _filter_by_city_name(df, city_name)
    df.drop_duplicates(inplace=True)
    for r in df.iterrows():
        yield r[1].to_list()


def _filter_by_prov_code(df: pd.DataFrame, prov_code) -> pd.DataFrame:
    prov_id = int(prov_code)
    df = df[df["prov_id"] == prov_id]
    return df


def _filter_by_prov_name(df: pd.DataFrame, prov_name) -> pd.DataFrame:
    df = df[df["prov_name"] == prov_name]
    return df


def _filter_by_city_code(df: pd.DataFrame, city_code) -> pd.DataFrame:
    city_id = int(city_code)
    df = df[df["city_id"] == city_id]
    return df


def _filter_by_city_name(df: pd.DataFrame, city_name) -> pd.DataFrame:
    df = df[df["city_name"] == city_name]
    return df


if __name__ == '__main__':
    print(list(all_china_districts(province_name="山东省", city_name="济宁市")))






