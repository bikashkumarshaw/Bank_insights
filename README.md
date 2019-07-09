# Bank_insights
Fetch Bank info

#### Note you would need postgresql installed in your system for this.

## Install postgresql
```
sudo apt-get update
sudo apt-get install postgresql postgresql-contrib
```

## Create username and db for postgresql
```
sudo -u postgres createuser <username>
sudo -u postgres createdb <dbname>
sudo -u postgres psql
alter user <username> with encrypted password '<password>';
grant all privileges on database <dbname> to <username> ;
```

## Clone:
```
git clone https://github.com/bikashkumarshaw/Bank_insights.git
```

## Install Virtual Environment:
```
pip install virtualenv

cd Bank_insights

virtualenv -p python3 [environment name eg. env]

source env/bin/activate (env is the name of the environment here. please set according to your environment name)

Now install all the dependencies as listed below
```

## Dependencies:
- pip install -r requirements.txt

## Run command:
```
python fyle.py --port `specify the port to host the service` --dbname `provide your postgresql db name` --ip `specify the ip of the machine where this service will be hosted` --user `provide your postgresql username` --password `specify the password of postgresql user`
```

## API'S supported:

```
get_bank_details (returns bank details for given ifsc code or branch details for banks in a city)
```

## get_bank_details

#### This api is used to view Bank details when the user specifies either ifsc code or bank name with their city.

### Positional params:

**ifsc:**

* ##### The api supports ifsc param, eg. ifsc=ABHY0065001, this would return bank details for the given ifsc code.

* Ref 1: http://159.69.60.242:2233/api/get_bank_details?ifsc=ABHY0065001&key=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJlbWFpbCI6ImJpa2FzaEBnbWFpbC5jb20ifQ.wDxbT05jXETcgQMj0II3OSI-a-G1EDBNpzVZ9wio93E

```jsond
{
  "result": [
    {
      "address": "ABHYUDAYA BANK BLDG., B.NO.71, NEHRU NAGAR, KURLA (E), MUMBAI-400024",
      "branch": "RTGS-HO",
      "state": "MAHARASHTRA",
      "city": "MUMBAI",
      "bank_name": "ABHYUDAYA COOPERATIVE BANK LIMITED",
      "bank_id": "60",
      "ifsc": "ABHY0065001",
      "district": "GREATER MUMBAI"
    }
  ]
}


```

**key:**

* #### This argument is compulsary for any given api, this is the jwt token that each user has to generate initially in the client tool.

eg. key=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJlbWFpbCI6ImJpa2FzaEBnbWFpbC5jb20ifQ.wDxbT05jXETcgQMj0II3OSI-a-G1EDBNpzVZ9wio93E

**bank_name:**

* #### This argument takes name of the bank as input, note the spaces between the name should be replaced by "_".

eg. bank_name=ABHYUDAYA_COOPERATIVE_BANK_LIMITED

* Ref : http://159.69.60.242:2233/api/get_bank_details?bank_name=ABHYUDAYA_COOPERATIVE_BANK_LIMITED&city=mumbai&num=20&page=1&key=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJlbWFpbCI6ImJpa2FzaEBnbWFpbC5jb20ifQ.wDxbT05jXETcgQMj0II3OSI-a-G1EDBNpzVZ9wio93E

```jsond
{
  "result": [
    {
      "address": "148 ELLORA SHOPPING CENTRE, DAFTARY ROAD, MALAD (EAST), MUMBAI-400097",
      "branch": "MALAD EAST",
      "state": "MAHARASHTRA",
      "city": "MUMBAI",
      "bank_name": "ABHYUDAYA COOPERATIVE BANK LIMITED",
      "bank_id": "60",
      "ifsc": "ABHY0065021",
      "district": "GREATER MUMBAI"
    },
    {
      "address": "SECTOR-3, CHANAKYA SHOPPING CENTRE, BELAPUR (CBD), NAVI MUMBAI-400614",
      "branch": "CBD BELAPUR",
      "state": "MAHARASHTRA",
      "city": "MUMBAI",
      "bank_name": "ABHYUDAYA COOPERATIVE BANK LIMITED",
      "bank_id": "60",
      "ifsc": "ABHY0065022",
      "district": "GREATER MUMBAI"
    }
  ]
}

```

**num:**

* #### num specifies the number of results to be shown, eg num=2. the default value of num=20.

**page:**

* #### Since we show 20 results(num=20) per page this parameter is used to see the next 20 results.

eg. page=2

Default page is 0.
