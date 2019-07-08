import csv
import json
import argparse
import requests
import jwt

class ClientTool(object):

    def run(self):
        self.define_args()
        if self.args.gen_key:
            key = self.prepare_key()
            print ("\n"+key.decode("utf-8")+"\n")
        else:
            self.Authenticate()

    def prepare_key(self):
        encoded_jwt = jwt.encode({'email': self.args.email_id}, self.args.password.lower(), algorithm='HS256')
        return (encoded_jwt)

    def Authenticate(self):
        if "@" not in self.args.email_id or ".com" not in self.args.email_id:
            raise Exception("Please specify valid email_id")

        encoded_jwt = self.prepare_key()

        r = requests.post("http://{0}:{1}/api/auth".format(self.args.ip, self.args.port), data=json.dumps(dict(key=encoded_jwt.decode("utf-8"))), headers={'Content-Type': 'application/json'})

        print (r.json())

    def define_args(self):
        parser = argparse.ArgumentParser()
        parser.add_argument("--ip", help="specify bank insights service ip", type=str, required=True)
        parser.add_argument("--port", help="specify bank insights service port", type=str, required=True)
        parser.add_argument("--email-id", type=str, help="specify your email id")
        parser.add_argument("--password", type=str, help= "specify password")
        parser.add_argument("--gen-key", type=bool, help="specify this as true to gen key for existing user", default=False)
        self.args = parser.parse_args()

if __name__== "__main__":
    ClientTool().run()

