from flask import Flask, render_template
import os
import time
import socket
import requests
import random

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/page1")
def page1():
    return render_template("page1.html")

@app.route("/page2")
def page2():
    return render_template("page2.html")

@app.route("/page3")
def page3():
    return render_template("page3.html")

def download_random_picture():
    # List of 4K picture URLs
    picture_urls = [
        "https://picsum.photos/4096/2160",
        "https://picsum.photos/3840/2160"]
    # Choose a random URL from the list
    picture_url = random.choice(picture_urls)
    # Download the picture from the URL
    response = requests.get(picture_url)
    # Check if the download was successful
    if response.status_code == 200:
        # Save the picture to the local file system
        with open("random_ picture.jpg", "wb") as picture_file:
            picture_file.write(response.content)
        print("Successfully downloaded random picture.")
    else:
        print("Failed to download random picture.")

def calculate_latency():
    start_time = time.time()
    # send a ping request to the server
    server = 'google.com'
    port = 80
    try:
        socket.create_connection((server, port), timeout=2)
        end_time = time.time()
        latency = end_time - start_time
        print("Latency: {} seconds".format(latency))
    except:
        print("Error: Failed to calculate latency")


def calculate_throughput():
    # send data to the server and measure the time taken
    message = b'x' * 1000000 # 1 MB of data
    start_time = time.time()
    server = ('google.com', 80)
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.connect(server)
        sock.sendall(message)
        sock.recv(len(message))
        end_time = time.time()
        throughput = len(message) / (end_time - start_time)
        print("Throughput: {} bytes/second".format(throughput))
    except:
        print("Error: Failed to calculate throughput")

        
calculate_latency()
calculate_throughput()
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=True,host='0.0.0.0',port=port)