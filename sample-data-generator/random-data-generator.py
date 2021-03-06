import pandas as pd
from faker import Faker
from collections import defaultdict
from sqlalchemy import create_engine

batch_size=10000
users_to_insert=100000

fake = Faker()
engine = create_engine('mysql://root:root@localhost/solr_test', echo=False)

def inser_users():

    fake_data = defaultdict(list)

    for _ in range(batch_size):
        fake_data["first_name"].append( fake.first_name() )
        fake_data["last_name"].append( fake.last_name() )
        fake_data["job"].append( fake.job() )
        fake_data["dob"].append( fake.date_of_birth() )
        fake_data["country"].append( fake.country() )

    df_fake_data = pd.DataFrame(fake_data)

    df_fake_data.to_sql('user', con=engine,index=False, if_exists='append')

def batch():
    for x in range(0, users_to_insert, batch_size):
        inser_users();

batch()        

