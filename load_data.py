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
            ]
        ]
        .set_index(["time", "county"])
        .apply(pandas.to_numeric)
        .sort_index()
    )
