from ldap3 import Server
from ldap3 import Connection
from ldap3 import ALL
from ldap3 import NTLM
from ldap3 import SUBTREE
from ldap3 import ALL_ATTRIBUTES

ad_server = Server('Your domain name.int', use_ssl=True, get_info=ALL)
conn = Connection(ad_server, user='your domain\\ user name', password='password', authentication=NTLM)

if not conn.bind():
    print('FAILED TO CONNECT')
else:
    who = conn.extend.standard.who_am_i()

    people = conn.search('dc=your domain, dc=int', '(&(objectclass=group)(sAMAccountName= user login))',
                     search_scope=SUBTREE, attributes=ALL_ATTRIBUTES, get_operational_attributes=True)

    print(conn.entries)
    print(who)
    print(conn)
