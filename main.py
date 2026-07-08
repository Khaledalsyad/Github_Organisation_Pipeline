from extract import extract_data
from transform import transform_data, incremental_filter
from load import loading_data
from metadata import get_last_run_time, updated_last_run_time
from notification import send_email

def run_pipeline():
    # extract the data from sources
    df = extract_data()

    # start the cleaning data and transforming
    df = transform_data(df)

    # get the last run of data
    last_run_time = get_last_run_time()
    print(last_run_time)

    # Filter if the updated data is bigger than the last run
    df = incremental_filter(df, last_run_time)

    # len of the last data run return
    if df.empty:
        print("No Last Run Found")
        return

    # start loading data
    loaded_result = loading_data(df)

    # report of smtplib notification
    report = {
        "status" : loaded_result["status"],
        "loaded_rows": loaded_result["loaded_rows"],
        "execution_time": "N/A",
        "message": "New repositories loaded successfuly"
    }

    try:
      send_email(report)
    except Exception as e:
        print(e)

    # max of last update run data
    max_update_run = df['updated_at'].max()

    updated_last_run_time(max_update_run)
    print('update data successfully')


if __name__ == "__main__":
    run_pipeline()