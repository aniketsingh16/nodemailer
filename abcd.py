
app = Flask(__name__)

# Sample data
data = pd.DataFrame({'team': ['A', 'A', 'A', 'A', 'B', 'B', 'B', 'B'],
                   'position': ['G', 'G', 'F', 'F', 'G', 'F', 'F', 'F'],
                   'all_star': ['Y', 'N', 'Y', 'Y', 'N', 'N', 'N', 'Y'],
                   'points': [4, 4, 6, 8, 9, 5, 5, 12]})

df = pd.DataFrame(data)

# Function to generate pivot table
def generate_pivot_table():
    pivot_df = pd.pivot_table(df, values='points',
                              index=['team', 'all_star'],
                              columns='position',
                              aggfunc='sum')
    return pivot_df

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate_report', methods=['POST'])
def generate_report():
    # category = request.form.get('category')
    pivot_table = generate_pivot_table()
    pivot_table_html = pivot_table.to_html()
    return render_template('report.html', pivot_table_html=pivot_table_html)

@app.route('/download_report')
def download_report():
    # You can customize the filename and file format as needed
    filename = 'pivot_report.csv'
    pivot_table = generate_pivot_table()  # Generate full pivot table
    pivot_table.to_csv(filename)
    return send_file(filename, as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True)


// HTML index
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Generate Report</title>
</head>
<body>
    <h1>Generate Pivot Table Report</h1>
    <form action="/generate_report" method="post">
        <label for="category">Select Category:</label>
        <select id="category" name="category">
            <option value="">All</option>
            <option value="A">Category A</option>
            <option value="B">Category B</option>
            <option value="C">Category C</option>
        </select>
        <button type="submit">Generate Report</button>
    </form>
    <br>
    <p><a href="/download_report">Download Report</a></p>
</body>
</html>

-- html report

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Report</title>
    <style>
        table {
            border-collapse: collapse;
            width: 100%;
        }
        th, td {
            border: 1px solid #dddddd;
            text-align: left;
            padding: 8px;
        }
        th {
            background-color: #f2f2f2;
        }
    </style>
</head>
<body>
    <h1>Report</h1>
    <div>
        {{ pivot_table_html | safe }}
    </div>
</body>
</html>
