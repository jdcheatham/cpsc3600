"""Pasword cracker
JD Cheatham
cpsc3600"""
import binascii
def main():
    password = {}
    x=""
    """with open('password_file') as fin:
        for each in fin:
            (key, val)=each.split(',')
            password[key]=val
    fin.close()"""
    password = {'bf5c8c73bac23e156421cd5fdedbc818':'d984ab2d70fab1c954479a9a51ca301e5fd490d0432c080f3cfc979e3bbe7a7d','34fba277a5bee82a3c808c8643dae63d':'fb2fcbe7205e0ebf901f03e089c5f3d5757b378243e842f8d663f6eb63ca2e72','363a381301dbdfee139a20c941d4ea20':'e0afdb696bfbd0105a0efa8a36d23f34a67b6a8e1627948fab77704a12b34dc7','6be714e37ed8007c1d0229c4ee37931a':'31f363dfbe8e2ac2fd3296531db26eb171172569f0faf7deb80e345835d2ecb2'}
    for each in password:
        x=str(password[each])

        print(binascii.unhexlify(each))
        print(binascii.unhexlify(x))


if __name__ == "__main__":
    main()