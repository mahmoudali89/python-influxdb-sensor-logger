# Python InfluxDB Sensor Logger

Simulates IoT sensor readings and stores them in InfluxDB (Time-Series database).

## Tech Stack
- Python 3.x
- InfluxDB 2.x (via Docker)

## Setup & Run

1. Start InfluxDB via Docker:
   \`\`\`bash
   docker run -d -p 8086:8086 --name influxdb influxdb:2
   \`\`\`

2. Set up InfluxDB at http://localhost:8086 (create org, bucket, and API token)

3. Install dependencies:
   \`\`\`bash
   pip install -r requirements.txt
   \`\`\`

4. Set your InfluxDB token as an environment variable:
   \`\`\`bash
   export INFLUXDB_TOKEN="your_token_here"
   \`\`\`

5. Run the script:
   \`\`\`bash
   python3 main.py
   \`\`\`