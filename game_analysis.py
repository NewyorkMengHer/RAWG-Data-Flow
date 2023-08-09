
from pyspark.sql import SparkSession
from pyspark.sql.functions import explode

# Initialize a SparkSession
spark = SparkSession.builder     .appName("RAWG data transformation")     .getOrCreate()

# Read the CSV file into a DataFrame
df = spark.read.option("header", "true").csv("raw data/cleaned_data.csv")

# Create a temporary view for SQL queries
df.createOrReplaceTempView("games")

# Most Popular Games
spark.sql("SELECT game_name, added FROM games ORDER BY added DESC LIMIT 5").show()

# Top Rated Games
spark.sql("SELECT game_name, rating FROM games ORDER BY rating DESC LIMIT 5").show()

# Most Played Games
spark.sql("SELECT game_name, playtime FROM games ORDER BY playtime DESC LIMIT 5").show()

# Game Releases Over Time
spark.sql("SELECT released, COUNT(*) as number_of_releases FROM games GROUP BY released ORDER BY released").show()

# Most Common Platforms
df.withColumn('platform', explode(df.platform_name)).createOrReplaceTempView("games_exploded_platforms")
spark.sql("SELECT platform, COUNT(*) as count FROM games_exploded_platforms GROUP BY platform ORDER BY count DESC").show()

# Most Common Stores
df.withColumn('store', explode(df.store_name)).createOrReplaceTempView("games_exploded_stores")
spark.sql("SELECT store, COUNT(*) as count FROM games_exploded_stores GROUP BY store ORDER BY count DESC").show()

# Popularity of ESRB Ratings
spark.sql("SELECT esrb_rating, COUNT(*) as count FROM games GROUP BY esrb_rating ORDER BY count DESC").show()

# Top Games by Status
spark.sql("SELECT game_name, added_by_status.beaten as beaten FROM games ORDER BY beaten DESC LIMIT 5").show()
spark.sql("SELECT game_name, added_by_status.toplay as toplay FROM games ORDER BY toplay DESC LIMIT 5").show()
spark.sql("SELECT game_name, added_by_status.dropped as dropped FROM games ORDER BY dropped DESC LIMIT 5").show()
spark.sql("SELECT game_name, added_by_status.playing as playing FROM games ORDER BY playing DESC LIMIT 5").show()

# Game Genre Popularity
df.withColumn('genre', explode(df.genre_name)).createOrReplaceTempView("games_exploded_genres")
spark.sql("SELECT genre, COUNT(*) as count FROM games_exploded_genres GROUP BY genre ORDER BY count DESC").show()
