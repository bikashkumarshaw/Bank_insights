SQL_QUERY = {
    "insert_data": "insert into Auth values('{}')",
    "bank_details": "select * from bank_db where ifsc='{0}' and id between {1} and {2}",
    "branch_details": "select * from bank_db where bank_name='{0}' and city='{1}' and id between {2} and {3}",
    "auth": "select auth from Auth where auth='{}'",
    "refresh": "delete from auth where Created <= CURRENT_DATE - INTERVAL '5 day'"
}
