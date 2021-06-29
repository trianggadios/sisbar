import psycopg2

def db_connect():
    conn = psycopg2.connect('postgres://gvnatsrdmpuiei:71bebeda59e3ed2169f820951cdeb99f54ce2494994aa384c551154b60fb525f@ec2-52-0-114-209.compute-1.amazonaws.com:5432/d4qbnkep1ksgfa', sslmode='require')
    return conn