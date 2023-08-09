from pyspark.sql import SparkSession
from pyspark.sql.functions import explode

# Initialize a SparkSession
spark = SparkSession.builder \
    .appName("RAWG data transformation") \
    .getOrCreate()

# Specify the path to the JSON file (in this case, a local file for testing)
json_file_path = 'raw data/rawg_games_data.json'

# Read the JSON file into a DataFrame
df = spark.read.json(json_file_path)

# Explode the results field
df = df.withColumn("results_flat", explode("results"))

# Create separate columns for the nested fields in the results field
df = df.select("*", "results_flat.*").drop("results", "results_flat")

# Rename the 'name' field to 'game_name' and 'id' field to 'game_id'
df = df.withColumnRenamed("name", "game_name").withColumnRenamed("id", "game_id")

# Explode the platforms field and rename the 'name' and 'id' fields
df = df.withColumn("platforms_flat", explode("platforms"))
df = df.select("*", "platforms_flat.platform.*").drop("platforms", "platforms_flat")
df = df.withColumnRenamed("name", "platform_name").withColumnRenamed("id", "platform_id")

# Explode the stores field and rename the 'name' and 'id' fields
df = df.withColumn("stores_flat", explode("stores"))
df = df.select("*", "stores_flat.store.*").drop("stores", "stores_flat")
df = df.withColumnRenamed("name", "store_name").withColumnRenamed("id", "store_id")

# Explode the genres field and rename the 'name' and 'id' fields
df = df.withColumn("genres_flat", explode("genres"))
df = df.select("*", "genres_flat.*").drop("genres", "genres_flat")
df = df.withColumnRenamed("name", "genre_name").withColumnRenamed("id", "genre_id")

# Filter out the necessary columns for analysis
columns_to_keep = [
    "game_id", "game_name", "released", "rating", "ratings_count", 
    "reviews_text_count", "added", "playtime", "platform_name", 
    "store_name", "genre_name", "esrb_rating.name", 
    "added_by_status.beaten", "added_by_status.dropped", 
    "added_by_status.owned", "added_by_status.playing", 
    "added_by_status.toplay", "added_by_status.yet"
]

df_filtered = df.select(*columns_to_keep)

# Display the filtered DataFrame
df_filtered.show(5)

# Assuming df is your final DataFrame
df_filtered.coalesce(1).write.format('csv').option('header',True).mode('overwrite').save('raw data/output.csv')


