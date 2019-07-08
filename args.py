import argparse

def _define_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("--dbname", help="specify the database name", type=str, required=True)
    parser.add_argument("--username", help="specify the username of the db", type=str, required=True)
    parser.add_argument("--port", help="specify the port to run server", type=int, required=True)
    parser.add_argument("--password", help="specify the password of postgresql user", type=str, required=True)
    parser.add_argument("--ip", help="specify the ip of the machine where this service will be hosted", type=str, required=True)
    args = parser.parse_args()
    return args
