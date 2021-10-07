## Steps to populate local DB with dummy data

1. Run `python manage.py shell` to start Python interactive console.

2. Run the following commands in the given order:
    ```
    import json
    from bank.models import Bank

    with open('Dummy_data/bank_dummy.json') as f:
        banks = json.load(f)

    for bank in banks:
        bank = Bank(
            ifsc=bank['ifsc'],
            bank_id=bank['bank_id'],
            branch=bank['branch'],
            address=bank['address'],
            city=bank['city'],
            district=bank['district'],
            state=bank['state'],
            bank_name=bank['bank_name']
            )
        bank.save()
    ```

    *Note: if you recieve any error then operation failed and we have to retry from starting of step-2.*

3. If no error recieved, exit the shell by typing `exit()`