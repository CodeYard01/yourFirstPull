# Runs a speed test to measure the down and Upload of you Mashines speed in megabits per second.


import speedtest


def run_speedtest_download():

    # Create a Speedtest object
    test = speedtest.Speedtest()

    # Perform the download speed test
    download = test.download()

    # Convert the download speed to megabits per second
    download_mbits = download / 1000000

    # Round the download speed to 3 decimal places
    download_mbits_rounded = round(download_mbits, 3)

    return download_mbits_rounded


def run_speedtest_upload():
    # Create a Speedtest object
    test = speedtest.Speedtest()

    # Perform the upload speed test
    upload = test.upload()

    # Convert the upload speed to megabits per second
    upload_mbits = upload / 1000000

    # Round the upload speed to 3 decimal places
    upload_mbits_rounded = round(upload_mbits, 3)

    return upload_mbits_rounded


def main():
    print("Running Speedtest [Download]...")
    download = run_speedtest_download()
    print(download)

    print("Running Speedtest [Upload]...")
    upload = run_speedtest_upload()
    print(upload)


main()
