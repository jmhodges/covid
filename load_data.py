import pandas


def load_cases():
    df = pandas.read_csv("data/cases.csv")
    df["time"] = pandas.to_datetime(df["Test Date"])
    df["county"] = df["County"].str.lower()
    return (
        df[
            [
                "time",
                "county",
                "New Positives",
                "Cumulative Number of Positives",
                "Total Number of Tests Performed",
                "Cumulative Number of Tests Performed",
            ]
        ]
        .set_index(["time", "county"])
        .apply(lambda s: s.str.replace(",", ""))
        .apply(pandas.to_numeric)
        .sort_index()
    )


def load_hospitalizations():
    df = pandas.read_csv("data/hospitalizations.csv")
    df["time"] = pandas.to_datetime(df["As of Date"])
    df["county"] = df["Facility County"].str.lower()
    df["Total Staffed Beds"] = df["Total Staffed Beds"].str.replace(
        ",", "").replace('"', "")
    df["Total Staffed Beds Currently Available"] = df["Total Staffed Beds Currently Available"].str.replace(
        ",", "").replace('"', "")
    return (
        df[
            [
                "time",
                "county",
                "Patients Currently Hospitalized",
                "Patients Newly Admitted",
                "Patients Positive After Admission",
                "Patients Discharged",
                "Patients Currently in ICU",
                "Patients Currently ICU Intubated",
                "Patients Expired",
                "Total Staffed Beds",
                "Total Staffed Beds Currently Available",
                # "Total Staffed ICU Beds",
                # "Total Staffed ICU Beds Currently Available",
                # "Total Staffed Acute Care Beds",
                # "Total Staffed Acute Care Beds Occupied",
                # "Total Staffed ICU Beds 1",
                # "Total Staffed ICU Beds Currently Occupied"
            ]
        ]
        .set_index(["time", "county"])
        .apply(pandas.to_numeric)
        .sort_index()
    )
