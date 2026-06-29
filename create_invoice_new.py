def create_invoice(invoice_no,*products,**customer):
    sub_total=0
    for i in products:
        sub_total+=i[1]*i[2]
    Value_added_tax=(sub_total*0.13)
    total=sub_total+Value_added_tax
    print("\tInvoice Detail\t")
    print(f' Invoice_no={invoice_no}\n Customer Name={customer.get('name','Name not provided')} \n Phone Number={customer.get('phone','Number not provided')}\n Address={customer.get('address','Address not provided')}')
    print(" Product Details:\n   Name \tquantiy price \t total ")
    for i,name in enumerate(products,1):
        print(f'{i}. {name[0]}\t {name[1]} \t {name[2]}\t {name[1]*name[2]}')

    print("___________________________________")
    print(f'Price without VAT: {sub_total}')
    print(f'VAT amount= {Value_added_tax}')
    print(f'Price with VAT= {total}')


create_invoice(
    "INV-001",
    ("Keyboard", 2, 1200),
    ("Mouse", 1, 800),
    ("Monitor", 1, 15000),
     name="Bidur",
    phone="9800000000",
    address="Kathmandu"
   
)
