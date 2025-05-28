from datetime import datetime
import os

# Get the folder where this script is located
script_dir = os.path.dirname(os.path.abspath(__file__))

# Input and Output Paths
input_file = os.path.join(script_dir, "..", "Reports", "sonar_ip_test_report.txt")
output_html = os.path.join(script_dir, "..", "Reports", "sonar_ip_test_report.html")

# Read the report
with open(input_file, "r") as file:
    lines = file.readlines()

# Extract Header and Test Cases
title = lines[0].strip()
generated_time = lines[1].strip().replace("Generated:", "").strip()
test_cases = [line.strip().split(",") for line in lines[4:]]

# HTML Template
html_content = f"""
<!DOCTYPE html>
<html>
<head>
    <title>{title}</title>
    <style>
        body {{
            font-family: Arial, sans-serif;
            padding: 20px;
        }}
        h2 {{
            color: #0052CC;
        }}
        table {{
            width: 100%;
            border-collapse: collapse;
            margin-top: 20px;
        }}
        th, td {{
            border: 1px solid #ccc;
            padding: 8px;
            text-align: center;
        }}
        th {{
            background-color: #f2f2f2;
        }}
        .pass {{
            color: green;
            font-weight: bold;
        }}
        .fail {{
            color: red;
            font-weight: bold;
        }}
    </style>
</head>
<body>
    <h2>{title}</h2>
    <p><strong>Generated:</strong> {generated_time}</p>
    <table>
        <tr>
            <th>Test Case Key</th>
            <th>Input</th>
            <th>Result</th>
        </tr>
"""

for case in test_cases:
    if len(case) == 3:
        tc_key, input_value, result = case
        result_class = "pass" if result.lower() == "pass" else "fail"
        html_content += f"""
        <tr>
            <td>{tc_key}</td>
            <td>{input_value}</td>
            <td class="{result_class}">{result}</td>
        </tr>
        """

html_content += """
    </table>
</body>
</html>
"""

# Save the HTML
with open(output_html, "w") as html_file:
    html_file.write(html_content)

print(f"✅ HTML report generated at: {output_html}")
