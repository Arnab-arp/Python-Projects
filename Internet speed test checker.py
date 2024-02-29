import speedtest


def test_internet_speed():
    st = speedtest.Speedtest()
    st.config()
    print("Testing download speed...")
    download_speed = st.download() / 10**6
    print("Download speed: {:.2f} Mbps".format(download_speed))

    print("Testing upload speed...")
    upload_speed = st.upload() / 10**6
    print("Upload speed: {:.2f} Mbps".format(upload_speed))


if __name__ == "__main__":
    test_internet_speed()
