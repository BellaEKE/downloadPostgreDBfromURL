#!/usr/bin/env python
# coding: utf-8

# In[3]:


pip install psycopg2


# In[2]:


import psycopg2

# Connection details
url = "postgres://Test:bQNxVzJL4g6u@ep-noisy-flower-846766-pooler.us-east-2.aws.neon.tech/Metrocar"

# Establish a connection
conn = psycopg2.connect(url)

# Create a cursor object
cursor = conn.cursor()

# Define the table names
tables = ["app_downloads", "signups", "ride_requests", "transactions", "reviews"]

# Iterate over the table names and select all rows
for table in tables:
    cursor.execute(f"SELECT * FROM {table}")
    result = cursor.fetchall()
    
    # Save the result to a file
    filename = f"{table}.csv"
    with open(filename, "w") as file:
        for row in result:
            file.write(",".join(str(value) for value in row))
            file.write("\n")
    
    print(f"Results from {table} saved to {filename}")

# Close the cursor and connection
cursor.close()
conn.close()


# In[ ]:




