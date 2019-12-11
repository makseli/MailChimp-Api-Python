# -*- coding:utf-8 -*-


from dotenv import load_dotenv
from mailchimp3 import MailChimp

load_dotenv()

client = MailChimp(mc_api='', mc_user='verilojistik')

# aa = client.lists.all(get_all=True, fields="lists.name,lists.id")
aa = client.lists.members.all('58c9187424', True, fields="members.email_address,members.id")
print(aa)