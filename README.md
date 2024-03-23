# QueryCounter
This Flask application provides an API endpoint to count the unique queries based on a given date prefix.
Installation

To run this service locally, follow these steps:

1. Clone the repository:
   git clone <repository_url>
   

2. Navigate to the project directory:
   cd query-counter
   

3. Install dependencies:
   pip install -r requirements.txt
   

4. Place the logs file (hn_logs.tsv) in the root directory of the project.

## Usage

To start the Flask server, run the following command:

python app.py


Once the server is running, you can access the API endpoint to get the count of unique queries .

### API Endpoint


GET /1/queries/count/<prefix>


- <prefix>: Date prefix to filter the queries (e.g., "2024-03-20").

Example usage:

http://localhost:5000/1/queries/count/2024-03-20


### Design Choices:

- *Flask Framework:* Chosen for its simplicity and ease of use in creating RESTful APIs.
- *TSV Log Parsing:* Utilized TSV format for the log file as it is lightweight and easy to parse.
- *Data Structure:* Used defaultdict(set) to efficiently store and retrieve query logs based on timestamps.

### Alternative Designs Considered:

- *Database Integration:* Instead of parsing a static log file, could use a database (e.g., SQLite) to store and retrieve query logs in real-time.
- *Caching:* Implement caching mechanisms to improve performance for frequently accessed date prefixes.

### Pros and Cons:

- *Current Design:*
  - Pros: Simple and straightforward implementation.
  - Cons: Limited scalability for large log files.

- *Alternative Designs:*
  - Pros: Offers better scalability and real-time data retrieval.
  - Cons: Adds complexity to the system and requires additional setup.

### User Perspective evaluation

- *Complexity & Scalability:* The algorithm scales linearly with the size of the log file. Alternative designs improve scalability by utilizing databases and caching.
- *Readability of Code:* The code is organized and follows best practices. Unit tests can be added to enhance readability and maintainability.
- *Correctness of Outputs:* The API endpoint accurately counts the unique queries based on the provided date prefix.
- *Design Choices:* Design choices are explained, and alternative designs are considered, weighing their pros and cons.

