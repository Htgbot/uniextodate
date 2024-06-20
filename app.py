from flask import Flask, request, jsonify
from datetime import datetime
import pytz

app = Flask(__name__)

# Set the time zone
colombo_tz = pytz.timezone('Asia/Colombo')

@app.route('/convert/<int:unix1>&<int:unix2>', methods=['POST'])
def convert_timestamps(unix1, unix2):
    # Convert Unix timestamps to datetime in Colombo time zone
    created_date = datetime.fromtimestamp(unix1, colombo_tz).strftime('%m/%d/%Y %I:%M %p')
    last_login_date = datetime.fromtimestamp(unix2, colombo_tz).strftime('%m/%d/%Y %I:%M %p')

    # Prepare response
    response = {
        "Created_Date": created_date,
        "LastLogin_Date": last_login_date
    }

    return jsonify(response)

if __name__ == '__main__':
    app.run(debug=True)

