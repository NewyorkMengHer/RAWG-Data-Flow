# RAWG Data Flow

## Introduction
"RAWG Data Flow" is an ETL pipeline designed to extract, transform, and load video game data from RAWG's API, the largest video game database. This project was born out of a dual passion: a keen interest in cloud technologies, specifically AWS, and a love for video games. As a dedicated gamer, I wanted to stay updated with the latest in the gaming world, but time constraints often got in the way. This pipeline serves as a solution to that, while also offering hands-on experience with AWS services.

## Features
- **Data Extraction**: Utilizes AWS Lambda to pull video game data in JSON format from RAWG's API.
- **Data Storage**: Safely stores the extracted JSON data in an AWS S3 bucket.
- **Data Transformation**: Employs AWS Glue and Spark to transform the JSON data, handling complexities like nested arrays, and converting it into a more accessible CSV format.
- **Final Storage**: The transformed CSV data is then stored back into an S3 bucket for further analysis or use.

## Workflow
1. **Lambda & EC2**: An AWS Lambda function, set up with the help of an EC2 environment due to initial challenges, makes an HTTP request using a provided API key to RAWG's API.
2. **S3 Storage**: The extracted JSON data from RAWG is stored in an S3 bucket.
3. **Data Review**: Using Visual Studio Code on a local machine, the data is reviewed to understand its structure and determine the necessary transformations.
4. **Glue & Spark Transformation**: AWS Glue extracts the data from the S3 bucket. Spark is then used to handle the transformation process, especially dealing with nested arrays in the data.
5. **Second Storage**: Post-transformation, the data is saved as a CSV and stored back in an S3 bucket.
6. **RedShift**: The CSV is further extracted and loaded into Amazon Redshift for queries
   
![image](images/RAWG%20Data%20Pipeline%20Architecture.JPG)

## Challenges
- **Lambda Setup**: Encountered issues in setting up Lambda to make HTTP requests. This was resolved by using EC2 to create a suitable Lambda environment.
- **Data Complexity**: The RAWG data had nested arrays in some columns. Decisions had to be made on whether to retain, flatten, or remove these arrays based on their relevance.

## Data Loading and Analysis

### Loading to RedShift
After the transformation process, the cleaned and structured CSV data is not just left sitting in the S3 bucket. It's further extracted and loaded into Amazon RedShift, a fully managed data warehouse service by AWS. This step is crucial for the subsequent analysis phase, as RedShift provides fast query performance using sophisticated query optimization, columnar storage on high-performance disks, and massively parallel query execution.

### Analysis with Tableau
With the data now housed in RedShift, the next logical step is to derive insights from it. For this, I employed Tableau, a powerful data visualization tool. By connecting Tableau to RedShift, I was able to run analytical queries directly on the data. This not only allowed me to fetch the specific data points I was interested in but also to visualize them in a more comprehensible manner.

The beauty of Tableau lies in its ability to transform raw data into interactive and visually appealing dashboards. As a gamer, this was particularly exciting for me. I could now see trends, player preferences, game ratings, and so much more, all represented graphically. It was like having a bird's eye view of the entire gaming landscape.

## Conclusion
"RAWG Data Flow" is a testament to the power of cloud technologies and data analytics. From extracting raw data from an API to visualizing meaningful insights in Tableau, every step of the journey was both challenging and rewarding. Whether you're a data enthusiast, a cloud computing aficionado, or a passionate gamer, I hope this project offers a blend of technical know-how and a dash of gaming excitement.
